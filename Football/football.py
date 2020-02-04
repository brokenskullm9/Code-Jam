from array import * 

N = int(input('N: '))   #total number of students for selection
P = int(input('P: '))   #number of students to be picked from N number of students
#initialising some of the required variables
mini = []
maxi = []
result = []
flag = 0
A = 0
B = 0
time = 0
#initialization of array to be used for skill of the student
a = array('i')

#taking the skill points from the user
for i in range(N):
    a.append(int(input('skill ')))

#fetching two minimum value from the array of skill points, and storing it into the list mini
for mi in range(2):
    mini.append(min(a))
    a.remove(min(a))
if mini[0]>mini[1]:         #calculating for the difference between two minimum value of the array skill points
    A = mini[0] - mini[1]
else:
    A = mini[1] - mini[0]

#fetching two maximum value from the array of skill points, and storing it into the list maxi
for ma in range(2):
    maxi.append(max(a))
    a.remove(max(a))
if maxi[0]>maxi[1]:         #calculating for the difference between two maximum value 
    B = maxi[0] - maxi[1]
else:
    B = maxi[1] - maxi[0]

#checking for the less differece between the two number of the list(both of the number belongs to the same list), from the list mini and maxi
if A>B:
    result = maxi
    flag = 1
else:
    result = mini
    flag = 0

#if flag = 0, two minimum numbers of the array has the less difference, and, if, flag = 1, two number of the array hanve the less difference
if flag == 0:
    a.append(maxi[0])
    a.append(maxi[1])
    for j in range(2, P):
        result.append(min(a))
        a.remove(min(a))
else:
    a.append(mini[0])
    a.append(mini[1])
    for j in range(2, P):
        result.append(max(a))
        a.remove(max(a))

#calculating the minimum time required for traning the students
for x in range(len(result)):
    time = time + (max(result) - result[x])

#printing the calculated minimum time
print(time)
