#!/usr/bin/bash

echo "--this script checks your ip addresses--"
echo ""
sleep 2
echo "Getting your Internal ip address..."
intip=`ifconfig | grep broadcast | awk {'print $2'}`
sleep 4
echo ""
echo "Done!"
echo ""
sleep 2
echo "Getting your External ip address..."
extip=`curl ifconfig.co`
sleep 4
echo ""
echo "Done!"
echo ""
sleep 2
echo "Checking your location..."
country=`curl ifconfig.co/country`
sleep 4
echo ""
echo "Done!"
sleep 3
echo "your internal ip address is" $intip, "your External ip address is" $extip "and your location is" $country.
sleep 2
echo 'Have a good day!'
