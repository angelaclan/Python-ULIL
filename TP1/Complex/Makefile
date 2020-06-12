PROJECT=Complex
AUTHOR=Raymond Calbuth, Achille Talon
PYTHONPATH=./src
export PYTHONPATH
SPHINXBUILD=python -m sphinx
CONFIGPATH=.
SOURCEDOC=sourcedoc
DOC=doc

.PHONY: clean doc archive author

clean:
	rm -f *~ */*~
	rm -rf __pycache__ src/__pycache__
	rm -rf $(DOC)
	rm -f $(PROJECT).zip

doc: author
	$(SPHINXBUILD) -c $(CONFIGPATH) -b html $(SOURCEDOC) $(DOC)

archive: clean
	zip -r $(PROJECT).zip images/* sourcedoc/* src/* _templates/* conf.py Makefile


author:
	sed -i -e 's/^project =.*/project = "$(PROJECT)"/g' conf.py
	sed -i -e 's/^copyright =.*/copyright = "2019, $(AUTHOR), Univ. Lille1"/g' conf.py
	sed -i -e 's/^author =.*/author = "$(AUTHOR)"/g' conf.py
