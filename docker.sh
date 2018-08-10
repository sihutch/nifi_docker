#! /bin/bash

docker run nifi -p 8443:8443 -e AUTH=tls -e KEYSTORE_PATH=/opt/certs/nifi-test.jks -e KEYSTORE_TYPE=JKS -e KEYSTORE_PASSWORD=password -e TRUSTSTORE_PATH=/opt/certs/truststore.jks -e TRUSTSTORE_PASSWORD=password -e TRUSTSTORE_TYPE=JKS -e INITIAL_ADMIN_IDENTITY='CN=Random User, O=Apache, OU=NiFi, C=US'
