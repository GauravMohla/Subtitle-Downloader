from bs4 import BeautifulSoup
import requests
import zipfile
import os
from shutil import copy
import urllib.request
import sys
import time

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

def downloadFile(location, filename):
    r  = requests.get("https://subscene.com/subtitles/release?q="+filename)
    soup = BeautifulSoup(r.text,'html.parser')
    for link in soup.find_all("td",{"class":"a1"}):
        if("English" in link.text):
            subscenelink = link.find('a').get('href')
            #print(subscenelink)
            r  = requests.get("https://subscene.com/"+subscenelink)
            soup = BeautifulSoup(r.text,'html.parser')
            for link1 in soup.find_all("a",{"id":"downloadButton"}):
                        #print("https://subscene.com/"+link1.get('href'))
                        urllib.request.urlretrieve("https://subscene.com/"+link1.get('href'),filename+".zip")
                        #Give it time to download. 5sec should be more than enough
                        time.sleep(5)
                        with zipfile.ZipFile(filename+".zip","r") as zip_ref:
                                                    zip_ref.extractall(location)
                                                    time.sleep(3)
                                                    #print (zip_ref.namelist()[0])
                                                    os.rename(location+"\\"+zip_ref.namelist()[0],location+"\\"+filename+".srt")
                        os.remove(filename+".zip")
            break
#print(sys.argv[1])

if(len(sys.argv) == 2):
    name = sys.argv[1]
    #print(name)
    filename = os.path.splitext(name)[0]
    print(filename)
    if(os.path.splitext(name)[1]) not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
        print('file is not a video file')
        input('press any key to exit\n')
        sys.exit()
    try:
        file = name.rsplit('\\')[-1]
        #print(file[:file.rfind('.')])
        downloadFile(name[:name.rfind('\\')],file[:file.rfind('.')])
    except:
        input('some exception occured. try again later')
else:
    url = input("Enter the folder path: ")
    for filename in os.listdir(url):
        fname = os.path.splitext(filename)[0]
        if(os.path.splitext(filename)[1]) not in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp",".3g2"]:
           continue
        try:
            downloadFile(url, fname)
        except:
            input('Some exeption occured. press any key to exit')
