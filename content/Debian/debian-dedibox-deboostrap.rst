Installation personnalisée de Debian sur Dedibox
################################################

:date: 2012-10-25 00:00
:tags: debian,dedibox,howto
:lang: fr

Suite à la baisse des prix des Dedibox, je me suis loué un petit SC histoire de migrer mon serveur@home dans un datacenter (et utiliser une vraie table basse dans le salon du coup).

Sauf que par défaut online.net vous propose un plan de partionnement, et vous n'avez pas le choix, c'est le leur ou rien. Vu que je compte m'amuser un peu avec du LVM, c'était pas très commode.

Du coup avec l'aide de l'ami Llew_ j'ai installé une version perso de Debian en utilisant debootstrap et chroot avec un partionnement à moi. J'ai écris une doc pour me souvenir de la démarche, que je partage comme d'habitude :

http://docs.solevis.net/debian/custom-install-dedibox.html

Maintenant j'ai une partition de 4GB pour ma Debian, et je compte utiliser le reste de mon disque pour installer un autre Debian (en gardant le premier en rescue) sur du LVM en tant que dom0 pour mes futurs domU netbsd.

.. _Llew: http://www.llew.me/
