import json

DATA_FILE = 'tweets_small.json'

def main():
    #open and load json data
    with open(DATA_FILE, "r") as tweetfile:
        tweetData = json.load(tweetfile)

    print("Tweet id: ", tweetData[0]["id"]) #give me the id of the first dictionary in the json file!

    print("Tweet text: ", tweetData[0]["text"]) #give me the text of the first dictionary in the json file

    #print id of all tweets 
    for i in range(len(tweetData)):
        print("Tweet id: ", tweetData[i]["id"])

    print("\nUsing other for loop")

    for tweet in tweetData:
        print("Tweet id: ", tweet["id"])

if __name__ == "__main__":
    main()
