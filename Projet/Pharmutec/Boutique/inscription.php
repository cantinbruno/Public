<?php
include('header.php');
include('inscription_back.php');
?>
<section class="u-section-2">
      <div class="u-sheet u-sheet-1">
        <p class="u-text-default u-text-1"> Inscrivez-vous</p>
        <div class="u-form-1">
          <form action="inscription.php" method="POST" style="padding: 10px;">
            <div class="u-form-group">
              <label>Identifiant</label>
              <input type="text" placeholder="Entrez votre identifiant" name="identifiant" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Email</label>
              <input type="email" placeholder="Entrez une adresse mail valide" name="email" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Mot de passe</label>
              <input type="password" pattern="(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[-+!*$@%_])([-+!*$@%_\w]{8,15})$" title="Le mot de passe doit contenir au moins 8 caractères dont 1 majuscule, 1 minuscule, 1 chiffre et 1 caractère spécial" placeholder="Entrez votre mot de passe" name="motdepasse" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Adresse</label>
              <input type="text" placeholder="Entrez votre adresse" name="adresse" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Téléphone</label>
              <input type="tel" pattern="\+?\d{0,2}[\s\(\-]?([0-9]{3})[\s\)\-]?([\s\-]?)([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})" placeholder="Entrez votre téléphone" name="numero" class="u-border-1 u-input" required="">
            </div>
            <div  class="u-align-center u-form-group">
              <button type="submit" class="u-btn u-btn-submit" name="register_pharma">Inscription</button>
            </div>
          </form>
        </div>
      </div>
    </section>
<?php
include('footer.php');
?>
