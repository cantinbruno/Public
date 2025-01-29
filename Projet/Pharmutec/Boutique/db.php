<?php

$db = new mysqli('localhost', 'dev', 'dev', 'pharmutek');

if ($db->connect_error) {
    die("Connection failed: " . $db->connect_error);
}
?>
