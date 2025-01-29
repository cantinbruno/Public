<?php
  include('refresh.php');
  include('Header.php');
  include('db.php');
  include('socket.php');
?>
<html>
  <body>
      <div class="u-sheet">
        <?php 
        if($result == 'irmateriauxon' ){
          $db->query('UPDATE etat SET irmateriaux = 1');
          }
        if($result == 'irmateriauxoff' ){
          $db->query('UPDATE etat SET irmateriaux = 0');
          }
	foreach($db->query('SELECT irmateriaux FROM etat') as $irmateriaux) {
        if($irmateriaux['irmateriaux'] == '1'){
          ?>
          <script>irmateriaux = 1</script><p> Infrarouge materiaux: actif</p>
          <?php
        }else{
          ?>
          <script>irmateriaux = 0</script><p> Infrarouge materiaux: inactif</p>
        <?php
        }}
        ?>
        
        <?php
        if($result == 'irdepoton' ){
          $db->query('UPDATE etat SET irdepot = 1');
          }
        if($result == 'irdepotoff' ){
          $db->query('UPDATE etat SET irdepot = 0');
          }
        foreach($db->query('SELECT irdepot FROM etat') as $irdepot) {
        if($irdepot['irdepot'] == '1'){ 
         ?>
          <script>irdepot = 1</script><p> Infrarouge depot: actif</p>
          <?php
        }else{
          ?>
          <script>irdepot = 0</script><p> Infrarouge depot: inactif</p>
          <?php
        }}
        ?>
        
        <?php 
        if($result == 'irpistonon' ){
          $db->query('UPDATE etat SET irpiston = 1');
          }
        if($result == 'irpistonoff' ){
          $db->query('UPDATE etat SET irpiston = 0');
          }
         foreach($db->query('SELECT irpiston FROM etat') as $irpiston) {
         if($irpiston['irpiston'] == '1'){ 
          ?>
          <script>irpiston = 1</script><p>Infrarouge piston: actif</p>
          <?php
        }else{
          ?>
          <script>irpiston = 0</script><p>Infrarouge piston: inactif</p>
          <?php
        }}
        ?>
        
        <?php 
        if($result == 'cameraon' ){
          $db->query('UPDATE etat SET camera = 1');
          }
        if($result == 'cameraoff' ){
          $db->query('UPDATE etat SET camera = 0');
          }
        foreach($db->query('SELECT camera FROM etat') as $camera) {
        if($camera['camera'] == '1'){ 
          ?>
          <script>camera = 1</script><p> Camera: actif</p>
          <?php
        }else{
          ?>
          <script>camera = 0</script><p> Camera: inactif</p>
          <?php
        }}
        ?>
        
        <?php 
        if($result == 'moteuron' ){
          $db->query('UPDATE etat SET moteur = 1');
          }
        if($result == 'moteuroff' ){
          $db->query('UPDATE etat SET moteur = 0');
          }
        foreach($db->query('SELECT moteur FROM etat') as $moteur) {
        if($moteur['moteur'] == '1'){ 
          ?>
          <script>moteur = 1</script><p> Moteur: actif</p>
          <?php
        }else{
          ?>
          <script>moteur = 0</script><p> Moteur: inactif</p>
          <?php
        }} 
        ?>
        
        <?php 
        if($result == 'pistonon' ){
          $db->query('UPDATE etat SET piston = 1');
          }
        if($result == 'pistonoff' ){
          $db->query('UPDATE etat SET piston = 0');
          }
        foreach($db->query('SELECT piston FROM etat') as $piston) {
        if($piston['piston'] == '1'){ 
          ?>
          <script>piston = 1</script><p> Piston: actif</p>
          <?php
        }else{
          ?>
          <script>piston = 0</script><p> Piston: inactif</p>
          <?php
        }}
        ?>
        
        <?php 
        if($result == 'proximiteon' ){
          $db->query('UPDATE etat SET proximite = 1');
          }
        if($result == 'proximiteoff' ){
          $db->query('UPDATE etat SET proximite = 0');
          }
        foreach($db->query('SELECT proximite FROM etat') as $proximite) {
        if($proximite['proximite'] == '1'){ 
          ?>
          <script>proximite = 1</script><p> Capteur proximite: actif</p>
          <?php
        }else{
          ?>
          <script>proximite = 0</script><p> Capteur proximite: inactif</p>
          <?php
        }}
        ?> 
         
        <?php 
        if($result == 'metalon' ){
          $db->query('UPDATE etat SET metal = 1');
          }
        if($result == 'metaloff' ){
          $db->query('UPDATE etat SET metal = 0');
          }
        foreach($db->query('SELECT metal FROM etat') as $metal) {
        if($metal['metal'] == '1'){ 
          ?>
          <script>metal = 1</script><p> Capteur Metal: actif</p>
          <?php
        }else{
          ?>
          <script>metal = 0</script><p> Capteur Metal: inactif</p>
          <?php
        }}
        ?>
        
      </div>
       <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
       <div id="chart_div" style="width: 100%; height: 250px;"></div>
        <script>
        google.charts.load('current', {
        'packages': ['corechart']
      });
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Nom élément', 'Etat'],
          ['IR Matériaux', irmateriaux],
          ['IR dépot', irdepot],
          ['IR Piston', irpiston],
          ['Caméra', camera],
          ['Moteur', moteur],
          ['Piston', piston],
          ['Proximite', proximite],
          ['Metal', metal]
        ]);
        var options = {
          title: 'Graphique des états du processus',
          hAxis: {
          },
          vAxis: {
            minValue: 0
          }
        };
        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
      </script>
    </head>
  </body>
</html>
