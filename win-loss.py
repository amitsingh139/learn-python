import random

def win_loss():
    x = random.randint(0,100)
    if(x>50):
        print("Win")
    else:
        print("Loss")
    return x 

# driver
w=0
l=0
for i in range(0,10):
    flag=win_loss()
    if(flag>50):
        w+=1
    else:
        l+=1    

if(w>l):
    print("Overall Win")
else:
    print("Overall loss")    