#animepahe

import requests
import re
import pandas as pd
url="https://animepahe.com/"

def search_apahe(query):
    global url
    url1=url+"api?m=search&q="+query
    r=requests.get(url1)
    data=r.json()
    clean_data=[]
    for i in data["data"]:
        hmm=[]
        hmm.append(i['title'])
        hmm.append(i['type'])
        hmm.append(i['episodes'])
        hmm.append(i['status'])
        hmm.append(i['year'])
        hmm.append(i['score'])
        hmm.append(i['session'])
        clean_data.append(hmm)
    return clean_data #name,type,episodes,status,year,score,session_id

#search_apahe("ghoul")

def mid_apahe(sid:str):
    global url
    url2=url+"api?m=release&id="+sid+"&sort=episode_asc"
    r=requests.get(url2)
    data=[]
    for i in (r.json())['data']:
        s=str(i['session'])
        data.append(s)
    return data# [id,id]
    
#mid_apahe('9bc185ce-c098-8379-b5b6-2fccf1986cf6')

def dl_apahe1(ok:str):
    global url
    eid=ok
    url1=url+"api?m=links&id="+eid+"&p=kwik"
    r=requests.get(url1)
    data=[]
    sed_dict=(r.json())['data']
    for i in (r.json())['data']:
        hmm=[]
        hmm.extend(list(i.keys()))
        size=round((i[(hmm[0])]['filesize'])/(1024*1024),0)
        hmm.append(str(size)+" MB ")
        hmm.append(i[(hmm[0])]['audio'])
        hmm.append(i[(hmm[0])]['kwik_pahewin'])
        data.append(hmm)
    return data



def dl_apahe2(url:str):
    r=requests.get(url)
    redirect_link=(re.findall(r'<a href="([^\"]+)" class="btn',r.text))[0]
    return redirect_link
    
    
q=input("enter anime : ")
x=search_apahe(q)
ch=0
for i in x :
    ch+=1
    print(ch, " : " ,i[0] ,i[1],i[2],i[3],i[4],i[5])
q=int(input("select anime : "))
q=q-1
link=[]
xx=mid_apahe((x[q][-1]))
ch=0
for i in xx:
    link.append(dl_apahe1(i))
    ch+=1
    print( ch," done ")
print("done")



dx=[]
ep=0
for i in link:
    ep+=1
    for j in i:
        df2=[ep,j[2], j[0],j[1],j[-1]]
        dx.append(df2)
        
df = pd.DataFrame(dx,columns =['EP No.', 'Language', 'Quality', 'Size','Link'])


_lang=list(df['Language'].unique())
for i in _lang:
    print(i)
ch=input("Which Language : ")
print("\n\n")
dfx=df[df['Language']==ch]


_qual=list(dfx['Quality'].unique())
for i in _qual:
    print(i)
ch=input("Which Quality : ")
print("\n\n")
dfx=dfx[dfx['Quality']==ch]
print(dfx)

x=list(dfx['Link'])
sele_url=[]
for i in x:
    sele_url.append(dl_apahe2(i))

print(sele_url)


## selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
# import Action chains 

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
options = Options()
options.binary_location = r'C:\Program Files\Chromium\Application\chrome.exe'
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

DIRECT_LINK=[]
for i in sele_url:
    driver.get(i)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    """action = ActionChains(driver)
    button = driver.find_element("css selector",".button")
    action.click(button).perform()"""
    wait=WebDriverWait(driver, 40).until(EC.element_to_be_clickable(("css selector", ".button"))).click()
    if len(driver.window_handles) != 1:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        wait=WebDriverWait(driver, 20).until(EC.element_to_be_clickable(("css selector", ".button"))).click()
    else:
        pass
    
    time.sleep(2)
    driver.get("chrome://downloads/")
    time.sleep(5)

    download_link = driver.execute_script('return document.querySelector("body > downloads-manager").shadowRoot.querySelector("#frb0").shadowRoot.querySelector("#url")')
    print(download_link.get_attribute('href'))
    DIRECT_LINK.append(download_link.get_attribute('href'))

    driver.execute_script("document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector(\"cr-button[focus-type='cancel']\").click()")
"driver.quit()"

print(DIRECT_LINK)
f=open("dl_links.txt","w+")
for i in DIRECT_LINK:
    f.write(i+"\n")
    
f.close()