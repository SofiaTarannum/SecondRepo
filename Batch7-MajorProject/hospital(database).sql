-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2023 at 09:04 PM
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
  `mail` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`mail`, `password`) VALUES
('sofiatarannumkits@gmail.com', 'hospital1234');

-- --------------------------------------------------------

--
-- Table structure for table `billings`
--

CREATE TABLE `billings` (
  `sid` int(10) NOT NULL,
  `rid` int(10) NOT NULL,
  `aid` int(10) NOT NULL,
  `cname` char(25) NOT NULL,
  `cdate` text NOT NULL,
  `dob` text NOT NULL,
  `age` int(2) NOT NULL,
  `fname` char(25) NOT NULL,
  `mname` char(25) NOT NULL,
  `phone` int(10) NOT NULL,
  `mail` varchar(30) NOT NULL,
  `docfee` int(5) NOT NULL,
  `room` int(5) NOT NULL,
  `medcost` int(5) NOT NULL,
  `charges` int(5) NOT NULL,
  `vaccost` int(5) NOT NULL,
  `total` int(5) NOT NULL,
  `ddate` text NOT NULL,
  `billfile` varchar(30) DEFAULT NULL,
  `vacbill` varchar(30) DEFAULT NULL,
  `report` varchar(30) DEFAULT NULL,
  `vacreport` varchar(30) DEFAULT NULL,
  `print` int(1) DEFAULT NULL,
  `printvac` int(1) DEFAULT NULL,
  `mailsent` int(1) NOT NULL,
  `reportsent` int(1) NOT NULL,
  `vacid` int(5) DEFAULT NULL,
  `vacname` varchar(10) DEFAULT NULL,
  `vacmailsent` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `billings`
--

INSERT INTO `billings` (`sid`, `rid`, `aid`, `cname`, `cdate`, `dob`, `age`, `fname`, `mname`, `phone`, `mail`, `docfee`, `room`, `medcost`, `charges`, `vaccost`, `total`, `ddate`, `billfile`, `vacbill`, `report`, `vacreport`, `print`, `printvac`, `mailsent`, `reportsent`, `vacid`, `vacname`, `vacmailsent`) VALUES
(62, 114, 1, 'sofia', '2023-03-27', '2023-03-08', 4, 'Ameer', '', 1234567891, 'sofiatarannum17@gmail.com', 500, 0, 0, 0, 0, 500, '2023-03-27', '114.pdf', NULL, 'Documentation-A', NULL, 1, NULL, 1, 1, NULL, NULL, 0),
(63, 0, 0, '', '', '', 0, '', '', 0, '', 0, 0, 0, 0, 0, 0, '', NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 125, 'sos', 0),
(69, 114, 1, 'sofia', '2023-03-27', '2023-03-08', 4, 'Ameer', '', 1234567891, 'sofiatarannum17@gmail.com', 500, 0, 0, 0, 0, 500, '2023-04-08', NULL, NULL, NULL, NULL, 1, NULL, 0, 0, NULL, NULL, 0),
(71, 114, 6, 'sofia', '2023-04-03', '2023-03-08', 4, 'Ameer', 'Farzana', 1234567891, 'sofiatarannum17@gmail.com', 500, 0, 1000, 0, 0, 1500, '2023-04-10', '114bill.pdf', NULL, NULL, NULL, 1, NULL, 1, 0, NULL, NULL, 0),
(73, 117, 7, 'Saba', '2023-04-03', '2023-03-28', 7, 'Akbar', 'Naziya', 1236547892, 'sofiatarannum17@gmail.com', 0, 0, 0, 0, 500, 500, '2023-04-10', NULL, NULL, NULL, NULL, NULL, 1, 0, 0, 125, 'sos', 0),
(74, 115, 2, 'Madhu', '2023-03-27', '2023-03-09', 6, 'Balaji', 'Aparna', 1254789632, 'madhumithauppala@gmail.com', 500, 0, 1000, 0, 0, 1500, '2023-04-10', NULL, NULL, NULL, NULL, 1, NULL, 0, 0, NULL, NULL, 0),
(77, 122, 17, 'Aakash', '', '', 0, '', '', 0, 'sofiatarannumkits@gmail.com', 0, 0, 0, 0, 0, 0, '', NULL, NULL, NULL, 'R4_vacreport_U5rHfq6.png', NULL, 1, 0, 1, NULL, NULL, 0),
(78, 120, 10, 'sofia', '2023-05-01', '2023-05-09', 12, 'rtyu', 'fdfd', 2147483647, 'sofiatarannum17@gmail.com', 0, 0, 0, 0, 2000, 2000, '2023-05-02', NULL, '120_LF0aJeT.pdf', NULL, NULL, NULL, 1, 0, 0, 178, 'kkl', 1),
(81, 123, 18, 'sofia', '', '', 0, '', '', 0, 'sofiatarannumkits@gmail.com', 0, 0, 0, 0, 0, 0, '', NULL, NULL, 'Presentation_5S8kJAk.pptx', NULL, NULL, NULL, 0, 1, NULL, NULL, 0),
(82, 115, 3, 'Madhu', '2023-03-27', '2023-03-09', 6, 'Balaji', 'Aparna', 1254789632, 'sofiatarannum17@gmail.com', 500, 0, 1000, 0, 0, 1500, '2023-05-02', '115.pdf', NULL, NULL, NULL, 1, NULL, 1, 0, NULL, NULL, 0),
(83, 120, 14, 'sofia', '', '', 0, '', '', 0, 'sofiatarannum17@gmail.com', 0, 0, 0, 0, 0, 0, '', '120.pdf', '', NULL, '120vac.pdf', NULL, 1, 1, 1, NULL, NULL, 0),
(85, 116, 4, 'asdfg', '2023-03-27', '2023-02-28', 6, 'Ajay', 'fdfd', 2147483647, 'sofiatarannum17@gmail.com', 500, 1000, 0, 0, 0, 1500, '2023-06-26', '116.pdf', NULL, NULL, NULL, 1, NULL, 1, 0, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `job`
--

CREATE TABLE `job` (
  `sno` int(10) NOT NULL,
  `aname` char(25) NOT NULL,
  `appaadhar` int(12) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` bigint(10) NOT NULL,
  `gender` char(8) NOT NULL,
  `dob` text NOT NULL,
  `age` int(2) NOT NULL,
  `address` varchar(30) NOT NULL,
  `city` char(10) NOT NULL,
  `pin` int(6) NOT NULL,
  `state` char(10) NOT NULL,
  `file` varchar(15) NOT NULL,
  `remove` int(1) NOT NULL,
  `jname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `job`
--

INSERT INTO `job` (`sno`, `aname`, `appaadhar`, `email`, `mobile`, `gender`, `dob`, `age`, `address`, `city`, `pin`, `state`, `file`, `remove`, `jname`) VALUES
(26, 'sofia', 2147483647, 'sofiatarannum17@gmail.com', 1234569874, 'female', '2023-03-29', 25, 'hhhhhh', 'Karimnagar', 505001, 'Telangana', '114_aHDW4L6.pdf', 0, ''),
(27, 'Madhu', 2147483647, 'sofiatarannumkits@gmail.com', 2147483647, 'female', '2023-03-29', 30, 'hhhhhh', 'ghgggghggg', 505001, 'Telangana', '117vac_2qPndBy.', 1, ''),
(28, 'Koushik', 2147483647, 'koushikyeluguri7@gmail.com', 2147483647, 'female', '2023-03-29', 50, 'ggggg', 'Karimnagar', 505001, 'Telangana', '117vac_fZkICOV.', 0, ''),
(29, 'Mahesh', 2147483647, 'sofiatarannum17@gmail.com', 2365478934, 'female', '2002-01-09', 21, 'ggggg', 'hhhhh', 505001, 'Telangana', 'Presentation (2', 0, 'madhu123'),
(30, 'Latha', 2147483647, 'sofiatarannumkits@gmail.com', 9545871236, 'female', '1993-01-18', 30, 'hhhhh', 'Karimnagar', 505001, 'Telangana', 'interview.txt', 0, 'madhu123');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `jid` int(10) NOT NULL,
  `jname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`jid`, `jname`) VALUES
(5, 'X-ray Technician'),
(6, 'Pharmacist'),
(7, 'Registered Nurse'),
(8, 'Medical Technologist'),
(10, 'Receptionist');

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `id` int(10) NOT NULL,
  `cname` char(20) NOT NULL,
  `dob` text NOT NULL,
  `age` int(2) NOT NULL,
  `gender` char(7) NOT NULL,
  `cbloodgrp` varchar(10) NOT NULL,
  `fname` char(25) NOT NULL,
  `faadhno` bigint(12) NOT NULL,
  `mname` char(25) NOT NULL,
  `maadhno` bigint(12) NOT NULL,
  `phone` bigint(10) NOT NULL,
  `mail` varchar(40) NOT NULL,
  `address` varchar(50) NOT NULL,
  `selecttype` int(1) NOT NULL,
  `rid` bigint(10) NOT NULL,
  `status` int(1) DEFAULT NULL,
  `aid` bigint(10) NOT NULL,
  `vacid` int(8) DEFAULT NULL,
  `vacname` varchar(25) DEFAULT NULL,
  `cdate` text NOT NULL,
  `billissue` int(1) NOT NULL,
  `vreportissue` int(1) NOT NULL,
  `dis` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`id`, `cname`, `dob`, `age`, `gender`, `cbloodgrp`, `fname`, `faadhno`, `mname`, `maadhno`, `phone`, `mail`, `address`, `selecttype`, `rid`, `status`, `aid`, `vacid`, `vacname`, `cdate`, `billissue`, `vreportissue`, `dis`) VALUES
(10, '', '0000-00-00', 0, '', '', '', 0, '', 0, 0, '', '', 0, 113, 1, 0, NULL, NULL, '0000-00-00', 1, 0, 1),
(74, 'sofia', '2023-03-08', 4, 'Female', 'O+', 'Ameer', 145623789123, 'Farzana', 123456456456, 1234567891, 'sofiatarannum17@gmail.com', '1111999abbbb ', 0, 114, 1, 1, NULL, NULL, '2023-03-27', 1, 0, 0),
(75, 'Madhu', '2023-03-09', 6, 'Female', 'O+', 'Balaji', 123456789012, 'Aparna', 98765432112, 1254789632, 'sofiatarannum17@gmail.com', '12345 bbbbb', 0, 115, 1, 2, NULL, NULL, '2023-03-27', 1, 0, 0),
(76, 'Madhu', '2023-03-09', 6, 'Female', 'O+', 'Balaji', 123456789012, 'Aparna', 98765432112, 1254789632, 'sofiatarannum17@gmail.com', '12345 bbbbb', 0, 115, 0, 3, NULL, NULL, '2023-03-27', 1, 0, 0),
(77, 'asdfg', '2023-02-28', 6, 'Female', 'O+', 'Ajay', 145678903214, 'fdfd', 345121212121, 4567847891, 'sofiatarannum17@gmail.com', 'hyut', 0, 116, 1, 4, NULL, NULL, '2023-03-27', 1, 0, 0),
(78, 'asdfg', '2023-02-28', 6, 'Female', 'O+', 'Arun', 145678903214, 'fdfd', 121454545454, 4567845457, 'sofiatarannum17@gmail.com', 'hyut', 0, 116, 0, 5, NULL, NULL, '2023-03-27', 0, 0, 0),
(79, 'sofia', '2023-03-08', 4, 'Female', 'O+', 'Ameer', 145623789123, 'Farzana', 123456456456, 1234567891, 'sofiatarannum17@gmail.com', '1111999abbbb ', 0, 117, 0, 6, NULL, NULL, '2023-04-03', 1, 0, 0),
(80, 'Saba', '2023-03-28', 7, 'Female', 'O+', 'Akbar', 123456789987, 'Naziya', 147899632547, 1236547892, 'sofiatarannum17@gmail.com', 'bbbb', 1, 118, 0, 7, 125, 'sos', '2023-04-03', 1, 1, 0),
(82, 'madhu', '2023-05-10', 13, 'Female', 'O+', 'raju', 132347878787, 'rani', 224412121212, 3656541456, 'sofiatarannum17@gmail.com', '4444', 0, 119, 0, 9, NULL, NULL, '2023-05-01', 0, 0, 0),
(83, 'sofia', '2023-05-09', 12, 'Male', 'O+', 'rtyu', 132347878787, 'fdfd', 224412478978, 3656547878, 'sofiatarannum17@gmail.com', '555', 1, 120, 0, 10, 178, 'kkl', '2023-05-01', 1, 0, 0),
(89, 'Hrihaan', '2010-01-26', 13, 'Male', 'O+', 'Hrithik', 123456789321, 'Suhana', 987456123177, 9125874369, 'sofiatarannum17@gmail.com', 'H.no: 7-1-601, Vidyanagar, Karimnagar', 0, 121, 0, 11, NULL, NULL, '2023-05-02', 0, 0, 0),
(90, 'Aakash', '2020-01-02', 4, 'Male', 'O+', 'Rajiv', 123478965478, 'Radhika', 121478965823, 9658741236, 'sofiatarannumkits@gmail.com', 'no:7-1-557, karimnagar', 1, 122, 0, 12, 149, 'mmm', '2023-05-02', 0, 1, 0),
(96, 'sofia', '2016-01-04', 7, 'Female', 'O+', 'Rihaan', 147147258369, 'Lubna', 987456123321, 9856231478, 'sofiatarannum17@gmail.com', 'Karimnagar', 0, 123, 0, 13, NULL, NULL, '2023-05-02', 0, 0, 0),
(100, 'sofia', '2023-05-09', 12, 'Male', 'O+', 'rtyu', 132347878787, 'fdfd', 224412478978, 3656547878, 'sofiatarannum17@gmail.com', '555', 1, 120, 0, 14, 751, 'IPV+HiB', '2023-06-27', 1, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `userblood`
--

CREATE TABLE `userblood` (
  `sno` int(10) NOT NULL,
  `daadhno` bigint(12) NOT NULL,
  `dname` char(25) NOT NULL,
  `mail` varchar(30) NOT NULL,
  `phone` int(10) NOT NULL,
  `bloodgrp` varchar(2) NOT NULL,
  `age` int(2) NOT NULL,
  `dob` text NOT NULL,
  `gender` char(7) NOT NULL,
  `remove` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userblood`
--

INSERT INTO `userblood` (`sno`, `daadhno`, `dname`, `mail`, `phone`, `bloodgrp`, `age`, `dob`, `gender`, `remove`) VALUES
(3, 789654123654, 'Alekhya', 'sofiatarannum17@gmail.com', 2147483647, 'o+', 20, '2023-03-29', 'female', 1),
(4, 147896325874, 'Ranbir', 'sofiatarannum17@gmail.com', 2147483647, 'o-', 24, '2023-04-07', 'female', 0),
(5, 145623145236, 'Hrithik', 'sofiatarannum17@gmail.com', 1414141414, 'o-', 25, '2023-03-28', 'female', 0),
(6, 457896321456, 'Alia', 'sofiatarannum17@gmail.com', 2147483647, 'o+', 65, '2023-05-03', 'female', 0),
(8, 268618666077, 'Sofia', 'sofiatarannum17@gmail.com', 2147483647, 'o+', 20, '2002-05-26', 'female', 1),
(9, 111111111111, 'Madhu', 'sofiatarannum17@gmail.com', 2147483647, 'o+', 21, '2001-07-25', 'female', 0),
(12, 111111111111, 'Raju', 'sofiatarannum17@gmail.com', 2147483647, 'A+', 22, '2001-01-17', 'female', 0);

-- --------------------------------------------------------

--
-- Table structure for table `vaccines`
--

CREATE TABLE `vaccines` (
  `sid` int(9) NOT NULL,
  `vid` varchar(3) NOT NULL,
  `vname` char(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vaccines`
--

INSERT INTO `vaccines` (`sid`, `vid`, `vname`) VALUES
(13, '751', 'IPV+HiB'),
(14, '149', 'DTap'),
(15, '789', 'Hepatitis B'),
(22, '178', 'OPv'),
(23, '454', 'HPV 1st dose'),
(24, '79', 'HPV 2nd dose'),
(25, '75', 'HPV 3rd dose'),
(26, '77', 'Hepatitis'),
(27, '45', 'MMR'),
(28, '8', 'Chicken Pox'),
(29, '1', 'DTP'),
(30, '756', 'IPV'),
(35, '12', 'BCG'),
(45, '125', 'Measles'),
(46, '122', 'Typhoid Vaccine');

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
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`jid`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userblood`
--
ALTER TABLE `userblood`
  ADD PRIMARY KEY (`sno`);

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
  MODIFY `sid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT for table `job`
--
ALTER TABLE `job`
  MODIFY `sno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `jid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `userblood`
--
ALTER TABLE `userblood`
  MODIFY `sno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `vaccines`
--
ALTER TABLE `vaccines`
  MODIFY `sid` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
