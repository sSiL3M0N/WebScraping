# -*- coding: utf-8 -*-
"""
Created on Jun 2022
Cajamarca
@author: sSiL3M0N
"""

import requests as r
from bs4 import BeautifulSoup as bs

url="https://simple.ripley.com.pe/audifonos-bluetooth-on-ear-sony-negro-wh1000xm4-2065254770831p"
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

req=r.get(url=url, headers=headers)

soup=bs(req.text,"html.parser")



#print(soup.find("section",class_="product-info").find(class_="prices-list").find(class_="attrDest"))
#print(soup.find("div",class_="product-price-container").text.split("S/ ")[1].replace(",","."))
#print(soup.find("div",class_="product-internet-price").text.split("S/ ")[1])

print(soup.title.text)
print(soup.find("span",class_="sku-value").text)


lista={}

lista2=soup.find("section",class_="product-info").find_all(class_="product-price-container")
for i in range(0,len(lista2)-1):
    #precio=lista2[i].find(class_="product-price").text.replace("S/ ","").replace(",","."),precio
    ##lista.setdefault(tipo,precio)
    lista.setdefault(lista2[i].find(class_="product-price").text.replace("S/ ","").replace(",","."), lista2[i].find(class_="product-price-type").text)
    

print(lista)

#valoracion
valoracion=soup.find(class_="stars-ranking").attrs["class"][-1][-1]
        

#print(soup.find("section",class_="product-info").find_all(class_="product-price-container")[1].find(class_="product-price").text)