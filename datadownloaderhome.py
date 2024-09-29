
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:07:00 2024

@author: alexatr
"""

import requests
from bs4 import BeautifulSoup
import os
import re


url = "https://www.ncei.noaa.gov/data/goes-space-environment-monitor/access/avg/"
res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser")
#Enter your Directory
datadirectory='E:/griff/UMichigan/data'
os.makedirs(datadirectory, exist_ok=True)  

#print(parsedData.prettify())
years = re.findall('a href="(20[0-9]+)/"', str(parsedData))
print(years)
years2=[]
gooyear= range(2009, 2021)
for year in years:
    if int(year) in gooyear:
        years2.append(year)
        os.makedirs(datadirectory+'/'+year, exist_ok=True)    
        

        
print(years2)
for year in years2:
    url2=url+year
    res = requests.get(url2)
    htmlData = res.content
    parsedData = BeautifulSoup(htmlData, "html.parser")
    #print(parsedData.prettify())
    months = re.findall('a href="([01][0-9])/"', str(parsedData))
    print(months)
    
    for month in months:
        url3=url2+'/'+month+'/'
        #print(url3)
        res = requests.get(url3)
        htmlData = res.content
        
        parsedData = BeautifulSoup(htmlData, "html.parser")
        #print(parsedData.prettify())
        #print(parsedData.prettify())
        goesnumbers = re.findall('a href="(goes1[35])/"', str(parsedData))
        print(goesnumbers)
        os.makedirs(datadirectory+'/'+year+'/'+month, exist_ok=True)
        for goesnumber in goesnumbers:
            url4=url3+'/'+goesnumber
            #print(url3)
            res = requests.get(url4)
            htmlData = res.content
            
            parsedData = BeautifulSoup(htmlData, "html.parser")
            #print(parsedData.prettify())
            #print(parsedData.prettify())
            csv = re.findall('a href="(csv)/"', str(parsedData))
            print(csv)
            
            
            url5=url4+'/'+'csv'
            #print(url3)
            res = requests.get(url5)
            htmlData = res.content
            
            parsedData = BeautifulSoup(htmlData, "html.parser")
            #print(parsedData.prettify())
            #print(parsedData.prettify())
            filenames = re.findall('a href="(g1.*csv)"', str(parsedData))
            print(filenames)
            for filename in filenames:
                
                url6=url5+'/'+filename
                response = requests.get(url6)
                if response.status_code == 200:
                    
                    file_name = os.path.join(datadirectory+'/'+year+'/'+month, url6.split('/')[-1])
                   
                    with open(file_name, 'wb') as file:
                            file.write(response.content)
                    print(f"Downloaded: {file_name}")
                else:
                    print(f"Failed to download: {url}")
            
                            
                