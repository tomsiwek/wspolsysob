#!/bin/bash

IFS=:
while read a b c l; do [ $c -ge 1000 ] && echo $a:$b:$c:$l ; done < /etc/passwd

echo -----

awk -F: '{if($3 >= 1000) print $0}' /etc/passwd

echo -----

egrep '^([^:]*:){2}[0-9]{4}' /etc/passwd
