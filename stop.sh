#!/bin/bash

ps -ef | grep node | grep -v grep | awk '{print $2}' | xargs kill
#pkill -f node
#nohup node server.js>log &
