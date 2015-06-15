Buildout pour pelican
#####################

:date: 2012-06-03 00:00
:tags: pelican,blog,python,buildout
:lang: fr

J'utilise depuis un petit moment maintenant `pelican <http://pelican.notmyidea.org>`_ pour mon blog. C'est un script Python qui génère statiquement
un blog écrit à partir de `RestructuredText <http://docutils.sourceforge.net/rst.html>`_.

Pour simplifier son installation sur mon serveur, j'ai écris un `script buildout <http://blog.solevis.net/stuff/configs/buildout.cfg>`_ que je vous fais partager :

.. code-block:: bash

    [buildout]
    parts =
        pelican

    eggs =
        argparse
        pelican
        docutils
        pygments
        feedgenerator
        jinja2

    extra-paths =

    extensions = mr.developer
    sources = sources
    sources-dir = parts
    auto-checkout = *

    [sources]
    pelican = git git://github.com/ametaireau/pelican.git

    [pelican]
    recipe = zc.recipe.egg
    eggs = ${buildout:eggs}
    interpreter = python
    entry-points = pelican=pelican:main


Il récupère et installe pelican depuis les sources Git du projet.

Pour l'utiliser (récuperer le script bootstrap.py `ici <http://python-distribute.org/bootstrap.py>`_), puis :

.. code-block:: bash

    python bootstrap.py -d
    ./bin/buildout


