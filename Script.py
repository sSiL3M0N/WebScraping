# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 09:04:08 2022

@author: M S I
"""

import requests as r

url="http://academicoplus.unc.edu.pe/Estudiante/Calificaciones"
req=r.get(url)

print(req.headers)
print(req.text)

peticion={"Verbo":req.request.method,"Ruta":req.request.url,"URL Base":req.request.path_url,"Cabecera":req.request.headers}
respuesta={"url":req.url, 'codigo estado':req.status_code}



print(" Request ".center(20,'#'))

for d in peticion:
    
    if d=="Cabecera":
        print(f"{d}")
        
        #for h in req.request.headers:
         #   print(f"  {h} : {req.request.headers[h]}")
            
        for x in peticion[d]:
            print(f" {x} : {peticion[d][x]}")
    else:
        print(f"{d} => {peticion[d]}")
        
    
print(" Response ".center(20,'#'))
for d in respuesta:
    print(f"{d} => {respuesta[d]}")   
    
print(" Response 2".center(20,'#'))
x=[f"{d} => {respuesta[d]}"  for d in respuesta]

print("\n".join(x))
