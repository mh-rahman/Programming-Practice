# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        Q = deque()
        visited = set()
        s = '/'.join(startUrl.split('/')[:3])
        Q.append(startUrl)
        visited.add(startUrl)
        
        while Q:
            curr = Q.popleft()
            nexturls = htmlParser.getUrls(curr)
            # print(nexturls)
            for url in nexturls:
                if url not in visited and url.split('/')[2] == s.split('/')[2]:
                    Q.append(url)
                    visited.add(url)
        return list(visited)
