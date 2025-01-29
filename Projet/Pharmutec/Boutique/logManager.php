<?php

include('db2.php');


function createLog($iduser, $message){
    global $db2;
    $query = "INSERT INTO log (idclient, log_message) VALUES ('$iduser', '$message')";
    mysqli_query($db2, $query);
}

?>