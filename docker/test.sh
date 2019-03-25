#!/bin/bash
if [[ "$(docker images -q galana 2> /dev/null)" == "" ]]; then
echo -e "\e[96mDocker tag not found. Building docker image..."
echo -e "\e[39m"
cd Dockerfiles/install
./install_base.sh
cd ../..
echo -e "\e[96mDocker image finished building."
echo -e "\e[39m"
cp Dockerfiles/base/Dockerfile Dockerfiles/current_installs/base/Dockerfile
else
	if cmp --silent Dockerfiles/base/Dockerfile Dockerfiles/current_installs/base/Dockerfile ; then
	 echo -e "\e[96mLabase version detected..."
	 echo -e "\e[39m"
	else
	 echo -e "\e[96mOld version detected. Installing new version..."
	 echo -e "\e[39m"
	 ./stop_all_containers.sh
	 cd Dockerfiles/uninstall
	 ./uninstall_base.sh
	 cd ../..
	 cd Dockerfiles/install
	 ./install_base.sh
	 cd ../..
         rm Dockerfiles/current_installs/base/Dockerfile
         cp Dockerfiles/base/Dockerfile Dockerfiles/current_installs/base/Dockerfile
	fi
fi
echo -e "\e[96mRunning galana-test container..."
echo -e "\e[39m"
docker run -ti --rm --net=host -v $(dirname "$(pwd)"):/galana:rw -u `id -u $USER`:`id -g $USER` galana bash -c "cd galana; python -m pytest --cov=galana/ -W ignore::DeprecationWarning"


