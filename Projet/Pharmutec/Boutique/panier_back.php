<?php 

include('db.php');
require_once('logManager.php');

if(isset($_SESSION['username'])){
    
    $products = getProducts();
    
}   

if(isset($_POST['validate'])) {
    $username = $_SESSION['idUser'];
    if(!empty($_POST['Type'])) {
        $type = $_POST['Type'];
        validatePanier($type);
    } else {
        echo 'Veuillez choisir un type de livraison';
    }
}

function getProducts(){ 
    global $db;
    $username = $_SESSION['idUser'];
    $query = "SELECT p.* FROM produit as p, panier as pa WHERE pa.idClient = '$username' AND p.qrcode = pa.qrProduit";
    $results = mysqli_query($db, $query);
    $products = array();
    while($row = mysqli_fetch_assoc($results)){
        $products[] = $row;
        
    }
    return $products;
}


function getProductQRCode($name){
    global $products;
    foreach($products as $product){
        if(strpos($product['nom_commercial'], $name) !== false){
            return $product['qrcode'];
        }
    }
}
function validatePanier($type){
    global $db;
    $username = $_SESSION['idUser'];
    $query = "SELECT p.qrCode FROM produit as p, panier as pa WHERE pa.idClient = '$username' AND p.qrcode = pa.qrProduit";
    $results = mysqli_query($db, $query);
    $products = array();
    while($row = mysqli_fetch_assoc($results)){
        $products[] = $row;    
    }
    $panier = array();
    foreach($products as $product){
        $qrcode = $product['qrCode'];
        $panier[] = $qrcode;
    }
    $panier = implode(',', $panier);
    $dateexpedition = date('d-m-Y');
    $datelivraison = date('d-m-Y', strtotime('+1 week'));
    if($type === 'enlevement'){
        $query2 = "INSERT INTO commande (idClient, produits, date_livraison, type_livraison, date_expedition, adresse, etat) VALUES ('$username', '$panier', '$datelivraison', '$type', '$dateexpedition', 'CFA UTEC' , '1')";
        mysqli_query($db, $query2);
        $query3 = "DELETE FROM panier WHERE idClient = '$username'";
        mysqli_query($db, $query3);
        $pyout = shell_exec("./runPythonScript.sh");
        createLog($username, "Validation_Commande_Enlevement");
        header('location: suivi.php'); 
        /* echo "Panier validé, commande passée"; */
    } else {
        $query2 = "INSERT INTO commande (idClient, produits, date_livraison, type_livraison, date_expedition, etat) VALUES ('$username', '$panier', '$datelivraison', '$type', '$dateexpedition', '1')";
        mysqli_query($db, $query2);
        $query3 = "DELETE FROM panier WHERE idClient = '$username'";
        mysqli_query($db, $query3);
        createLog($username, "Validation_Commande_Livraison");
        header('location: adresse.php');
        /* echo "Panier validé, commande passée"; */
    }
}
?>
