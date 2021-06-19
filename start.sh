#!/bin/bash -x
PWD=`pwd`
activate () {
    source $PWD/BotTesterVenv/bin/activate
}

activate

#!/usr/bin/python3
python3 Bot_Tester.py
