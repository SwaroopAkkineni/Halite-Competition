#!/usr/bin/env bash
clear

rm -rf *.hlt *.log

./client.py gym -r "python3 MyBot.py" -r "python3 MyBot.py" -b "./halite" -i 10 -H 240 -W 160