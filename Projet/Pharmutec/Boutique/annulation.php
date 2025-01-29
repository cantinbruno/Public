<?php
include('header.php');
include('annulation_back.php');
?>
 <section class="u-section-6">
      <div class="u-sheet u-sheet-1">
        <p class="u-text-default u-text-1"> Etes-vous sur d'annuler votre commande ?</p>
        <form action="annulation.php" method="POST">
            <input type="submit" class="u-btn u-button-style u-palette-2-light-1 u-btn-1" name="confirm" value="Confirmer"/>
            <input type="submit" class="u-btn u-button-style u-grey-30 u-btn-2" name="annuler" value="Annuler"/>
        </form>
      </div>
    </section>
<?php
include('footer.php');
?>