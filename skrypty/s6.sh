#!/bin/bash

for i in *.TXT; do mv $f "${f%.TXT}.txt"; done

echo ------

sed 's#[.]TXT#.txt#'
