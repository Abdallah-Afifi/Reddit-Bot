import praw
import time

# Set up your Reddit API credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT',
    username='YOUR_REDDIT_USERNAME',
    password='YOUR_REDDIT_PASSWORD'
)

def run_bot(subreddit_name='python', keywords=['python']):
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.new(limit=5):  # Adjust the limit as needed
        process_submission(submission, keywords)

def process_submission(submission, keywords):
    title_lower = submission.title.lower()
    
    if any(keyword in title_lower for keyword in keywords):
        print(f"Found relevant submission: {submission.title}")
        
        # Add your bot's action here, e.g., commenting or upvoting
        # For demonstration purposes, let's just print the submission URL
        print(f"Submission URL: {submission.url}")

def main():
    while True:
        run_bot()
        time.sleep(60)  # Adjust the sleep interval as needed (in seconds)

if __name__ == "__main__":
    main()
