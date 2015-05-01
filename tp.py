#! /usr/bin/python
# Web crawler parsing T&P page for information about companies
# coming for campus recruitment.
import sys
import requests
import lxml.html


def getLinks(w):
  f = open(w+'.txt','wb')
  f.write(w.upper()+'\n\n')
  print "Getting links:\n"
  links = []
  text_links = []
  for j in range (30,125):
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
  #print text_links  
  
  data = []
  i = 0 
  datastr = ""
  maxi = 0
  data1 = [] 
  for e in text_links:
    e = e.lower()
    if(e.find(w)!=-1):
      #print e
      hx = lxml.html.document_fromstring(requests.get("http://tp.iitkgp.ernet.in/notice"+links_tmp[i]).content)
      print links_tmp[i]
      f.write("http://tp.iitkgp.ernet.in/notice"+links_tmp[i]+'\n') 
      tmp = hx.xpath('//div/text()')
      print tmp
      f.write(u' '.join(tmp).encode('utf-8'))
      f.write('\n')
      data.append(tmp)
      #print tmp	 
    i = i + 1 
  f.close()

def topLinks(w):
  f = open(w+'.txt','wb')
  f.write(w.upper()+'\n\n')
  print "Getting links:\n"
  links = []
  text_links = []
  for j in range (30,55):
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
  #print text_links  
  
  data = []
  i = 0 
  datastr = ""
  maxi = 0
  data1 = [] 

  for e in text_links:
    e = e.lower()
    #if(e.find(w)!=-1):
      #print e
    hx = lxml.html.document_fromstring(requests.get("http://tp.iitkgp.ernet.in/notice"+links_tmp[i]).content)
    print links_tmp[i]
    tmp = hx.xpath('//div/text()')
    for f in tmp:
      if(f.find(w)!=-1):
        print "Company "+ str(i)
        f.write("http://tp.iitkgp.ernet.in/notice"+links_tmp[i]+'\n') 
        f.write(text_links[i]+'\n')
        print tmp
        f.write(u' '.join(tmp).encode('utf-8'))
        f.write('\n\n')
    #print tmp   
    i = i + 1 
  f.close()