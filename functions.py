# SOLUTIONS!

# ###############################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
	
def print_hello():
	"""Prints hello world"""

	print "Hello World"

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.


name = raw_input('What is your name? ')

def greet_name(name):
	"""Takes input and prints 'Hi', input"""

	print 'Hi', name 


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def mult_int(num1,num2):
	"""Multiples two integer inputs"""

	product = num1 * num2
	print product

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def repeat_string(string, integer):
	"""Repeatedly prints 'string', int number of times"""
	
	print string*integer 


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def high_low(num):
	"""Checks if num is higher, lower, or equal to 0 and prints result"""

	if num == 0: 
		print "Zero"
	elif num > 0:
		print "Higher than 0"
	else:
		print "Lower than 0"

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divis_by_three(num):
	"""Returns True or False depending on if num is divisible by 3"""

	if num%3 == 0:
		return True 
	else:
		return False

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def number_of_spaces(string_sentence):
	"""Return number of spaces in string"""

	num_space = string_sentence.count(' ')

	if num_space == 0:
		return "There are no spaces in this string"
	
	return num_space


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def calculate_tip(meal_price, tip_percent=15):
	"""Returns total amount paid with meal price and tip included.
		If tip not included, tip defaults to 15%"""

	tip_percent = float(tip_percent/100.00)
	total_amount = meal_price + (meal_price * tip_percent) 

	print '{:.2f}'.format(total_amount)


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
# 	 should be returned in a list.

def integer_info(integer):
	"""Returns two strings of information about integer inputted as a list"""

	info_list = []

	if integer > 0: #Check sign
		result1 = 'Positive'
		info_list.append(result1)
	else:
		result1 = 'Negative'
		info_list.append(result1)

	if integer%2 == 0: #Check parity
		result2 = 'Even'
		info_list.append(result2)
	else:
		result2 = 'Odd'
		info_list.append(result2)

	return info_list

# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

# info_list = integer_info(integer) #calling function here

# sign = info_list[0]
# parity = info_list[1]

# print sign
# print parity


# ###############################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def total_cost(price, state, tax = 0.05):
	"""Calculating total cost of item. Tax parameter varies by state"""

	if state == 'CA':
		total = price + (0.07 * price)
	else:
		total = price + (tax * price)

	return '{:.2f}'.format(total)

# 2. Turn the block of code from the directions into a function.
# 	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
# 	 Return the person's title and name.

name = raw_input('What is your name? ')

def print_job_title(name, job_title = 'Engineer'):
	"""Return job title and name"""

	return name,job_title

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

receiver = print_job_title(name)
r_name = receiver[0]
r_job = receiver[1]

def greeting_letter(receiver_name, receiver_job, sender_name):
	"""Print greeting letter to receiver from print_job_title function 
		and sign from sender"""

	print 'Dear {} {}, I think you are amazing!\nSincerely, {}.'.format(receiver_job,
																		receiver_name,
																		sender_name)
#Function call - greeting_letter(r_name,r_job,'Hackbright')

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

numbers = []

def add_list(num):
	"""Add num to numbers list"""

	numbers.append(num)

	print numbers















