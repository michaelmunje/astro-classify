if [[ "$(docker images -q astro-classify-test 2> /dev/null)" == "" ]]; then
cd Dockerfiles/install
./install_test.sh
cd ..
fi
docker run -ti --rm --net=host -v $(dirname "$(pwd)"):/astro-classify:rw -u `id -u $USER`:`id -g $USER` astro-classify-test bash -c "cd astro-classify; pytest"


