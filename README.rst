What is Matterllo ?
===================
Simple integration between Trello and Mattermost: send Trello activity notifications to Mattermost channels 

Is it ready ?
=============
Very soon: https://github.com/Lujeni/matterllo/milestones/0.1

Usage
=====

.. code-block:: bash

    # Create your config file and export it
    # see examples/myboard.yaml
    $ export MATTERLLO_CONFIG_FILE='path/to/config.yaml'

    # Create the necessary webhook
    $ python matterllo/scripts/helper.py --init

    # Launch the application
    $ python run.py

Events
======
Mostly events will be supported very soon.

.. code-block:: bash

    createCard
    createList

Requirements
============
This code has been tested under Python **2.7**.

.. code-block:: bash

  # install by the setup
  Flask==0.10.1
  matterhook==0.1
  py-trello==0.4.3
  PyYAML==3.11

Installation
============
Pypi
----
Using pip (very soon):
::

    $ pip install matterllo
