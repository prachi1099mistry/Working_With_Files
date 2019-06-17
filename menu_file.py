def create_file():              #function to create a new empty file.
    a=input("Enter the file name you want to create=")      #Take file name as input.
    f=open(a,'w')           #open the given file in write mode.
    f.close()                   #close the open file.
    return menu()           #call to the menu function.


def append_file():          #Function to write in a file already created.
    b=input("enter the file name u want to append=")        #Take file name as input.
    f=open(b,'a')             #open the given file in append mode.
    print("Enter 'q' to stop writing")          #to stop writing in a file.
    print("Enter the input:\n ROLLNO-NAME-MARKS")   
    c=input()           #take input from user to append in the file.
    while c != 'q':         #finite loop.
        f.writelines(c)     #writing to the file.
        f.write("\n")               
        c=input()           #take other input.
    f.close()                   #close the open file.
    return menu()            #call to the menu function.


def update_file():          #Function to Update the content of the file.
    c=input("Enter the file name to update:")            #Take file name as input.
    f=open(c,'r')           #Open the given file in read mode.
    l1=f.readlines()        #Store the contents of the file.
    for i in range(len(l1)):            
        print(i,'=',l1[i])      #creating a list.
    p=int(input("Enter the record number you want to update:"))
    j=input("Enter the new record:")
    l1[p]=j+"\n"            #updating the list.
    f=open(c,'w')           #again opening the file in write mode.
    f.writelines(l1)        #writing the updates to the file.
    f.close()                   #close the open file.
    return menu()           #call to the menu function.


def view_file():            #Function to read a perticular file.
    d=input("Enter the file name you want to read:")          #Take file name as input.
    f=open(d)               #Open the given file in read mode.
    print(f.read())         #print the content of the file.
    f.close()                    #close the open file.
    return menu()            #call to the menu function.


def view_record():          #Function to read a perticular record in the file.
    d=input("Enter the file name you want to read:")     #Take file name as input.
    f=open(d,'r')           #Open the given file in read mode.
    u=f.readlines()         #Store the contents of the file.
    w=[]                        #creating a list.
    e=[0,1,2,3,4,5,6,7,8,9,10,11,12]        #Creating a list.
    for x in e:             #loop
        w.append((e[x],u[x]))           #join the content of 2 list.
    m=int(input("Enter the rollno="))       #User input.
    for i,j in w:
        if i==m:                #Searching for the record.
            print("ROLLNO-NAME-MARKS:")
            print(j)                #printing the matched record.
            break                   #Go out of the loop.
    f.close()         #close the open file.
    return menu()           #call to the menu function.


def menu():                 #Function to display the Menu of content.
    print("\t\t\tMENU")     
    print("\t\t\tChoose from the following:-")
    print("\t\t\t1=create new file.")
    print("\t\t\t2=Append a file.")
    print("\t\t\t3=Update a file.")
    print("\t\t\t4=view file.")
    print("\t\t\t5=view record.")
    print("\t\t\t6=exit.")
    s=int(input("make ur choice:"))
    if s == 1:
          create_file()                 #call to the function Specified by the user.
    elif s == 2:
          append_file()             #call to the function Specified by the user.
    elif s == 3:
          update_file()             #call to the function Specified by the user.
    elif s == 4:
          view_file()               #call to the function Specified by the user.
    elif s == 5:
          view_record()         #call to the function Specified by the user.
    elif s == 6:
          exit(1)
    else:
          print("invalid choice")
          menu()


menu()                      #Call to the starting function.
