<?php
include('header.php');
include('panier_back.php');
?>
    <section>
        <div class="u-sheet u-sheet-1">
        <table>
            <tr>
                <th> Produits de votre panier</th>
            </tr>
            <?php if(isset($_SESSION['idUser'])) {?>
            <?php foreach($products as $product): ?>
                <tr>
                    <td><?= $product['nom_commercial'] ?></td>
                </tr>
            <?php endforeach; ?>
            <?php } else { ?>
                <tr>
                    <td>Vous n'êtes pas connecté</td>
                </tr>
            <?php } ?>
            </table>
            <form method="POST" action="panier.php" id="validate">
                <select name="Type">
                    <option value="" disabled selected>>-- Type Livraison --<</option>
                    <option value="enlevement">Enlèvement</option>
                    <option value="livraison">Livraison</option>
                </select>
                <input type="submit" name="validate" class="u-btn u-btn-submit" value="Valider"/>
            </form>
        </div>
        </section>
 <br><br>
<?php
include('footer.php');
?>
