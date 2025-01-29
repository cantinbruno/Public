-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : lun. 06 juin 2022 à 18:09
-- Version du serveur : 5.7.24
-- Version de PHP : 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `pharmutec`
--

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `identifiant` varchar(255) NOT NULL,
  `motdepasse` varchar(255) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `date_signature` date DEFAULT NULL,
  `nom_officine` varchar(255) NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`identifiant`, `motdepasse`, `type`, `date_signature`, `nom_officine`, `adresse`, `telephone`, `email`, `nom`, `prenom`) VALUES
('jojo', '7510d498f23f5815d3376ea7bad64e29', NULL, NULL, 'Pharmacie', 'jo', '1234567891', 'jojo@jojo.fr', NULL, NULL),
('mike', 'mike', NULL, NULL, 'mike', 'mike', 'mike', 'mike', NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

CREATE TABLE `commande` (
  `id` int(11) NOT NULL,
  `idClient` varchar(255) NOT NULL,
  `produits` varchar(255) NOT NULL,
  `date_livraison` varchar(200) NOT NULL,
  `type_livraison` varchar(255) NOT NULL,
  `adresse` varchar(255) DEFAULT NULL,
  `date_expedition` varchar(200) NOT NULL,
  `etat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `commande`
--

INSERT INTO `commande` (`id`, `idClient`, `produits`, `date_livraison`, `type_livraison`, `adresse`, `date_expedition`, `etat`) VALUES
(1, 'mike', 'spasfon', 'date', 'livraison', 'Boulevard Olof Palme, Emerainville', 'date', 'etat');

-- --------------------------------------------------------

--
-- Structure de la table `logs`
--

CREATE TABLE `logs` (
  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `idclient` varchar(255) DEFAULT NULL,
  `log_message` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `panier`
--

CREATE TABLE `panier` (
  `id` int(11) NOT NULL,
  `idClient` varchar(255) NOT NULL,
  `qrProduit` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

CREATE TABLE `personne` (
  `identifiant` varchar(255) NOT NULL,
  `motdepasse` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `telephone` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`identifiant`, `motdepasse`, `type`, `nom`, `prenom`, `telephone`) VALUES
('mael', 'b8ef3ea340a387863f5ced2d19cfc2f6', 'mael', 'mael', 'mael', '0750882375');

-- --------------------------------------------------------

--
-- Structure de la table `produit`
--

CREATE TABLE `produit` (
  `qrcode` int(11) NOT NULL,
  `etat` varchar(255) NOT NULL,
  `stock_actuel` int(11) NOT NULL,
  `stock_prevu` int(11) NOT NULL,
  `nom_commercial` varchar(255) NOT NULL,
  `principe_actif` varchar(255) NOT NULL,
  `descriptif` varchar(255) NOT NULL,
  `categorie` varchar(255) NOT NULL,
  `lab_fabricant` varchar(255) NOT NULL,
  `lieu_stockage` varchar(255) NOT NULL,
  `img` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `produit`
--

INSERT INTO `produit` (`qrcode`, `etat`, `stock_actuel`, `stock_prevu`, `nom_commercial`, `principe_actif`, `descriptif`, `categorie`, `lab_fabricant`, `lieu_stockage`, `img`) VALUES
(1, 'etat', 200, 200, 'spasfon', 'jsp', 'douleur', 'comprime', 'utec', 'garage', 'spasfon'),
(7, 'solide', 25, 26, 'doliprane', 'paracetamol', 'soigner douleur', 'dodo', 'utec', 'utec', 'doliprane');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`identifiant`),
  ADD KEY `type` (`type`);

--
-- Index pour la table `commande`
--
ALTER TABLE `commande`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idClient` (`idClient`),
  ADD KEY `produits` (`produits`);

--
-- Index pour la table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`Time`),
  ADD KEY `idclient` (`idclient`);

--
-- Index pour la table `panier`
--
ALTER TABLE `panier`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idClient` (`idClient`),
  ADD KEY `qrProduit` (`qrProduit`);

--
-- Index pour la table `personne`
--
ALTER TABLE `personne`
  ADD PRIMARY KEY (`identifiant`),
  ADD KEY `type` (`type`),
  ADD KEY `identifiant` (`identifiant`);

--
-- Index pour la table `produit`
--
ALTER TABLE `produit`
  ADD PRIMARY KEY (`qrcode`),
  ADD KEY `nom_commercial` (`nom_commercial`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `commande`
--
ALTER TABLE `commande`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT pour la table `panier`
--
ALTER TABLE `panier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `produit`
--
ALTER TABLE `produit`
  MODIFY `qrcode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `commande`
--
ALTER TABLE `commande`
  ADD CONSTRAINT `commande_ibfk_1` FOREIGN KEY (`idClient`) REFERENCES `client` (`identifiant`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `panier`
--
ALTER TABLE `panier`
  ADD CONSTRAINT `panier_ibfk_1` FOREIGN KEY (`idClient`) REFERENCES `client` (`identifiant`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `panier_ibfk_2` FOREIGN KEY (`qrProduit`) REFERENCES `produit` (`qrcode`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
