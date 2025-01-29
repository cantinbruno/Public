<?php
  include('Header.php');
  include('refresh.php');
  include('db.php');
  include('socket.php');
  
?> 
<html>
  <body>
    <div class="u-sheet">
      <p> File d'attente:
      <?php
      if($result == 'filedattenteplus'||$result == 'filedattentemoins'){
        foreach($db->query("SELECT COUNT(result) FROM socket WHERE result = 'filedattenteplus'") as $fileplus){
        $fileplus = $fileplus['COUNT(result)'];
        }
        foreach($db->query("SELECT COUNT(result) FROM socket WHERE result = 'filedattentemoins'") as $filemoins){
        $filemoins = $filemoins['COUNT(result)'];
        }
        $file = $fileplus - $filemoins;
        
        if($file < 0){
          $file = 0;
          }
        $db->query("UPDATE commande SET attente = '$file'");
        }
      foreach($db->query('SELECT attente FROM commande') as $file) {
      $file = $file['attente'];
      }
      echo($file);
      ?>
      </p>
      
      <p> En cours:
      <?php 
      if($result == 'coursplus'||$result == 'coursmoins'){
        foreach($db->query("SELECT COUNT(result) FROM socket WHERE result = 'coursplus'") as $coursplus){
        $coursplus = $coursplus['COUNT(result)'];
        }
        foreach($db->query("SELECT COUNT(result) FROM socket WHERE result = 'coursmoins'") as $coursmoins){
        $coursmoins = $coursmoins['COUNT(result)'];
        }
        $cours = $coursplus - $coursmoins;
        if($cours < 0){
          $cours = 0;
          }
        if($cours > 4){
          $cours = 4;
          }
        $db->query("UPDATE commande SET cours = '$cours'");
        }
      foreach($db->query('SELECT cours FROM commande') as $cours) {
      $cours = $cours['cours'];
      }
      echo($cours);
      ?>
      </p>
      
      <p> En zone d'enlevement:
      <?php 
      if($result == 'enlevement'){
        foreach($db->query("SELECT COUNT(result) FROM socket WHERE result = 'enlevement'") as $enlevement){
        $enlevement = $enlevement['COUNT(result)'];
        }
        if($enlevement < 0){
          $enlevement = 0;
          }
        $db->query("UPDATE commande SET enlevement = '$enlevement'");
        }
      foreach($db->query('SELECT enlevement FROM commande') as $enlevement) {
      $enlevement = $enlevement['enlevement'];
      }
      echo($enlevement);
      ?>
      </p>
    
      <p> En zone de livraison: 
      <?php 
      if($result == 'livraison'){
        foreach($db->query("SELECT COUNT(result) FROM socket WHERE result ='livraison'") as $livraison){
        $livraison = $livraison['COUNT(result)'];
        }
        if($livraison < 0){
          $livraison = 0;
          }
        $db->query("UPDATE commande SET livraison = '$livraison'");
        }
      foreach($db->query('SELECT livraison FROM commande') as $livraison) {
      $livraison = $livraison['livraison'];
      }
      echo($livraison);
      ?>
      </p>
    
      <p> Identifiant commande convoyé:
      <?php
      if(preg_match('/[0-9]+[a-z]+/', $result)){
        $sql = "INSERT INTO identifiant (idcommande) VALUES ('$result') ON DUPLICATE KEY UPDATE idcommande = idcommande";
        $db->query($sql);
 	}
      $result = $db->query('SELECT idcommande FROM identifiant');
      if($result->num_rows > 0) {
  	while($row = $result->fetch_assoc()) {
    	  echo $row["idcommande"] . " ";
       }} 
      ?>
      </p>
    </div>
    <head>
   <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <div id="chart_div"style="width: 100%; height: 400px;"></div>
  <script>
  google.charts.load('current', {packages: ['corechart', 'bar']});
  google.charts.setOnLoadCallback(drawBasic);
  function drawBasic() {
      var data = google.visualization.arrayToDataTable([
        ['City', 'Nombre',],
        ['File attente', <?=$file?>],
        ["", 0],
        ['En cours', <?=$cours?>],
        ["", 0],
        ['Enlevement', <?=$enlevement?>],
        ["", 0],
        ['Livraison', <?=$livraison?>]
      ]);
      var options = {
        title: 'Graphique des états des commande',
        chartArea: {width: '50%'},
        hAxis: {
          minValue: 0
        },
        vAxis: {
        }
      };
      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }
  </script>
    </head>
  </body>
</html>
