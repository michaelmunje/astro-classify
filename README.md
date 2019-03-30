Galana
======

Galana: **Gal**actic **Ana**lyzer is an open-source tool for applying machine learning to galaxies.

[![Build Status](https://travis-ci.com/michaelmunje/galana.svg?branch=master)](https://travis-ci.com/michaelmunje/galana)
 [![Coverage Status](https://coveralls.io/repos/github/michaelmunje/galana/badge.svg?branch=coveralls)](https://coveralls.io/github/michaelmunje/galana?branch=coveralls) [![Documentation Status](https://readthedocs.org/projects/galana/badge/?version=latest)](https://galana.readthedocs.io/en/latest/?badge=latest)

Documentation
-------------

The documentation for ``galana`` is available [here](https://galana.readthedocs.io/en/latest/?)

Installation & Dependencies
---------------------------

Dependencies: `Docker`

Installation: `Automatically installs by launching.`

How to Launch
-------------

Basic system: `./run.sh`

Jupyter notebook: `./run.sh jupyter`

Testing suite: `./run.sh test`

Troubleshooting
---------------

For those with an IDE, a virtual environment is available. This can also be used to troubleshoot.

Installing and running the virtual environment:

`cd envs; ./install.sh; source activate_env.sh`

Sometimes multiple docker container instances of the same image could cause problems. Run `./stop.sh` to retire all current containers.

Uninstalling
------------

Uninstallation: `./uninstall.sh`
