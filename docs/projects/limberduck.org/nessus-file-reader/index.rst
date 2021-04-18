nessus file reader
==================

|latest_release| |stars_from_users| |supported_platform| |license|

.. image:: https://limberduck.org/en/latest/_images/LimberDuck-nessus-file-reader-logo.png
   :alt: LimberDuck nessus-file-reader logo
   :width: 120px
   :align: left
   :target: https://limberduck.org/en/latest/nessus-file-reader

This is a python module which enables you to quickly parse nessus files containing the results 
of scans performed by using *Nessus* or *Tenable.sc* by © Tenable, Inc. used
for |VA| [1]_ process. This module will let you get data 
through functions grouped into categories like file, scan, host, and plugin to get 
specific information from the provided nessus scan files e.g. file size, report name, 
report hosts names, the number of target hosts, the number of hosts scanned with 
credentialed checks, the number of reported plugins per Risk Factor, exact host scan 
times, outputs of particular plugins and a lot more. It's free and Open Source [2]_ tool.

.. list-table:: nessus file reader project details
    :widths: 25 75
    :stub-columns: 1

    * - main page
      - https://limberduck.org/en/latest/nessus-file-reader


technology stack
----------------

.. image:: https://www.python.org/static/community_logos/python-logo-master-v3-TM.png
   :alt: Python logo
   :target: https://python.org
   :width: 220px

.. |license| image:: https://img.shields.io/github/license/LimberDuck/nessus-file-reader.svg?style=social
    :target: https://github.com/LimberDuck/nessus-file-reader/blob/master/LICENSE
    :alt: License

.. |supported_platform| image:: https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=social
    :target: https://github.com/LimberDuck/nessus-file-reader
    :alt: Supported platform

.. |stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/nessus-file-reader?label=Stars%20from%20users&style=social
    :target: https://github.com/LimberDuck/nessus-file-reader
    :alt: Stars from users

.. |latest_release| image:: https://img.shields.io/github/v/release/LimberDuck/nessus-file-reader?label=Latest%20release&style=social
    :target: https://github.com/LimberDuck/nessus-file-reader/releases
    :alt: Latest release

.. rubric:: Footnotes

.. [1] read more about :term:`Vulnerability Assessment` in glossary
.. [2] read more about :term:`Open Source` in glossary