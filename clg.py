# 1. write a program to accept a number from user and determine if it is a int,float,string . describe data type

input_value=input("enter a value")
print(type(input_value)


# 2. create a  list of 10 random int to find the max min , avg value of the list in python .
	
	num=int(input("enter a number : "))
	r=[]
	for n in range(num):
	    number=int(input("enter a value of number: "))
	    r.append(number)
	    print(r)
	    avg=sum(r)/len(r)
	print("max value of number is :", max(r))
	print("min value of number is: ", min(r))
        print("avg value of number is: ", avg)



# 3. write a program in python  to convert to  string into a list.
	
string_list = ["42", "not_a_number", "58", "100", "abc", "123"]
integer_list =[]
for string in string_list:
try:
integer = int(string)
            integer_list.append(integer)
except:
	print("invalid Value: " , string)
	print(integer_list)
	

# 4. function take argument and returns its data type

	def get_datatype(value):
	    return type(value)
	
	print(get_datatype(10))         
	print(get_datatype(3.14))       
	print(get_datatype("Hello"))   
	print(get_datatype([1, 2, 3]))  
	print(get_datatype(None))
	print(get_datatype(1,5,8)) 

# 5. write a program to check if a given variable is true ,false or none.handle these cases and print approptiate messages

def check_variable(var):
    if var is True:
        print("The variable is True.")
    elif var is False:
        print("The variable is False.")
    elif var is None:
        print("The variable is None.")
    else:
        print("The variable is neither True, False, nor None.")

check_variable(True)
check_variable(False)
check_variable(None)
check_variable(42)

#6.Multiplication two matrix

A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
B=[[1,2,1],
   [3,2,1],
   [2,1,2]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]


for i in range(len(A)):
    for j in range(len(B[0])):
     for k in range (len(A)):
        result [i][j] += A[i][k] * B[k][j]
for r in result:
    print(r)











	
