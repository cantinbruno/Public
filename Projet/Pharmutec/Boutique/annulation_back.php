<?php

include('db.php');
require_once('logManager.php');

function removeCommande(){
    global $db;
    $username = $_SESSION['idUser'];
    $query = "DELETE FROM commande WHERE idClient = '$username'";
    $result = mysqli_query($db, $query);
}

if(isset($_POST['confirm'])){
    removeCommande();
    createLog($_SESSION['idUser'], "Annulation_Commande");
    header('Location: index.php');
}
if(isset($_POST['annuler'])){
    header('Location: suivi.php');
}

?>