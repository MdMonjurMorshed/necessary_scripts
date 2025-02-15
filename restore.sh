#!/bin/bash

echo "Host: "
read host

echo "Port:"
read port

echo "username: "
read username

echo "Dump file: "
read file

echo "db_name: "
read dbname

pg_restore --host $host --port $port --username $username --dbname $dbname --verbose $file
