# guest_count = [1,2,3,4]
guest_count = [1,2,1,3,2,1,0,2,1,0]
count = 0
for i in range(len(guest_count)):
    # print(i)
    # print(guest_count[i])

    if guest_count[i] == 1:
        count = count +1

print(count)

 