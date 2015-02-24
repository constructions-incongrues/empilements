#!/usr/bin/env bash

# Mise à jour des dépots
apt-get -qq update

# Configuration de la timezone
echo "Europe/Paris" > /etc/timezone
apt-get install -y tzdata
dpkg-reconfigure -f noninteractive tzdata

# Installation de Java
apt-get -y install openjdk-7-jre-headless

# Installation de Apache et PHP
apt-get -y install libapache2-mod-php5 php5-cli

# Configuration de Apache
sed -i s/AllowOverride\ None/AllowOverride\ All/g /etc/apache2/sites-enabled/000-default
a2enmod rewrite
a2enmod expires
service apache2 reload

# Configuration du projet
apt-get install -y ant
cd /vagrant
./composer.phar install --prefer-dist --no-progress
ant configure build -Dprofile=vagrant

# Mise à disposition du projet dans Apache
ln -sf /vagrant/src/public/* /var/www/
rm -f /var/www/index.html

# Informations
echo
echo -e "Le site est disponible à l'adresse : http://empilements.vagrant.dev/app_dev.php"
