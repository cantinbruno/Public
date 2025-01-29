<?php
include('db.php');
require_once('logManager.php');

if(isset($_POST['login'])){
    $username = $_POST['identifiant'];
    $password = $_POST['motdepasse'];
    $password = md5($password);
    if(login_user($username, $password)){
        $user = getUserDetails($username);
        $_SESSION['username'] = $user['identifiant'];
        $_SESSION['idUser'] = $user['id'];
        $_SESSION['admin'] = true;
        createLog($user['identifiant'], "Connexion_Admin");
        header('location: ajout.php');  
    }
    else{
        echo "Identifiant ou mot de passe incorrect";
    }  
}

function login_user($username, $password){
    global $db;
    $query = "SELECT * FROM personne WHERE identifiant='$username' AND motdepasse='$password'";
    $results = mysqli_query($db, $query);
    if(mysqli_num_rows($results) == 1){
        return true;
    }else{
        return false;
    }
}

function getUserDetails($username){
    global $db;
    $query = "SELECT * FROM personne WHERE identifiant='$username'";
    $result = mysqli_query($db, $query);
    $user = mysqli_fetch_assoc($result);
    return $user;
}
?>
