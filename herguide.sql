-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: herguide
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `questions_log`
--

DROP TABLE IF EXISTS `questions_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` text,
  `answer` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions_log`
--

LOCK TABLES `questions_log` WRITE;
/*!40000 ALTER TABLE `questions_log` DISABLE KEYS */;
INSERT INTO `questions_log` VALUES (1,'Test Q','Test A','2025-07-06 12:10:02'),(2,'Test Q','Test A','2025-07-06 12:12:20'),(3,'Test Q','Test A','2025-07-06 12:13:22'),(4,'Test Q','Test A','2025-07-06 12:13:37'),(5,'Test Q','Test A','2025-07-06 12:13:46'),(6,'Test Q','Test A','2025-07-06 12:13:46'),(7,'Test Q','Test A','2025-07-06 12:16:20'),(8,'Test Q','Test A','2025-07-06 12:17:12'),(9,'Test Q','Test A','2025-07-06 12:17:19'),(10,'Test Q','Test A','2025-07-06 12:17:26'),(11,'Test Q','Test A','2025-07-06 12:17:33'),(12,'Mujhe loan kaise milega?','Aap PM Mudra Yojana ke liye apply kar sakti hain.','2025-07-06 13:17:21'),(13,'मुझे लोन कैसे मिलेगा?','आप मुद्रा योजना के लिए अप्लाई कर सकती हैं।','2025-07-06 14:03:23'),(14,'लोन कैसे ले','मुद्रा लोन योजना','2025-07-06 16:44:39'),(15,'एमी क्या होती है','वित्तीय योजनाएं','2025-07-06 17:08:29'),(16,'लोन क्या होता है','मुद्रा लोन योजना','2025-07-06 17:19:26');
/*!40000 ALTER TABLE `questions_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skillher_profiles`
--

DROP TABLE IF EXISTS `skillher_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skillher_profiles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `business` varchar(200) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skillher_profiles`
--

LOCK TABLES `skillher_profiles` WRITE;
/*!40000 ALTER TABLE `skillher_profiles` DISABLE KEYS */;
INSERT INTO `skillher_profiles` VALUES (1,'सीमा','दिल्ली','सिलाई का काम','9876543210','2025-07-06 14:03:23'),(2,'सीमा','उत्तर प्रदेश','सिलाई','9983738220','2025-07-06 15:35:05'),(3,'सीमा','उत्तर प्रदेश','सिलाई','9983738220','2025-07-06 16:37:31'),(4,'राधा','उत्तर प्रदेश','मेहँदी','9983738220','2025-07-06 16:42:55'),(5,'नीता','उत्तर प्रदेश','पापड़ / अचार / मसाले बनाना और बेचना','9878673451','2025-07-06 17:10:00'),(6,'भावना','राजस्थान','थैली बनाना','9087562912','2025-07-06 17:18:22');
/*!40000 ALTER TABLE `skillher_profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suraksha_reports`
--

DROP TABLE IF EXISTS `suraksha_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suraksha_reports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` text,
  `flagged` tinyint(1) DEFAULT NULL,
  `reason` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suraksha_reports`
--

LOCK TABLES `suraksha_reports` WRITE;
/*!40000 ALTER TABLE `suraksha_reports` DISABLE KEYS */;
INSERT INTO `suraksha_reports` VALUES (1,'जल्दी भुगतान करें वरना अकाउंट बंद हो जाएगा',1,'संभावित स्कैम','2025-07-06 14:03:23'),(2,'आईएफ थे स्किन में डबल कर सकता हूं',0,'कोई स्कैम संकेत नहीं मिला','2025-07-06 16:58:38'),(3,'मैं आपके पैसे दो दिन में डबल कर सकता हूं',1,'संभावित स्कैम कीवर्ड मिला','2025-07-06 16:58:56'),(4,'मैं आपका दोस्त बात कर रहा हूं क्या आप मुझे हर रुपए अभी भेज सकती हैं',0,'कोई स्कैम संकेत नहीं मिला','2025-07-06 17:10:18'),(5,'आपका दोस्त बात कर रहा हूं क्या आप मुझे अभी की अभी 10000 रुपए भेज सकती हैं',0,'कोई स्कैम संकेत नहीं मिला','2025-07-06 17:10:34'),(6,'मैं आपके पास की बैंक से बोल रहा हूं आपके बैंक के अंदर कुछ दिक्कत आ गई है तो आपको तुरंत ही 10000 रुपए जमा करवाने होंगे',0,'कोई स्कैम संकेत नहीं मिला','2025-07-06 17:18:56'),(7,'मेरा नाम मुकेश',0,'कोई स्कैम संकेत नहीं मिला','2025-07-06 17:28:18'),(8,'मेरा नाम मुकेश है और मैं फटीचर बैंक से बात कर रहा हूं और',0,'कोई स्कैम संकेत नहीं मिला','2025-07-06 17:28:29');
/*!40000 ALTER TABLE `suraksha_reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yojana_recommendations`
--

DROP TABLE IF EXISTS `yojana_recommendations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yojana_recommendations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `salary` float DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `suggestion` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yojana_recommendations`
--

LOCK TABLES `yojana_recommendations` WRITE;
/*!40000 ALTER TABLE `yojana_recommendations` DISABLE KEYS */;
INSERT INTO `yojana_recommendations` VALUES (1,'राधा',35,200000,'उत्तर प्रदेश','जनधन योजना','2025-07-06 14:03:23'),(2,'राधा',23,8000,'महाराष्ट्र','राधा जी, आपकी जानकारी के अनुसार, आप महाराष्ट्र राज्य में रहने वाले हैं और आपकी उम्र 23 वर्ष है। आप प्रधानमंत्री जन धन योजना, मुद्रा लोन योजना, और सुकन्या योजना (यदि applicable) के लिए पात्र हो सकते हैं।','2025-07-06 16:43:54'),(3,'सविता',25,6000,'बिहार','सविता जी, आपकी जानकारी के अनुसार, आप बिहार राज्य में रहने वाले हैं और आपकी उम्र 25 वर्ष है। आप प्रधानमंत्री जन धन योजना, मुद्रा लोन योजना, और सुकन्या योजना (यदि applicable) के लिए पात्र हो सकते हैं।','2025-07-06 17:01:15'),(4,'रेखा',30,10000,'अन्य','रेखा जी, आपकी जानकारी के अनुसार, आप अन्य राज्य में रहने वाले हैं और आपकी उम्र 30 वर्ष है। आप प्रधानमंत्री जन धन योजना, मुद्रा लोन योजना, और सुकन्या योजना (यदि applicable) के लिए पात्र हो सकते हैं।','2025-07-06 17:08:54'),(5,'भावना',31,4000,'राजस्थान','भावना जी, आपकी जानकारी के अनुसार, आप राजस्थान राज्य में रहने वाले हैं और आपकी उम्र 31 वर्ष है। आप प्रधानमंत्री जन धन योजना, मुद्रा लोन योजना, और सुकन्या योजना (यदि applicable) के लिए पात्र हो सकते हैं।','2025-07-06 17:17:37');
/*!40000 ALTER TABLE `yojana_recommendations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-07 10:21:41
