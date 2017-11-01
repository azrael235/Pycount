file=open("test.txt","r+")
new_file=open("new_test.txt","r+")
list1= file.read().split()
list2=new_file.read().split()
for x in list1:
    if x in list2:
        y=list2.count(x)
        print(x,":",y)


file.close()
new_file.close()

