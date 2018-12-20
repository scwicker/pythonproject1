#main file for python project.  Initial commit

#this program will prompt the user for 2 numbers and multiply them together. 



#print introduce user to the program 

print ("This program will take two integers between 0-999 and display their product")

#While loop around the whole program so user can choose to play again.

playagain = True
while playagain:

#invalid input - display invalid input message and jump to prompt user for input. 
	def inputValidation(usernum):
		if (usernum < 0 or usernum > 999):
			return False
		else:
		
			return True

	



	validInputs = 0	
	while (validInputs < 1):
		num1 = input("Please enter your first number: ")
		num1 = int(num1)

		if inputValidation(num1):
			print("first number accepted")
			validInputs += 1


		else:
			print("invalid input, integers between 0-999 only")
	

	

	while (validInputs < 2):
		num2 = input("please enter your second number: ")
		num2 = int(num2)
		if inputValidation(num2):
			print ("second number accepted")
			validInputs +=1
	
		else:
			print ("invalid input, integers between 0-999 only")
	



#set valid inputs to 0
	validinputs = 0
	




#exit while loop with our two valid nums


#create variable numsProduct


#calculate product

	product = num1 * num2



#display the product, prompt user to enter 2 more numbers, or to exit. 

	print ("The product of your two numbers is " + str(product) + ".")



#if y, play again.  If q, quit program.

	def again(playagain):

		userchoice = input("Would you like to play again or quit? y = yes, q = quit: ")
	
		if (userchoice == "y" or userchoice == "Y" or userchoice == "yes"):
			playagain = True

		elif (userchoice == "q" or userchoice == "Q" or userchoice == "no" or userchoice == "No"):
			playagain = False

		else:
			print ("please make a valid selection")
		#	again()

	again(playagain)




			
	






#input validation function
#could probably make this a boolean function
