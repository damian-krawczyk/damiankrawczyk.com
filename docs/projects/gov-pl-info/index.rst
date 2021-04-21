GOV PL Info
===========

**GOV PL Info** is a project initiated on April 1, 2021. The main goal of this 
project is to provide information being sent by the Polish Government in the 
form of mobile notifications. This has been easily achieved by using 
`Telegram Channels <https://telegram.org/tour/channels>`_. Since the source of 
information is provided in Polish, all notifications are being sent in Polish. 
However in addition they are automatically translated into English by the 
Google Translate service which should make life a bit easier for foreigners in 
Poland.

.. note::
    Check :doc:`THE LIST OF AVAILABLE GPI TELEGRAM CHANNELS <channels/index>` 
    and subscribe to the most interesting ones for you.

First steps
-----------

1. If you don't have Telegram yet, download it from here https://telegram.org.
   
    Supported Operating Systems: Android, iOS, iPadOS, Windows, macOS, Linux.

2. Register following instructions on screen.
3. Subscribe to the |GPI| Telegram Channels listed below or check for more details about them :doc:`here <channels/index>`.


    .. list-table::
        :widths: 45 55
        :stub-columns: 1

        * - |GPI| |GIS| |MSI| Channel
          - https://t.me/gpi_gis
        * - |GPI| |GIF| |MPI| Channel
          - https://t.me/gpi_gif
        * - |GPI| Coronavirus Channel
          - https://t.me/gpi_koronawirus
        * - |GPI| Health Check Channel
          - https://t.me/gpi_health_check


technology stack
----------------

python
******

.. image:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png
    :alt: Python logo
    :target: https://python.org
    :align: left
    :width: 165px

Python has been used here to write the code to download the data from 
the selected `gov.pl <https://www.gov.pl>`_ subpages, parse it, extract 
articles lately released, translate them using Google Translate service and 
finally prepare them to be sent to the created Telegram Channels.

.. list-table::
    :widths: 25 75
    :stub-columns: 1

    * - |GPI| source code
      - https://github.com/damian-krawczyk/gov-pl-info

GitHub Actions
**************

.. image:: https://avatars.githubusercontent.com/u/44036562
    :alt: GitHub Actions logo
    :target: https://github.com/features/actions
    :align: left
    :width: 55px

GitHub Actions have been used to define workflows for selected 
`gov.pl <https://www.gov.pl>`_ threads and dedicated Telegram Channels. 
Each workflow starts after midnight |CET| or |CEST| to get articles 
released on the previous day.

.. list-table::
    :widths: 25 75
    :stub-columns: 1

    * - |GPI| workflows
      - https://github.com/damian-krawczyk/gov-pl-info/actions

Telegram
********

.. image:: https://telegram.org/img/t_logo.png
    :alt: Telegram
    :target: https://telegram.org
    :align: left
    :width: 55px

Here, Telegram is the main medium to provide notifications about articles 
extracted from selected `gov.pl <https://www.gov.pl>`_ subpages. Thanks to an
unlimited amount of subscribers, it should be possible to provide 
notifications to everyone living in Poland (38 137 795 - |GUS| |CSO| in Poland 
2020 - `source <https://stat.gov.pl/obszary-tematyczne/ludnosc/ludnosc/ludnosc-piramida/>`_).
Telegram supports the following Operating Systems: Android, iOS, iPadOS, Windows, macOS, Linux.

.. list-table::
    :widths: 45 55
    :stub-columns: 1

    * - |GPI| |GIS| |MSI| Channel
      - https://t.me/gpi_gis
    * - |GPI| |GIF| |MPI| Channel
      - https://t.me/gpi_gif
    * - |GPI| Coronavirus Channel
      - https://t.me/gpi_koronawirus
    * - |GPI| Health Check Channel
      - https://t.me/gpi_health_check


      
Google Translate
****************

.. image:: https://upload.wikimedia.org/wikipedia/commons/d/db/Google_Translate_Icon.png
    :alt: Google Translate service
    :target: https://translate.google.com
    :align: left
    :width: 55px

Google Translate is used to translate notifications from Polish to English.
Notifications containing information in both languages are being sent to 
dedicated Telegram Channels.

contact
-------

.. important::
    Have you ever faced any problem with this solution? 
    
    Have you noticed any errors?
    
    Would you like me to create similar solution suited to your exact needs? 
    
    **Let me know about it!**
    
    :doc:`CONTACT DETAILS <../../contact/index>`


.. toctree::
    :maxdepth: 2
    :glob:
    :hidden:
 
    channels/index