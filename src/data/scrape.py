import praw
from praw.models import MoreComments
import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from data import config

reddit = praw.Reddit(
    user_agent = config.user_agent,
    client_id= config.client_id,
    client_secret= config.client_secret,
    username = config.username,
    password = config.password
    )

for url in config.post_urls:
    submission = reddit.submission(url=url)

    submission.comments.replace_more(limit=None)

    with open('/Users/logno/Documents/GitHub/conspiracy_generation/data/interim/corpus.txt', 'w') as fout:
        for comment in submission.comments.list():
            fout.write(comment.body.replace("\n", "") + '\n' * 2)