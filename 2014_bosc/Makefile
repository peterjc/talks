.PHONY: abs pres

ABSTRACT_DIR := abstract

all: abs

abs:
	cd $(ABSTRACT_DIR) && pdflatex *.tex && pdflatex *.tex && pdflatex *.tex && cd ..

clean:
	rm -rf $(ABSTRACT_DIR)/*.aux $(ABSTRACT_DIR)/*.log $(ABSTRACT_DIR)/*.out $(ABSTRACT_DIR)/*.pdf
