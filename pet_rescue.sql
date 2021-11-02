-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: pet-rescue.chhw3ihaqbuw.ap-southeast-1.rds.amazonaws.com    Database: pet_rescue
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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

-- SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

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
  `update_at` date NOT NULL,
  `account_number` varchar(255) NOT NULL,
  `transaction_code` varchar(255) NOT NULL,
  `donations` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_donate_info_idx` (`sponsor_id`),
  CONSTRAINT `fk_donate_info` FOREIGN KEY (`sponsor_id`) REFERENCES `sponsors` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donate_detail`
--

LOCK TABLES `donate_detail` WRITE;
/*!40000 ALTER TABLE `donate_detail` DISABLE KEYS */;
INSERT INTO `donate_detail` VALUES (12,11,'2021-08-10','2021-08-10','19034884488012','HQCS134567',10000000),(13,11,'2021-08-10','2021-08-10','123123','141234',12341234),(14,13,'2021-08-10','2021-08-10','50210000103590','QWER123465',1000000000);
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
  `veterinary_clinic_id` int NOT NULL,
  `created_at` date NOT NULL,
  `update_at` varchar(45) NOT NULL,
  `weight` double NOT NULL,
  `health_condition` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_health_report_1_idx` (`pet_id`),
  KEY `fk_health_report_2_idx` (`veterinary_clinic_id`),
  CONSTRAINT `fk_health_report_1` FOREIGN KEY (`pet_id`) REFERENCES `pets` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_health_report_2` FOREIGN KEY (`veterinary_clinic_id`) REFERENCES `veterinary_clinic` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_report`
--

LOCK TABLES `health_report` WRITE;
/*!40000 ALTER TABLE `health_report` DISABLE KEYS */;
INSERT INTO `health_report` VALUES (6,37,17,'2021-08-10','2021-08-10',30,'Tình trạng sức khoẻ tốt','tính trạng sức khoẻ tốt , không bị giun sán, ham ăn, nhiều năng lượng'),(7,34,19,'2021-08-10','2021-08-10',20,'tốt','sức khoẻ tốt, ăn uống đầy đủ, không bị giun sán, nhưng mà hơi ngáo, hay sủa linh tinh'),(8,29,16,'2021-08-10','2021-08-10',2.5,'tốt','tốt');
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
  CONSTRAINT `fk_image_pet` FOREIGN KEY (`pet_id`) REFERENCES `pets` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet_images`
--

