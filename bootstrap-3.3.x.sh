#!/bin/sh
ln -fs plone-3.3.x.cfg buildout.cfg
python2.4 plone-3.3.x-bootstrap.py -v 1.4.4
mkdir -p downloads
./bin/buildout
