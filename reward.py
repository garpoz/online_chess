#! /usr/bin/python3.8
#garpozir@gmail.com
#god-baba

import random
import datetime
import json

inv_json=open('public/invitation.json')
inv_json=json.load(inv_json)
inv_keys=list(inv_json.keys())
j=open('public/contact.json')
current_time = datetime.datetime.now()
current_time=str(current_time).split(' ')[0]
current_time=str(current_time)
data=json.load(j)
los=open('./los','r')
win=open('./win','r')
win=win.readlines()
los=los.readlines()
davati=False
for wi in win:
    wi=str(wi.strip())
    wi=wi.split('&')
    win_mail=wi[0]
    win_reward=wi[1]
    win_mail=win_mail[8:]
    win_reward=win_reward[7:-4]
    win_reward=int(win_reward)
    pool=(win_reward*10)/100
    komis_davat=int(pool/2)
    win_reward-=pool
    fnl=data['member'][win_mail]
    fnl=int(fnl)
    fnl+=win_reward
    fnl=int(fnl)
    data['member'][win_mail]=fnl
    if win_mail in inv_keys:
        davati=True
        davat_konandeh=inv_json[win_mail]
        pool_davat=data['member'][davat_konandeh]
        data['member'][davat_konandeh]=komis_davat+pool_davat

for lo in los:
    lo=str(lo.strip())
    lo=lo.split('&')
    los_mail=lo[0]
    los_reward=lo[1]
    los_mail=los_mail[8:]
    los_reward=los_reward[7:-4]
    los_reward=int(los_reward)
    pool=int((los_reward*10)/100)
    fnl=data['member'][los_mail]
    fnl=int(fnl)
    fnl-=los_reward
    fnl=int(fnl)
    if fnl<0:fnl=0
    data['member'][los_mail]=fnl

    num_rnd = random.randint(1,100000000)
    chr_rnd = random.randint(65,90)
    chr_rnd=chr(chr_rnd)
    #if davati:
        #first_txt=chr_rnd+str(num_rnd)+"**"+str(int(pool/2))
    #else:
        #first_txt=chr_rnd+str(num_rnd)+"**"+str(pool)
    if int(pool)<1:pool=1
    first_txt=chr_rnd+str(num_rnd)+"**"+str(pool)
    data['level'][first_txt]=current_time

iiprint=json.dumps(data)

ij=open('public/contact.json','w')
ij.write(iiprint)
