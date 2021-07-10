'''def swapFileData():
    file1 = input("Enter File Name: ")
    file2 = input("Enter File Name: ")

    
    with open(file1,'r') as a:
        dataa = a.read()
        
	with open(file2,'r') as b:
        datab = b.read()
        
    with open(file1,'w') as a:
        a.write(datab)
        

    with open(file2,'w') as b:
        b.write(dataa)

swapFileData()'''

def swap():
    file1=input("Enter the file name: ")
    file2=input("Enter the 2file name: ")
    a=open(file1,"r")
    data1=a.read()
    b=open(file2,"r")
    data2=b.read()
    a=open(file1,'w')
    a.write(data2)
    b=open(file2,"w")
    b.write(data1)

swap()
    