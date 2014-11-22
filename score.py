def score(scenes):
'''count the times every agent appears in scenes(scenes have a attribute where a kind of agent appear,in this code it is
   the index 1'''
	agents=[]
	for i in scenes:
		agents.append(i[1])
	sagents=list(set(agents))
	count=[(cits.count(i),i) for i in agents]
	return count
