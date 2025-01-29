<?php

include('db.php');

$utec = "6 Bd Olof Palme, 77184 Émerainville";

function getLocation(){
    global $db;
    $username = $_SESSION['idUser'];
    $query = "SELECT * FROM commande WHERE idClient = '$username'";
    $result = mysqli_query($db, $query);
    $commande = mysqli_fetch_assoc($result);
    $adresse = $commande['adresse'];
    return $adresse;
}

function formatAdress($adresse){
    $adresse = str_replace(" ", "%20", $adresse);
    return $adresse;
}

function getAdress(){
    $adresse = getLocation();
    $adresse = formatAdress($adresse);
    $src = '//maps.google.com/maps?output=embed&amp;q=' . $adresse . 'z=10&amp;t=m" data-map="JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk1hbmhhdHRhbiUyQyUyME5ldyUyMFlvcmslMjIlMkMlMjJ6b29tJTIyJTNBMTAlMkMlMjJ0eXBlSWQlMjIlM0ElMjJyb2FkJTIyJTJDJTIybGFuZyUyMiUzQW51bGwlMkMlMjJhcGlLZXklMjIlM0FudWxsJTJDJTIybWFya2VycyUyMiUzQSU1QiU1RCU3RA=="';
    return $src;
}

function getProducts(){ 
    global $db;
    $username = $_SESSION['idUser'];
    $query = "SELECT * FROM commande WHERE idClient = '$username'";
    $result = mysqli_query($db, $query);
    $commande = mysqli_fetch_assoc($result);
    $products = $commande['produits'];
    return $products;
}

function getProductsDetails($products){
    global $db;
    $products = explode(',', $products);
    $productsDetails = array();
    foreach($products as $product){
        $query = "SELECT * FROM produit WHERE qrcode = '$product'";
        $result = mysqli_query($db, $query);
        $productDetail = mysqli_fetch_assoc($result);
        $productsDetails[] = $productDetail;
    }
    return $productsDetails;
}

$products = getProductsDetails(getProducts());
$location = getAdress();

/* echo getLocation(); */




?>