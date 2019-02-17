# Illini Datathon 2019

For this project we trialled several machine learning algorithms to predict the stock prices for Bayer, Honeywell, 3m, and Synchrony from January 1 2019 until present day (February 17). We graphed the actual stock prices and our predictions. An example graph is below, and the rest our in the visualization folder.

![Zebra Video](https://github.com/danielferriss/convert-to-ascii/blob/master/media/zebra.gif)

We got supplemental data by analysing the sentiment of each companies' 10-K reports, which are 
## Built With

* [scikit-learn](https://scikit-learn.org/stable/) - Used to make our models
* [scipy](https://www.scipy.org/) - Used to find optimal alpha value for models
* [nltk sentiment vader](https://www.nltk.org/_modules/nltk/sentiment/vader.html) - Used to analyse text sentiment
* [pandas](https://pandas.pydata.org/) - Used for data manipulation
* [chart.js](https://www.chartjs.org/) - Used to create graphs
* [tqdm](https://pypi.python.org/pypi/tqdm) - Used to make progress bar
* [New York Times API](https://developer.nytimes.com/) - Used to get news articles
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Used to parse article HTML
* [urllib.request](https://docs.python.org/3/library/urllib.request.html) - Used to open urls for news articles
* [json](https://docs.python.org/3/library/json.html) - Used to decode json
* [datetime](https://docs.python.org/2/library/datetime.html) - Used to convert timestamps





## Authors

* **Daniel Ferriss** - [github](https://github.com/danielferriss)
* **Han Bai** - [github](https://github.com/hanbai2)
* **Divya Bhati** - [github](https://github.com/DivyaBhati)
* **Anmol Nigam** - [github](https://github.com/the-master-guy)

## Acknowledgements

* Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
