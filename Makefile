go:
	cp ../GMAT/R2022a/output/ContactLocator1.txt ContactLocator$(ID).txt
	python3 parse.py $(ID)
	python3 filter.py $(ID)