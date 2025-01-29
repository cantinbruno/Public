<?php
include('header.php');
include('suivi_back.php');

if(!isset($_SESSION['idUser'])){
  header('Location: index.php');
}
?>
 <section class="u-section-5">
      <div class="u-sheet u-sheet-1">
        <p class=" u-text-1"> Suivi de votre commande :</p>
        <p > Description de votre commande<br> </p>
        <?php foreach($products as $product): ?>
          <div id="<?= $product['nom_commercial'] ?>">
              <p> - <?= $product['nom_commercial'] ?></p>
          </div>
        <?php endforeach; ?>
        <div class="u-map u-map-1">
          <div class="embed-responsive">
            <iframe class="embed-responsive-item" src="<?= $location ?>"></iframe>
          </div>
        </div>
        <a href="mailto:emailclient@test.fr?subject=Votre%20commande%20" class="u-btn u-button-style u-palette-3-light-2 u-btn-1">E-Mail récapitulatif</a>
        <a href="annulation.php" class="u-btn u-button-style u-palette-2-light-2 u-btn-2">Annuler ma commande</a>
        <a href="index.php" class="u-btn u-button-style u-palette-1-light-1 u-btn-3">Retourner à l'acceuil</a>
      </div>
    </section>
<?php
include('footer.php');
?>
