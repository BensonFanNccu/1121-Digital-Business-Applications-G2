CREATE DATABASE  IF NOT EXISTS `project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 34.80.114.185    Database: project
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.20.04.1

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
-- Table structure for table `airplanetype`
--

DROP TABLE IF EXISTS `airplanetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airplanetype` (
  `AirplaneTypeID` int NOT NULL AUTO_INCREMENT,
  `SeatNumber` int NOT NULL,
  PRIMARY KEY (`AirplaneTypeID`),
  UNIQUE KEY `AirplaneTypeID_UNIQUE` (`AirplaneTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airplanetype`
--

LOCK TABLES `airplanetype` WRITE;
/*!40000 ALTER TABLE `airplanetype` DISABLE KEYS */;
INSERT INTO `airplanetype` VALUES (1,180),(2,188);
/*!40000 ALTER TABLE `airplanetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `LastName` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `PhoneNumber` varchar(20) NOT NULL,
  `Birthday` date NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `LTV` double DEFAULT NULL,
  `PCV` double DEFAULT NULL,
  `RFM` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CustomerID`),
  UNIQUE KEY `CustomerID_UNIQUE` (`CustomerID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'chen','yen','male','0912345678','2000-03-05','yen@gmail.com','台北市文山區指南路二段64號',55973.61187051206,37434,'5'),(2,'fan','benson','male','0987654321','2001-01-01','benson@gmail.com','台北市信義區信義路五段7號',44550.42577448919,17034,'4'),(3,'rose','mary','female','09147258369','2000-01-01','mary@gmail.com','台中市中區中山路20號',24750.236541382885,14280,'3'),(4,'liu','yu','male','09258369147','1999-01-01','yu@gmail.com','台南市安平區延平街',54831.29326090977,28968,'5'),(5,'wan','tim','male','09369258147','1999-01-02','tim@gmail.com','新北市板橋區',0,6120,'2'),(6,'chen','ting','male','09147369258','2002-01-01','ting@gmail.com','高雄市左營區',26654.10089072003,7140,'1'),(7,'lin','jenny','female','09465987132','2003-01-01','jenny@gmail.com','桃園市中壢區',39981.15133608004,15198,'3');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `FlightID` int NOT NULL AUTO_INCREMENT,
  `AirplaneTypeID` int NOT NULL,
  `Origin` varchar(45) NOT NULL,
  `Destination` varchar(45) NOT NULL,
  `DepartureTime` varchar(45) NOT NULL,
  `ArrivalTime` varchar(45) NOT NULL,
  `FlightCode` varchar(45) NOT NULL,
  PRIMARY KEY (`FlightID`),
  UNIQUE KEY `FlightID_UNIQUE` (`FlightID`),
  KEY `AirplaneTypeID_idx` (`AirplaneTypeID`),
  CONSTRAINT `AirplaneTypeID_flight` FOREIGN KEY (`AirplaneTypeID`) REFERENCES `airplanetype` (`AirplaneTypeID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,1,'TPE','NRT','10:00','13:00','MM620');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historicalprice`
--

DROP TABLE IF EXISTS `historicalprice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historicalprice` (
  `Date` date NOT NULL,
  `FlightID` int NOT NULL,
  `Price` varchar(45) NOT NULL,
  PRIMARY KEY (`Date`,`FlightID`),
  KEY `flightID_idx` (`FlightID`),
  CONSTRAINT `flightID_hp` FOREIGN KEY (`FlightID`) REFERENCES `flight` (`FlightID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historicalprice`
--

LOCK TABLES `historicalprice` WRITE;
/*!40000 ALTER TABLE `historicalprice` DISABLE KEYS */;
INSERT INTO `historicalprice` VALUES ('2023-12-05',1,'5000'),('2023-12-11',1,'6400');
/*!40000 ALTER TABLE `historicalprice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelparameter`
--

DROP TABLE IF EXISTS `modelparameter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelparameter` (
  `ParameterID` int NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Demand` double DEFAULT NULL,
  `AbsentRate` double DEFAULT NULL,
  `FlightID` int NOT NULL,
  PRIMARY KEY (`ParameterID`),
  UNIQUE KEY `ParameterID_UNIQUE` (`ParameterID`),
  KEY `FlightID_idx` (`FlightID`),
  CONSTRAINT `FlightID_para` FOREIGN KEY (`FlightID`) REFERENCES `flight` (`FlightID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelparameter`
--

LOCK TABLES `modelparameter` WRITE;
/*!40000 ALTER TABLE `modelparameter` DISABLE KEYS */;
INSERT INTO `modelparameter` VALUES (1,'2023-12-01',150,0.08,1),(2,'2023-12-05',140,0.05,1),(3,'2023-12-11',160,0.1,1),(4,'2023-12-25',180,0.09,1),(5,'2023-12-25',180,0.09,1),(6,'2023-12-25',180,0.09,1),(7,'2023-12-25',180,0.09,1),(8,'2023-12-25',180,0.09,1),(9,'2023-12-25',180,0.09,1),(10,'2023-12-25',180,0.09,1),(11,'2023-12-25',180,0.09,1),(12,'2023-12-25',180,0.09,1),(13,'2023-12-25',180,0.09,1),(14,'2023-12-25',180,0.09,1),(15,'2023-12-25',180,0.09,1),(16,'2023-12-25',180,0.09,1),(17,'2023-12-25',180,0.09,1),(18,'2023-12-25',180,0.09,1),(19,'2023-12-25',180,0.09,1);
/*!40000 ALTER TABLE `modelparameter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `OrderID` int NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `PriceLevel` varchar(45) NOT NULL,
  `SeatID` int NOT NULL,
  `CustomerID` int NOT NULL,
  `FlightID` int NOT NULL,
  `Status` varchar(45) NOT NULL,
  `Amount` int NOT NULL,
  PRIMARY KEY (`OrderID`),
  UNIQUE KEY `OrderID_UNIQUE` (`OrderID`),
  KEY `CustomerID_idx` (`CustomerID`),
  KEY `FlightID_idx` (`FlightID`),
  KEY `ticketPrice_order_idx` (`PriceLevel`,`Date`,`FlightID`),
  CONSTRAINT `CustomerID_order` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`CustomerID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FlightID_order` FOREIGN KEY (`FlightID`) REFERENCES `flight` (`FlightID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `TicketPrice_order` FOREIGN KEY (`PriceLevel`, `Date`, `FlightID`) REFERENCES `ticketprice` (`PriceLevel`, `Date`, `FlightID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=144 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2023-12-01','A',1,1,1,'OK',1),(2,'2023-12-05','B',5,6,1,'OK',1),(3,'2023-12-11','A',11,2,1,'OK',1),(4,'2023-08-01','C',8,5,1,'OK',1),(5,'2023-09-01','A',9,3,1,'OK',1),(6,'2022-12-25','A',25,1,1,'OK',1),(7,'2023-02-01','A',2,4,1,'OK',1),(8,'2023-12-01','D',10,2,1,'OK',1),(9,'2023-12-01','C',20,3,1,'OK',1),(10,'2023-12-12','A',12,7,1,'OK',1),(11,'2023-12-25','A',25,1,1,'OK',1),(12,'2022-12-01','B',12,2,1,'OK',1),(13,'2022-11-01','C',11,3,1,'OK',1),(14,'2022-10-01','E',10,4,1,'OK',1),(15,'2023-01-01','D',1,7,1,'OK',1),(16,'2023-04-01','A',4,1,1,'OK',1),(17,'2023-07-01','A',7,1,1,'OK',1),(18,'2023-03-02','B',32,1,1,'OK',1),(19,'2023-02-02','C',22,2,1,'OK',1),(20,'2023-05-05','B',55,4,1,'OK',1),(21,'2023-11-01','A',11,4,1,'OK',1),(22,'2023-12-01','B',2,4,1,'OK',1),(23,'2023-12-01','E',3,7,1,'OK',1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seat`
--

DROP TABLE IF EXISTS `seat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seat` (
  `SeatID` int NOT NULL AUTO_INCREMENT,
  `Date` date NOT NULL,
  `Status` varchar(45) NOT NULL,
  PRIMARY KEY (`SeatID`,`Date`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seat`
--

LOCK TABLES `seat` WRITE;
/*!40000 ALTER TABLE `seat` DISABLE KEYS */;
INSERT INTO `seat` VALUES (1,'2023-12-01','ordered'),(2,'2023-02-01','ordered'),(2,'2023-12-01','ordered'),(3,'2023-12-01','ordered'),(4,'2023-12-01','available'),(5,'2023-12-01','available'),(5,'2023-12-05','ordered'),(8,'2023-08-01','ordered'),(9,'2023-09-01','ordered'),(10,'2023-12-01','ordered'),(10,'2023-12-11','available'),(11,'2023-12-11','ordered'),(12,'2023-12-12','ordered'),(20,'2023-12-01','ordered'),(25,'2022-12-25','ordered');
/*!40000 ALTER TABLE `seat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticketprice`
--

DROP TABLE IF EXISTS `ticketprice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticketprice` (
  `PriceLevel` varchar(10) NOT NULL,
  `Date` date NOT NULL,
  `FlightID` int NOT NULL,
  `Price` double NOT NULL,
  `Amount` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`PriceLevel`,`Date`,`FlightID`),
  KEY `FlightID_tp_idx` (`FlightID`),
  CONSTRAINT `FlightID_tp` FOREIGN KEY (`FlightID`) REFERENCES `flight` (`FlightID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketprice`
--

LOCK TABLES `ticketprice` WRITE;
/*!40000 ALTER TABLE `ticketprice` DISABLE KEYS */;
INSERT INTO `ticketprice` VALUES ('A','2022-12-25',1,7600,'15'),('A','2023-01-19',1,6933,'19'),('A','2023-02-01',1,7000,'20'),('A','2023-02-19',1,6933,'19'),('A','2023-03-19',1,6933,'19'),('A','2023-04-01',1,7400,'25'),('A','2023-04-19',1,6933,'19'),('A','2023-05-19',1,6933,'19'),('A','2023-06-19',1,6933,'19'),('A','2023-07-01',1,7600,'30'),('A','2023-07-19',1,6933,'19'),('A','2023-08-19',1,6933,'19'),('A','2023-09-01',1,7500,'10'),('A','2023-09-19',1,6933,'19'),('A','2023-10-19',1,6933,'19'),('A','2023-11-01',1,7400,'20'),('A','2023-11-19',1,6933,'19'),('A','2023-12-01',1,7200,'10'),('A','2023-12-05',1,7100,'10'),('A','2023-12-11',1,7200,'10'),('A','2023-12-12',1,7500,'10'),('A','2023-12-19',1,6933,'19'),('A','2023-12-25',1,7500,'20'),('A','2023-12-29',1,8760,'18.0'),('B','2022-12-01',1,6800,'15'),('B','2023-01-15',1,6376,'32'),('B','2023-02-15',1,6376,'32'),('B','2023-03-02',1,7000,'15'),('B','2023-03-15',1,6376,'32'),('B','2023-04-15',1,6376,'32'),('B','2023-05-05',1,7000,'25'),('B','2023-05-15',1,6376,'32'),('B','2023-06-15',1,6376,'32'),('B','2023-07-15',1,6376,'32'),('B','2023-08-15',1,6376,'32'),('B','2023-09-15',1,6376,'32'),('B','2023-10-15',1,6376,'32'),('B','2023-11-15',1,6376,'32'),('B','2023-12-01',1,7000,'20'),('B','2023-12-05',1,7000,'20'),('B','2023-12-15',1,6376,'32'),('B','2023-12-29',1,7590,'36.0'),('C','2022-11-01',1,6000,'10'),('C','2023-01-16',1,5258,'51'),('C','2023-02-02',1,5000,'10'),('C','2023-02-16',1,5258,'51'),('C','2023-03-16',1,5258,'51'),('C','2023-04-16',1,5258,'51'),('C','2023-05-16',1,5258,'51'),('C','2023-06-16',1,5258,'51'),('C','2023-07-16',1,5258,'51'),('C','2023-08-01',1,6000,'20'),('C','2023-08-16',1,5258,'51'),('C','2023-09-16',1,5258,'51'),('C','2023-10-16',1,5258,'51'),('C','2023-11-16',1,5258,'51'),('C','2023-12-01',1,6500,'30'),('C','2023-12-16',1,5258,'51'),('C','2023-12-29',1,5493,'54.0'),('D','2023-01-01',1,4400,'5'),('D','2023-01-09',1,4050,'2'),('D','2023-02-09',1,4050,'2'),('D','2023-03-09',1,4050,'2'),('D','2023-04-09',1,4050,'2'),('D','2023-05-09',1,4050,'2'),('D','2023-06-09',1,4050,'2'),('D','2023-07-09',1,4050,'2'),('D','2023-08-09',1,4050,'2'),('D','2023-09-09',1,4050,'2'),('D','2023-10-09',1,4050,'2'),('D','2023-11-09',1,4050,'2'),('D','2023-12-01',1,4500,'5'),('D','2023-12-09',1,4050,'2'),('D','2023-12-29',1,4088,'0.0'),('E','2022-10-01',1,4000,'5'),('E','2023-01-04',1,3198,'71'),('E','2023-02-04',1,3198,'71'),('E','2023-03-04',1,3198,'71'),('E','2023-04-04',1,3198,'71'),('E','2023-05-04',1,3198,'71'),('E','2023-06-04',1,3198,'71'),('E','2023-07-04',1,3198,'71'),('E','2023-08-04',1,3198,'71'),('E','2023-09-04',1,3198,'71'),('E','2023-10-04',1,3198,'71'),('E','2023-11-04',1,3198,'71'),('E','2023-12-01',1,3000,'5'),('E','2023-12-04',1,3198,'71'),('E','2023-12-29',1,2920,'72.0');
/*!40000 ALTER TABLE `ticketprice` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-29 10:43:51
