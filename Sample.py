import random
import numpy as np

n=int(input("no of jobs : "));
m=int(input("no of machines:"));
s=int(input("enter a random seed: "));


# look at what waquar told

#for a in range(1,n+1):
    #for l in range(10):
         #print(random.randint(0,10), end=' ') 
         #print(random.randint(0,100), end=' ')
    #print("\n")
  

# for x in range(1,3):
#     print(x)
        
       
def generate_job_shop(i,j,k):
    print(i,end=' ')
    print(j)
    for a in range(1,i+1):
        for l in range(10):
            random.seed(k)
            # print(k)
            # print(random.randint(0,10), end=' ') 
            # print(random.randint(0,100), end=' ')
            print(int((np.random.uniform(1,100))))
        print("\n")


generate_job_shop(n,m,s)





