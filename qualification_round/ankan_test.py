import sys

def roadMapping():
    # First Line Input
    firstLine=input().split()
    duration = int(firstLine[0])
    intersection = int(firstLine[1])
    streets = int(firstLine[2])
    cars = int(firstLine[3])
    bonus = int(firstLine[4])

    #Taking inputs for streets 
    streets_info=[]
    for i in range(streets):
        s= input.split()
        streets_info.append(int(s[0]),int(s[1]),s[2],int(s[3])) # connected path beg, end, name , time
    #Taking inputs for cars
    car=[]
    probality_factor=[]
    for i in range(cars):
        c=input.split()
        roads=int(c[0])
        car.append(roads,c[1:])
        a=1
        time=[]
        for j in range(roads):
            road_name=c[a]
            x,y=0,0
            t=0
            for k in range(streets):
                if(road_name==streets_info[k][2]):
                    t+=streets_info[k][3]
            time.append(int(t))
        tot_time=0
        for j in time:
            tot_time+=int(j)
        probality_factor(int((duration/tot_time)*100))            
    

    #Signaling process
    signaling=dict()
    for a in range(cars):
        maximum= probality_factor.index(max(probality_factor))
        probality_factor.pop(maximum)
        time=0
        locations = car[maximum][1:]
        for loc in locations:
            for k in range(streets):
                if(loc==streets_info[k][2]):
                    end = streets[k][1]
                    time+=streets[k][3]
                    key=[]
                    try:
                        key=signaling[loc]
                    signaling[loc]=key.append(end,time)

    print(len(signaling.keys()))
    end=[]
    name=[]
    for keys in signaling.keys():
        data=signaling[loc]
        end=data[0][1]
        print(end)






                    




            




if _name_ == "_main_":
	filenames = ['a']

	for name in filenames:
		sys.stdin = open(f"{name}.in", 'r')
		sys.stdout = open(f"{name}.out", 'w')
        roadMapping()