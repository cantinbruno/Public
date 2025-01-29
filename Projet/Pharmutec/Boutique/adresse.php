<?php
include('header.php');
include('adresse_back.php');

if(!isset($_SESSION['idUser'])){
    header('Location: index.php');
}

?>
<section class="u-section-4">
      <div class="u-sheet u-sheet-1">
        <p class="u-align-center u-text-1">Vos informations de livraison</p>
        <div class="u-form-1">
          <form action="adresse.php" method="POST" style="padding: 10px;">
            <div class="u-form-group">
              <label>Ville</label>
              <input type="text" placeholder="Entrez votre ville ou celle de l'officine" name="ville" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label >Code postal</label>
              <input type="text" placeholder="Entrez votre code postal ou celle de l'officine" name="codepostal" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Adresse</label>
              <input type="text" placeholder="Entrez votre adresse ou celle de l'officine" name="adresse" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Complement d'adresse</label>
              <input type="text" placeholder="Entrez votre complement d'adresse ou celle de l'officine" name="complement" class="u-border-1 u-input">
            </div>
            <div class="u-align-center u-form-group">
              <button type="submit" class="u-btn u-btn-submit" name="submitaddress">Soumettre</button>
            </div>
          </form>
        </div>
      </div>
    </section>
<?php
include('footer.php');
?>
