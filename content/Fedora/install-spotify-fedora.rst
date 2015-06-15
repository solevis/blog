Installation de Spotify sur Fedora
##################################

:date: 2014-11-02 00:00
:tags: fedora,spotify,howto
:lang: fr

Rapide HOWTO sur l'installation de Spotify sur Fedora. J'ai testé sur fedora 20 et ça fonctionne sans problème. Il y a deux méthodes pour installer
Spotify sur Fedora, soit utiliser lpf-spotify-client du dépôt RPMFusion, ou via installation manuelle. Personnellement je n'ai pas réussi à faire fonctionner lpf-spotify-client, du coup je me suis rabbatu sur l'installation manuelle (du même auteur que le RPM lpf-spotify-client) :

Récupération des sources :

.. code-block:: bash

    git clone https://github.com/leamas/spotify-make.git

Compilation :

.. code-block:: bash

    cd spotify-make
    ./configure  --prefix=/opt/local --bindir=/usr/bin
    make download
    make install

Création du fichier Desktop :

.. code-block:: bash

    make register

Et voilà, bonne écoute ;)
