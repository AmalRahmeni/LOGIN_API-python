/*
Navicat MySQL Data Transfer

Source Server         : Localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : login_api

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2021-09-04 23:20:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `last_login` datetime NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'Saber Abdel', 'saber@gmail.com', 'Male', '0000-00-00 00:00:00', '*00A51F3F48415C7D4E8908980D443C29C69B60C9');
