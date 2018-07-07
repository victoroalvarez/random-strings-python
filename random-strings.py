import string
import random
def rs_generator(string_size=12, alphanumeric_characters=string.ascii_lowercase + string.digits):
	return ''.join(random.SystemRandom().choice(alphanumeric_characters) for _ in range(string_size))
print(rs_generator(6))
