from nytimesarticle import articleAPI
import time

def main():
	print get_range_headlines_and_wordcount(1980, 1980)

def get_range_headlines_and_wordcount(start, end):
	'''
	Returns a dictionary mapping a year to all headlines from that year
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
    and it will return a list of headlines
    for that year.
    '''
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