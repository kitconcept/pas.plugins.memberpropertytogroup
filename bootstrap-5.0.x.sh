#!/bin/sh

# see https://community.plone.org/t/not-using-bootstrap-py-as-default/620
ln -s plone-5.0.x.cfg buildout.cfg
rm -r ./lib ./include ./local ./bin
virtualenv --clear .
./bin/pip install zc.buildout 
./bin/buildout 
