# Makefile for Sphinx documentation
#
# $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/$$lang;
#

# You can set these variables from the command line.
BUILDDIR     = build
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         = a4
SHELL = /bin/bash
TRANSLATIONS_STATIC  = en
TRANSLATIONS_I18N  = de fr it ro
LANGUAGES     = $(TRANSLATIONS_STATIC) $(TRANSLATIONS_I18N)
BUILD_LANGUAGES = $(TRANSLATIONS_I18N) $(TRANSLATIONS_STATIC)

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees/$$lang $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) -c . -A language=$$lang -D language=$$lang -A languages='$(LANGUAGES)'

ALLSPHINXOPTSI18N = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) -c . -a -A language=$$lang -D language=$$lang -A languages='$(LANGUAGES)'

# Only for Gettext
I18NSPHINXOPTS   = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) -c . -A language=en -D language=en -A languages='en'

.PHONY: help clean html web pickle htmlhelp latex changes linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  init      to preprocess translation directories"
	@echo "  compile_messages    to compile po to mo files"
	@echo "  generate_po_from_tmpl    to duplicate pot to po files for a language, e.g from i18n\pot directory to i18n\lang"
	@echo "  pickle    to make pickle files"
	@echo "  json      to make JSON files"
	@echo "  htmlhelp  to make HTML files and a HTML help project"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  all-pdf   to make PDF file"
	@echo "  all-ps    to make PS file"
	@echo "  changes   to make an overview over all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"
	@echo "  gettext   to generate pot files from en rst files"
	@echo "  gettext_copy   to duplicate pot files from gettext dir to i18n\pot"

clean:
	-rm -rf $(BUILDDIR)/* init compile_messages

clean-repo: clean
	@set -e; for lang in $(TRANSLATIONS_STATIC) ;\
	do \
		for file in `find $$lang -type f -a -regex '.*\.*$$' -a -not -regex '.*\.$$' -a -not -regex '.*\.svn.*' -printf "%p\n" ; cd ..;`; \
		do \
			echo "Working on "$$file ; \
#			is file in git? \
			if [ ! -d "$$file" -a -n "`git status --porcelain $$file`" ]; then  \
				rm -f "$$file"; \
#				is dir empty? \
				ldir=`dirname "$$file" `; \
				if [ ! -n "`ls -1 $$ldir`" ]; then \
					echo "Removing empty dir "$$ldir; \
					rm -rf "$$ldir"; \
				fi \
			fi \
		done ; \
	done
	@echo "Clean-repo finished."

init: en/*
	@set -e; for lang in $(TRANSLATIONS_STATIC) ;\
	do \
		for file in `cd en; find . -type f -name '*.rst' ; cd ..;`; \
		do \
			if [ ! -f $$lang/$$file ]; then  \
				mkdir -p `dirname "$$lang/$$file"`; \
				(echo ".. meta::"; echo "  :ROBOTS: NOINDEX") | cat - "en/$$file" > "$$lang/$$file"; \
			fi \
		done; \
		for file in `cd en; find . -type f ; cd ..;`; \
		do \
			if [ ! -f $$lang/$$file ]; then  \
				mkdir -p `dirname "$$lang/$$file"`; \
				cp -p "en/$$file" "$$lang/$$file"; \
			fi \
		done; \
	done
	@echo "Init finished. Other target can now be built.";\
	touch init

transifex_sync: gettext
	@set -e;\
	./scripts/create_transifex_resources.sh; \
	tx push -s; \
	tx pull
	@echo "Transifex resources synchronized"

compile_messages: init i18n/*/*.po
	@set -e; for lang in $(TRANSLATIONS_I18N) ;\
	do \
		echo "Compiling messages for $$lang..."; \
		for f in `find ./i18n/$$lang -type f -name \*.po`; \
		do \
		bn=`basename $$f .po`; \
		echo "Compiling messages for $$f"; \
		mkdir -p ./i18n/$$lang/LC_MESSAGES; \
		msgfmt $$f -o ./i18n/$$lang/LC_MESSAGES/$$bn.mo; \
		done; \
	done
	@echo "Messages compiled. Now you can build updated version for html and pdf.";\
	touch compile_messages

html: compile_messages
	@set -e; \
	lang=en; \
	mkdir -p $(BUILDDIR)/html $(BUILDDIR)/doctrees/$$lang; \
	echo $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/html; \
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/html; \
	for lang in $(BUILD_LANGUAGES); \
	do \
		mkdir -p $(BUILDDIR)/html/$$lang $(BUILDDIR)/doctrees/$$lang; \
		if [[ "$(TRANSLATIONS_STATIC)" =~ "$$lang" ]]; then \
		  mkdir -p $(BUILDDIR)/doctrees/$$lang; \
			$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/html/$$lang; \
		else \
		  if [[ "$(TRANSLATIONS_I18N)" =~ "$$lang" ]]; then \
				$(SPHINXBUILD) -b html $(ALLSPHINXOPTSI18N) en build/html/$$lang; \
			fi \
		fi \
	done
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html/<language>.";

