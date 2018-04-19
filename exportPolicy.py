adminToken=`cat adminToken.temp | awk -F"\"" '{print $4}'`

import requests

url = "https://malmu06-s10712.ca.com:8443/ca/api/sso/services/policy/v1/deployment/export"

payload = "{\r\n  \"mainObjectsMethod\": \"ADD\",\r\n  \"closureObjectsMethod\": \"ADD\",\r\n  \"passPhrase\": \"Siteminder1\",\r\n  \"suggestedFileName\": \"Exportfile_2\",\r\n  \"objects\": [\r\n    {\r\n      \"path\": \"/SmDomains/mytest4rest\"\r\n    }\r\n  ]\r\n}"
headers = {
    'content-type': "text/xml",
    'accept': "application/octet-stream",
    'authorization': "Bearer $adminToken",
#    'authorization' : "Bearer eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiZGlyIn0..i_nzdT1C4ys5Vn4h.DhZKT1Fok6bpKVoWTzqtIo2y9T2MD7jVxGkwGxJnpRxLC5teHa6eP4tStWp9N8xqrA5AoX1XA3fiza7C3kHtWfIZn0cOOz4LvoycIn1RvWc1lOzeOkLou3jDvrJpK6HZEQFb30XT4t-qdWPn6upL4utXXNQTFvvXaHrqElREuZ4jvu5gHieYeCGLwVJU-bF34TRIlE9wVTZb5MkbP549c95STPntPP-USAtraxuzABVXWVf9ucgeFiYiqqPGQpf-P6PRtMiK25WWE8_nWBVGuWE0Jrmf2Yv3YeCG9GQCi6VUWpxcVsmlJ1Rov6YqUELbnZDMnMeKbjGj5R6GW6dfbkVjLyGxgEbdIfhG3rBCcyl6Yq143CkblJTMHhQdE98TPH1IQTF8gmFiHj1SzoC-Zv7614uNzf-6xB7BFS1BzPTmjRwqKmMv8_mXPSDABvl5WT0g28P4zL7uJWSvhEfa0JNRe96R2hZwyC1E_wA1O6cF2R8Z0h8ti2M4w0M5pMSkrMihtnaGogleID6VYeGkGc-FDrLQTayNNyzNLjq-.S1PuJBePwZKbZi3Qsw19yg",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
