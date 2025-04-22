#!/bin/bash

site_name="geeks-site"

cd /home/blog/geeks

echo "MKDOCS build Starts"

mkdocs build --site-dir /var/www/${site_name}

echo "Successfully build ${site_name}"

chown -R www-data:www-data /var/www/${site_name}

echo "Successfully changed the user permission for the geek site"

