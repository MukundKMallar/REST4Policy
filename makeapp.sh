#!/bin/bash
# assumes apache-01 and BasicForm existed
# assume DemoUser1 created on CA Directory
APPVDIR=newapp4t
SMAGENT=newagent4t
SMAUTH=BasicForm
SMDOMAIN=$APPVDIR
SMREALM=REALM$APPVDIR
SMRULE=AllowGetPost
SMDIR=test4polexportDir
#bash crDir.sh "$SMDIR" "$SMLDAPHOST" "$SMLDAPPORT"
bash crAgent.sh "$SMAGENT"
bash crDomain.sh "$APPVDIR" "$SMDIR"
bash crRealm.sh "$APPVDIR" "$SMAGENT" "$SMAUTH" "$SMDOMAIN"
bash crRule.sh "$SMDOMAIN" "$SMREALM"
bash crPolicy.sh "$SMDOMAIN" "$SMREALM" "$SMRULE" "$SMDIR"

rm [0-9]*.json
