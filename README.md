# aarp_scraper

Simple [AARP Jobs](https://jobs.aarp.org) scraper to make it easier to filter
results to my preferences. Only scrapes the search results page, not full listing.

Change the `start_urls` in [myspider.py](myspider.py) to that of the first results page from your initial search.

Run the scraper
```
scrapy runspider -o jobs.json myspider.py
```

Use [notebook.ipynb](notebook.ipynb) to load, sort, filter, and display your results.

### Shell with custom user-agent
```
scrapy shell -s USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8' '<results-url goes here>'
```
