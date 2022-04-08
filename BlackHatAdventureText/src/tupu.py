# a tool to unpack the tuple created by the adventure function calls


def tupu(tupin,which):

	tmp_lst = [tupin]
	if which == '1':
		return tmp_lst[0]
	elif which == '2':
		return tmp_lst[1]
		
		
if __name__ == '__main__':

	print(tupu(('testing',3)))
