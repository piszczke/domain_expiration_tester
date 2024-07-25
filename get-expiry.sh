#!/bin/bash

DOMAIN_LIST="piszczke.pl onet.pl"

echo "Expiration dates:"

for domain in $DOMAIN_LIST
do
  echo -n "$domain : "
  whois $domain | grep 'renewal date' | awk '{print $3}'
done