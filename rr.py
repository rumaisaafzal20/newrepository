class Queue:
	def __init__ (self):
		self.item = []

	#def isempty(self):
	#	return self.item == []

	def enqueue(self,item):
		self.item.insert(0,item)

	def dequeue(self):
		return self.item.pop()

	#def size(self):
	#	return len(self.item)

print ("enter no of processes : ")
n = int(input())

print ("enter the quantum time : ")
quantum=int(input())

processes=[]
processcomplete=[]
bursttime=[]
arrivaltime =[]
completiontime=[]
turnaroundtime=[]
waitingtime=[]
procesinqueue=[]

for i in range (0,n):
	processes.insert(i,i+1)
	processcomplete.insert(i,0)
	completiontime.insert(i,0)
	turnaroundtime.insert(i,0)
	waitingtime.insert(i,0)
	procesinqueue.insert(i,0)
	bursttime.insert(i,int(raw_input("enter the burst time : ")))
	arrivaltime.insert(i,int(raw_input("enter arrival time : ")))

chartarray=[]
processarray=[]
chartarray.insert(0,arrivaltime[0])
processarray.insert(0,-1)
sum=arrivaltime[0]
sumindex=1

count = 0

q=Queue()
q.enqueue(processes[0])
procesinqueue[0]=1

while (count < n):
	d=q.dequeue()-1
	if processcomplete[d]!=1:
		if bursttime[d] < quantum:
			sum+=bursttime[d]
			bursttime[d] -= bursttime[d]
		else:
			sum+=quantum
			bursttime[d]-=quantum
		chartarray.insert(sumindex,sum)
		sumindex += 1
	for i in range(0,n):
		if arrivaltime[i] <= sum and procesinqueue[i] !=1:
			q.enqueue(processes[i])
			procesinqueue[i]=1
	if bursttime[d]==0:
		count += 1
		processcomplete[d]=1
		completiontime[d]=sum
	else:
		q.enqueue(processes[d])

for i in range (0,n):
	turnaroundtime[i]=completiontime[i]-arrivaltime[i]
	waitingtime[i]=turnaroundtime[i]-bursttime[i]

print (chartarray)
print ("comletion time : ",completiontime)
print ("turnaround time : ",turnaroundtime)
print ("waiting time : ",waitingtime)
