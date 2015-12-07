# Running this program
There are 2 ways that this program can be used - using the automator module,
which runs the main() in the walmartScrape module hourly. The walmartScrape
module can also be run manually, if the call to main() at the bottom of the
module is uncommented.

Either way, when the program is run it either creates or appends to a file
named 'results.csv'. This file name can be changed, as indicated in the
comments in the code. 
A row of the .csv file contains the following information:
brand, search rank, # of reviews, time, search phrase

Each row of the csv represents a single search result.

# Dependencies
This program uses the BeautifulSoup and APScheduler libraries.

