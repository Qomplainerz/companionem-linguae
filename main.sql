-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 21, 2023 at 09:20 PM
-- Server version: 10.5.20-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `the name of your database`
--
CREATE DATABASE IF NOT EXISTS `the name of your database` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `the name of your database`;

-- --------------------------------------------------------

--
-- Table structure for table `TBL_Languages`
--

DROP TABLE IF EXISTS `TBL_Languages`;
CREATE TABLE `TBL_Languages` (
  `Language_ID` bigint(20) NOT NULL COMMENT 'Primary key of TBL_Languages',
  `Language_Code_639` varchar(255) NOT NULL COMMENT 'The language code according to ISO 639',
  `Language_Name` varchar(255) NOT NULL COMMENT 'The name of the language',
  `Child_Of_Language_Family_ID` bigint(20) NOT NULL COMMENT 'Reference to the language ID of  TBL_Language_Families',
  `Source` varchar(255) NOT NULL COMMENT 'Source where the language was found',
  `Date_Created` date NOT NULL DEFAULT current_timestamp() COMMENT 'Date when the language was added to the DB',
  `Date_Edited` date NOT NULL DEFAULT current_timestamp() COMMENT 'Date when the language was updated in the DB'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `TBL_Languages`
--

INSERT INTO `TBL_Languages` (`Language_ID`, `Language_Code_639`, `Language_Name`, `Child_Of_Language_Family_ID`, `Source`, `Date_Created`, `Date_Edited`) VALUES
(1, 'apq', 'A-Pucikwar', 5, 'https://www.ethnologue.com/language/apq/', '2023-09-20', '2023-09-20'),
(2, 'aou', 'A’ou', 69, 'https://www.ethnologue.com/language/aou/', '2023-09-20', '2023-09-20'),
(3, 'aiw', 'Aari', 2, 'https://www.ethnologue.com/language/aiw/', '2023-09-20', '2023-09-20'),
(4, 'aas', 'Aasáx', 2, 'https://www.ethnologue.com/language/aas/', '2023-09-20', '2023-09-20'),
(5, 'kbt', 'Abadi', 11, 'https://www.ethnologue.com/language/kbt/', '2023-09-20', '2023-09-20'),
(6, 'abf', 'Abai Sungai', 11, 'https://www.ethnologue.com/language/abf/', '2023-09-20', '2023-09-20'),
(7, 'bzy', 'Abanglekou', 97, 'https://www.ethnologue.com/language/bzy/', '2023-09-20', '2023-09-20'),
(8, 'abm', 'Abanyom', 97, 'https://www.ethnologue.com/language/abm/', '2023-09-20', '2023-09-20'),
(9, 'aau', 'Abau', 117, 'https://www.ethnologue.com/language/aau/', '2023-09-20', '2023-09-20'),
(10, 'abq', 'Abaza', 1, 'https://www.ethnologue.com/language/abq/', '2023-09-20', '2023-09-20'),
(11, 'aba', 'Abé', 97, 'https://www.ethnologue.com/language/aba/', '2023-09-20', '2023-09-20'),
(12, 'aaq', 'Abenaki, Eastern', 3, 'https://www.ethnologue.com/language/aaq/', '2023-09-20', '2023-09-20'),
(13, 'abe', 'Western Abenaki', 3, 'https://www.ethnologue.com/language/abe/', '2023-09-20', '2023-09-20'),
(14, 'abi', 'Abidji', 97, 'https://www.ethnologue.com/language/abi/', '2023-09-20', '2023-09-20'),
(15, 'bsa', 'Abinomn', 74, 'https://www.ethnologue.com/language/bsa/', '2023-09-20', '2023-09-20'),
(16, 'axb', 'Abipon', 46, 'https://www.ethnologue.com/language/axb/', '2023-09-20', '2023-09-20'),
(17, 'pcn', 'Abishi', 97, 'https://www.ethnologue.com/language/pcn/', '2023-09-20', '2023-09-20'),
(18, 'abk', 'Abkhaz', 1, 'https://www.ethnologue.com/language/abk/', '2023-09-20', '2023-09-20'),
(19, 'aob', 'Abom', 133, 'https://www.ethnologue.com/language/aob/', '2023-09-20', '2023-09-20'),
(20, 'abo', 'Abon', 97, 'https://www.ethnologue.com/language/abo/', '2023-09-20', '2023-09-20'),
(21, 'abr', 'Abron', 97, 'https://www.ethnologue.com/language/abr/', '2023-09-20', '2023-09-20'),
(22, 'ado', 'Abu', 112, 'https://www.ethnologue.com/language/ado/', '2023-09-20', '2023-09-20'),
(23, 'aah', 'Abu’', 131, 'https://www.ethnologue.com/language/aah/', '2023-09-20', '2023-09-20'),
(24, 'abn', 'Abua', 97, 'https://www.ethnologue.com/language/abn/', '2023-09-20', '2023-09-20'),
(25, 'abz', 'Abui', 133, 'https://www.ethnologue.com/language/abz/', '2023-09-20', '2023-09-20'),
(26, 'kgr', 'Abun', 74, 'https://www.ethnologue.com/language/kgr/', '2023-09-20', '2023-09-20'),
(27, 'abu', 'Abure', 97, 'https://www.ethnologue.com/language/abu/', '2023-09-20', '2023-09-20'),
(28, 'mgj', 'Abureni', 97, 'https://www.ethnologue.com/language/mgj/', '2023-09-20', '2023-09-20'),
(29, 'ace', 'Aceh', 11, 'https://www.ethnologue.com/language/ace/', '2023-09-20', '2023-09-20'),
(30, 'aca', 'Achagua', 78, 'https://www.ethnologue.com/language/aca/', '2023-09-20', '2023-09-20'),
(31, 'acn', 'Achang', 119, 'https://www.ethnologue.com/language/acn/', '2023-09-20', '2023-09-20'),
(32, 'yif', 'Ache', 119, 'https://www.ethnologue.com/language/yif/', '2023-09-20', '2023-09-20'),
(33, 'guq', 'Aché', 137, 'https://www.ethnologue.com/language/guq/', '2023-09-20', '2023-09-20'),
(34, 'acz', 'Acheron', 97, 'https://www.ethnologue.com/language/acz/', '2023-09-20', '2023-09-20'),
(35, 'acr', 'Achi', 84, 'https://www.ethnologue.com/language/acr/', '2023-09-20', '2023-09-20'),
(36, 'ach', 'Acholi', 98, 'https://www.ethnologue.com/language/ach/', '2023-09-20', '2023-09-20');

-- --------------------------------------------------------

--
-- Table structure for table `TBL_Language_Families`
--

DROP TABLE IF EXISTS `TBL_Language_Families`;
CREATE TABLE `TBL_Language_Families` (
  `Language_Family_ID` bigint(20) NOT NULL COMMENT 'Primary Key of TBL_Language_Families',
  `Language_Family_Name` varchar(255) NOT NULL COMMENT 'The name of the language family',
  `Source` varchar(255) NOT NULL COMMENT 'Source where the language family was found',
  `Date_Created` date NOT NULL DEFAULT current_timestamp() COMMENT 'Date when the language was added to the DB',
  `Date_Edited` date NOT NULL DEFAULT current_timestamp() COMMENT 'Date when the language was updated in the DB'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `TBL_Language_Families`
--

INSERT INTO `TBL_Language_Families` (`Language_Family_ID`, `Language_Family_Name`, `Source`, `Date_Created`, `Date_Edited`) VALUES
(1, 'Abkhaz-Adyghe', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(2, 'Afro-Asiatic', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(3, 'Algic', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(4, 'Amto-Musan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(5, 'Andamanese', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(6, 'Arafundi', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(7, 'Arai (Left May)', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(8, 'Arauan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(9, 'Australian', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(10, 'Austro-Asiatic', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(11, 'Austronesian', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(12, 'Aymaran', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(13, 'Barbacoan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(14, 'Bayono-Awbono', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(15, 'Border', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(16, 'Bororoan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(17, 'Botocudoan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(18, 'Caddoan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(19, 'Cahuapanan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(20, 'Cariban', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(21, 'Central Solomons', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(22, 'Chapacuran', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(23, 'Chibchan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(24, 'Chimakuan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(25, 'Chinookan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(26, 'Chipaya-Uru', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(27, 'Chocoan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(28, 'Cholonan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(29, 'Chon', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(30, 'Chukotko-Kamchatkan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(31, 'Chumashan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(32, 'Cochimí-Yuman', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(33, 'Comecrudan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(34, 'Constructed languages', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(35, 'Coosan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(36, 'Creole', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(37, 'Dravidian', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(38, 'East Bird\'s Head-Sentani', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(39, 'East Geelvink Bay', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(40, 'East New Britain', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(41, 'Eastern Trans-Fly', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(42, 'Eskimo-Aleut', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(43, 'Eyak-Athabaskan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(44, 'Fas', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(45, 'Guajiboan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(46, 'Guaykuruan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(47, 'Gum', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(48, 'Haida', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(49, 'Harákmbut', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(50, 'Hmong-Mien', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(51, 'Huavean', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(52, 'Indo-European', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(53, 'Iroquoian', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(54, 'Jabutian', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(55, 'Japonic', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(56, 'Jean', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(57, 'Jicaquean', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(58, 'Jivaroan', 'https://www.ethnologue.com/browse/families/', '2023-09-18', '2023-09-18'),
(59, 'Kamakanan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(60, 'Karajá', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(61, 'Kartvelian', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(62, 'Katukinan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(63, 'Kaure', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(64, 'Kaweskaran', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(65, 'Keresan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(66, 'Khoe-Kwadi', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(67, 'Kiowa-Tanoan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(68, 'Koreanic', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(69, 'Kra-Dai', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(70, 'Kuki-Chin-Naga', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(71, 'Kwomtari', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(72, 'Kx’a', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(73, 'Lakes Plain', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(74, 'Language isolate', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(75, 'Lencan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(76, 'Lower Mamberamo', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(77, 'Maiduan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(78, 'Maipurean', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(79, 'Mairasi', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(80, 'Mapudungu', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(81, 'Mascoyan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(82, 'Matacoan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(83, 'Maxakalian', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(84, 'Mayan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(85, 'Maybrat', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(86, 'Misumalpan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(87, 'Miwok-Costanoan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(88, 'Mixe-Zoquean', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(89, 'Mixed language', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(90, 'Mongol-Langam', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(91, 'Mongolic', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(92, 'Mosetenan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(93, 'Muran', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(94, 'Muskogean', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(95, 'Nakh-Daghestanian', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(96, 'Nambikwara', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(97, 'Niger-Congo', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(98, 'Nilo-Saharan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(99, 'Nimboran', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(100, 'North Bougainville', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(101, 'Otomanguean', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(102, 'Paezan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(103, 'Palaihnihan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(104, 'Panoan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(105, 'Pauwasi', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(106, 'Piawi', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(107, 'Pidgin', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(108, 'Pomoan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(109, 'Puinavean', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(110, 'Purian', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(111, 'Quechuan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(112, 'Ramu-Lower Sepik', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(113, 'Sahaptian', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(114, 'Salish', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(115, 'Sálivan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(116, 'Senagi', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(117, 'Sepik', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(118, 'Sign language', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(119, 'Sino-Tibetan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(120, 'Siouan-Catawban', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(121, 'Skou', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(122, 'Somahai', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(123, 'South Bougainville', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(124, 'South-Central Papuan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(125, 'Tacanan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(126, 'Takelman', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(127, 'Tarascan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(128, 'Tequistlatecan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(129, 'Tiniguan', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(130, 'Tor-Kwerba', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(131, 'Torricelli', 'https://www.ethnologue.com/browse/families/', '2023-09-19', '2023-09-19'),
(132, 'Totonacan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(133, 'Trans-New Guinea', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(134, 'Tsimshian', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(135, 'Tucanoan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(136, 'Tungusic', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(137, 'Tupian', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(138, 'Turkic', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(139, 'Tuu', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(140, 'Unclassified', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(141, 'Uralic', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(142, 'Uto-Aztecan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(143, 'Wakashan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(144, 'West Papuan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(145, 'Wintuan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(146, 'Witotoan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(147, 'Yaguan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(148, 'Yanomaman', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(149, 'Yele-West New Britain', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(150, 'Yeniseian', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(151, 'Yokutsan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(152, 'Yuat', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(153, 'Yukaghir', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(154, 'Yukian', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(155, 'Zamucoan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20'),
(156, 'Zaparoan', 'https://www.ethnologue.com/browse/families/', '2023-09-20', '2023-09-20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `TBL_Languages`
--
ALTER TABLE `TBL_Languages`
  ADD PRIMARY KEY (`Language_ID`);

--
-- Indexes for table `TBL_Language_Families`
--
ALTER TABLE `TBL_Language_Families`
  ADD PRIMARY KEY (`Language_Family_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `TBL_Languages`
--
ALTER TABLE `TBL_Languages`
  MODIFY `Language_ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'Primary key of TBL_Languages', AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `TBL_Language_Families`
--
ALTER TABLE `TBL_Language_Families`
  MODIFY `Language_Family_ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key of TBL_Language_Families', AUTO_INCREMENT=157;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
