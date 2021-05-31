import praw
from praw.models import MoreComments

url = "https://www.reddit.com/r/conspiracy/comments/7t02zc/rconspiracy_round_table_9_bankers_oligarchs_one/"


reddit = praw.Reddit(
    user_agent="scaper:com.logno.conspiracyscaper:v0.0.1 (by /u/cashquatch01)",
    client_id="FNA572O2Ec2ALw",
    client_secret="a4c_VFDaYq8ZpPX-x4apONkChqrBpg",
    username = 'cashquatch01',
    password = 'Lokan15z'
    )

submission = reddit.submission(url=url)

submission.comments.replace_more(limit=0)

post_comments = list()
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    post_comments.append(comment.body)

print(post_comments[33])