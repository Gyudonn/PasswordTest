password = 'a123456'
password_count = 3

while True:
	if password_count  >= 0:		
		password_input = input('Please input your password: ')
		if password_input != password:
			if password_count > 0 :
				print('Wrong password, you have ' + str(password_count) + ' times to try.')
		else:
			print('Login success!')
			break
		password_count = password_count - 1
	else:
		print('System error.')
		break