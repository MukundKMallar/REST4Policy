#!/bin/sh -x

#Generate admin token needed for rest of the api calls
#/bin/python adminToken.py > adminToken.temp 2> /dev/null

#set admin token in the variable
#adminToken=`cat adminToken.temp | awk -F"\"" '{print $4}'`

#echo $adminToken;

/bin/sh exportPolicy.sh > exportfile.xml 2> /dev/null

PASSPHRASE=`grep passPhrase exportPolicy.sh | awk -F"\"" '{print $4}'`

echo $PASSPHRASE > exportfile.temp1
cat exportfile.xml >> exportfile.temp1

/bin/sh importPolicy.sh 2> /dev/null
