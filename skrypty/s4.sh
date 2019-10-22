#!/bin/bash
wypisz_n_razy()
{
	for i in $(seq 1 $2); do echo "$1 "; done
} ;

koty()
{
	if [ $1 -eq 1 ] ; then echo "Ala ma kota"; 
	elif [ $1 -le 4 ] ; then echo "Ala ma " $1 " koty"; 
	else echo "Ala ma " $1 " kotow";
	fi
} ;

wypisz_n_razy takisobietekst 3
koty 1
koty 3
koty 7
