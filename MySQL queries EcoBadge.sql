-- -------------------------------------------------------------
-- TablePlus 4.6.0(406)
--
-- https://tableplus.com/
--
-- Database: ecobadge
-- Generation Time: 2022-03-29 21:48:28.3290
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


CREATE TABLE `business` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `postcode` varchar(50) DEFAULT NULL,
  `pNumber` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `cuisine` varchar(255) DEFAULT NULL,
  `scored` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `user` (
  `id` varchar(20) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `priority` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  `business_id` int DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  `reply_of` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `business_id` (`business_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`business_id`) REFERENCES `business` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `score` (
  `business_id` int NOT NULL,
  `score` int DEFAULT NULL,
  `vegan` tinyint(1) DEFAULT NULL,
  `singleUsePlastic` tinyint(1) DEFAULT NULL,
  `foodwasteCollection` tinyint(1) DEFAULT NULL,
  `localProduce` tinyint(1) DEFAULT NULL,
  `latest` tinyint(1) DEFAULT NULL,
  `dateOfScore` datetime NOT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`business_id`,`dateOfScore`),
  CONSTRAINT `score_ibfk_1` FOREIGN KEY (`business_id`) REFERENCES `business` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `user` (`id`, `email`, `name`, `priority`) VALUES
('11', 'yo@gmail.com', 'hi', 2),
('1234', '222@gmail.com', 'mon2', 3),
('9asd9as8ad0', 'vish@gmail.com', 'vish', 0);

INSERT INTO `business` (`id`, `name`, `address`, `postcode`, `pNumber`, `email`, `description`, `website`, `cuisine`, `scored`) VALUES
(1, 'mcs', 'old george street', 'pl11dz', '0745235342', 'surya@gmail.com', 'the best burger biz in town', 'mcd.com', 'fast food', 1),
(3, 'kfx', 'geooorggeee', 'pl11dz', '09862323', 'geroed@gmail.com', 'kfc best chickens in the biz', 'kfc.com', 'chickens', 1),
(4, 'zahut', 'old trownnn', 'pl1 2df', '8456212756', 'zzaaahut@zahut.com', 'Pizza for everyone yoooo', 'zahut.com', 'pizza', 1);

INSERT INTO `review` (`id`, `content`, `user_id`, `business_id`, `date_created`, `reply_of`) VALUES
(1, 'sucks', '11', 1, '2020-01-03 00:00:00', NULL),
(4, 'Kinda good but kinda hot so idk', '1234', 4, '2022-03-25 16:17:06', 0),
(5, 'Kinda good but kinda hot so idk', '1234', 4, '2022-03-25 16:17:32', 4);

INSERT INTO `score` (`business_id`, `score`, `vegan`, `singleUsePlastic`, `foodwasteCollection`, `localProduce`, `latest`, `dateOfScore`, `price`) VALUES
(1, 76, 1, 1, 1, 1, 0, '2020-01-01 00:00:00', 1),
(1, 75, 1, 1, 1, 1, 0, '2020-03-03 00:00:00', 1),
(1, 89, 0, 1, 0, 1, 0, '2022-03-24 23:31:26', 2),
(1, 99, 0, 1, 0, 1, 0, '2022-03-24 23:31:42', 2),
(1, 34, 0, 1, 0, 1, 0, '2022-03-24 23:32:11', 2),
(1, 34, 0, 1, 0, 1, 1, '2022-03-24 23:33:12', 2),
(3, 88, 0, 1, 1, 1, 1, '2021-09-01 00:00:00', 3),
(4, 34, 0, 1, 0, 1, 0, '2022-03-24 23:37:11', 2),
(4, 84, 1, 1, 0, 1, 1, '2022-03-24 23:37:35', 2);

CREATE VIEW `businessscore` (`business_id`,`name`,`address`,`postcode`,`description`,`cuisine`,`score`,`vegan`,`singleUsePlastic`,`foodwasteCollection`,`localProduce`,`price`) AS select `s`.`business_id` AS `business_id`,`b`.`name` AS `name`,`b`.`address` AS `address`,`b`.`postcode` AS `postcode`,`b`.`description` AS `description`,`b`.`cuisine` AS `cuisine`,`s`.`score` AS `score`,`s`.`vegan` AS `vegan`,`s`.`singleUsePlastic` AS `singleUsePlastic`,`s`.`foodwasteCollection` AS `foodwasteCollection`,`s`.`localProduce` AS `localProduce`,`s`.`price` AS `price` from (`score` `s` join `business` `b`) where ((`s`.`business_id` = `b`.`id`) and (`s`.`latest` = 1));


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;