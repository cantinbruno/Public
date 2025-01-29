<?php
  include('Header.php');
  include('db.php');
  include('socket.php');
?>
<html>
  <body>
      <div class="u-sheet">
	<pre><?php echo "Logs du site web lapharmutec :" . "<br>" . "<br>";?></pre>
	<?php
	$result = $db->query('SELECT time, idclient, log_message FROM log');
	if ($result->num_rows > 0) {
  	while($row = $result->fetch_assoc()) {
  	?>
    	<pre><?php echo $row["time"] ." ". $row["idclient"] ." ". $row["log_message"]. "<br>";?></pre>
    	<?php
  	}}
  	?>
      </div>
  </body>
</html>
