[OSX] Connexion au Sheevaplug depuis la console série 
#####################################################

:date: 2010-12-10 00:00
:tags: osx,sheevaplug
:lang: fr

Alors que depuis un GNU/Linux un simple screen ou minicom suffit pour utiliser la console série d'un Sheevaplug (Jtag), sous OSX il faut effectuer quelques manipulations comme l'installation de drivers.

Installation du driver
~~~~~~~~~~~~~~~~~~~~~~
Rendez-vous sur le site de FTDIChip pour télécharger la dernière version du driver VCP.

http://www.ftdichip.com/Drivers/VCP.htm

Patch du driver
~~~~~~~~~~~~~~~
Actuellement le driver ne semble pas reconnaître le Sheevaplug. Il faut appliquer un patch sur */System/Library/Extensions/FTDIUSBSerialDriver.kext/Contents/Info.plist*.

`Télécharger le patch`__

__ ../static/patchs/FTDI_sheeva.patch

::

    $ sudo cp /System/Library/Extensions/FTDIUSBSerialDriver.kext/Contents/Info.plist /System/Library/Extensions/FTDIUSBSerialDriver.kext/Contents/Info.plist.sav
    $ sudo patch -p0 < FTDI_sheeva.patch
    $ sudo kextload /System/Library/Extensions/FTDIUSBSerialDriver.kext

Pour finir
~~~~~~~~~~
Dorénavant vous devriez voir deux nouveaux devices::

    $ ll /dev/tty.usbserial-FTSYFXGE*
    crw-rw-rw-  1 root  wheel   11,   6 30 jan 14:18 /dev/tty.usbserial-FTSYFXGEA
    crw-rw-rw-  1 root  wheel   11,   4 30 jan 14:18 /dev/tty.usbserial-FTSYFXGEB


Pour se connecter au port série on peut soit utiliser tout simplement **mnicom** ou alors passer par **screen**.    
::

    $ screen /dev/tty.usbserial-FTSKB964B 115200
