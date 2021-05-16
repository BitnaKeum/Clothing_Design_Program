CREATE TABLE `image` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `username` varchar(30) DEFAULT NULL COMMENT 'author of image file',
  `image` varchar(255) DEFAULT NULL COMMENT 'image file name',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

CREATE TABLE `outimage` (
  `real_id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `id` int NOT NULL COMMENT 'id of user original image',
  `username` varchar(30) DEFAULT NULL COMMENT 'username',
  `image` varchar(255) DEFAULT NULL COMMENT 'new image',
  PRIMARY KEY (`real_id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;

CREATE TABLE `sessions` (
  `session_id` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `expires` int unsigned NOT NULL,
  `data` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `authId` varchar(50) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `salt` varchar(255) DEFAULT NULL,
  `displayName` varchar(50) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authId` (`authId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;