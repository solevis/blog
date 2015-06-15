De l'UTF-8 dans ton $SHELL BSD
##############################

:date: 2011-04-16 00:00
:tags: shell
:lang: fr

La semaine dernière j'ai eu quelques soucis d'encodage suite à une installation par défaut de NetBSD. jpcw_ ayant eu le même soucis sur son FreeBSD, je vous donne les commandes magiques pour avoir des accents du plus bel effet dans votre $SHELL :

.. code-block:: bash
    
    echo "export LANG=en_US.UTF-8" >> ~/.profile
    echo "export LC_ALL=en_US.UTF-8" >> ~/.profile
    (ou .zprofile sur zsh)

Pour avoir la même chose dans tmux, on ajoute ceci dans sa configuration :

.. code-block:: bash
    
    echo "set-window-option -g utf8 on" >> ~/.tmux.conf

C'est tout bête, mais quand on le sait pas...

.. _jpcw: http://jp.camguilhem.net/
