import sys
import os
import random
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
count=1200
os.system("apt install toilet")
color1=["\033[1;31;40m","\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m"]
def color():
 return str(random.choice(color1))
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F gay Bot")
 print("    \033[1;36;40m Code made by: \033[1;32;40m tuhin1729")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/tuhin1729")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/tuhin1729")
 print("    \033[1;36;40m YouTube     : \033[1;32;40m https://bit.ly/TuhinTheHacker")
 print("    \033[1;36;40m Dedicated to: \033[1;34;40m Diya Saha")
 print("        \033[1;31;40mSome Proxies May Be Dead. :(")
 print("        \033[1;31;40mRemember:The Website In Which You Are Testing May Identify This Bot.")
 print("\n\n") 
def req(proxy_url,target_url,timeo,stay_time):
 r=requests.get(proxy_url)
 soup=BeautifulSoup(r.content,'html.parser')
 list = soup.find(class_='table table-striped table-bordered')
 list1 = list.findAll('td')
 iplist=[]
 portlist=[]
 j=0
 while(j<(8*count)):
  try:
   a=str(list1[j].contents[0])
   iplist.append(a)
   j=j+8
  except:
   break
 j=1
 while(j<(8*count)):
  try:
   a=str(list1[j].contents[0])
   portlist.append(a)
   j=j+8
  except:
   break
 for index in range (0,(len(iplist)-1)): 
  try:   
   PROXY=iplist[index]+":"+portlist[index]
   print("\033[1;32;40mTrying From "+color()+str(PROXY))
   webdriver.DesiredCapabilities.FIREFOX['proxy']={"httpProxy":PROXY,"ftpProxy":PROXY,"sslProxy":PROXY,"proxyType":"MANUAL"}
   driver=webdriver.Firefox()
   driver.set_page_load_timeout(timeo)
   driver.get(target_url)
   time.sleep(stay_time)
   driver.close()
  except Exception as e: 
   driver.close()
banner()
target=input("\033[1;33;40mEnter The Target URL(Ex: https://www.uniazeeza.com) :")
if("tuhin1729" in target):
 print("You can't perform it in my Website")
 sys.exit()
timeout=int(input("\033[1;33;40mEnter The Time Out(In Seconds)(Recommended 100) :"))
stay=int(input("\033[1;33;40mEnter The Stay Time(In Seconds) :"))
urllist=["https://www.sslproxies.org","https://us-proxy.org","https://free-proxy-list.net/uk-proxy.html","https://free-proxy-list.net/anonymous-proxy.html","https://free-proxy-list.net","https://www.socks-proxy.net"]
for purl in urllist:
 banner()
 req(purl,target,timeout,stay)
 print("\033[1;32;40mSleeping For 10 Seconds")
 time.sleep(10)
 
