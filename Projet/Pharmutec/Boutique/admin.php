<?php
include('header.php');
include('admin_back.php');

if(isset($_SESSION['idUser'])){
  header('Location: index.php');
}


?>
 <section class="u-section-8">
      <div class="u-sheet u-sheet-1">
        <p class="u-text-default u-text-1">Connectez-vous en tant que administrateur</p>
        <div class="u-form-1">
          <form action="admin.php" method="POST" style="padding: 10px;">
            <div class="u-form-group">
              <label>Identifiant</label>
              <input type="text" placeholder="Entrez votre identifiant" name="identifiant" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label>Mot de passe</label>
              <input type="text" placeholder="Entrez votre mot de passe" name="motdepasse" class="u-border-1 u-input">
            </div>
            <div class="u-align-center u-form-group">
              <button type="submit" class="u-btn u-btn-submit" name="login">Connexion</button>
            </div>
          </form>
        </div>
      </div>
    </section>
<?php
include('footer.php');
?>
