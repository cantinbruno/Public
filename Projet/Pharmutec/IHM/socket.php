<?php
foreach($db->query('SELECT result FROM socket where num = (SELECT MAX(num) FROM socket)') as $result) {
$result = $result['result'];
} 
?>



