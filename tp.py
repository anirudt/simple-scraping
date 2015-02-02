#! /usr/bin/python
# Web crawler parsing T&P page for information about companies
# coming for campus recruitment.
import sys
import requests
import lxml.html

def getLinks():
  print "Getting links:\n"
  links = []
  text_links = []
  for j in range (51,100):
    hxs = lxml.html.document_fromstring(requests.get("http://tp.iitkgp.ernet.in/notice/index.php?page=" + str(j)).content)
    try:
      l = hxs.xpath('//a[@class="notice"]/@href')
      g = hxs.xpath('//a[@class="notice"]/text()')
      text_links = text_links + g
      links = links + l
    except IndexError:
      print "error"
    print j  
#  print links
  print "Check1"
  links_tmp=[]
# Link rectification 
  for e in links:
    if(e[0]=='/'):
      links_tmp.append(e);
      continue
    else:
      links_tmp.append('/' + e)
#  print text_links  
  data = []
  i = 0  
  for e in text_links:
    e = e.lower()
    if(e.find('american')!=-1):
      print e
      hx = lxml.html.document_fromstring(requests.get("http://tp.iitkgp.ernet.in/notice"+links_tmp[i]).content)
      print links_tmp[i]
      tmp = hx.xpath('//div/text()')
      data.append(tmp) 
    i = i + 1 
  for e in data:
    print e  