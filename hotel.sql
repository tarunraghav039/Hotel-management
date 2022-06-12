-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Jun 12, 2022 at 07:46 AM
-- Server version: 8.0.18
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `hotel_table`
--

DROP TABLE IF EXISTS `hotel_table`;
CREATE TABLE IF NOT EXISTS `hotel_table` (
  `roomid` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `mob_no` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `room_type` varchar(30) NOT NULL,
  `no_of_days` int(11) NOT NULL,
  `check_in` varchar(30) NOT NULL,
  `t_bill` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hotel_table`
--

INSERT INTO `hotel_table` (`roomid`, `name`, `mob_no`, `address`, `room_type`, `no_of_days`, `check_in`, `t_bill`) VALUES
(14, 'Tharun Raghav SV', '6383187673', 'KK - Nagar', 'General', 4, '9', 2800);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
