#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DEVELOPED BY Di0nJ@ck - August 2018 - v1.0
__author__      = 'Di0nj@ck'
__version__     = 'v1.0'
__last_update__ = 'August 2018'

import requests
import csv

def main():
   
    #READ OUR CSV WITH THE PHISHING DOMAINS TO MONITOR AND THEIR ORIGINAL SIZES
    with open('Phishing_domains.csv', 'rb') as csvfile:
 
        domain_reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        
        for row in domain_reader:
            print ("- Analyzing the domain: " + row['Domain'] + "\n")
            
            try:
                resp = requests.get('https://' + row['Domain'], timeout=5)
            except Exception as e:
                print ("Error. The URL can not be open")      
            
            current_size = len(resp.content)
            last_size = row['Last_size']
            
            if int(current_size) == int(last_size):
                
                print ("         * Result: OK. The phishing website is not active" + "\n")
                print ("         * Current size: " + str(current_size) + " bytes" + " (no changes on size)" + "\n")
                
            else:  
                print ("         * Result: KO. Phishing site is active again on this domain!" + "\n")
                print ("         * Current size: " + str(current_size) + " bytes " + "(original size of " + row['Last_size'] + " bytes)" + "\n")
                print ("         * Content: " + "\n" + "\n" + resp.content + "\n")            

main()