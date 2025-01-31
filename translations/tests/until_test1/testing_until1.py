import random
import sys
sys.path.append("/home/berkay/Monitoring-using-DDlog/translations/tests")
from myLib import test_binary
    


#Formula is p(x) UNTIL[0,3] q(x)
I_min = 0
I_max = 3
size = 200
path = "/home/berkay/Monitoring-using-DDlog/translations/until/until_ddlog/target/release/until_cli <"

logFile = "until_test1.log"
datFile = "until_test1.dat"

print()
print('\x1b[6;30;47m' + 'Testing formula p(x) UNTIL[' + str(I_min) + ',' + str(I_max) + '] q(x)' + ' \x1b[0m')
print()
print()



print('\x1b[6;30;47m'+ 'First Testblock: At each timepoint we have a single event (either p(x) or q(x))'  + '\x1b[0m')
print()

# Testing until under formula: p(x) UNTIL[0,3] q(x), i.e. case where zero is in intervall (special care needed)
# Generals note: List Data has structure: [[class,id,ts]] meaning: class = 1 means P(id), class = 2 means Q(id). id is identity integer, ts is timestamp

# Case1: all id's get satisfied
Data = []
ts = I_max
for i in range(size):
    id = random.randint(0,4)
    ts = ts + I_max + 1
    chainlength = random.randint(I_min, I_max)
    coin = random.randint(0,1)
    Data.append([2,id,ts])
    if(coin == 1):
        for dist in range(chainlength):
            Data.append([1,id,ts + (dist+1)])
    else:
        for dist in range(chainlength):
            Data.append([1,id,ts + dist])
        Data.append([1,id,ts + chainlength])

#special case where we have @ts p(x) q(x) (should be still satisfied since I_min == 0)
ts = ts + I_max + 1
Data.append([2,size,ts])
Data.append([1,size,ts])

test_description = 'Test where each id satisfies the Formula, all wrapped'
test_binary(path,test_description,Data, datFile, logFile, I_min,I_max,-1,False)



# Case2: No satisfaction. i.e. no q's
Data = []
ts = I_max
for i in range(size):
    id = random.randint(0,10)
    ts = ts + random.randint(0, I_max-1)
    Data.append([1,id,ts])

test_description = 'Test with no q(x), so formula gets never satisfied, "random" wrapping'
test_binary(path,test_description,Data, datFile, logFile, I_min,I_max,4,True)



# Third test case: random input (mainly here to check wheter output of ddlog matches with MonPoly's output)
Data = []
ts = I_max
for i in range(size):
    ts = ts + random.randint(0,2)
    id = random.randint(1,10)
    signature = random.randint(1,2)
    Data.append([signature,id,ts])

test_description = 'Random input, checks wheter DDlog produces same output as MonPoly, "random" wrapped' 
test_binary(path,test_description,Data, datFile, logFile, I_min,I_max,3,True)




#basically repeat above, slightly modify
Data = []
ts = I_max
for i in range(size):
    id = random.randint(0,10)
    ts = ts + random.randint(0,5)
    chainlength = random.randint(I_min, I_max)
    coin = random.randint(0,1)
    Data.append([2,id,ts])
    if(coin == 1):
        for dist in range(chainlength):
            Data.append([1,id,ts + (dist+1)])
    else:
        for dist in range(chainlength):
            Data.append([1,id,ts + dist])
        Data.append([1,id,ts + chainlength])
test_description = 'Test where each id satisfies the Formula, complete wrapped'
test_binary(path,test_description,Data, datFile, logFile, I_min,I_max,-1,False)




Data = []
ts = I_max
for i in range(size):
    id = random.randint(0,10)
    ts = ts + random.randint(0, I_max-1)
    Data.append([1,id,ts])
test_description = 'Test with no q(x), so formula gets never satisfied, not wrapped'
test_binary(path,test_description,Data, datFile, logFile, I_min,I_max,1,False)



# Third test case: random input (mainly here to check wheter output of ddlog matches with MonPoly's output)
Data = []
ts = I_max
for i in range(size):
    ts = ts + random.randint(0,2)
    id = random.randint(1,10)
    signature = random.randint(1,2)
    Data.append([signature,id,ts])

test_description = 'Random input, checks wheter DDlog produces same output as MonPoly, "random" wrapped'
test_binary(path,test_description,Data, datFile, logFile, I_min,I_max,3,True)
