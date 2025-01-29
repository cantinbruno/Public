<?php

session_start();

require_once('logManager.php');

if (isset($_GET['logout'])) {
    createLog($_SESSION['username'], "Déconnexion");
    session_destroy();
    unset($_SESSION['username']);
    header("location: index.php");
}

?>
<html>
  <head>
    <title>LAPHARMUTEC</title>
    <link rel="stylesheet" href="reglage.css">
    <link rel="stylesheet" href="site.css" >
    <script  type="text/javascript" src="jquery.js"></script>
    <script type="text/javascript" src="reglage.js"></script>
  </head>
  <body class="u-body u-xl-mode">
    <header class=" u-header u-palette-4-light-3">
      <div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-custom-font u-font-georgia u-text-1">
          <span style="font-size: 3rem;">LAPHARMUTEC</span>
        </p>
        <nav class="u-menu u-menu-1">
          <div>
     <ul class="u-nav u-unstyled u-nav-1">
     <li class="u-nav-item"><a class="u-nav-link u-text-hover-palette-2-base" href="index.php" style="padding: 10px;">Accueil</a>
</li><li class="u-nav-item"><a class="u-nav-link u-text-hover-palette-2-base" href="inscription.php" style="padding: 10px;">Inscription</a>
</li><li class="u-nav-item"><a class="u-nav-link u-text-hover-palette-2-base" href="connexion.php" style="padding: 10px;">Connexion</a>
</li><li class="u-nav-item"><a class="u-nav-link u-text-hover-palette-2-base" href="produits.php" style="padding: 10px;">Nos produits</a>
</li><li class="u-nav-item"><a class="u-nav-link u-text-hover-palette-2-base" href="panier.php" style="padding: 10px;">Panier</a>
</li><li class="u-nav-item"><a class="u-nav-link u-text-hover-palette-2-base" href="index.php?logout='1'" style="padding: 10px;">Deconnexion</a>
</li></ul>
        </div>
      </nav>
    <img class="u-expanded-height u-image u-image-1" src="images/Logo-Pharmacie.png">
  </div></header>
  <br>
    <div style="display:flex; justify-content: center; align-items: center; font-size:medium; margin-top: -25px !important;">
        <?php if (isset($_SESSION['username'])) : ?>
            <p>Connecté en tant que : <strong><?php echo $_SESSION['username']; ?></strong></p>
        <?php endif ?>
    </div>
