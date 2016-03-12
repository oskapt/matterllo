What is Matterllo ?
===================
Simple integration between Trello and Mattermost: send Trello activity notifications to Mattermost channels

.. image:: examples/matterllo.png

Is it ready ?
=============
Very soon: https://github.com/Lujeni/matterllo/milestones/0.1

Documentation
=============

`Here <http://matterllo.readthedocs.org/en/issue_2/requirements.html>`_

Usage
=====

.. code-block:: bash

    # Create your config file and export it
    # see examples/myboard.yaml
    $ export MATTERLLO_CONFIG_FILE='path/to/config.yaml'

    # Create the necessary trello webhook
    $ python matterllo/scripts/helper.py --init

    # Launch the application
    $ python run.py

Supported actions
=================

Boards and lists
----------------
- [x] List created
- [x] List renamed
- [x] List moved to other board
- [x] List archived/unarchived

Cards
-----
- [x] Card created
- [x] Card moved
- [x] Card renamed
- [x] Comment added to card
- [x] Attachment added to card
- [x] Description changed
- [x] Due date changed
- [x] Label changed
- [x] Member added to card
- [x] Card archived/unarchived

Checklists
----------
- [x] Checklist added to card
- [x] Checklist Item created
- [x] Checklist Item marked complete/incomplete

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
