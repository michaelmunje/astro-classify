#!/bin/bash
docker container stop $(docker ps -aq -f "ancestor=galana")
