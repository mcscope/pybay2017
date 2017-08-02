#/bin/sh

echo "Starting"
python microservice.py app 9000 &
python microservice.py render 9001 &
python microservice.py fetch 9002 &
sleep 1
echo "Press enter to close"
read
pkill -f microservice
