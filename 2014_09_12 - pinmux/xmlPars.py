import xmltodict

print("ahoj")

name = "randomPinPebCut_sdk__notRouted.peb"
file = name
#with open(path, 'r') as content_file:
#    content = content_file.readline()


import linecache
import re
#import xml.etree.ElementTree as ET
import bs4
import string

i = 100
num0to32 = "(3[1-2]|[1-2][0-9]|[0-9])"
portLetters = "([A-E])"
reLine = (".*PT%s%s.*_UserName.*") % (portLetters, num0to32)
#regex_str = ".*PT([A-E])([0-9]|[1-2][0-9]|3[1-2]).*_UserName.*"
regexLine = re.compile(reLine)
while True:
    line = linecache.getline(file, i)
   
    if line:
        #line = "PTA0_LK_UserName</ItemSymbol>"
        #print(line)
        r = regexLine.match(line)
        if r: # something was foun)
            portpin = r.groups()
            print(portpin)
            # get name of signal
#            head = '<?xml version="1.0" encoding="UTF-8"?>'
#            xml_str = "\n".join([head,line.strip()])
#            tree = ET.parse( xml_str)
#            root = tree.getroot()
#            signal = root[0]
#____________________________________________________
            #soup = bs4.BeautifulSoup(line.strip()+"\n")
            #print(line.strip())
            #print(soup)
            #signal = soup.find('ItemSymbol')
            #signal
#            print(line)
            #print(soup.a)
            #print(signal.string)
#____________________________________________________)
            tag = "ItemSymbol"
            reValue = ("<%s>(.*)</%s>") % (tag,tag)
            reValue = "<ItemSymbol>(.*)</ItemSymbol>"
            regexValue = re.compile(reValue)
            r = regexValue.match(line.strip())
            print( r.groups() )
                
            
            if 0:
                i = i+3
                user_name = linecache.getline(file, i)
                print(user_name)

        i=i+1
    else:
        break

print("end")
         


    
    
#doc = xmltodict.parse(content)
