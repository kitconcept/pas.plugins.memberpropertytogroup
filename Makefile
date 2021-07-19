# keep in sync with: https://github.com/kitconcept/buildout/edit/master/Makefile
# update by running 'make update'
SHELL := /bin/bash
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


# We like colors
# From: https://coderwall.com/p/izxssa/colored-makefile-for-golang-projects
RED=`tput setaf 1`
GREEN=`tput setaf 2`
RESET=`tput sgr0`
YELLOW=`tput setaf 3`

all: build
	bin/test

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
.PHONY: help
help: ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: Update Buildout
update: ## Update Buildout
	wget -O requirements.txt https://raw.githubusercontent.com/kitconcept/buildout/master/requirements.txt
	wget -O plone-5.2.x.cfg https://raw.githubusercontent.com/kitconcept/buildout/master/plone-5.2.x.cfg
	wget -O versions.cfg https://raw.githubusercontent.com/kitconcept/buildout/master/versions.cfg

bin/pip:
	python3 -m venv .
	bin/pip install --upgrade pip
	bin/pip install -r requirements.txt

.PHONY: Run buildout
bin/buildout: bin/pip
	bin/pip install --upgrade pip
	bin/pip install -r requirements.txt
	@touch -c $@
	
.PHONY: Build Plone 5.2
build-plone-5.2: bin/pip
	bin/pip install --upgrade pip
	bin/pip install -r requirements.txt
	bin/buildout -c plone-5.2.x.cfg

.PHONY: Build Latest Plone
build:
	make build-plone-5.2

.PHONY: Code Analysis
code-analysis:  ## Code Analysis
	bin/code-analysis
	bin/black src/ setup.py --check

.PHONY: Lint Python files
lint:  ## Lint files
	bin/code-analysis
	bin/isort setup.py src/
	bin/black setup.py src/

test:
	bin/test

test-all:
	bin/test --all

release:
	bin/fullrelease

clean:
	git clean -Xdf

.PHONY: all clean
