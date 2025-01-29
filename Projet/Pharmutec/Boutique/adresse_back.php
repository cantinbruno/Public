<?php

include('db.php');

if(isset($_POST['submitaddress'])){
    $ville = $_POST['ville'];
    $codepostal = $_POST['codepostal'];
    $adresse = $_POST['adresse'];
    $complement = $_POST['complement'] ? $_POST['complement'] : '';
    $adressecomplet = $adresse . " " . $codepostal . " " . $ville;
    comfirmAdresse($adressecomplet);
    $pyout = shell_exec("./runPythonScript.sh");
    header('location: suivi.php');
}

function comfirmAdresse($adresse){
    global $db;
    $username = $_SESSION['idUser'];
    $query = "UPDATE commande SET adresse = '$adresse' WHERE idClient = '$username'";
    mysqli_query($db, $query);
}
?>

