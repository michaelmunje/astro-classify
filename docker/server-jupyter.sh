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
docker run -ti --rm --net=host -v $(dirname "$(pwd)"):/home/jovyan/:rw -u `id -u $USER`:`id -g $USER` galana start.sh bash -c "rm -rf /home/joyvan/work;jupyter lab"
