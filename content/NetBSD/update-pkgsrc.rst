Mise à jour de Pkgsrc en 2012Q3
###############################

:date: 2012-10-03 00:00
:tags: netbsd,pkgsrc,tips
:lang: fr

Depuis le 01 Octobre est disponible la branche 2012Q3_ de Pkgsrc. J'ai donc mis à jour mon /usr/pkgsrc grâce à cette commande (merci GuiGui2_) :

.. code-block:: bash
    
    cd /usr/pkgsrc
    sudo cvs -q update -dP -rpkgsrc-2012Q3

Aprés quelques minutes je suis passé en 2012Q3. Il ne me reste plus qu'à refaire tourner mon bulk, puis un pkgin fug pour mettre à jour mes programmes.

.. _GuiGui2: http://www.guigui2.net/dotclear/
.. _2012Q3: http://mail-index.netbsd.org/tech-pkg/2012/10/01/msg010099.html
