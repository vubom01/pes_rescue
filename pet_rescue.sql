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
)

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
)

CREATE TABLE `pet_images` (
  `pet_id` int NOT NULL,
  `url` varchar(255) NOT NULL,
  KEY `fk_image_pet_idx` (`pet_id`),
  CONSTRAINT `fk_image_pet` FOREIGN KEY (`pet_id`) REFERENCES `pets` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
)
INSERT INTO `pet_images` VALUES (1,'https://www.facebook.com'),(1,'http://res.cloudinary.com/pet-rescue/image/upload/v1627379486/pet-rescue/1/dduj9m1ajy7m6rrarzug.jpg');

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
)
INSERT INTO `pets` VALUES (1,'a','a','a','a',1,'a','a');

CREATE TABLE `sponsors` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
)

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
)
INSERT INTO `users` VALUES (2,'test','$2b$12$Bi5b9aGYwlSk0nqGzJnjc.VRBJTXOhe84OZrKe2G5q6GWj8j0kfDC','admin','string','string','string','string'),(3,'huuvuot','$2b$12$SXWdF/8ZHtI434prjAqdFOiHuXKsjmGWbl3UBwjxUgCS54toTuaQW','volunteer','string','string','string','string');

CREATE TABLE `veterinarians` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `work_in_week` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE `work_schedule` (
  `user_id` int NOT NULL,
  `working_shift` varchar(255) NOT NULL,
  `working_day` date NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT 'registered',
  KEY `fk_user_time_idx` (`user_id`),
  CONSTRAINT `fk_user_time` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
)
INSERT INTO `work_schedule` VALUES (3,'0','2021-03-25','registered'),(3,'0','2021-03-25','registered'),(3,'0','2021-07-28','registered');