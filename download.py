# https://cowtransfer.com/s/a04cf6e1362343

import os
import zipfile
import requests

url = 'https://static.c-t.work/QN_HZ_cowtransfer-file-5af749ad-38e4-4474-b885-f11ab58c6887%252Fmoyuland.zip?t-s=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJndWlkK3RpbWVzdGFtcCI6Imlsb3ZlY293dHJhbnNmZXIyMDIxXzE2NTQ3NDU3ODQxNjEifQ.oGVDDgBeiFmEfCP5xp0xwX79bza7JGgPTLQ0t_ik7D0&t-c=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJndWlkK3RpbWVzdGFtcCI6IjIwMjJ8Nnw5fDExIn0.yjE0iKom_8xk_E2S8o3AiAWCuMYYOlvZII9F_K_gbJk&user=47da725e-ef97-400f-8667-09dbfd739d7e&ut=0&rt=0&rk=ff_98940af2-a4a8-4b49-98b7-b25ce2a68ad9&owner=47da725e-ef97-400f-8667-09dbfd739d7e&tid=a04cf6e1-3623-43a0-a4ac-696c1c927987&batch=1654745784149&attname=moyuland.zip'
r = requests.get(url)

name = 'moyuland'

f = open(os.getcwd()+'/.minecraft/'+name+'.zip', 'wb')
f.write(r.content)

f = zipfile.ZipFile('.minecraft/'+name+'.zip','r')
for file in f.namelist():
    f.extract(file,'.minecraft/')
f.close()

try:
    os.remove(os.getcwd()+'/.minecraft/'+name+'.zip')
except:
    pass