-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: pet_rescue
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
-- Table structure for table `animal`
--

DROP TABLE IF EXISTS `animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animal` (
  `idanimal` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `age` varchar(45) NOT NULL,
  `color` varchar(45) NOT NULL,
  `healthCondition` varchar(45) NOT NULL,
  `weight` varchar(45) NOT NULL,
  `Description` longtext,
  `species` varchar(45) NOT NULL,
  PRIMARY KEY (`idanimal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animal`
--

LOCK TABLES `animal` WRITE;
/*!40000 ALTER TABLE `animal` DISABLE KEYS */;
/*!40000 ALTER TABLE `animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donate_info`
--

DROP TABLE IF EXISTS `donate_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donate_info` (
  `iddonate_info` varchar(45) NOT NULL,
  `id_donater` varchar(45) NOT NULL,
  `date_donate` date NOT NULL,
  `so_tai_khoan` varchar(45) NOT NULL,
  `ma_giao_dich` varchar(45) NOT NULL,
  `ten_ngan_hang` varchar(45) NOT NULL,
  `message` longblob NOT NULL,
  PRIMARY KEY (`iddonate_info`),
  KEY `fk_donate_donater_idx` (`id_donater`),
  CONSTRAINT `fk_donate_donater` FOREIGN KEY (`id_donater`) REFERENCES `sponsors` (`id_sponsor`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donate_info`
--

LOCK TABLES `donate_info` WRITE;
/*!40000 ALTER TABLE `donate_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `donate_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `healthreport`
--

DROP TABLE IF EXISTS `healthreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `healthreport` (
  `idhealthreport` varchar(45) NOT NULL,
  `idAnimal` varchar(45) NOT NULL,
  `date_create` date NOT NULL,
  `idVeterinarian` varchar(45) NOT NULL,
  `health_status` varchar(45) NOT NULL,
  `weight` double NOT NULL,
  `Description` longblob NOT NULL,
  `image` longblob NOT NULL,
  PRIMARY KEY (`idhealthreport`),
  KEY `fk_report_animal_idx` (`idAnimal`),
  KEY `fk_report_veterinarian_idx` (`idVeterinarian`),
  CONSTRAINT `fk_report_animal` FOREIGN KEY (`idAnimal`) REFERENCES `animal` (`idanimal`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_report_veterinarian` FOREIGN KEY (`idVeterinarian`) REFERENCES `veterinarians` (`id_veterinarian`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `healthreport`
--

LOCK TABLES `healthreport` WRITE;
/*!40000 ALTER TABLE `healthreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `healthreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_work_time`
--

DROP TABLE IF EXISTS `register_work_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_work_time` (
  `idregister_work_time` varchar(45) NOT NULL,
  `id_volunteer` varchar(45) NOT NULL,
  `time` varchar(45) NOT NULL,
  `date_in_week` varchar(45) NOT NULL,
  PRIMARY KEY (`idregister_work_time`),
  KEY `fk_time_veterinarian_idx` (`id_volunteer`),
  CONSTRAINT `fk_time_veterinarian` FOREIGN KEY (`id_volunteer`) REFERENCES `volunteers` (`id_volunteers`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_work_time`
--

LOCK TABLES `register_work_time` WRITE;
/*!40000 ALTER TABLE `register_work_time` DISABLE KEYS */;
/*!40000 ALTER TABLE `register_work_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sponsors`
--

DROP TABLE IF EXISTS `sponsors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sponsors` (
  `id_sponsor` varchar(45) NOT NULL,
  `fullname` varchar(45) NOT NULL,
  `age` int NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(90) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id_sponsor`),
  CONSTRAINT `fk_donater_donate` FOREIGN KEY (`id_sponsor`) REFERENCES `donate_info` (`iddonate_info`)
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
  `id_user` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `date_register` date NOT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinarians`
--

DROP TABLE IF EXISTS `veterinarians`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinarians` (
  `id_veterinarian` varchar(45) NOT NULL,
  `fullname` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `address` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `facebooklink` varchar(100) DEFAULT NULL,
  `work_in_week` varchar(45) NOT NULL,
  PRIMARY KEY (`id_veterinarian`)
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
-- Table structure for table `volunteers`
--

DROP TABLE IF EXISTS `volunteers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volunteers` (
  `id_volunteers` varchar(45) NOT NULL,
  `fullname` varchar(45) NOT NULL,
  `age` int NOT NULL,
  `phone` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `date_register` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `position` varchar(45) NOT NULL,
  PRIMARY KEY (`id_volunteers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteers`
--

LOCK TABLES `volunteers` WRITE;
/*!40000 ALTER TABLE `volunteers` DISABLE KEYS */;
/*!40000 ALTER TABLE `volunteers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-09 16:38:40
