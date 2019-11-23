PLIKI=*.txt

all: witaj.txt
	echo AAA
	for f in $(PLIKI); do echo $$f; done

co.txt:
	echo cosiu > co.txt

witaj.txt: co.txt
	echo -n "Witaj " > witaj.txt
	cat co.txt >> witaj.txt
	date >> witaj.txt
