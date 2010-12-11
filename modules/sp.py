#!/usr/bin/env python
"""
sp.py - South Park Module
Author: Michael Yanovich
Jenney (about): http://inamidst.com/phenny/

Feature requested by AJoseph
"""

#from BeautifulSoup import BeautifulSoup
#import web, datetime, time, re
import datetime

def sp (jenney, input):
    """ Displays how many days, hours, minutes, and seconds until the next *new* episode of South Park """
    '''
    html = web.get("http://www.imdb.com/title/tt0121955/episodes")
    soup = BeautifulSoup(html)
    b = soup.findAll(attrs={"class":"odd"})
    
    # if it's less than 7 days 
    c = str(b[-1])
    soup2 = BeautifulSoup(c)
    find_date = re.compile(r'<a href="/tvgrid/.*/.*">')
    d = find_date.findall(c)
    date = d[0][17:27]
    timee = d[0][28:32]
    g = date.split('-')
    #h = str(date) + " " + str(timee) 
    #j = time.mktime(time.strptime(h, '%Y-%m-%d %H%M'))
    #k = time.time() - j
    #jenney.say("date: " + date)
    #jenney.say("time: " + timee)
    p = datetime.datetime(int(g[0]), int(g[1]), int(g[2]), int(timee[:2]), int(timee[2:]))
    q = p - datetime.datetime.now()
    r = unicode(q)
    
    if r[0] == '-':
        jenney.reply("")
    else:
        jenney.reply("Next episode of South Park in " + r)
    '''
    p = datetime.datetime(2011, 4, 11, 22, 00)
    q = p - datetime.datetime.now()
    r = unicode(q)
    jenney.say("Next new episode of South Park in " + r)
sp.commands = ['sp']

if __name__ == '__main__':
    print __doc__.strip()