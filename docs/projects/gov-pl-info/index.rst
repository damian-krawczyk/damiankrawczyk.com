GPI - GOV PL Info
=================

.. image:: ../../_static/img/GPI-article-cover.png
    :alt: GPI - GOV PL Info article cover
    :target: .
    :align: center
    :width: 550px

**GPI - GOV PL Info** is a project initiated on April 1, 2021. The main goal of this 
project is to provide information being sent by the Polish Government in the 
form of mobile notifications. This has been easily achieved by using 
`Telegram Channels <https://telegram.org/tour/channels>`_. Since the source of 
information is provided in Polish, all notifications are being sent in Polish. 
However in addition they are automatically translated into English by the 
Google Translate service which should make life a bit easier for foreigners in 
Poland.

Target audience
---------------

This solution is dedicated **for everyone who cares about their health** and wants 
to receive information about:

- |MSI| - Main Sanitary Inspectorate in Poland warnings about **food products and 
  everyday products withdrawn** from sale in Poland due to different reasons,
- |MPI| - Main Pharmaceutical Inspectorate in Poland messages about **medicines 
  withdrawn** from sale in Poland due to different reasons,
- Polish Government announcements and **actions regarding the coronavirus** / COVID-19.

This solution is dedicated **for everyone who cares about their time** and wants 
to receive information in convenient way like:

- notifications directly on smartphone, tablet or computer,
- notifications in English and Polish which are easily to forward,
- information directly from source (`gov.pl <https://www.gov.pl>`_),
- information without advertisements,
- instant search of the message you're looking for, even among millions, 
  e.g. `gluten <https://t.me/s/gpi_gis?q=gluten>`_, 
  `Salmonella <https://t.me/s/gpi_gis?q=Salmonella>`_,
  `Pfizer <https://t.me/s/gpi_gif?q=Pfizer>`_,
  `Janssen <https://t.me/s/gpi_gif?q=Janssen>`_,
  `AstraZeneca <https://t.me/s/gpi_gif?q=AstraZeneca>`_,
  `Anti-crisis shield <https://t.me/s/gpi_koronawirus?q=Anti-crisis+shield>`_,
  etc.

Finally, this solution is dedicated for everyone who wants to give yourself a 
break from Facebook, Twitter, TV or radio.

How it works
------------

Current implementation of the solution works as follows:

1. Every day after midnight, content is being downloaded from `gov.pl <https://www.gov.pl>`_ websites.
2. If any articles were published on them on the previous day, 
   you will receive a notification in the Telegram application 
   on your smartphone, tablet or computer.

How to subscribe
----------------

1. If you don't have Telegram yet, download it from here https://telegram.org/dl/.
   
    Supported Operating Systems: Android, iOS, iPadOS, Windows, macOS, Linux.

2. Register following instructions on screen.
3. Subscribe to the |GPI| Telegram Channels.

  .. note::
    | **Your phone number is not visible to the rest of subscribers!** 
    | By default, your number is only visible to people who you've added to your address book as contacts. 
    | Read more here https://telegram.org/faq#q-who-can-see-my-phone-number

Channel list
------------

.. seealso::
  Check :doc:`THE LIST OF AVAILABLE GPI TELEGRAM CHANNELS <channels/index>` 
  and subscribe to the most interesting ones for you.

Technology stack
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

Contact
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