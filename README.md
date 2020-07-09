# katrina

Nous souhaitons utiliser un modèle de Deep Learning, afin de produire un moteur de rendu capable d’adopter une stylisation « type » telle que la peinture chinoise. Dans un premier temps, il s’agira de proposer un modèle d’abstraction des peintures sélectionnées comme base d’apprentissage et d’utiliser le couple « peinture originale » / « abstraction » pour l’entraînement. Par la suite, un moteur de rendu d’abstractions sera connecté au réseau profond qui produira une peinture sur la base de l’abstraction.

Le modèle généré devra d'une part adopter la stylisation retenue mais aussi interpréter l'abstraction d'origine.



<h1>Sate of art</h1>
<br>
<strong>Holistically-Nested Edge Detection</strong><br>
https://github.com/s9xie/hed</br>

<strong>Pix2pix</strong><br>
https://github.com/eriklindernoren/Keras-GAN/blob/master/pix2pix/pix2pix.py<br>

<strong>GauGan</strong><br>
https://github.com/NVlabs/SPADE<br>

<strong>CycleGAN and pix2pix in PyTorch</strong><br>
https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix<br>




<h1>App</h1>

<strong>Requirements</strong>
<ul>
    <li>Npm</li>
    <li>python3</li>
    <li>keras</li>
</ul>

<strong>Usage</strong>
npm install<br>
node start.js<br>
go to : localhost:8080/index</br>




