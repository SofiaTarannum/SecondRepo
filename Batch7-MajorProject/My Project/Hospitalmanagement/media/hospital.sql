-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2023 at 10:43 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `mail` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`mail`, `password`) VALUES
('madhu@gmail.com', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `billings`
--

CREATE TABLE `billings` (
  `sid` int(100) NOT NULL,
  `rid` int(100) NOT NULL,
  `aid` int(100) NOT NULL,
  `cname` char(100) NOT NULL,
  `cdate` text NOT NULL,
  `dob` text NOT NULL,
  `age` int(10) NOT NULL,
  `fname` char(50) NOT NULL,
  `phone` int(10) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `docfee` int(100) NOT NULL,
  `room` int(100) NOT NULL,
  `medcost` int(100) NOT NULL,
  `charges` int(100) NOT NULL,
  `total` int(100) NOT NULL,
  `ddate` text NOT NULL,
  `billfile` varchar(100) DEFAULT NULL,
  `report` varchar(50) DEFAULT NULL,
  `print` int(10) NOT NULL,
  `mailsent` int(10) NOT NULL,
  `reportsent` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `billings`
--

INSERT INTO `billings` (`sid`, `rid`, `aid`, `cname`, `cdate`, `dob`, `age`, `fname`, `phone`, `mail`, `docfee`, `room`, `medcost`, `charges`, `total`, `ddate`, `billfile`, `report`, `print`, `mailsent`, `reportsent`) VALUES
(26, 124, 1, 'asdfg', '2023-03-16', '2023-03-08', 6, 'ee', 365654, 'vijay@gmail.com', 500, 100, 0, 0, 600, '2023-03-17', NULL, NULL, 0, 0, 0),
(27, 125, 2, 'asdfg', '2023-03-16', '2023-03-08', 6, 'ee', 365654, 'vijay@gmail.com', 500, 500, 0, 0, 1000, '2023-03-17', NULL, NULL, 0, 0, 0),
(28, 126, 3, 'asdfg', '2023-03-16', '2023-03-07', 14, 'ee', 365654, 'sofiatarannum17@gmail.com', 0, 0, 100, 100, 200, '2023-03-17', NULL, NULL, 0, 0, 0),
(29, 127, 4, 'asdfg', '2023-03-16', '2023-03-07', 14, 'ee', 365654, 'sofiatarannum17@gmail.com', 100, 0, 0, 0, 100, '2023-03-17', 'madhu_9nlLW3y.pdf', NULL, 0, 1, 0),
(60, 128, 5, 'sofia', '2023-03-16', '2023-03-07', 14, 'ee', 365654, 'sofiatarannum17@gmail.com', 500, 1000, 1500, 0, 3000, '2023-03-18', '128_fJD5Lji.pdf', 'RESUME_5GG8sI3.pdf', 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `sno` int(11) NOT NULL,
  `aname` char(50) NOT NULL,
  `appaadhar` bigint(12) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` int(10) NOT NULL,
  `gender` char(20) NOT NULL,
  `dob` text NOT NULL,
  `age` int(10) NOT NULL,
  `address` varchar(60) NOT NULL,
  `city` char(30) NOT NULL,
  `pin` int(20) NOT NULL,
  `state` char(30) NOT NULL,
  `file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`sno`, `aname`, `appaadhar`, `email`, `mobile`, `gender`, `dob`, `age`, `address`, `city`, `pin`, `state`, `file`) VALUES
(1, '', 12345678765432, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-02-03', 54, 'ghftr', 'fdres', 4352, 'khgf', ''),
(2, '', 123423456, 'madhumithauppala@gmail.com', 2147483647, 'female', '2023-02-01', 32, 'qwerw', 'dfres', 5463, 'khgf', ''),
(5, '', 12345678765432323, 'madhumithauppala@gmail.com', 54637899, 'female', '2023-02-17', 75, 'kjhg', 'kjhgfgh', 9875609, 'kjgfdfgh', ''),
(6, '', 2686122511, 'koushikyeluguri7@gmail.com', 232223, 'female', '2023-02-16', 4, 'ggsaygssggsgaygs', 'ghgggghggg', 505001, 'trrrarrrtar', ''),
(7, '', 855655565, 'vijay@gmail.com', 121121112, 'female', '2023-02-25', 4, 'nmnnysgysg', 'Karimnagar', 505001, 'trrrarrrtar', ''),
(9, '', 268612251112, 'mo@gmail.com', 2147483647, 'female', '2023-02-23', 45, 'ghgsgahg', 'Karimnagar', 505002, 'dfdsdf', ''),
(10, '', 268612251112, 'as@gmail.com', 2147483647, 'female', '2023-02-28', 36, 'ghdggeryr', 'Karimnagar', 505001, 'trrrarrrtar', ''),
(11, '', 1233, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-02-22', 45, 'sdsdsdd', 'Karimnagar', 12334, 'ap', ''),
(12, 'a', 111111111111, 'a@gmail.co', 1111111111, 'female', '2023-02-13', 12, 'fdfdfds', 'Karimnagar', 1212121, 'trrrarrrtar', 'xyz.png'),
(13, 'aqqq', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-02-14', 1, 'ss', 's', 1111, 's', 'xyz.png'),
(14, 'fgaffgfa', 111111111111, 'koushikyeluguri7@gmail.com', 2147483647, 'female', '2023-02-12', 4, 'aaa', 'Karimnagar', 11111, 'trrrarrrtar', 'xyz.png'),
(15, 'a', 111111111111, 'as@gmail.com', 2147483647, 'female', '2023-02-01', 4, 'aaa', 'Karimnagar', 11, 'trrrarrrtar', 'Resume.pdf'),
(16, 'fgaffgfa', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-02-16', 4, 'fgsffgsf', 'Karimnagar', 505001, 'trrrarrrtar', 'Noureen_yWjGqew.jpg'),
(17, 'fgaffgfa', 111111111111, 'as@gmail.com', 2147483647, 'female', '2023-03-16', 45, 'ffff', 'aaa', 1111111, 'sss', 'ilovepdf_merged (2).pdf'),
(18, 'sofia', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-03-02', 4, 'qqq', 'Karimnagar', 505001, 'ap', 'Electronic Sensors.pdf'),
(19, 'fgaffgfa', 111111111111, 'sofiatarannumkits@gmail.com', 2147483647, 'female', '2023-03-01', 36, 'hhhh', 'ghgggghggg', 505001, 'sss', 'Electronic Sensors.pdf'),
(20, 'abc', 123456778912, 'as@gmail.com', 232223, 'female', '2023-03-07', 36, 'bbbbbb', 'Karimnagar', 505001, 'dfdsdf', 'report.pdf'),
(21, 'zzz', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-03-03', 4, 'ffff', 'Karimnagar', 505001, 'ap', 'report_DuK6v0l.pdf'),
(22, 'fgaffgfa', 123456778912, 'vijay@gmail.com', 2147483647, 'female', '2023-03-09', 45, 'aaaa', 'Karimnagar', 505001, 'dfdsdf', 'report_qKqtzlI.pdf'),
(23, 'fgaffgfa', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-04-04', 36, 'aaa', 'Karimnagar', 505001, 'trrrarrrtar', 'Documents.pdf'),
(24, 'fgaffgfa', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-04-04', 36, 'aaa', 'Karimnagar', 505001, 'trrrarrrtar', 'Documents_5dQvE21.pdf'),
(25, 'xampp', 111111111111, 'sofiatarannum17@gmail.com', 2147483647, 'female', '2023-03-14', 45, 'jjjj', 'Karimnagar', 505001, 'Telangana', 'RESUME.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(10) NOT NULL,
  `cname` char(50) NOT NULL,
  `dob` text NOT NULL,
  `age` int(20) NOT NULL,
  `gender` char(50) NOT NULL,
  `cbloodgrp` varchar(20) NOT NULL,
  `fname` char(50) NOT NULL,
  `faadhno` bigint(12) NOT NULL,
  `mname` char(50) NOT NULL,
  `maadhno` bigint(12) NOT NULL,
  `phone` bigint(10) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `selecttype` int(30) NOT NULL,
  `rid` bigint(50) NOT NULL,
  `status` int(10) DEFAULT NULL,
  `aid` bigint(100) NOT NULL,
  `vacid` int(100) DEFAULT NULL,
  `vacname` varchar(100) DEFAULT NULL,
  `cdate` text NOT NULL,
  `billissue` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `cname`, `dob`, `age`, `gender`, `cbloodgrp`, `fname`, `faadhno`, `mname`, `maadhno`, `phone`, `mail`, `address`, `selecttype`, `rid`, `status`, `aid`, `vacid`, `vacname`, `cdate`, `billissue`) VALUES
(10, '', '0000-00-00', 0, '', '', '', 0, '', 0, 0, '', '', 0, 113, 1, 0, NULL, NULL, '0000-00-00', 1),
(46, 'asdfg', '2023-03-08', 6, 'Female', 'O+', 'ee', 757, 'qwert', 2244, 365654, 'vijay@gmail.com', '111', 0, 124, 1, 1, NULL, NULL, '2023-03-16', 1),
(47, 'asdfg', '2023-03-08', 6, 'Female', 'O+', 'ee', 757, 'qwert', 2244, 365654, 'vijay@gmail.com', '111', 0, 125, 1, 2, NULL, NULL, '2023-03-16', 1),
(48, 'asdfg', '2023-03-07', 14, 'Female', 'O+', 'ee', 13234, 'fdfd', 345, 365654, 'sofiatarannum17@gmail.com', 'ssss', 0, 126, NULL, 3, NULL, NULL, '2023-03-16', 1),
(49, 'asdfg', '2023-03-07', 14, 'Female', 'O+', 'ee', 13234, 'fdfd', 345, 365654, 'sofiatarannum17@gmail.com', 'ssss', 0, 127, NULL, 4, NULL, NULL, '2023-03-16', 1),
(50, 'sofia', '2023-03-07', 14, 'Female', 'O+', 'ee', 13234, 'fdfd', 345, 365654, 'sofiatarannum17@gmail.com', 'ssss', 0, 128, NULL, 5, NULL, NULL, '2023-03-16', 1),
(60, 'Madhu', '2023-03-01', 4, 'Female', 'O-', 'ee', 13234, 'fdfd', 2244, 365654, 'h@hhh.hhhh', 'ggg', 0, 130, 1, 8, NULL, NULL, '2023-03-16', 0),
(73, 'aaa', '', 1, 'Male', 'O+', '', 145678903214, '', 123456987789, 365654, 'sofiatarannum17@gmail.com', 'hhhh', 1, 131, 0, 9, 12, 'hh', '2023-03-18', 0);

-- --------------------------------------------------------

--
-- Table structure for table `userblood`
--

CREATE TABLE `userblood` (
  `sno` int(11) NOT NULL,
  `daadhno` bigint(12) NOT NULL,
  `dname` char(30) NOT NULL,
  `mail` varchar(11) NOT NULL,
  `phone` int(10) NOT NULL,
  `bloodgrp` varchar(10) NOT NULL,
  `age` int(20) NOT NULL,
  `dob` text NOT NULL,
  `gender` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userblood`
--

INSERT INTO `userblood` (`sno`, `daadhno`, `dname`, `mail`, `phone`, `bloodgrp`, `age`, `dob`, `gender`) VALUES
(1, 256665, 'abc', 'koushikyelu', 2147483647, 'o+', 4, '2023-02-18', 'female'),
(2, 12454454, 'abc', 'as@gmail.co', 45445445, 'o+', 4, '2023-02-01', 'female');

-- --------------------------------------------------------

--
-- Table structure for table `vaccines`
--

CREATE TABLE `vaccines` (
  `sid` int(30) NOT NULL,
  `vid` varchar(50) NOT NULL,
  `vname` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vaccines`
--

INSERT INTO `vaccines` (`sid`, `vid`, `vname`) VALUES
(13, '751', 'sss'),
(14, '149', 'mmm'),
(15, '789', 'lll'),
(16, '14', 'kk'),
(17, '501', 'ffff'),
(19, '777', 'hhh'),
(20, '888', 'jjj'),
(22, '178', 'kkl'),
(23, '454', 'klu'),
(24, '79', 'lku'),
(25, '75', 'io'),
(26, '77', 'lk'),
(27, '45', 'oo'),
(28, '8', 'ee'),
(29, '1', 't'),
(30, '756', 'jkl'),
(35, '12', 'hh'),
(36, '11', 'q'),
(37, '0555', 'eeee'),
(38, '1111l', 'lhh'),
(39, '1113', 'j'),
(40, '122', 'eee'),
(41, '099', 'ggg'),
(42, '11133', 'eeee'),
(43, '444', 'gg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`mail`);

--
-- Indexes for table `billings`
--
ALTER TABLE `billings`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userblood`
--
ALTER TABLE `userblood`
  ADD PRIMARY KEY (`sno`),
  ADD UNIQUE KEY `daadhno` (`daadhno`);

--
-- Indexes for table `vaccines`
--
ALTER TABLE `vaccines`
  ADD PRIMARY KEY (`sid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `billings`
--
ALTER TABLE `billings`
  MODIFY `sid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `userblood`
--
ALTER TABLE `userblood`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `vaccines`
--
ALTER TABLE `vaccines`
  MODIFY `sid` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
