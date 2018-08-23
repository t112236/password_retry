password = 'a123456'
while True:
	i = input('請輸入密碼: ')
	if i == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有2次機會')		
	i = input('請輸入密碼: ')
	if i == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤! 還有1次機會')
	i = input('請輸入密碼: ')
	if i == password:
		print('登入成功')
		break
	else:
		print('暫停輸入30分鐘, 請稍後再試!')
		break
