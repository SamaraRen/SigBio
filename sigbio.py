import random
def wRand (listA, listB):
	sum = 0
	for i in range(0, len(listB)):
		sum += float(listB[i])
	print sum
	temp = random.uniform(0, sum)
	for i in range(0, len(listB)-1):
		accumulate = 0.0
	j = -1
	while accumulate < temp:
		j +=1
		accumulate += float(listB[j])
	return listA[j]
#test
print wRand([1,2,3,4,5],[4,4,4,4,4])

def crossover (listA, listB, pivot):
	return listA[:pivot]+listB[pivot:]
#test
print crossover([1,2,3,4,5],[6,7,8,9,10], 2)

def mutation (list, chance, size):
	num = int(size*chance)
	choice = random.sample(xrange(len(list)), num)
	for i in choice:
		list[i] = (list[i]+1)%2
	return list

#test
print mutation([1,0,1,0,0,0,1], 0.5, 9)

def gene(geneSize):
	geneResult = []
	for i in range(0,geneSize):
		geneResult.append(random.choice([0,1]))
	return geneResult

#test
print gene(10)

def genePop(geneSize, popSize):
	popResult = []
	for i in range(0, popSize):
		popResult.append(gene(geneSize))
	return popResult

#test
print genePop(4,4)

def rand(list):
	return random.choice(list)

#test
print rand([1,2,3,4])