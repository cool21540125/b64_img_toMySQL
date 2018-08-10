
--;# CREATE DATABASE `pic` CHARACTER SET `utf8` COLLATE `utf8_unicode_ci`;

USE `pic`;

--;# DROP TABLE IF EXISTS `img`;

CREATE TABLE `img` (
    `logo`   BLOB    NOT NULL
) CHARSET=`utf8` COLLATE=`utf8_unicode_ci`;

--;# BLOG : 上限 65535 bytes (64KB)