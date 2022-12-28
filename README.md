# animepahe

Welcome to the animepahe package! This package allows you to search for and download anime from the website animepahe.ru.

## Finding your Chrome version

In order to use the chromedriver that is required for this package, you will need to ensure that you have the correct version of Chrome installed on your machine. To find your Chrome version:

1. Open Chrome
2. Click on the three dots in the top right corner of the window
3. Click on "Help"
4. Click on "About Google Chrome"
5. Your Chrome version will be displayed on this page

## Downloading chromedriver

In order to use the chromedriver with this package, you will need to download it from the following link:

https://chromedriver.chromium.org/downloads

Be sure to download the version of chromedriver that corresponds to the version of Chrome that you have installed.

## Finding the path to your Chrome executable

To find the path to your Chrome executable:

1. Open Chrome
2. Click on the three dots in the top right corner of the window
3. Click on "Help"
4. Click on "About Google Chrome"
5. Click on the "Details" button
6. The path to the Chrome executable will be listed under the "Executable Path" heading

## Changing the base URL

If the base URL for animepahe.ru is no longer working, you can change it to a different URL by modifying the `url` variable at the beginning of the script. Simply replace `https://animepahe.ru/` with the desired base URL.

## Using the package

To use the animepahe package, import the necessary functions and call them with the appropriate parameters. For example:

```
from animepahe import search_apahe, mid_apahe, dl_apahe1, dl_apahe2

# Search for anime with a given query
results = search_apahe("ghoul")

# Get a list of episode IDs for a given session ID
episodes = mid_apahe('9bc185ce-c098-8379-b5b6-2fccf1986cf6')

# Get a list of download links for a given episode ID
links = dl_apahe1('episode_id')

# Follow a redirect link to get the final download link
download_link = dl_apahe2('redirect_link')

```
