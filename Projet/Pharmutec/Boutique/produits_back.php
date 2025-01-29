<?php

include('db.php');
require_once('logManager.php');

$query = "SELECT * from produit";
$test = mysqli_query($db, $query);
 $products = array();
while($row = mysqli_fetch_assoc($test)){
    $products[] = $row;
}

if(isset($_POST['addPanier'])){
    $name = str_replace('Add ', '', $_POST['addPanier']);
    $name = str_replace(' to Panier', '', $name);
    $qrcode = getProductQRCode($name);
    if(!isset($_SESSION['username'])){
        echo 'Vous n\'êtes pas connecté';
    } else {
        $user = $_SESSION['idUser'];
        createLog($user, "Ajout_Produit");
        $query = "INSERT INTO panier (idClient, qrProduit) VALUES ('$user','$qrcode')";
        mysqli_query($db, $query);
    }  
}

function getProductQRCode($name){
    global $products;
    foreach($products as $product){
        if($product['nom_commercial'] == $name){
            return $product['qrcode'];
        }
    }
}
?>