#!/bin/bash

curl -s https://www.morfix.co.il/$1 | grep "normal_translation_div" -A1 |cut -d" " -f1 |rev |tr -s " " |head -2 |tail -1
