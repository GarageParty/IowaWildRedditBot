from unittest import mock
import praw

from iowa_wild_reddit_bot import main


class FakeReddit:
    def __init__(self):
        self.read_only = False


class TestMain:
    @staticmethod
    @mock.patch.object(praw, "Reddit")
    def test_main(patched_praw):
        patched_praw.return_value = FakeReddit()
        assert not main.main()
