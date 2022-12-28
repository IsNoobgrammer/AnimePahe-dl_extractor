# animepahe

import requests
import re
import pandas as pd

# Base URL for animepahe.ru
url = "https://animepahe.ru/"

def search_apahe(query: str) -> list:
    """
    Search animepahe.ru for anime matching the given query.
    
    Parameters:
        query (str): The search query.
    
    Returns:
        A list of lists, where each inner list contains the following information
        about a search result:
            - Title
            - Type (e.g. TV, movie)
            - Number of episodes
            - Status (e.g. completed, airing)
            - Year
            - Score
            - Session ID
    """
    global url
    url1 = url + "api?m=search&q=" + query
    r = requests.get(url1)
    data = r.json()
    clean_data = []
    for i in data["data"]:
        hmm = []
        hmm.append(i['title'])
        hmm.append(i['type'])
        hmm.append(i['episodes'])
        hmm.append(i['status'])
        hmm.append(i['year'])
        hmm.append(i['score'])
        hmm.append(i['session'])
        clean_data.append(hmm)
    return clean_data

def mid_apahe(sid: str) -> list:
    """
    Get a list of episode IDs for the given session ID.
    
    Parameters:
        sid (str): The session ID.
    
    Returns:
        A list of episode IDs.
    """
    global url
    url2 = url + "api?m=release&id=" + sid + "&sort=episode_asc"
    r = requests.get(url2)
    data = []
    for i in (r.json())['data']:
        s = str(i['session'])
        data.append(s)
    return data

def dl_apahe1(ok: str) -> list:
    """
    Get a list of download links for the given episode ID.
    
    Parameters:
        ok (str): The episode ID.
    
    Returns:
        A list of lists, where each inner list contains the following information
        about a download link:
            - Quality
            - Size (in MB)
            - Language
            - Link
    """
    global url
    eid = ok
    url1 = url + "api?m=links&id=" + eid + "&p=kwik"
    r = requests.get(url1)
    data = []
    sed_dict = (r.json())['data']
    for i in (r.json())['data']:
        hmm = []
        hmm.extend(list(i.keys()))
        size = round((i[(hmm[0])]['filesize']) / (1024 * 1024), 0)
        hmm.append(str(size) + " MB ")
        hmm.append(i[(hmm[0])]['audio'])
        hmm.append(i[(hmm[0])]['kwik_pahewin'])
        data.append(hmm)
    return data

def dl_apahe2(url: str) -> str:
    """
    Follow a redirect link to get the final download link.
    
    Parameters:
        url (str): The redirect link.
    
    Returns:
        The final download link.
    """
    r = requests.get(url)
    redirect_link = (re.findall(r'<a href="([^\"]+)" class="btn', r.text))[0]
    return redirect_link

# Prompt user for search query
q = input("Enter anime: ")

# Search for anime with the given query
x = search_apahe(q)

# Print search results
ch = 0
for i in x:
    ch += 1
    print(ch, ":", i[0], i[1], i[2], i[3], i[4], i[5])

# Prompt user to select an anime from the search results
q = int(input("Select anime: "))
q = q - 1

# Get a list of episode IDs for the selected anime
link = []
xx = mid_apahe((x[q][-1]))

# Get a list of download links for each episode
ch = 0
for i in xx:
    link.append(dl_apahe1(i))
    ch += 1
    print(ch, "done")
print("done")

# Create a list of download links with associated metadata
dx = []
ep = 0
for i in link:
    ep += 1
    for j in i:
        df2 = [ep, j[2], j[0], j[1], j[-1]]
        dx.append(df2)

# Create a pandas DataFrame from the list of download links
df = pd.DataFrame(dx, columns=['EP No.', 'Language', 'Quality', 'Size', 'Link'])
# Prompt user to select a language
_lang = list(df['Language'].unique())
for i in _lang:
    print(i)
ch = input("Which language: ")

# Filter DataFrame to include only the selected language
dfx = df[df['Language'] == ch]

# Prompt user to select a quality
_qual = list(dfx['Quality'].unique())
for i in _qual:
    print(i)
ch = input("Which quality: ")

# Filter DataFrame to include only the selected quality
dfx = dfx[dfx['Quality'] == ch]

# Print the filtered DataFrame
print(dfx)

# Prompt user to select an episode
ch = int(input("Enter episode no: "))

# Get the download link for the selected episode
dl_link = dfx[dfx['EP No.'] == ch]['Link'].values[0]

# Follow the redirect link to get the final download link
dl_link = dl_apahe2(dl_link)

print("Download link:", dl_link)

# To change the base URL from animepahe.ru to another URL, simply change the value
# of the `url` variable at the beginning of the script.
