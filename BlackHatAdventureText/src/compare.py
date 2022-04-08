# comparison function, accepts lists and compares their contents


def compare(one,two):
	
	it = 0
	determine = 0
	one = list(one)
	two = list(two)
	if len(one) == len(two):

		for letter in one:
			if one[it] == two[it]:
				determine += 1

			it += 1
	print('lenone   '+str(len(one)))
	print('lentwo   '+str(len(two)))
	print('determine   '+str(determine))
	return determine == len(one)
	
	

if __name__ == '__main__':

	ina = 'SuperDragon'
	inb = 'SupeDsragon'

	compare(ina,inb)
	
