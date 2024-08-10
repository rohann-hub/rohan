# 1. write a program to accept a number from user and determine if it is a int,float,string . describe data type

user_input = input("Enter a value: ")

if user_input.isdigit():
    print("The entered value is of type: Integer")
else:
   
    try:  // Try to convert the input to a float
        float(user_input)
        print("The entered value is of type: Float")
    except ValueError:  // If conversion to float fails, it's a string
               print("The entered value is of type: String")


	# 2. create a  list of 10 random int to find the max min , avg value of the list in python .
	
	num=int(input("enter a number : "))
	arr=[]
	for n in range(num):
	    number=int(input("enter a value of number: "))
	    arr.append(number)
	    print(arr)
	    avg=sum(arr)/len(arr)
	print("max value of number is :", max(arr))
	print("min value of number is: ", min(arr))
        print("avg value of number is: ", avg)


	# 3. write a program in python  to convert to  string into a list.
	
	l=[]
	for a in range(1,4):
	    n=input("enter the value"+str(a)+": ")  
	    l.append(n)
	print(l)


# 4. function take argument and returns its data type

	def get_datatype(value):
	    return type(value).__name__
	
	print(get_datatype(10))         
	print(get_datatype(3.14))       
	print(get_datatype("Hello"))   
	print(get_datatype([1, 2, 3]))  
	print(get_datatype(None))
	

	
