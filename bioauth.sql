-- phpMyAdmin SQL Dump
-- version 4.7.6
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 21, 2023 at 09:10 AM
-- Server version: 8.0.27
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bioauth`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `name` varchar(500) NOT NULL,
  `email` varchar(500) NOT NULL,
  `fathername` varchar(500) NOT NULL,
  `mothername` varchar(500) NOT NULL,
  `address` varchar(500) NOT NULL,
  `isnew` int DEFAULT '2',
  `status` int DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `fathername`, `mothername`, `address`, `isnew`, `status`) VALUES
(10, 'Candice Leblanc', 'govata@mailinator.com', 'Reagan Oliver', 'Yen Stokes', 'Lorem proident cons', 0, 1),
(11, 'Reese Hardin', 'nymomefuq@mailinator.com', 'Nola Hayes', 'Travis Mercado', 'Maxime dignissimos l', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `watcher`
--

CREATE TABLE `watcher` (
  `id` int NOT NULL,
  `userid` int NOT NULL,
  `name` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL,
  `isNewUserRegistered` int NOT NULL,
  `status` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `watcher`
--

INSERT INTO `watcher` (`id`, `userid`, `name`, `email`, `password`, `isNewUserRegistered`, `status`) VALUES
(1, 1, 'Anupama Parameshwaran', 'test1@gmail.com', 'password', 0, 1),
(2, 2, 'Rakul Preet Singh', 'test2@gmail.com', 'password', 0, 1),
(3, 3, 'Sushant Singh Rajput', 'test3@gmail.com', 'password', 0, 1),
(4, 4, 'Priya Vadlamani', 'test4@gmail.com', 'password', 0, 1),
(5, 77, 'asdcasd', 'asckj', 'klacml', 1, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `watcher`
--
ALTER TABLE `watcher`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `watcher`
--
ALTER TABLE `watcher`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
