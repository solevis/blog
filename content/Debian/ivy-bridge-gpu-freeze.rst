Debian, Ivy Bridge, HD 4000 et freeze à gogo
############################################

:date: 2013-02-28 00:00
:tags: debian,intel,gpu,freeze,tips
:lang: fr

J'ai installé sur mon nouveau lappy Debian Wheezy, et j'ai été confronté à quelques soucis : des freeze aléatoire du système. J'ai d'abord pensé à un crash de Xorg, mais je ne pouvais même pas me connecter via SSH, pas de capslock, juste un bon hard poweroff des familles.

Après quelques recherches sur Google et une recommandation de `Llew <http://www.llew.me/>`_ je suis tombé sur ce `PR <http://bugs.debian.org/cgi-bin/bugreport.cgi?archive=no&bug=689268>`_. Il s'avère que la nouvelle architecture Intel Ivy Bridge est pas vraiment stable avant la version 3.4 du kernel. Sauf que bien sûr Debian Wheezy est livré par défaut avec le kernel 3.2.

J'ai donc installé la version experimental du kernel, donc voici un rapide howto :

Ajouter le dépôt experimental :

.. code-block:: bash

    echo 'deb http://ftp.de.debian.org/debian experimental main' >> /etc/apt/sources/list

Installer la dernière version du kernel :

.. code-block:: bash

    aptitude install -t experimental linux-image-3.7-trunk-amd64

Plus aucun freeze depuis maintenant deux jours.

Pour rendre ça plus propre, on peut ajouter un peu de pinning :

.. code-block:: bash

    cat /etc/apt/preferences << EOF
    Package: linux-image-*
    Pin: release a=experimental
    Pin-Priority: 900
    EOF

On vérifie :

.. code-block:: bash

    apt-policy linux-image-3.7

.. code-block:: bash

    linux-image-3.7-trunk-amd64-dbg:
      Installé : (aucun)
      Candidat : 3.7.8-1~experimental.1
     Table de version :
         3.7.8-1~experimental.1 900
            700 http://ftp.univ-pau.fr/linux/mirrors/debian/ experimental/main amd64 Packages
    linux-image-3.7-trunk-amd64:
      Installé : 3.7.8-1~experimental.1
      Candidat : 3.7.8-1~experimental.1
     Table de version :
     *** 3.7.8-1~experimental.1 900
            700 http://ftp.univ-pau.fr/linux/mirrors/debian/ experimental/main amd64 Packages
            100 /var/lib/dpkg/status


