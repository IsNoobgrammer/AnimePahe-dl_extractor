# Animepahe-dl

This is a python script that allows you to search for anime, view the available episodes, and download them from the website animepahe.ru.

## Requirements

- Python 3
- requests
- re
- pandas


## Installation

You can install these libraries using `pip`, the Python package manager. For example:
`pip [pip3] install requests pandas`


## Usage as a script

To use this script, open a terminal and navigate to the directory where the script is saved. Then, run the script using the `python` command, followed by the name of the script.

For example: `python animepahe.py`
You will be prompted to enter the name of an anime that you want to search for. Type in the name of the anime and press Enter. The script will search animepahe.ru for anime matching your search query, and display a list of results.

Select the anime that you want to download by entering its number in the list. You will be asked to select an episode to download. Enter the number of the episode that you want to download.
And it will return its direct link.



## Using as a module
To use this script in your project, simply copy the code into a `[name].py` file and import it using `from [name] import [functions] `.

## Functions

- `search_apahe(query: str) -> list`: Searches for anime with the given query and returns a list of search results. Each result is a list containing the following information about the anime:
  - Title
  - Type
  - Number of episodes
  - Status
  - Year
  - Score
  - Session ID
- `mid_apahe(sid: str) -> list`: Given the session ID of an anime, returns a list of episode IDs.
- `dl_apahe1(ok: str) -> list`: Given the episode ID, returns a list of lists containing information about the available download links:
  - Quality
  - Size (in MB)
  - Language
  - Link
- `dl_apahe2(url: str) -> str`: Given a redirect link, follows the link and returns the final download link.

## Example usage

```python
import animepahe

# Search for anime with the query "ghoul"
results = animepahe.search_apahe("ghoul")

# Print the search results
for result in results:
    print(result[0])  # Print the title of the anime

# Get the session ID of the first search result
session_id = results[0][-1]

# Get the episode IDs of the anime with the given session ID
episode_ids = animepahe.mid_apahe(session_id)

# Print the episode IDs
print(episode_ids)

# Get the download links for the first episode
download_links = animepahe.dl_apahe1(episode_ids[0])

# Print the download links
for link in download_links:
    print(link[0], link[1], link[2], link[3])
    
    
# Get the final download link for the first link in the list
final_link = animepahe.dl_apahe2(download_links[0][-1])

print(final_link)
```

# Disclaimer
This script is for educational purposes only. We do not endorse or encourage the illegal download of copyrighted material. Please support the official release of the anime.Please respect the terms of service of animepahe and use animepahe responsibly
