<?php 

include('header.php');
include('produits_back.php');

?>           

<head>
    <title>Nos produits</title>
</head>
    <body>
        <section class="container_products">
            <div class="products">
                <?php foreach($products as $product): ?>
                    <?php $img = 'images/' . $product['img']. ".png"; ?>
                    <div class="product" id="<?= $product['nom_commercial'] ?>">
                        <img class="prod_img" src="<?= $img ?>" alt="<?= $product['nom_commercial'] ?>">
                        <h3><?= $product['nom_commercial'] ?></h3>
                        <p><?= $product['descriptif'] ?></p>
                        <form action="produits.php" method="POST">
                            <input type="submit" name="addPanier" value="Add <?= $product['nom_commercial'] ?> to Panier"/>
                        </form>
                    </div>
                <?php endforeach; ?>
            </div>
        </section>
        </section>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
    </body>
</html>
<?php

include('footer.php');

?>
