#!/bin/bash
. ./authn4Token
AUTHN="Authorization: Bearer ${TOKEN}"
#PASSPHRASE="Siteminder1"

curl -k -X POST \
  https://malmu06-s10712.ca.com:8443/ca/api/sso/services/policy/v1/deployment/export \
  -H "${AUTHN}" \
  -H 'content-type: application/json' \
  -d '{
  "mainObjectsMethod": "ADD",
  "closureObjectsMethod": "ADD",
  "passPhrase": "Siteminder1",
  "suggestedFileName": "Exportfile_2",
  "objects": [
    {
      "path": "/SmDomains/mytest4rest"
    }
  ]
}'
