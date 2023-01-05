-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Jan 05, 2023 at 04:09 PM
-- Server version: 5.7.34
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ag_betssport`
--

-- --------------------------------------------------------

--
-- Table structure for table `bets`
--

CREATE TABLE `bets` (
  `id` int(100) NOT NULL,
  `match_id` int(100) NOT NULL,
  `ratio_id` int(100) NOT NULL,
  `user_id` int(100) NOT NULL,
  `created_at` datetime NOT NULL,
  `amount` double NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `agent_id` int(11) DEFAULT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bets`
--

INSERT INTO `bets` (`id`, `match_id`, `ratio_id`, `user_id`, `created_at`, `amount`, `deleted_at`, `agent_id`, `status`) VALUES
(1, 15, 2, 1, '2023-01-04 00:00:00', 8000, NULL, NULL, '1'),
(2, 38, 3, 1, '2023-01-04 00:00:00', 135, NULL, NULL, '1'),
(3, 33, 2, 1, '2023-01-04 00:00:00', 7000, NULL, NULL, '1');

-- --------------------------------------------------------

--
-- Table structure for table `matchs`
--

CREATE TABLE `matchs` (
  `id` int(100) NOT NULL,
  `home_team_id` int(100) NOT NULL,
  `move_team_id` int(100) NOT NULL,
  `priority_id` int(100) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `agent_id` int(100) NOT NULL,
  `country` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `matchs`
--

INSERT INTO `matchs` (`id`, `home_team_id`, `move_team_id`, `priority_id`, `created_at`, `updated_at`, `deleted_at`, `agent_id`, `country`) VALUES
(15, 16, 15, 3, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(16, 15, 16, 3, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'HAITI'),
(17, 15, 16, 3, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(18, 15, 16, 3, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(19, 16, 15, 3, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(20, 16, 15, 3, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(21, 27, 29, 1, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(22, 18, 24, 1, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(23, 28, 25, 1, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'ESPAGNE'),
(24, 30, 20, 1, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(25, 26, 31, 1, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(26, 25, 24, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(27, 18, 29, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(28, 27, 16, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'ESPAGNE'),
(29, 30, 20, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'HAITI'),
(30, 31, 26, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'HAITI'),
(31, 18, 27, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(32, 31, 16, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(33, 20, 28, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(34, 25, 26, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'ANGLETERRE'),
(35, 24, 29, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'ANGLETERRE'),
(36, 27, 25, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(37, 16, 26, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'HAITI'),
(38, 31, 24, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'FRANCE'),
(39, 29, 28, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'PORTUGAL'),
(40, 18, 30, 4, '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, 1, 'ESPAGNE');

-- --------------------------------------------------------

--
-- Table structure for table `match_teams`
--

CREATE TABLE `match_teams` (
  `match_id` int(11) NOT NULL,
  `home_team_id` int(11) NOT NULL,
  `away_team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `match_teams`
--

INSERT INTO `match_teams` (`match_id`, `home_team_id`, `away_team_id`) VALUES
(17, 15, 16),
(18, 15, 16),
(19, 16, 15),
(20, 16, 15),
(21, 27, 29),
(22, 18, 24),
(23, 28, 25),
(24, 30, 20),
(25, 26, 31),
(26, 25, 24),
(27, 18, 29),
(28, 27, 16),
(29, 30, 20),
(30, 31, 26),
(31, 18, 27),
(32, 31, 16),
(33, 20, 28),
(34, 25, 26),
(35, 24, 29),
(36, 27, 25),
(37, 16, 26),
(38, 31, 24),
(39, 29, 28),
(40, 18, 30);

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(100) NOT NULL,
  `match_id` int(100) NOT NULL,
  `amount` double NOT NULL,
  `created_at` int(11) NOT NULL,
  `user_id` int(100) NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `agent_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `play_match`
--

CREATE TABLE `play_match` (
  `id` int(100) NOT NULL,
  `match_id` int(100) NOT NULL,
  `score_1` int(255) NOT NULL,
  `score_2` int(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `agent_id` int(100) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `priority`
--

CREATE TABLE `priority` (
  `id` int(100) NOT NULL,
  `title` varchar(255) NOT NULL,
  `ratio` int(255) NOT NULL,
  `visible` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `priority`
--

INSERT INTO `priority` (`id`, `title`, `ratio`, `visible`) VALUES
(1, 'Ligue des champions', 1, 1),
(2, 'Coupe du monde', 950, 1),
(3, 'Eliminatoire', 200, 1),
(4, 'Amical', 100, 1),
(5, 'Liga', 10, 1),
(6, 'Premier League', 700, 1),
(7, 'Ligue 1', 500, 1);

-- --------------------------------------------------------

--
-- Table structure for table `priority_teams`
--

CREATE TABLE `priority_teams` (
  `priority_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `priority_teams`
--

INSERT INTO `priority_teams` (`priority_id`, `team_id`) VALUES
(2, 15),
(3, 15),
(3, 16),
(4, 16),
(1, 18),
(4, 18),
(5, 18),
(1, 20),
(5, 20),
(4, 20),
(1, 24),
(4, 24),
(5, 24),
(1, 25),
(4, 25),
(5, 25),
(1, 26),
(4, 26),
(5, 26),
(1, 27),
(4, 27),
(5, 27),
(1, 28),
(4, 28),
(7, 28),
(1, 29),
(4, 29),
(7, 29),
(1, 30),
(4, 30),
(7, 30),
(1, 31),
(4, 31),
(7, 31);

-- --------------------------------------------------------

--
-- Table structure for table `ratios`
--

CREATE TABLE `ratios` (
  `id` int(100) NOT NULL,
  `title` varchar(255) NOT NULL,
  `ratio` int(255) NOT NULL,
  `visible` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ratios`
--

INSERT INTO `ratios` (`id`, `title`, `ratio`, `visible`) VALUES
(1, '1-0', 1, 1),
(2, '0-0', 3, 1),
(3, '0-1', 1, 1),
(4, '1-1', 2, 1),
(5, '2-0', 3, 1),
(6, '0-2', 3, 1),
(7, '3-1', 4, 1),
(8, '1-3', 3, 1),
(9, '3-0', 3, 1),
(10, '0-3', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `solde`
--

CREATE TABLE `solde` (
  `id` int(100) NOT NULL,
  `code_user` varchar(255) NOT NULL,
  `action` int(100) NOT NULL COMMENT '1=deposit| 2=withdraw',
  `montant` double NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `agent_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `solde`
--

INSERT INTO `solde` (`id`, `code_user`, `action`, `montant`, `created_at`, `updated_at`, `deleted_at`, `agent_id`) VALUES
(1, 'TEST_2113', 1, 150, '2023-01-03 02:32:48', '2023-01-03 02:32:48', NULL, 1),
(2, 'TEST_2113', 1, 5000, '2023-01-03 02:32:48', '2023-01-03 02:32:48', NULL, 1),
(3, 'TEST_2113', 2, 450, '2023-01-03 02:32:48', '2023-01-03 02:32:48', NULL, 1),
(4, 'TEST_2113', 1, 400, '2023-01-05 00:00:00', '2023-01-05 00:00:00', NULL, 1),
(5, 'CODE_480', 1, 300, '2023-01-05 00:00:00', '2023-01-05 00:00:00', NULL, 1),
(6, 'CODE_255', 1, 500, '2023-01-05 00:00:00', '2023-01-05 00:00:00', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `id` int(100) NOT NULL,
  `img` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `level` int(255) NOT NULL,
  `agent_id` int(100) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `img`, `title`, `level`, `agent_id`, `created_at`, `updated_at`, `deleted_at`) VALUES
(15, 'assets/images/teams/fcb.png', 'hhhhhhhsssa', 1000, 1, '2022-12-28 00:00:00', '2022-12-28 00:00:00', NULL),
(16, 'assets/images/teams/fcb.png', 'Hello', 100, 1, '2022-12-28 00:00:00', '2022-12-28 00:00:00', NULL),
(18, 'assets/images/teams/fcb.png', 'Real Madrid', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(20, 'assets/images/teams/fcb.png', 'FC Barcelona', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(24, 'assets/images/teams/fcb.png', 'Atletico Madrid', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(25, 'assets/images/teams/fcb.png', 'Valence', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(26, 'assets/images/teams/fcb.png', 'Real Betis', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(27, 'assets/images/teams/fcb.png', 'Villa Real', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(28, 'assets/images/teams/fcb.png', 'Paris SG', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(29, 'assets/images/teams/fcb.png', 'Marseille', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(30, 'assets/images/teams/fcb.png', 'Monaco', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL),
(31, 'assets/images/teams/fcb.png', 'Lyon', 1000, 1, '2022-12-30 00:00:00', '2022-12-30 00:00:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(100) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `tel` varchar(255) NOT NULL,
  `code_user` varchar(255) NOT NULL,
  `address` text NOT NULL,
  `username` varchar(255) NOT NULL,
  `nif` varchar(255) NOT NULL,
  `sexe` varchar(255) NOT NULL,
  `dataNais` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `is_admin` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `tel`, `code_user`, `address`, `username`, `nif`, `sexe`, `dataNais`, `password`, `created_at`, `updated_at`, `deleted_at`, `is_admin`) VALUES
(1, 'Sylainx', 'Gauthier', 'hi@gmail.com', '4444444', 'TEST_2113', 'John', 'mrtop', '49382888', 'Masculin', '25/25/2022', '$2b$12$mjUuVJn1Z7n3VjmtKYIoQOwLw6MM782YyAI9qJJIORxuuinwZ6pxm', '2022-12-14 02:40:49', '2022-12-13 20:40:55', NULL, 1),
(2, 'hdhd', 'ksksk', 'hello@gmail.com', 'kdkkdk', '1', 'sksksk', 'sksk', 'dkkd', 'Feminin', '2022-12-21', '$2b$12$7JB.9LJHw5KBhXBrTBmhrO3hp3A7BuuGN62A/CAxbI9wCAyW/.n8K', '2022-12-14 00:00:00', '2022-12-14 00:00:00', NULL, NULL),
(3, 'test', 'test', 'test', '37373772 ', 'CODE_480', 'hell', 'test', '1235', 'Feminin', '2000-01-01', '$2b$12$bMhalBOLaZHOPTg.noxOwuZFnYDF.g/1c3qAcBXyH9MP7eaRrKtsi', '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, NULL),
(4, 'helllo test', 'hello test', 'hlslsl', 'ddjjd', 'CODE_95', 'test', 'test', '3456789', 'Feminin', '2000-01-01', '$2b$12$I4oMjyZL8qcTIslfoJvUGOnPATEj4wj5POnaQnInK4f9URc9QmDp.', '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, NULL),
(5, 'tesssss', 'tessss', 'tesskk', '3837377', 'CODE_255', 'delmas', 'tessss', '377373', 'Feminin', '2000-01-01', '$2b$12$/.TkNchQGvdFR3Gl42lCw.ma4.wz6/pYRHBv0PqFezLEwwV.g5dHG', '2023-01-03 00:00:00', '2023-01-03 00:00:00', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bets`
--
ALTER TABLE `bets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_results_agent` (`agent_id`),
  ADD KEY `FK_results_match` (`match_id`),
  ADD KEY `FK_results_ratio` (`ratio_id`),
  ADD KEY `FK_results_user` (`user_id`);

--
-- Indexes for table `matchs`
--
ALTER TABLE `matchs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_matchs_home_team` (`home_team_id`),
  ADD KEY `FK_matchs_move_team` (`move_team_id`),
  ADD KEY `FK_matchs_agent` (`agent_id`),
  ADD KEY `FK_matchs_priority` (`priority_id`);

--
-- Indexes for table `match_teams`
--
ALTER TABLE `match_teams`
  ADD UNIQUE KEY `match_id` (`match_id`),
  ADD KEY `FK_match_teams_homeTeam_id` (`home_team_id`),
  ADD KEY `FK_match_teams_awayTeam_id` (`away_team_id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_payments_match` (`match_id`),
  ADD KEY `FK_payments_user` (`user_id`),
  ADD KEY `FK_payments_agent` (`agent_id`);

--
-- Indexes for table `play_match`
--
ALTER TABLE `play_match`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_play_matchs_agent` (`agent_id`),
  ADD KEY `FK_play_matchs_ID_match` (`match_id`);

--
-- Indexes for table `priority`
--
ALTER TABLE `priority`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `priority_teams`
--
ALTER TABLE `priority_teams`
  ADD KEY `FK_priority_teams_team_id` (`team_id`),
  ADD KEY `FK_priority_teams_priority_id` (`priority_id`);

--
-- Indexes for table `ratios`
--
ALTER TABLE `ratios`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `solde`
--
ALTER TABLE `solde`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_solde_agent` (`agent_id`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_team_agent` (`agent_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uniq_email` (`email`),
  ADD UNIQUE KEY `uniq_tel` (`tel`),
  ADD UNIQUE KEY `code_user` (`code_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bets`
--
ALTER TABLE `bets`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `matchs`
--
ALTER TABLE `matchs`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `play_match`
--
ALTER TABLE `play_match`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `priority`
--
ALTER TABLE `priority`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `ratios`
--
ALTER TABLE `ratios`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `solde`
--
ALTER TABLE `solde`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `teams`
--
ALTER TABLE `teams`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bets`
--
ALTER TABLE `bets`
  ADD CONSTRAINT `FK_results_agent` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_results_match` FOREIGN KEY (`match_id`) REFERENCES `matchs` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_results_ratio` FOREIGN KEY (`ratio_id`) REFERENCES `ratios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_results_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `matchs`
--
ALTER TABLE `matchs`
  ADD CONSTRAINT `FK_matchs_agent` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_matchs_home_team` FOREIGN KEY (`home_team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_matchs_move_team` FOREIGN KEY (`move_team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_matchs_priority` FOREIGN KEY (`priority_id`) REFERENCES `priority` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `match_teams`
--
ALTER TABLE `match_teams`
  ADD CONSTRAINT `FK_match_teams_awayTeam_id` FOREIGN KEY (`away_team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_match_teams_homeTeam_id` FOREIGN KEY (`home_team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_match_teams_match_id` FOREIGN KEY (`match_id`) REFERENCES `matchs` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `FK_payments_agent` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_payments_match` FOREIGN KEY (`match_id`) REFERENCES `matchs` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_payments_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `play_match`
--
ALTER TABLE `play_match`
  ADD CONSTRAINT `FK_play_matchs_ID_match` FOREIGN KEY (`match_id`) REFERENCES `matchs` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_play_matchs_agent` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `priority_teams`
--
ALTER TABLE `priority_teams`
  ADD CONSTRAINT `FK_priority_teams_priority_id` FOREIGN KEY (`priority_id`) REFERENCES `priority` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_priority_teams_team_id` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `solde`
--
ALTER TABLE `solde`
  ADD CONSTRAINT `FK_solde_agent` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `teams`
--
ALTER TABLE `teams`
  ADD CONSTRAINT `FK_team_agent` FOREIGN KEY (`agent_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
