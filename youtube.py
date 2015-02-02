import requests
import lxml.html
import numpy as np
def getLinks():
  links = []
  class_name = "playlist-video clearfix  spf-link" 
  parent_link = "https://www.youtube.com/watch?v=ZZ4cqPkdEPc&list=PL2D862035774C877C"
  relative_parent_link = "/watch?v=ZZ4cqPkdEPc&list=PL2D862035774C877C"
  hxs = lxml.html.document_fromstring(requests.get(parent_link).content)
  links = hxs.xpath('//li[@class="yt-uix-scroller-scroll-unit "]/a/@href')
  # div/a/@href gets some results.
  i = 0
  for e in links:
  	print e
  	if(e.find(relative_parent_link)!=-1):
  		print "here"
  		break
  	i = i + 1
  print i
  while(i<len(links)):
  	print links(i)
  	i = i + 1	
  download_link = "http://www.vidtomp3.com/"
  down = lxml.html.document_fromstring(requests.get(download_link).content)
  down.forms[0].fields['url'] = download_link  
  result = lxml.html.parse(lxml.html.submit_form(down.forms[0])).getroot()
#  print form.inputs
#  form.inputs.type['text'] = 'Anirud'
#  print form.inputs.type['text']
  print result


