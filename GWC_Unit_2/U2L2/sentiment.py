import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
DATA_FILE = "tweets_small.json"

# Continue your program below!

'''
make_textblob: example function -- change this however you want!
'''
def make_textblob(string):
    # Textblob sample:
    tb = TextBlob(string)
    return tb

'''
main: this is our main function where everything happens
'''
def main():
    polarity_sum = 0
    polatrity_list = []
    subjectivity_list = []
    #Get the JSON data
    with open(DATA_FILE, "r") as tweetFile:
        tweetData = json.load(tweetFile)

    for tweet in tweetData:
        blob = make_textblob(tweet["text"])
        polatrity_list.append(blob.polarity)

    for value in polatrity_list:
        polarity_sum += value

    polarity_average = polarity_sum / len(tweetData)
    print(polarity_average)

    for tweet in tweetData:
        blob = make_textblob(tweet["text"])
        subjectivity_list.append(blob.subjectivity)

    technical_graph(polatrity_list)

    techno_grif(subjectivity_list)

    word_cloud(tweetData)


def plot_histogram(data, data_bins, axis_list):
    plt.hist(data, bins=data_bins)
    plt.xlabel('Polarity Range')
    plt.ylabel('Frequency')
    plt.title('Tweet Sentiment Data')
    plt.axis(axis_list)
    plt.grid(True)
    plt.show()

def technical_graph(polatrity_list):
    someList = polatrity_list
    bins = [-1, -0.5, 0.0, 0.5, 1]
    axes = [-1.0, 1.0, 0, 100]
    plot_histogram(someList, bins, axes)

def plot_histogram2(data, data_bins, axis_list):
    plt.hist(data, bins=data_bins)
    plt.xlabel('Subjectivity Range')
    plt.ylabel('Frequency')
    plt.title('Tweet Sentiment Data 2')
    plt.axis(axis_list)
    plt.grid(True)
    plt.show()

def techno_grif(subjectivity_list):
    someList = subjectivity_list
    bins = [-1, -0.5, 0.0, 0.5, 1]
    axes = [-1.0, 1.0, 0, 100]
    plot_histogram2(someList, bins, axes)

def word_cloud(twitter):
    empty_string = ""
    filteredWords = {}
    filter_out = ["http", "about", "even", "although", "will", "much", "kevin", "they", "lets", "bring", "any", "from", "this", "using", "some", "that", "there", "these", "post", "though", "ever", "realdonaldtrump"]

    for tweet in twitter:
        empty_string = empty_string + tweet["text"]

    blob_string = make_textblob(empty_string)

    for word in blob_string.words:
        if word.isalpha() and (len(word)>3) and word.lower() not in filter_out:
            filteredWords[word] = blob_string.words.count(word)

    print(filteredWords)
    #generating a word cloud
    cloud = WordCloud().generate_from_frequencies(filteredWords)

    return cloud

if __name__ == '__main__':
    main()
