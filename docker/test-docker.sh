docker run -ti --rm --net=host -v $(dirname "$(pwd)"):/astro-classify:rw -u `id -u $USER`:`id -g $USER` astro-classify-test
