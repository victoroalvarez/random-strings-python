# libraries import
import string
import random

# String generator function, takes an integer argument which determines string length
# and another with all alpha-numeric characters
def rs_generator(string_size=12, alphanumeric_characters=string.ascii_lowercase + string.digits):
	# returns alpha numeric string of particular string length determined by the string_size parameter
	return ''.join(random.SystemRandom().choice(alphanumeric_characters) for _ in range(string_size))

# Calls rs_generator function with 6 as a integer argument for setting string length
print(rs_generator(6))
