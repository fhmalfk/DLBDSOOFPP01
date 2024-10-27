-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2024 at 05:08 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `habittrackerapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `habits`
--

CREATE TABLE `habits` (
  `id_habit` int(11) NOT NULL,
  `fk_period` int(11) NOT NULL,
  `name` text NOT NULL,
  `success` tinyint(1) NOT NULL,
  `createdAt` datetime NOT NULL,
  `nextTime` datetime NOT NULL,
  `streakCounter` int(11) NOT NULL,
  `streakHighscore` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `habits`
--

INSERT INTO `habits` (`id_habit`, `fk_period`, `name`, `success`, `createdAt`, `nextTime`, `streakCounter`, `streakHighscore`) VALUES
(1, 1, '10K Schritte', 0, '2024-09-25 16:09:31', '2024-10-23 16:09:31', 0, 12),
(2, 1, 'Kochen', 0, '2024-09-25 16:10:45', '2024-10-23 16:10:45', 0, 4),
(3, 1, 'Sportlich betaetigen', 0, '2024-09-25 16:10:45', '2024-10-23 16:10:45', 0, 7),
(4, 2, '100 Seiten lesen', 0, '2024-10-22 16:10:45', '2024-10-29 16:10:45', 1, 7),
(5, 3, 'Hund kaemmen', 0, '2024-09-14 16:10:45', '2024-09-22 16:10:45', 3, 3),
(6, 4, 'Staubsaugen', 0, '2024-10-22 16:10:45', '2024-10-23 16:10:45', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id_history` int(11) NOT NULL,
  `fk_habits` int(11) NOT NULL,
  `date` date NOT NULL,
  `success` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id_history`, `fk_habits`, `date`, `success`) VALUES
(1, 1, '2024-10-22', 1),
(2, 1, '2024-10-21', 1),
(3, 1, '2024-10-20', 1),
(4, 1, '2024-10-19', 1),
(5, 1, '2024-10-18', 1),
(6, 1, '2024-10-17', 0),
(7, 1, '2024-10-16', 1),
(8, 1, '2024-10-15', 1),
(9, 1, '2024-10-14', 1),
(10, 1, '2024-10-13', 1),
(11, 1, '2024-10-12', 1),
(12, 1, '2024-10-11', 1),
(13, 1, '2024-10-10', 1),
(14, 1, '2024-10-09', 1),
(15, 1, '2024-10-08', 1),
(16, 1, '2024-10-07', 1),
(17, 1, '2024-10-06', 1),
(18, 1, '2024-10-05', 1),
(19, 1, '2024-10-04', 0),
(20, 1, '2024-10-03', 1),
(21, 1, '2024-10-02', 1),
(22, 1, '2024-10-01', 1),
(23, 1, '2024-09-30', 0),
(24, 1, '2024-09-29', 1),
(25, 1, '2024-09-28', 1),
(26, 1, '2024-09-27', 1),
(27, 1, '2024-09-26', 1),
(28, 1, '2024-09-25', 0),
(29, 2, '2024-10-22', 0),
(30, 2, '2024-10-21', 1),
(31, 2, '2024-10-20', 1),
(32, 2, '2024-10-19', 1),
(33, 2, '2024-10-18', 1),
(34, 2, '2024-10-17', 0),
(35, 2, '2024-10-16', 1),
(36, 2, '2024-10-15', 1),
(37, 2, '2024-10-14', 1),
(38, 2, '2024-10-13', 0),
(39, 2, '2024-10-12', 1),
(40, 2, '2024-10-11', 1),
(41, 2, '2024-10-10', 1),
(42, 2, '2024-10-09', 1),
(43, 2, '2024-10-08', 0),
(44, 2, '2024-10-07', 1),
(45, 2, '2024-10-06', 1),
(46, 2, '2024-10-05', 1),
(47, 2, '2024-10-04', 0),
(48, 2, '2024-10-03', 1),
(49, 2, '2024-10-02', 1),
(50, 2, '2024-10-01', 1),
(51, 2, '2024-09-30', 0),
(52, 2, '2024-09-29', 1),
(53, 2, '2024-09-28', 0),
(54, 2, '2024-09-27', 1),
(55, 2, '2024-09-26', 0),
(56, 2, '2024-09-25', 0),
(57, 3, '2024-10-22', 1),
(58, 3, '2024-10-21', 1),
(59, 3, '2024-10-20', 1),
(60, 3, '2024-10-19', 1),
(61, 3, '2024-10-18', 1),
(62, 3, '2024-10-17', 0),
(63, 3, '2024-10-16', 1),
(64, 3, '2024-10-15', 1),
(65, 3, '2024-10-14', 1),
(66, 3, '2024-10-13', 1),
(67, 3, '2024-10-12', 1),
(68, 3, '2024-10-11', 1),
(69, 3, '2024-10-10', 1),
(70, 3, '2024-10-09', 0),
(71, 3, '2024-10-08', 0),
(72, 3, '2024-10-07', 1),
(73, 3, '2024-10-06', 1),
(74, 3, '2024-10-05', 1),
(75, 3, '2024-10-04', 0),
(76, 3, '2024-10-03', 1),
(77, 3, '2024-10-02', 1),
(78, 3, '2024-10-01', 1),
(79, 3, '2024-09-30', 0),
(80, 3, '2024-09-29', 1),
(81, 3, '2024-09-28', 1),
(82, 3, '2024-09-27', 1),
(83, 3, '2024-09-26', 0),
(84, 3, '2024-09-25', 0),
(85, 4, '2024-10-22', 1),
(86, 4, '2024-10-20', 1),
(87, 4, '2024-10-18', 1),
(88, 4, '2024-10-16', 1),
(89, 4, '2024-10-14', 1),
(90, 4, '2024-10-12', 0),
(91, 4, '2024-10-10', 1),
(92, 4, '2024-10-08', 1),
(93, 4, '2024-10-06', 1),
(94, 4, '2024-10-04', 1),
(95, 4, '2024-10-02', 1),
(96, 4, '2024-09-30', 1),
(97, 4, '2024-09-28', 1),
(98, 4, '2024-09-26', 0),
(99, 4, '2024-09-24', 0),
(100, 4, '2024-09-22', 1),
(101, 5, '2024-10-22', 1),
(102, 5, '2024-10-08', 1),
(103, 5, '2024-09-14', 1);

-- --------------------------------------------------------

--
-- Table structure for table `period`
--

CREATE TABLE `period` (
  `id_period` int(11) NOT NULL,
  `durationDays` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `period`
--

INSERT INTO `period` (`id_period`, `durationDays`) VALUES
(1, 1),
(2, 7),
(3, 14),
(4, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `habits`
--
ALTER TABLE `habits`
  ADD PRIMARY KEY (`id_habit`),
  ADD UNIQUE KEY `id_habit` (`id_habit`),
  ADD KEY `fk_period` (`fk_period`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id_history`),
  ADD UNIQUE KEY `id_history` (`id_history`),
  ADD KEY `fk_habits` (`fk_habits`);

--
-- Indexes for table `period`
--
ALTER TABLE `period`
  ADD PRIMARY KEY (`id_period`),
  ADD UNIQUE KEY `id_period` (`id_period`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `habits`
--
ALTER TABLE `habits`
  MODIFY `id_habit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id_history` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT for table `period`
--
ALTER TABLE `period`
  MODIFY `id_period` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `habits`
--
ALTER TABLE `habits`
  ADD CONSTRAINT `habits_ibfk_1` FOREIGN KEY (`fk_period`) REFERENCES `period` (`id_period`);

--
-- Constraints for table `history`
--
ALTER TABLE `history`
  ADD CONSTRAINT `history_ibfk_1` FOREIGN KEY (`fk_habits`) REFERENCES `habits` (`id_habit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
