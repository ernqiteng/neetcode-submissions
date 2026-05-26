from collections import defaultdict
class Twitter:

    def __init__(self):
        self.users = defaultdict(set) #user, follows
        self.posts = [] #tweetid, userid

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append([tweetId, userId])    

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        for i in range(len(self.posts)-1, -1, -1):
            if self.posts[i][1] == userId or self.posts[i][1] in self.users.get(userId, set()):
                news.append(self.posts[i][0])
                if len(news) == 10:
                    break
        return news        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
