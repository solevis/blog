Buildout pour pelican v2
########################

:date: 2013-02-27 00:00
:tags: pelican,blog,python,buildout
:lang: fr

J'ai mis à jour mon buildout pour `pelican <http://pelican.notmyidea.org/>`_. Je n'utilise plus la version git depuis que les releases sont plus fréquentes sur `pypi <https://pypi.python.org/pypi/pelican/>`_

.. code-block:: bash

    [buildout]
    newest = true
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

    [pelican]
    recipe = zc.recipe.egg
    eggs = ${buildout:eggs}
    interpreter = python
    entry-points = pelican=pelican:main

Pour l'utiliser (récuperer le script bootstrap.py `ici <http://python-distribute.org/bootstrap.py>`_), puis :

.. code-block:: bash

    python bootstrap.py -d
    ./bin/buildout

En bonus un Makefile pour se faciliter les choses :

.. code-block:: bash

    build:
        bin/pelican -s solevis.cfg.py content

    clean:
        rm -rfv output/

