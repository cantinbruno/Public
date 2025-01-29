<?php

include('db.php');
require_once('logManager.php');

function removeClient(){
    global $db;
    $username = $_SESSION['idUser'];
    $query = "DELETE FROM client WHERE identifiant = '$username'";
    $result = mysqli_query($db, $query);
}

if(isset($_POST['confirm'])){
    $username = $_SESSION['idUser'];
    createLog($username, "Désinscription");
    session_destroy();
    removeClient();
    header('Location: index.php');  
}
if(isset($_POST['annuler'])){
    header('Location: index.php');
}


?>

