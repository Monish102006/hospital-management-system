-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital_db
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (1,1,1,'2024-01-10','Completed'),(2,2,2,'2024-01-11','Completed'),(3,3,3,'2024-01-12','Completed'),(4,4,4,'2024-01-13','Completed'),(5,5,1,'2024-01-14','Cancelled'),(6,6,5,'2024-01-15','Completed'),(7,7,2,'2024-01-16','Scheduled'),(8,8,3,'2024-01-17','Scheduled'),(9,1,1,'2024-01-10','Completed'),(10,2,2,'2024-01-11','Completed'),(11,3,3,'2024-01-12','Completed'),(12,4,4,'2024-01-13','Completed'),(13,5,1,'2024-01-14','Cancelled'),(14,6,5,'2024-01-15','Completed'),(15,7,2,'2024-01-16','Scheduled'),(16,8,3,'2024-01-17','Scheduled'),(18,8,5,'2024-5-28','Scheduled');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Cardiology','Block-A'),(2,'Neurology','Block-B'),(3,'Orthopedics','Block-C'),(4,'Pediatrics','Block-D'),(5,'General Medicine','Block-E');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (1,'Dr.Arjun Sharma','Cardiologist','9876543210',1),(2,'Dr.Priya Mehta','Neurologist','9846743410',2),(3,'Dr.Ravi Kumar','Orthopedic Surgeon','8875543212',3),(4,'Dr.Sneha Reddy','Pediatrician','7976643710',4),(5,'Dr.Vikram Nair','General Physician','9949543210',5);
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'Rahul Verma',35,'MALE','9001234567','O+'),(2,'Anita Singh',28,'FEMALE','9001234568','A+'),(3,'Suresh Babu',52,'MALE','9001234569','B+'),(4,'Kavya Nair',7,'FEMALE','9001234570','AB+'),(5,'Mohan Das',45,'MALE','9001234571','O-'),(6,'Lakshmi Rao',31,'FEMALE','9001234572','A-'),(7,'Arun Patel',60,'MALE','9001234573','B-'),(8,'Divya Krishnan',22,'FEMALE','9001234574','O+');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `prescriptions`
--

LOCK TABLES `prescriptions` WRITE;
/*!40000 ALTER TABLE `prescriptions` DISABLE KEYS */;
INSERT INTO `prescriptions` VALUES (1,1,'Aspirin','75mg once daily','Take after food'),(2,1,'Atorvastatin','10mg at night','Avoid fatty food'),(3,2,'Gabapentin','300mg twice daily','Do not skip doses'),(4,3,'Ibuprofen','400mg thrice daily','Take with food'),(5,4,'Amoxicillin','250mg thrice daily','Complete full course'),(6,6,'Paracetamol','500mg as needed','Max 3 times a day');
/*!40000 ALTER TABLE `prescriptions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-27 22:55:54
