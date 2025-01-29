<?php

require_once('logManger.php');

if (isset($_GET['logout'])) {
    createLog($_SESSION['idUser'], "Déconnexion");
    session_destroy();
    unset($_SESSION['username']);
    header('location: index.php');
}
?>