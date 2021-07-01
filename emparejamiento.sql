-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 30, 2021 at 11:03 PM
-- Server version: 10.3.29-MariaDB-0+deb10u1
-- PHP Version: 7.3.27-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `emparejamiento`
--

-- --------------------------------------------------------

--
-- Table structure for table `hechos`
--

CREATE TABLE `hechos` (
  `folio` int(11) NOT NULL,
  `emisora` varchar(20) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `titulos` decimal(20,0) DEFAULT NULL,
  `comprador` varchar(5) DEFAULT NULL,
  `folio_comprador` int(11) DEFAULT NULL,
  `vendedor` varchar(5) DEFAULT NULL,
  `folio_vendedor` int(11) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `p_compra`
--

CREATE TABLE `p_compra` (
  `folio` int(11) NOT NULL,
  `emisora` varchar(20) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `titulos` decimal(20,0) DEFAULT NULL,
  `casa` varchar(5) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `p_compra`
--

INSERT INTO `p_compra` (`folio`, `emisora`, `precio`, `titulos`, `casa`, `fecha_hora`) VALUES
(4, 'AMX_L', '10.00', '1000', 'IXE', '2021-02-27 21:57:40'),
(5, 'AMX_L', '10.00', '943', 'IXE', '2021-02-27 21:57:40'),
(6, 'AMX_L', '10.00', '306', 'IXE', '2021-02-27 21:57:40');

-- --------------------------------------------------------

--
-- Table structure for table `p_venta`
--

CREATE TABLE `p_venta` (
  `folio` int(11) NOT NULL,
  `emisora` varchar(20) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `titulos` decimal(20,0) DEFAULT NULL,
  `casa` varchar(5) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `p_venta`
--

INSERT INTO `p_venta` (`folio`, `emisora`, `precio`, `titulos`, `casa`, `fecha_hora`) VALUES
(1, 'AMX_L', '10.00', '133', 'JPM', '2021-02-27 19:09:16'),
(2, 'AMX_L', '10.00', '869', 'JPM', '2021-02-27 19:09:16'),
(3, 'AMX_L', '10.00', '244', 'JPM', '2021-02-27 19:09:16'),
(4, 'AMX_L', '10.00', '816', 'JPM', '2021-02-27 21:57:40'),
(5, 'AMX_L', '10.00', '264', 'JPM', '2021-02-27 21:57:40'),
(6, 'AMX_L', '10.00', '643', 'JPM', '2021-02-27 21:57:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hechos`
--
ALTER TABLE `hechos`
  ADD PRIMARY KEY (`folio`);

--
-- Indexes for table `p_compra`
--
ALTER TABLE `p_compra`
  ADD PRIMARY KEY (`folio`);

--
-- Indexes for table `p_venta`
--
ALTER TABLE `p_venta`
  ADD PRIMARY KEY (`folio`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hechos`
--
ALTER TABLE `hechos`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `p_compra`
--
ALTER TABLE `p_compra`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `p_venta`
--
ALTER TABLE `p_venta`
  MODIFY `folio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
