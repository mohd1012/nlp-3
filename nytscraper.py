from nytimesarticle import articleAPI
import time

def main():
<<<<<<< HEAD:nytscraper.py
	headlines_wordcounts = get_range_headlines_and_wordcount(1980, 1980)
=======
	print get_range_headlines_and_wordcount(1980, 1980)
>>>>>>> a5aecdd20ecb0d809f3898b61b49244d5048c342:nytimes.py

def get_range_headlines_and_wordcount(start, end):
	'''
	Returns a tuple of a dictionary mapping a year to all headlines from that year
	and a second dictionary mapping year to average wordcount
	for all years from start to end (dates)
	'''
	headlines = list()
	avg_wordcounts = list()
	for i in range(start, end + 1):
		#tuple with avg_wordcount and headlines from a year i
		headline_wordcount = get_headlines_and_wordcount(str(i))
		avg_wordcounts.append((i, headline_wordcount[0]))
		headlines.append((i, headline_wordcount[1]))
	#dictionary with year -> list of article headlines
	headlines = dict(headlines)
	avg_wordcounts = dict(avg_wordcounts)
	return (avg_wordcounts, headlines)

def parse_wordcount(articles):
	'''
	Parses query result for word count from each article
	Returns a list of word counts
	'''
	wordcounts = list()
	for i in articles['response']['docs']:
		wordcounts.append(i['word_count'])
	return wordcounts

def parse_headlines(articles):
	'''
	Parses query result for headlines from each article
	Returns a list of headlines
	'''
	headlines = list()
	for i in articles['response']['docs']:
		headlines.append((i['headline']['main'].encode("utf8")).lower())
	return headlines

def get_headlines_and_wordcount(date):
    '''
    This function accepts a year in string format (e.g.'1980')
    and it will return a tuple of average wordcount and a list headlines
    for that year.
    '''
    #please dont use my key :)
    api = articleAPI('fad6d61d6d69a16df4ef1e0f38ec9c00:10:73444277')
    headlines = []
    wordcounts = []
    for i in range(0,100):
        articles = api.search(fq = {'source':['The New York Times']},
               begin_date = date + '0101',
               end_date = date + '1231',
               sort='oldest',
               page = str(i))
        headlines += parse_headlines(articles)
        wordcounts += parse_wordcount(articles)
        time.sleep(1) #10 requests per second (10 items on a page)
    #find the average wordcount for this year
    avg_wordcount = 0
    for i in wordcounts:
    	avg_wordcount += i
    avg_wordcount = avg_wordcount / len(wordcounts)
    return (avg_wordcount, headlines)

if __name__ == '__main__':
	main()
