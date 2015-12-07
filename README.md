# Running this program
This program is written in Python 3.4 and should be run using the appropriate
interpreter.

There are 2 ways that this program can be used - with the automator module,
which runs the main() in the walmartScrape module hourly or the walmartScrape
module can also be run manually, if the call to main() at the bottom of the
module is uncommented. 

Either way, when the program is run it either creates or appends to a file
named 'results.csv'. This file name can be changed, as indicated in the
comments in the code.

Each row of the .csv represents a single search result.
A row contains the following information:
brand, search rank, # of reviews, time, search phrase

# Dependencies
This program uses the BeautifulSoup and APScheduler libraries.

