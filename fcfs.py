def returnFirstarrivaltime():
    for i in range(0,len(arrivaltime)):
        if processcomplte[i] != 1:
            return i

def returnIndexOfLowestOrder():
    min = returnFirstarrivaltime()
    for i in range(returnFirstarrivaltime() + 1,len(arrivaltime)):
        if arrivaltime[i] < arrivaltime[min] and processcomplte[i] != 1:
            min = i
    processcomplte[min] = 1
    return min

print("ENTER NUMBER OF PROCESSES : ")
n=int(input())

process=[]
processcomplte=[]
order=[]
arrivaltime=[]
bursttime=[]
waiting=[]

for i in range(0,n):
	process.insert(i,i+1)
	processcomplte.insert(i,0)
	bursttime.insert(i,int(raw_input("ENTER BURST TIME OF PROCESS ")))
	arrivaltime.insert(i,int(raw_input("ENTER ARRIVAL TIME : ")))


for i in range(0,n):
	order.insert(i,arrivaltime[i])

def swap(t1,t2):
	return t2,t1

sum=0
waiting=[]
runningprocess=[]
turnaround=[]
waiting.insert(0,0)
for i in range(0,n):
	proces=returnIndexOfLowestOrder()
	runningprocess.insert(i,proces+1)
	sum+=bursttime[proces]	
	waiting.insert(i+1,sum)
	turnaround.insert(i,sum-arrivaltime[i])
	
print(waiting)
print(turnaround)

sum1=0.0
sum2=0.0

for i in range(0,len(waiting)-1):
	sum1+=waiting[i]-arrivaltime[i]
	sum2+=turnaround[i]
	print("WAITING TIME OF PROCESS "+str(runningprocess[i])+" is "+str(waiting[i]-arrivaltime[i]))
 	print("Arrival time of Process" + str(runningprocess[i]) + " is  "+ str(turnaround[i]))

print("average waiting time is "+ str(float(float(sum1)/n)))
print("average turnaround time is "+ str(float(float(sum2)/n)))
