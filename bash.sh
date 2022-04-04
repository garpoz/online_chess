#!/bin/bash
cat log|egrep -oa "?invitation=.*@gmail.com"|egrep -oa "=.*"|sed 's/=//'>invitation
cat log|egrep -oa "?gmail=.*@gmail.com"|egrep -oa "=.*"|sed 's/=//'>gmail
python3.8 main.py
sleep 2
cat log|egrep -oa "[lw].*@gmail.com&reward=.*baba">tmpfile
cat log|egrep -oa osus\|inus>log
cat tmpfile|egrep win>win
cat tmpfile|egrep los>los
rm tmpfile
python3.8 reward.py
