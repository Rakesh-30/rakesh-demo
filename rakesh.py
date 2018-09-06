pas=True
while pas:
	name=input("Enter your name: ")
	print(f"Hello {name} ")
	choice=input("Press Y to retry and N to exit. ").upper()
	if(choice=='Y'):
		pas=True
		continue
	else:
		break;