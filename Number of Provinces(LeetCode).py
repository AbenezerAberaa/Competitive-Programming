class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		result = 0
		if not isConnected:
			return 0
		leng = len(isConnected)
		visited=[0]*leng
		for i in range(leng):
			if visited[i]==1:
				continue
			self.dfs(isConnected,visited,leng,i)
			result +=1
		return result

	def dfs(self,isConnected,visited,leng,cur):
		if visited[cur]==1:
			return
		visited[cur]=1
		for i in range(leng):
			if isConnected[cur][i]==1 and visited[i]==0:
				self.dfs(isConnected,visited,leng,i)
