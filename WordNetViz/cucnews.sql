# Host: localhost  (Version 5.7.14-log)
# Date: 2018-12-28 17:49:04
# Generator: MySQL-Front 6.0  (Build 1.157)


#
# Structure for table "cucnews"
#

CREATE TABLE `cucnews` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `newsfrom` varchar(255) DEFAULT NULL,
  `newsdate` varchar(50) DEFAULT NULL,
  `contents` varchar(10000) DEFAULT NULL,
  `newscount` int(11) DEFAULT NULL,
  `newsurl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8828 DEFAULT CHARSET=utf8;
