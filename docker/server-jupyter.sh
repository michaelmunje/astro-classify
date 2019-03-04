#!/bin/bash
if [[ "$(docker images -q galana 2> /dev/null)" == "" ]]; then
echo -e "\e[96mDocker tag not found. Building docker image..."
echo -e "\e[39m"
cd Dockerfiles/install
./install_ml.sh
cd ../..
echo -e "\e[96mDocker image finished building."
echo -e "\e[39m"
fi
echo -e "\e[96mRunning galana container..."
echo -e "\e[39m"
nohup docker run -ti --rm --net=host -v $(dirname "$(pwd)"):/home/jovyan/:rw -v $(dirname $(dirname "$(pwd)"))/certs:/etc/certs/ -u `id -u $USER`:`id -g $USER` galana start.sh bash -c "rm -rf /home/joyvan/work;jupyter lab --NotebookApp.keyfile=/etc/certs/notebook.key --NotebookApp.certfile=/etc/certs/notebook.crt" > jup.log &
