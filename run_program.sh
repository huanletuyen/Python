#!/bin/sh
rm -f ./command.sh
python3 gencode.py 
chomod +x ./command.sh
echo "========================STARTING PROGRAM ========================"
sh ./command.sh
echo "======================== ENDTED PROGRAM ========================"
echo " the program was endted, plesea check !!!!"