LOCK TABLES `pet_images` WRITE;
/*!40000 ALTER TABLE `pet_images` DISABLE KEYS */;
INSERT INTO `pet_images` VALUES (19,'http://res.cloudinary.com/pet-rescue/image/upload/v1628346392/pet-rescue/19/flchsknonuwr0vsj86uw.jpg'),(29,'http://res.cloudinary.com/pet-rescue/image/upload/v1628385668/pet-rescue/29/hhrakpgo0sli1jxj5lex.jpg'),(32,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556101/pet-rescue/32/darnjmzy7pjmcqkr13u4.jpg'),(33,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556184/pet-rescue/33/rmxmb1ltqv9mh0od7tv2.jpg'),(34,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556374/pet-rescue/34/jjd3vbtuihuunpamtiga.jpg'),(35,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556485/pet-rescue/35/lwgdiyqvwcgho6goedjm.jpg'),(36,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556604/pet-rescue/36/tmj5dlvhq5zyszgxh0hi.jpg'),(37,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556890/pet-rescue/37/kvbtji0snn2lzfudlyej.jpg'),(37,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556891/pet-rescue/37/kq1xqtltdi28xhjm03rj.jpg'),(37,'http://res.cloudinary.com/pet-rescue/image/upload/v1628556892/pet-rescue/37/vtjayak39sybclipew4m.jpg');
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
  `gender` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `health_condition` varchar(255) NOT NULL,
  `weight` double NOT NULL,
  `description` longtext NOT NULL,
  `species` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets`
--

LOCK TABLES `pets` WRITE;
/*!40000 ALTER TABLE `pets` DISABLE KEYS */;
INSERT INTO `pets` VALUES (19,'chó','young','male','vàng','tốt',12,'chó corgi','dog'),(29,'putdo','mature','male','xanh xám','tốt ',20.5,'là chú chó lang thang được người cứu về trong tình trạng bị thương ở chân phải , sau khi được sự chăm sóc của các tình nguyện viên thì đã khoẻ mạnh trở lại và lợi hại hơn xưa','dog'),(32,'Khoai tây','mature','male','vàng xám','Tốt',5,'Bé dễ thương đáng yêu, biết đứng lạy khi đòi ăn hay bế','dog'),(33,'Vừng jinx','young','male','trắng','tốt',2,'Vừng (Jinx) được cứu khi lang thang ngoài đường. Bé rất tinh nghịch, ham chơi ham vui.','cat'),(34,'john ngáo','mature','male','đen trắng','tốt',28,'Chó Husky có ngoại hình đẹp, thân thiện nhưng lại khá nghịch ngợm, đôi mắt của chó Husky rất trong, sáng và tinh ranh.','dog'),(35,'Chewie','young','female','trắng','tốt',0.5,'Bé bị chủ cắt lông nham nhở rồi thẳng tay vứt đi, trong lúc mon men bò ra đường thì gặp tai nạn xe. Lúc tnv nhóm nhận tin đến nơi thì người dân đem bỏ bé ra lùm cây, bé chắc hẳn đã rất hoảng sợ, nằm cuộn tròn im thin thít trong cái mũ bảo hiểm đã vỡ. Bé thở yếu, người lạnh, niêm mạc nhợt nhạt, và nấm toàn thân. May mà kịp thời cứu được bé đi viện...','cat'),(36,'xi xi','young','male','tam thể','tốt',2,'Xi Xi được cứu khi đang lang thang ở ngoài đường lúc bụng mang dạ chửa. Nhóm đã tìm được mái ấm cho tất cả các con của con, thế nhưng Xi Xi vẫn chưa có gia đình của riêng mình. Ban đầu con sẽ dè chừng chút, nhưng sau đó sẽ rất tình thương mến thương. Thích leo lên lòng nằm để được ôm được vuốt ve chiều chuộng. Còn thích ngủ ngáy giữa ban ngày hoặc nằm ngửa bụng phơi nắng nữa cơ ^^','cat'),(37,'Bim Bim','old','male','vàng xám','tốt',14,'Bim Bim suýt bị chủ bán thịt vì bé bị ghẻ và ký sinh trùng máu, may là bé đã về với nhóm kịp thời và được chữa trị tử tế. Bim Bim tính tình vui vẻ, ham chơi, mới gần 1 tủi thôi nên còn hơi ngáo ngáo ngơ ngơ, dễ tin người :))) Thích nhất là được tung tăng đi dạo và rất ngoan khi dắt dây. Có chút nhút nhát khi thấy mèo và chó bé, nhưng Bim Bim rất thích làm bạn với mấy bạn chó lớn. Foster của Bim Bim đảm bảo bé nó siêu cấp hiền lành, không làm đau cả một con ruồi lun á nè ? Bim Bim đã tiêm phòng đầy đủ, nhưng chưa triệt sản. Thân hình hiện tại hơi \"mình dây\" nên cần gia đình vỗ về yêu thương, nhất là vỗ béo :)))','dog');
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
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sponsors`
--

LOCK TABLES `sponsors` WRITE;
/*!40000 ALTER TABLE `sponsors` DISABLE KEYS */;
INSERT INTO `sponsors` VALUES (10,'quynh','trần','123 trần hưng đạo','j@gmail.com','091239812'),(11,'Vuot','Nguyen','Hoàng Cung','petcare@gmail.com','02466508126'),(12,'mingh','nguyen','123 hà nội','b@mi.com','09123979'),(13,'Vu','Le Huy','Thanh Hoa','vudeptrai@gmail.com','0123456789');
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
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'guest',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (15,'admin','$2b$12$FxEYx3gt8G8Vv.IxwX0BIOxHXb7htJTkKAlYZCvmFWh4IzFE9XM.e','Super','Admin','0123456789','admin@gmail.com','admin'),(16,'volunteer','$2b$12$OYf.i4.L4K5yg.UV/ksf5eIJpAgUBs/Jilon4sebiuaO6cskaUCa.','Tôi là','Volunteer','0987654321','volunteer@gmail.com','volunteer'),(17,'guest','$2b$12$EENCTdUa7YXshV1MKEyaGeDrtsxU6CQkXM/0EhBYSklzBpQ99Uz5i','Tôi là','Guest','0123456987','guest@gmail.com','guest');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinary_clinic`
--

DROP TABLE IF EXISTS `veterinary_clinic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinary_clinic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinary_clinic`
--

LOCK TABLES `veterinary_clinic` WRITE;
/*!40000 ALTER TABLE `veterinary_clinic` DISABLE KEYS */;
INSERT INTO `veterinary_clinic` VALUES (16,'Bệnh viện thú y nonae','240 Âu Cơ, Tây Hồ, Hà Nội','0908428882','pethealth@gmail.com'),(17,'Bệnh viện thú cưng Pet Mart','242 Nguyễn Trãi, Thanh Xuân','02471069906','petmart@gmail.com'),(18,'Bệnh viện thú y Hà Nội Hải Đăng PetCare','Số 14, Ngõ 102 Khuất Duy Tiến.','0964004115','petcare@gmail.com'),(19,'Phòng khám thú y Hà Nội Dr.Hai','2F Hoàng Hoa Thám','02466508126','haido@yahoo.com');
/*!40000 ALTER TABLE `veterinary_clinic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_schedule`
--

DROP TABLE IF EXISTS `work_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work_schedule` (
  `user_id` int NOT NULL,
  `working_day` date NOT NULL,
  `working_shift` int DEFAULT NULL,
  KEY `fk_user_time_idx` (`user_id`),
  CONSTRAINT `fk_user_time` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_schedule`
--

LOCK TABLES `work_schedule` WRITE;
/*!40000 ALTER TABLE `work_schedule` DISABLE KEYS */;
INSERT INTO `work_schedule` VALUES (16,'2021-08-18',1),(16,'2021-08-19',2),(16,'2021-08-20',2),(16,'2021-08-21',1),(16,'2021-08-22',NULL),(16,'2021-08-23',NULL);
/*!40000 ALTER TABLE `work_schedule` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-15 20:04:49
