#!/bin/bash
echo "Sposób 1 (for)"
for file in *; do echo "<a href=\"$file\">$file<\a>"; done
echo "Sposób 2 (while)"
ls . | while read file; do echo "<a href=\"$file\">$file<\a>"; done
