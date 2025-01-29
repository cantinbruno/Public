<?php
include('header.php');
include('ajout_back.php');

/* if(!isset($_SESSION['idUser'])){
  header('Location: index.php');
} */
?>

<section class="u-section-9">
      <div class="u-sheet u-sheet-1">
        <p class="u-text-default u-text-1">Ajouter un produit</p>
        <div class="u-form u-form-1">
          <form action="ajout.php" method="POST" style="padding: 10px;">
            <div class="u-form-group">
              <label>Nom commercial</label>
              <input type="text" placeholder="Entrez le nom commercial" name="nomcommercial" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Etat</label>
              <input type="text" placeholder="Entrez l'etat" name="etat" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label">Stock actuel</label>
              <input type="text" placeholder="Entrez le stock actuel" name="stockactuel" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Stock prevu</label>
              <input type="text" placeholder="Entrez le stock prevu" name="stockprevu" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label>Principe actif</label>
              <input type="text" placeholder="Entrez le principe actif" name="principeactif" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label>Descriptif</label>
              <input type="text" placeholder="Entrez le descriptif" name="descriptif" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label>Categorie</label>
              <input type="text" placeholder="Entrez la categorie" name="categorie" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label>Laboratoire fabricant</label>
              <input type="text" placeholder="Entrez le laboratoire fabricant" name="laboratoirefabricant" class="u-border-1 u-input">
            </div>
            <div class="u-form-group">
              <label>Lieu de stockage</label>
              <input type="text" placeholder="Entrez le lieu de stockage" name="lieustockage" class="u-border-1 u-input" required="">
            </div>
            <div class="u-form-group">
              <label>Nom de l'image</label>
              <input type="text" placeholder="Entrez le nom de l'image" name="image" class="u-border-1 u-input">
            </div>
            <div class="u-align-center u-form-group">
              <button type="submit" class="u-btn u-btn-submit" name="ajout">Soumettre</button>
            </div>
          </form>
        </div>
      </div>
    </section>
<?php
include('footer.php');
?>
