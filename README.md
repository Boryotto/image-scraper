# image-scraper
Download images from a website depending on an xpath of the img's father node

## Note

This script needs Selenium and Google Chrome's webdriver to work.

## Arguments

* --webdriver-path (string, optional): The path to a chrome webdriver executable. If not specified, the script will look
for a file named "chromedriver.exe" in the current script's folder
* --url (string, required): The URL of the webpage to scrape images from
* --parent-xpath (string, optional): An XPATH to the parent node of the images
* --dest (string, required): The destination folder absolute path
* --trim-url (flag, optional): Trim query strings from image urls. This is useful in case that
 the urls contain a query string that asks the server for a minified version of the image