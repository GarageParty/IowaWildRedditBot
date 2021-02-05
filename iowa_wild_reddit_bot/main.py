import os
import praw


def main():
    reddit = praw.Reddit(
        client_id=os.getenv("IOWA_WILD_BOT_KEY"),
        client_secret=os.getenv("IOWA_WILD_BOT_SECRET"),
        user_agent="iowa_wild_bot_user_agent",
        username="IowaWildBot",
        password=os.getenv("IOWA_WILD_BOT_PASSWORD")
    )

    print(reddit.read_only)
    return reddit.read_only


if __name__ == "__main__":
    main()
