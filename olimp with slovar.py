index=[]
all_arr=[]
point_arr=[]
for i in range(50000):
    f = input()
    if f != "":
        print('Количество баллов -', end=" ")
        f1=input()
    else:
        break
    if f != '':
        all_arr.append(f)
        point_arr.append(f1)
    else:
        break
all_arr=set(all_arr)
all_arr=list(all_arr)
for i in range (len(all_arr)):
    index_arr=(f'{i+1}_{all_arr[i][0][0]}_{len(all_arr[i][1])}, ')
    index.append(index_arr)
d={"name":all_arr,"point":point_arr,"id":index}
print(d["name"])