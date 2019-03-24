#!/bin/bash
if [[ "$(docker images -q galana-mine 2> /dev/null)" == "" ]]; then
echo -e "\e[96mDocker tag not found. Building docker image..."
echo -e "\e[39m"
cd Dockerfiles/install
./install_mine.sh
cd ../..
echo -e "\e[96mDocker image finished building."
echo -e "\e[39m"
cp Dockerfiles/mine/Dockerfile Dockerfiles/current_installs/mine/Dockerfile
else
	if cmp --silent Dockerfiles/mine/Dockerfile Dockerfiles/current_installs/mine/Dockerfile ; then
	 echo -e "\e[96mLatest version detected..."
	 echo -e "\e[39m"
	else
	 echo -e "\e[96mOld version detected. Installing new version..."
	 echo -e "\e[39m"
	 ./stop_all_containers.sh
	 cd Dockerfiles/uninstall
	 ./uninstall_mine.sh
	 cd ../..
	 cd Dockerfiles/install
	 ./install_mine.sh
	 cd ../..
	 rm Dockerfiles/current_installs/mine/Dockerfile
	 cp Dockerfiles/mine/Dockerfile Dockerfiles/current_installs/mine/Dockerfile
	fi
fi
echo -e "\e[96mRunning galana-mine container..."
echo -e "\e[39m"
docker run -ti --rm --net=host -v $(dirname "$(pwd)"):/galana:rw -u `id -u $USER`:`id -g $USER` galana-mine



