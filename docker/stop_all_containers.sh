#!/bin/bash
docker container stop $(docker ps -aq -f "ancestor=galana" -f "ancestor=galana-ml")
# NOTE: Below line is not required because we have -rm in our docker launch options
# docker container rm $(docker ps -aq -f "ancestor=galana" -f "ancestor=galana-mine" -f "ancestor=galana-test")
