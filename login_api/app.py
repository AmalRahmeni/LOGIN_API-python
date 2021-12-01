# Import Modules
from datetime import datetime
from flask import Flask, make_response, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "amalrahmeni2020"

######## Parameters ##############################

API_KEYS = {
	"amalkeylogin": "login",
	"amalkeyreg": "register",
}
JSON_KEY_STATUS_CODE = "responseCode"
JSON_KEY_STATUS_MESSAGE = "responseMessage"

# MySQL
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWD = ""
MYSQL_DATABASE = "login_api"

######## Prepare MySQL ###########################

conn = mysql.connector.connect(
	host = MYSQL_HOST,
	user = MYSQL_USER,
	passwd = MYSQL_PASSWD,
	database = MYSQL_DATABASE
)
cur = conn.cursor(dictionary=True)

######## Routes ##################################

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():

	# get params
	api_key = request.form.get("api_key")
	email = request.form.get("email")
	password = request.form.get("password")
	
	# REQUEST_PARAMS_MISSING
	if not api_key or not email or not password:
		return make_response(jsonify({JSON_KEY_STATUS_CODE: 301, JSON_KEY_STATUS_MESSAGE: "REQUEST_PARAMS_MISSING"}), 301)
		
	# ACCESS_PERMISSION_DENIED
	if api_key not in API_KEYS:
		return make_response(jsonify({JSON_KEY_STATUS_CODE: 911, JSON_KEY_STATUS_MESSAGE: "ACCESS_PERMISSION_DENIED"}), 911)

	# WRONG_API_METHOD_CALLED
	if API_KEYS[api_key] != "login":
		return make_response(jsonify({JSON_KEY_STATUS_CODE: 901, JSON_KEY_STATUS_MESSAGE: "WRONG_API_METHOD_CALLED"}), 901)

	# find user in database
	sql = "SELECT id, name, email_id, gender, last_login, IF(password=PASSWORD(%s), 1, 0) as cor_pwd FROM users WHERE email_id = %s LIMIT 1;"
	cur.execute(sql, (password, email,))
	res = cur.fetchone()

	# USER_NOT_FOUND
	if not res:
		return make_response(jsonify({JSON_KEY_STATUS_CODE: 401, JSON_KEY_STATUS_MESSAGE: "USER_NOT_FOUND"}), 401)

	# INVALID_LOGIN_DETAILS
	if not res["cor_pwd"]:
		return make_response(jsonify({JSON_KEY_STATUS_CODE: 410, JSON_KEY_STATUS_MESSAGE: "INVALID_LOGIN_DETAILS"}), 410)

	# update last login datetime
	sql = "UPDATE users SET last_login = %s LIMIT 1;"
	cur.execute(sql, (datetime.now(),))
	conn.commit()

	# return success result
	res.pop("cor_pwd")
	return make_response(jsonify({JSON_KEY_STATUS_CODE: 1000, JSON_KEY_STATUS_MESSAGE: "Success", "user": res}), 1000)

##########################################################

if __name__=="__main__":
	app.run(debug=True)
