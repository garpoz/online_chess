#! /usr/bin/python3.8
#garpozir@gmail.com
#god-baba

import json, os
from os.path import exists

file_exists = exists('invitation.txt')
exists=None
if file_exists:
    exists=True
    inv=open('invitation.txt','r')
    inv=inv.readlines()
    inv=inv[0]
    inv=inv.strip('#')
else:exists=False

inv_json=open('public/invitation.json')
inv_json=json.load(inv_json)
j=open('public/contact.json')
data=json.load(j)
i=open('gmail','r')
r=i.readlines()
r=list(set(r))
if len(r)>0:
    os.system('rm invitation.txt')
rint=list(data['member'].keys())
for w in r:
    pint=str(w.strip())
    if pint not in rint:
        data['member'][pint]=10
        if exists:
            inv_json[pint]=inv
            exists=False
            iiprintinv=json.dumps(inv_json)
            ijinv=open('public/invitation.json','w')
            ijinv.write(iiprintinv)
iiprint=json.dumps(data)

ij=open('public/contact.json','w')
ij.write(iiprint)
