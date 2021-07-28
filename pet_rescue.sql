-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pet_rescue
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `donate_detail`
--

DROP TABLE IF EXISTS `donate_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donate_detail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sponsor_id` int NOT NULL,
  `created_at` date NOT NULL,
  `so_tai_khoan` varchar(255) NOT NULL,
  `ma_giao_dich` varchar(255) NOT NULL,
  `ten_ngan_hang` varchar(255) NOT NULL,
  `message` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_donate_info_idx` (`sponsor_id`),
  CONSTRAINT `fk_donate_info` FOREIGN KEY (`sponsor_id`) REFERENCES `sponsors` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donate_detail`
--

LOCK TABLES `donate_detail` WRITE;
/*!40000 ALTER TABLE `donate_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `donate_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_report`
--

DROP TABLE IF EXISTS `health_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `health_report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pet_id` int NOT NULL,
  `create_at` date NOT NULL,
  `veterinarian_id` int NOT NULL,
  `health_status` varchar(255) NOT NULL,
  `weight` double NOT NULL,
  `description` longblob NOT NULL,
  `image` longblob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_report_pet_idx` (`pet_id`),
  KEY `fk_report_veterian_idx` (`veterinarian_id`),
  CONSTRAINT `fk_report_pet` FOREIGN KEY (`pet_id`) REFERENCES `pets` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_report_veterian` FOREIGN KEY (`veterinarian_id`) REFERENCES `veterinarians` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_report`
--

LOCK TABLES `health_report` WRITE;
/*!40000 ALTER TABLE `health_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pet_images`
--

DROP TABLE IF EXISTS `pet_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pet_images` (
  `pet_id` int NOT NULL,
  `url` varchar(255) NOT NULL,
  KEY `fk_image_pet_idx` (`pet_id`),
  CONSTRAINT `fk_image_pet` FOREIGN KEY (`pet_id`) REFERENCES `pets` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet_images`
--

LOCK TABLES `pet_images` WRITE;
/*!40000 ALTER TABLE `pet_images` DISABLE KEYS */;
INSERT INTO `pet_images` VALUES (1,'https://www.facebook.com'),(1,'http://res.cloudinary.com/pet-rescue/image/upload/v1627379486/pet-rescue/1/dduj9m1ajy7m6rrarzug.jpg');
/*!40000 ALTER TABLE `pet_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets`
--

DROP TABLE IF EXISTS `pets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `health_condition` varchar(255) NOT NULL,
  `weight` double NOT NULL,
  `description` longtext,
  `species` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets`
--

LOCK TABLES `pets` WRITE;
/*!40000 ALTER TABLE `pets` DISABLE KEYS */;
INSERT INTO `pets` VALUES (1,'a','a','a','a',1,'a','a');
/*!40000 ALTER TABLE `pets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sponsors`
--

DROP TABLE IF EXISTS `sponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sponsors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sponsors`
--

LOCK TABLES `sponsors` WRITE;
/*!40000 ALTER TABLE `sponsors` DISABLE KEYS */;
/*!40000 ALTER TABLE `sponsors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'guest',
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'test','$2b$12$Bi5b9aGYwlSk0nqGzJnjc.VRBJTXOhe84OZrKe2G5q6GWj8j0kfDC','admin','string','string','string','string'),(3,'huuvuot','$2b$12$SXWdF/8ZHtI434prjAqdFOiHuXKsjmGWbl3UBwjxUgCS54toTuaQW','volunteer','string','string','string','string');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinarians`
--

DROP TABLE IF EXISTS `veterinarians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinarians` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `work_in_week` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinarians`
--

LOCK TABLES `veterinarians` WRITE;
/*!40000 ALTER TABLE `veterinarians` DISABLE KEYS */;
/*!40000 ALTER TABLE `veterinarians` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_schedule`
--

DROP TABLE IF EXISTS `work_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work_schedule` (
  `user_id` int NOT NULL,
  `working_shift` varchar(255) NOT NULL,
  `working_day` date NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT 'registered',
  KEY `fk_user_time_idx` (`user_id`),
  CONSTRAINT `fk_user_time` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_schedule`
--

LOCK TABLES `work_schedule` WRITE;
/*!40000 ALTER TABLE `work_schedule` DISABLE KEYS */;
INSERT INTO `work_schedule` VALUES (3,'0','2021-03-25','registered'),(3,'0','2021-03-25','registered'),(3,'0','2021-07-28','registered');
/*!40000 ALTER TABLE `work_schedule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-28 21:43:04
