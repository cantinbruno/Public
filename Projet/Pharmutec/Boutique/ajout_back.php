<?php

include('db.php');
require_once('logManager.php');

if(!isset($_SESSION['admin'])){
    header('Location: index.php');
}

if(isset($_POST['ajout'])){
    $nomcommercial = $_POST['nomcommercial'];
    $etat = $_POST['etat'];
    $stockactuel = $_POST['stockactuel'];
    $stockprevu = $_POST['stockprevu'];
    $principeactif = $_POST['principeactif'];
    $descriptif = $_POST['descriptif'];
    $categorie = $_POST['categorie'];
    $laboratoirefabricant = $_POST['laboratoirefabricant'];
    $lieustockage = $_POST['lieustockage'];
    $image = $_POST['image'];
    $query = "INSERT INTO produit (nom_commercial, etat, stock_actuel, stock_prevu, principe_actif, descriptif, categorie, lab_fabricant, lieu_stockage, img) VALUES ('$nomcommercial', '$etat', '$stockactuel', '$stockprevu', '$principeactif', '$descriptif', '$categorie', '$laboratoirefabricant', '$lieustockage', '$image')";
    mysqli_query($db, $query);
    createLog($_SESSION['idUser'], "Ajout_Produit");
    header('location: index.php');
}
?>
