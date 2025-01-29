<?php

$db2 = new mysqli('10.17.105.91', 'dev', 'dev', 'supervision');

if ($db2->connect_error) {
    die("Connection failed: " . $db2->connect_error);
}
?>
