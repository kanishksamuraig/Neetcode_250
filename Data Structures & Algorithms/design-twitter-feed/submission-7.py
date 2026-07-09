import heapq
class User:
    def __init__(self,userid:int):
        self.userid=userid
        self.userpost=[]
        self.followeepost=[]
        self.followers=[]

    def insert(self,userid,post,counter):
        if userid==self.userid:
            self.userpost.append((counter,post,userid))
            return
        self.followeepost.append((counter,post,userid))  
    def delete(self,userid):
        lst=[]
        for val in self.followeepost:
            if val[2]!=userid:
                lst.append(val)
        self.followeepost=lst[:]

    def feed(self):
        lst=[];heap=[]
        for i in self.userpost:
            heapq.heappush(heap,i)
            if len(heap)>10:
                heapq.heappop(heap)
        for i in self.followeepost:
            heapq.heappush(heap,i)
            if len(heap)>10:
                heapq.heappop(heap)
        x=len(heap)
        for i in range(x):
            lst.append(heapq.heappop(heap))
        lst.reverse()
        return [x[1] for x in lst]

class Twitter:

    def __init__(self):
        self.users={}
        self.followers={}
        self.posts={}
        self.counter=0


    def postTweet(self, userid: int, tweetid: int) -> None:
        if userid not in self.users:
            self.users[userid]=User(userid)
            self.followers[userid]=[]
            self.posts[userid]=[]
        self.posts[userid].append((tweetid,self.counter))
        self.users[userid].insert(userid,tweetid,self.counter)
        for user in self.followers[userid]:
            self.users[user].insert(userid,tweetid,self.counter)
        self.counter+=1
    def getNewsFeed(self, userid: int) -> List[int]:
        return self.users[userid].feed()

    def follow(self, followerid: int, followeeid: int) -> None:
        
        if followerid not in self.users:
            self.users[followerid]=User(followerid)
            self.followers[followerid]=[]
            self.posts[followerid]=[]
        if followeeid not in self.users:
            self.users[followeeid]=User(followeeid)
            self.followers[followeeid]=[]
            self.posts[followeeid]=[]
        if followerid==followeeid or followerid in self.followers[followeeid]:
            return
        self.followers[followeeid].append(followerid)
        for posts,counter in self.posts[followeeid]:
            self.users[followerid].insert(followeeid,posts,counter)
    
    def unfollow(self, followerid: int, followeeid: int) -> None:
        if followerid==followeeid or followerid not in self.followers[followeeid]:
            return
        self.followers[followeeid].remove(followerid)
        self.users[followerid].delete(followeeid)
        
