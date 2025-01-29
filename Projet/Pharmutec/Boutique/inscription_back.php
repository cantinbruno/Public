<?php

include('db.php');
require_once('logManager.php');

if(isset($_POST['register_pharma'])){
    $username = $_POST['identifiant'];
    $email = $_POST['email'];
    $password = $_POST['motdepasse'];
    $adresse = $_POST['adresse'];
    $numero = $_POST['numero'];
    $password = md5($password);
    $query = "INSERT INTO client (identifiant, motdepasse, adresse, telephone, email, nom_officine) VALUES ('$username', '$password', '$adresse', '$numero', '$email', 'Pharmacie')";
    mysqli_query($db, $query);
    $_SESSION['username'] = $username;
    createLog($username, "Inscription");
    header('location: index.php');
}
?>