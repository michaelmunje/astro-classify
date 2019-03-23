#!/bin/bash

java -jar xamin.jar runquery table=metainfo distinct fields=name sortvar=name constraint=type=\'table\',value=\'galaxy\'
