from bs4 import BeautifulSoup
import requests
import zipfile
import os
from shutil import copy
import urllib.request
import time

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def downloadFile(URL=None):
    import httplib2
    h = httplib2.Http(".cache")
    resp, content = h.request(URL, "GET")
    return content

tempDir = r'C:\tempDir'
url = input("Enter the folder path: ")
#url = sys.argv[1]
for filename in os.listdir(url):
	fname = os.path.splitext(filename)[0]
	if(os.path.splitext(filename)[1]) not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
           continue
	r  = requests.get("https://subscene.com/subtitles/release?q="+os.path.splitext(filename)[0])
	data = r.text
    #print(data)
#hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
	soup = BeautifulSoup(data,'html.parser')

	for link in soup.find_all("td",{"class":"a1"}):
				if("English" in link.text):
					print(link.find('a').get('href'))
					r  = requests.get("https://subscene.com/"+link.find('a').get('href'))
					data = r.text
					soup = BeautifulSoup(data,'html.parser')
					for link1 in soup.find_all("a",{"id":"downloadButton"}):
						urllib.request.urlretrieve("https://subscene.com/"+link1.get('href'),os.path.splitext(filename)[0]+".zip")
						time.sleep(10)
						with zipfile.ZipFile(os.path.splitext(filename)[0]+".zip","r") as zip_ref:
                                                    
                                                    
                                                    
                                                    
                                                    zip_ref.extractall(url)
                                                    time.sleep(3)
                                                    print (zip_ref.namelist()[0])
                                                    os.rename(url+"\\"+zip_ref.namelist()[0],url+"\\"+fname+".srt")
						os.remove(os.path.splitext(filename)[0]+".zip")
					break
if os.path.exists(tempDir):
    os.removedirs(tempDir)
				


