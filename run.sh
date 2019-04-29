#!/bin/bash
if [[ "$(docker images -q galana 2> /dev/null)" == "" ]]; then
echo -e "\e[96mDocker tag not found. Building docker image..."
echo -e "\e[39m"
docker build . -t galana -f docker/Dockerfile
echo -e "\e[96mDocker image finished building."
echo -e "\e[39m"
cp docker/Dockerfile docker/Dockercache
else
	if cmp --silent docker/Dockerfile docker/Dockercache ; then
	 echo -e "\e[96mLatest version detected..."
	 echo -e "\e[39m"
	else
	 echo -e "\e[96mOld version detected. Installing new version..."
	 echo -e "\e[39m"
	 ./uninstall.sh
         docker build . -t galana -f docker/Dockerfile
	 rm docker/Dockercache
	 cp docker/Dockerfile docker/Dockercache
	fi
fi
echo -e "\e[96mRunning galana container..."
echo -e "\e[39m"

length=$(command -v nvidia-docker | wc -c)
DOCKER_ALIAS=docker

if [ "$length" -gt "1" ]; then
	DOCKER_ALIAS=nvidia-docker
fi

if [[ $1 == 'test' ]]; then
	$DOCKER_ALIAS run -ti --rm --net=host -v $(pwd):/galana:rw -u `id -u $USER`:`id -g $USER` galana bash -c "cd galana; python -m pytest --cov=galana/ -W ignore::DeprecationWarning"
elif [[ $1 == 'jupyter' ]]; then
	$DOCKER_ALIAS run -ti --rm --net=host -v $(pwd):/home/jovyan/:rw -u `id -u $USER`:`id -g $USER` galana bash -c "rm -rf /home/joyvan/work;jupyter notebook"
else
	$DOCKER_ALIAS run -ti --rm --net=host -v $(pwd):/galana:rw -u `id -u $USER`:`id -g $USER` galana bash -c "cd galana; bash"
fi
