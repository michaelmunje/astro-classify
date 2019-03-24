#!/bin/bash

java -jar xamin.jar table="$1" fields=Standard Format=aligned > "../data/tables/$1.txt"