#count the times every agent appears
def score(scenes):
	agents=[]
	for i in scenes:
		agents.append(i[1])
	sagents=list(set(agents))
	count=[(cits.count(i),i) for i in agents]
	return count
