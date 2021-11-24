#!/bin/sh

cmd <<- EOM
	echo Backing up database...
	copy "\\\TENGAH-PC\kita_mart_group\FB_nPOS.FDB" "C:\msys64\home\KITAGROUP\KASIRRUSAK\POS.FDB" /Y
	copy "\\\TENGAH-PC\kita_mart_group\FB_nRETAIL.FDB" "C:\msys64\home\KITAGROUP\KASIRRUSAK\BACKOFFICE.FDB" /Y
	echo Back-up done
EOM
