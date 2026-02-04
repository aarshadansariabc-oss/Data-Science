#using loops in list
nums = [1,2,3,10,4]
x = 10
idx = 0
for val in nums:
    if val == x:
        print(f"X found at {x} index")
        break
    idx+=1

#this searching is also called linear Search