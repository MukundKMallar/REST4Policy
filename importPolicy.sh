#!/bin/bash
. ./authn4Token
AUTHN="Authorization: Bearer ${TOKEN}"

curl -k -X POST \
  https://malmu06-s10712.ca.com:8443/ca/api/sso/services/policy/v1/deployment/import \
  -H "${AUTHN}" \
  -H 'content-type: application/json' \
  --data-binary @exportfile.xml
