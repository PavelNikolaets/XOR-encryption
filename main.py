


def XOR_choice_start(def_come,def_key):
	print("Select 1 encryption or 2 decryption. Enter a number.")
	choise = int(input("Enter: "))
	if choise == 1:
		XOR_cipher(def_come,def_key)
	elif choise == 2:
		XOR_uncipher(def_come,def_key)
	else:
		print("ERROR. Invalid selection entered")



def XOR_data_enter_start():
	print("Welcom to XOR-project!")
	come = input("Enter data for encryption/decryption: " )
	print("The key length must be at least 11 characters.")
	key = input("Enter the encryption/decryption key: ")

	XOR_choice_start(come,key)



def XOR_cipher(encryption_data, encryption_key):

	guests = None
	final_new : str = None

	home = []
	new_one = []
	total_new = []

	list_key = list(encryption_key)

	for x in encryption_data:
		guests = format(ord(x), "b")
		home.append(guests)

		print(home)

	for x in home:
		i = 0
		bin_element = list(x)

		for y in bin_element:

			print(i)

			if int(y) == 0 and int(list_key[i]) == 0:
				new_one.append(0)
			elif int(y) == 0 and int(list_key[i]) == 1:
				new_one.append(1)
			elif int(y) == 1 and int(list_key[i]) == 0:
				new_one.append(1)
			elif int(y) == 1 and int(list_key[i]) == 1:
				new_one.append(0)
			else:
				print("ERROR The condition is not met!")
				print(f"Bin element {y} and Key element {list_key[i]}")

			i += 1


		total_new.append("".join(str(e) for e in new_one))
		new_one = []

	final_new = " ".join(a for a in total_new)
	print(f"Result: {final_new}")



def XOR_uncipher(encryption_data, encryption_key):

	new_one = []
	total_new = []
	final_new = []

	print(f"Data entered, encryption_data - {encryption_data} & encryption_key - {encryption_key}")

	split_data = encryption_data.split()
	element_key = list(encryption_key)

	for x in split_data:
		i = 0
		element_x = list(x)
		print(element_x)

		for y in element_x:
			if int(y) == 0 and int(element_key[i]) == 0:
				new_one.append(0)
			elif int(y) == 0 and int(element_key[i]) == 1:
				new_one.append(1)
			elif int(y) == 1 and int(element_key[i]) == 0:
				new_one.append(1)
			elif int(y) == 1 and int(element_key[i]) == 1:
				new_one.append(0)
			else:
				print("ERROR The condition is not met!")
				print(f"Bin element {y} and Key element {element_key[i]}")

			i += 1
			
		total_new.append("".join(str(e) for e in new_one))
		new_one = []
		print(total_new)

	final_new = " ".join(a for a in total_new)
	print(f"Result: {final_new}")
		


XOR_data_enter_start()