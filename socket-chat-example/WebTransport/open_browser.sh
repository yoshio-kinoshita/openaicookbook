#!/bin/bash
HASH=`openssl x509 -pubkey -noout -in cert.pem |
    openssl pkey -pubin -outform der |
    openssl dgst -sha256 -binary |
    base64`

chromium \
    --ignore-certificate-errors-spki-list=$HASH \
    https://localhost:3000