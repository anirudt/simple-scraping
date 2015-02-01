import requests
import lxml.html

def getLinks():
  links = []
  class_name = "playlist-video clearfix  spf-link" 
  parent_link = "https://www.youtube.com/watch?v=ZZ4cqPkdEPc&list=PL2D862035774C877C"
  hxs = lxml.html.document_fromstring(requests.get(parent_link).content)
  links = hxs.xpath('//div[@class="playlist-videos-container yt-scrollbar-dark yt-scrollbar"]/ol[@class="playlist-videos-list yt-uix-scroller"]/li[@class="yt-uix-scroller-scroll-unit "]/a[@class="playlist-video clearfix  spf-link"]/@href')
  print links


