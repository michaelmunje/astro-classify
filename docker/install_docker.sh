docker build . -t astro-classify -f machine-learning/Dockerfile
docker build . -t astro-classify-mine -f mine/Dockerfile
docker build . -t astro-classify-test -f test/Dockerfile
# to do: add cloud docker when necessary