gettext:
		mkdir -p $(BUILDDIR)/gettext/en $(BUILDDIR)/doctrees/en; \
		echo "$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) en $(BUILDDIR)/gettext/en";\
		$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) en i18n/pot;\

	@echo "Build finished. The pot files pages are in i18n/pot.";\

singlehtml: compile_messages
	@set -e; for lang in en $(TRANSLATIONS_STATIC);\
	do \
		mkdir -p $(BUILDDIR)/singlehtml/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/singlehtml/$$lang;\
	done
	@set -e; for lang in $(TRANSLATIONI18N);\
	do \
		mkdir -p $(BUILDDIR)/singlehtml/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTSI18N) en $(BUILDDIR)/singlehtml/$$lang;\
	done
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/singlehtml/<language>.";\

pickle: compile_messages
	@set -e; for lang in en $(TRANSLATIONS_STATIC);\
	do \
		mkdir -p $(BUILDDIR)/pickle/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/pickle/$$lang;\
	done
	@set -e; for lang in $(TRANSLATIONI18N);\
	do \
		mkdir -p $(BUILDDIR)/pickle/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTSI18N) en $(BUILDDIR)/pickle/$$lang;\
	done
	@echo
	@echo "Build finished; now you can process the pickle files."

web: pickle

json: compile_messages
	@set -e; for lang in en $(TRANSLATIONS_STATIC);\
	do \
		mkdir -p $(BUILDDIR)/json/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/json/$$lang;\
	done
	@set -e; for lang in $(TRANSLATIONI18N);\
	do \
		mkdir -p $(BUILDDIR)/json/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b json $(ALLSPHINXOPTSI18N) en $(BUILDDIR)/json/$$lang;\
	done
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp: compile_messages
	@set -e; for lang in en $(TRANSLATIONS_STATIC);\
	do \
		mkdir -p $(BUILDDIR)/htmlhelp/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/htmlhelp/$$lang;\
	done
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp/<language>."

latex: compile_messages
	@set -e; for lang in $(LANGUAGES);\
	do \
	  mkdir -p $(BUILDDIR)/latex/$$lang $(BUILDDIR)/doctrees/$$lang; \
    $(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) en $(BUILDDIR)/latex/$$lang; \
	done
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex/<language>."
	@echo "Run \`make all-pdf' or \`make all-ps'"

pdf: compile_messages
	@set -e;\
	$(SPHINXBUILD) -b pdf $(ALLSPHINXOPTS) en $(BUILDDIR)/pdf;\
	for lang in $(TRANSLATIONS_STATIC);\
	do \
		mkdir -p $(BUILDDIR)/pdf/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b pdf $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/pdf/$$lang;\
	done
	@set -e; for lang in $(TRANSLATIONS_I18N);\
	do \
		mkdir -p $(BUILDDIR)/pdf/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b pdf $(ALLSPHINXOPTSI18N) en $(BUILDDIR)/pdf/$$lang;\
	done
	@echo
	@echo "Build finished; the PDF files are in $(BUILDDIR)/pdf/<language>."\
	@echo "Run \`make pdf' "

epub: compile_messages
	@set -e; for lang in en;\
	do \
		mkdir -p $(BUILDDIR)/epub/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/epub/$$lang;\
	done
	@echo
	@echo "Build finished; the epub files are in $(BUILDDIR)/epub/<language>."\
	@echo "Run \`make epub' "

all-pdf: latex
	@set -e; \
	for lang in $(LANGUAGES); \
	do \
	  make -C $(BUILDDIR)/latex/$$lang all-pdf ; \
		if [ -d $(BUILDDIR)/html/$$lang ]; then \
			cp -f $(BUILDDIR)/latex/$$lang/QGEP.pdf $(BUILDDIR)/html/$$lang ; \
		fi \
	done; \
	if [ -d $(BUILDDIR)/html/$$lang ]; then \
		cp -f $(BUILDDIR)/latex/en/QGEP.pdf $(BUILDDIR)/html; \
	fi; \

all-ps: latex
	@set -e; for lang in $(LANGUAGES);\
	do \
		make -C $(BUILDDIR)/latex/$$lang all-ps ; \
	done

changes:
	@for lang in $(LANGUAGES);\
	do \
		mkdir -p $(BUILDDIR)/changes/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/changes/$$lang;\
	done
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes/<language>."

linkcheck:
	@for lang in $(LANGUAGES);\
	do \
		mkdir -p $(BUILDDIR)/linkcheck/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/linkcheck/$$lang;\
	done
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/<language>/output.rst."

labels:
	@for lang in $(LANGUAGES);\
	do \
		mkdir -p $(BUILDDIR)/labels/$$lang $(BUILDDIR)/doctrees/$$lang; \
		$(SPHINXBUILD) -b labels $(ALLSPHINXOPTS) $$lang $(BUILDDIR)/labels/$$lang;\
		cp $(BUILDDIR)/labels/$$lang/labels.rst $$lang/include/labels.inc;\
	done
	@echo
	@echo "Label generation complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/labels/<language>/labels.rst."


all: html all-pdf epub all-ps
