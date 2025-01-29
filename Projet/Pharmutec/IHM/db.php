<?php
$db = new mysqli('localhost', 'dev', 'dev', 'supervision');
if ($db->connect_error) {
    die("Connection failed: " . $db->connect_error);
}
?>
