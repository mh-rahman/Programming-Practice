class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = {} # 2:(1,4) -> 2 follows 1,4 (value = influencers)
        self.allTweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.follows:
            self.follows[userId] = set([userId])
        self.allTweets.append([userId,tweetId])

        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.follows:
            self.follows[userId] = set([userId])
            return []
        newsFeed = []
        for u,t in reversed(self.allTweets):
            if len(newsFeed) == 10:
                break
            if u in self.follows[userId]:
                newsFeed.append(t)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows:
            self.follows[followerId] = set([followerId])
        if followeeId not in self.follows:
            self.follows[followeeId] = set([followeeId])
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows:
            self.follows[followerId] = set([followerId])
            return
        if followerId == followeeId or followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)

            

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)