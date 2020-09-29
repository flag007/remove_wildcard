# -*- coding: UTF-8 -*-

from socket import gethostbyname
from pandas import Series
import argparse
import sys

colors = True
machine = sys.platform
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors shouldn't be displayed in mac & windows
if not colors:
    end = red = white = green = yellow = run = bad = good = info = que = ''
else:
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

parser = argparse.ArgumentParser()

parser.add_argument('-f', help='target file', dest='file')
args = parser.parse_args() 

domain = args.domain

DOMAIN = file

domains = []
ips = []

print ('%sWait ..........................%s'% (red, end))
with open(DOMAIN,'r') as f:
    for line in f.readlines() :
        try:
            ip = gethostbyname(line.strip('\n'))
        except Exception as e:
            pass
        else:
            ips.append(ip)
            domains.append(line.strip('\n'))

print('%sStatistics.....................%s'% (red, end))

def ip_to_frequencies(ips):
    myDict = {}
    for word in ips:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  #remove word from dict
        else:
            done = True
    return result



ips_dicc = ip_to_frequencies(ips)
framel = Series(ips_dicc)
print(framel)


results = []


for line in domains:
    try:
        ip = gethostbyname(line)
    except Exception as e:
        pass
    else:
        if ip not in ips:
            results.append('[!] '+line) 
        elif ip in ips and ips_dicc[ip] < 20:
            results.append('[!] '+line)  

print(*results, sep='\n')
print()
print('%sEasy Win%s' %(red, end))
