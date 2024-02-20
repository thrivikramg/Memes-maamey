from flask import Flask, render_template
import praw
import random

app = Flask(__name__)

def get_random_meme():
    reddit = praw.Reddit(
        client_id='72Q4AcuLZoAUKjIMMxtFgQ',
        client_secret='zmzSlbiAP4SQnxKqrIDAkw78jCg3kg',
        user_agent='meme'
    )

    # Subreddit to fetch memes from
    subreddit_name = 'dankmeme'
    submissions = list(reddit.subreddit(subreddit_name).hot(limit=500)) 
    random_submission = random.choice(submissions)

    # Extracting meme details
    meme_url = random_submission.url

    return meme_url, subreddit_name

@app.route('/')
def index():
    meme_url, subreddit_name = get_random_meme()
    return render_template('index.html', meme_url=meme_url, subreddit_name=subreddit_name)

if __name__ == '__main__':
    app.run(debug=True)
