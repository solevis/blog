Ajouter le support de Piwik dans Sphinx
#######################################

:date: 2012-10-15 00:00
:tags: sphinx,piwik,doc
:lang: fr

Dans Pelican il est simple de rajouter le code Javascript pour le tracking de Piwik à l'aide des options :

.. code-block:: bash
    
    PIWIK_URL="mon.piwik.net"
    PIWIK_SITE_ID="1"

Par contre, rien n'est prévu dans Sphinx (qui génére ma `documentation <http://docs.solevis.net>`_). Du coup il faut modifier le layout.html de son thème pour
ajouter le code Javascript.

On peut soit copier l'ensemble du thème qu'on utilise (s'il fait partie des thèmes par défaut) et modifier directement le layout.html. Ou alors plus simplement étendre le thème qu'on utilise pour rajouter seulement notre code Javascript.
Pour cela il faut configurer son conf.py et y ajouter l'option :

.. code-block:: bash
    
    cd /source/de/la/doc
    ${EDITOR} conf.py

.. code-block:: bash
    
    templates_path = ['_templates']

Ensuite on créé le dossier **_templates** à la racine de nos sources et un fichier **layout.html** à l'intèrieur:

.. code-block:: bash
    
    mkdir _templates
    ${EDITOR} _templates/layout.html

Il suffit ensuite "d'hériter" du layout original du thème et de rajouter notre code :

.. code-block:: html
    
    {% extends "!layout.html" %}

    {% block footer %}
    {{ super() }}
    <!-- Piwik -->
      <script type="text/javascript">
      var pkBaseURL = (("https:" == document.location.protocol) ? "https://mon.piwik.net/" : "http://mon.piwik.net/");
      document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));

      </script>

      <script type="text/javascript">

        try {
        var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 1);
        piwikTracker.trackPageView();
        piwikTracker.enableLinkTracking();
        } catch( err ) {}
      </script>
      <noscript><p><img src="http://mon.piwik.net/piwik.php?idsite=1" style="border:0" alt="" /></p></noscript>
    <!-- End Piwik Tracking Code -->
    {% endblock %}

Dorénavant toutes les pages de la documentation Sphinx possèderont le code Javascript du tracking de Piwik.

