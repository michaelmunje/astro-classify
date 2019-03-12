docker container stop $(docker ps -aq -f "ancestor=galana" -f "ancestor=galana-mine" -f "ancestor=galana-test")
# NOTE: Below line is not required because we have -rm in our docker launch options
# docker container rm $(docker ps -aq -f "ancestor=astro-classify" -f "ancestor=astro-classify-mine" -f "ancestor=astro-classify-test")
