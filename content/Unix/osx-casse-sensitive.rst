[OSX] Disque sensible à la casse et applications récalcitrantes
######################################################################

:date: 2011-03-01 00:00
:tags: osx
:lang: fr

Il m'est arrivé plusieurs fois de ne pas pouvoir utiliser une application car celle-ci s'obstinait à ce que mon filesystem ne soit pas sensible à la casse comme par défaut sur OSX.

Il y a plusieurs solutions possibles pour y remédier :
- Reformater le disque
- Partitionner une partie du disque non sensible à la casse
- Utiliser une image disque

La dernière solution étant préférable pour ceux comme moi qui n'ont pas envie de s'amuser à formater leur disque.

Mise en place
~~~~~~~~~~~~~
Il suffit tout simplement de se rendre dans "Applications/Utilitaires/Utilitaire de Disque", ou via le terminal::

    $ open -a 'Disk Utility'

Puis "Nouvelle image"

- Nom : foobar
- Taille : C'est la taille maximale de l'image (celle-ci étant dynamique)
- Format : Mac OS étendu (journalisé)
- Partitions : Aucune table de partition
- Format d'image : Image disque SparseBundle

Utilisation
~~~~~~~~~~~
L'image est dorénavant accéssible comme n'importe quel disque depuis le Finder ou via::

    $ cd /Volumes/mon_image

Il suffit ensuite de glisser l'application dans l'image. Il y aura peut être des soucis au niveau des fichiers de configurations. 

La solution consiste à faire des liens symboliques depuis l'image.
