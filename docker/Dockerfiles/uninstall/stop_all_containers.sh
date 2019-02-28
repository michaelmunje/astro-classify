docker container stop $(docker ps -aq -f "ancestor=astro-classify" -f "ancestor=astro-classify-mine" -f "ancestor=astro-classify-test")
# NOTE: Below line is not required because we have -rm in our docker launch options
# docker container rm $(docker ps -aq -f "ancestor=astro-classify" -f "ancestor=astro-classify-mine" -f "ancestor=astro-classify-test")
