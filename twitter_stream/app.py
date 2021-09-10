from flask import Flask , render_template
from tweet_store import TweetStore

app = Flask(__name__)

store=TweetStore()

@app.route('/tweets')
def display_tweets():
    print('------------------inn app')
    tweets = store.tweets()
    print(tweets)

    return render_template('index.html',tweets=tweets)
    


if __name__ == "__main__":
    app.run(debug=True)