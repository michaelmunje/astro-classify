#!/bin/bash
cd ../..
./stop_all_containers.sh
cd Dockerfiles/uninstall
./uninstall_base.sh
./uninstall_ml.sh
