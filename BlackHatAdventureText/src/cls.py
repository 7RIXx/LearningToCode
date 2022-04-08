import os
from subprocess import Popen, PIPE

# two funcs to help with formatting the screen

#function crafted by Mr Hai ; not working yet ; this is an evolution of the third item in cls func
def exec_command(self, command, blocking = True, shell_env = True):
        '''TODO: add formatting'''
        try:
            if blocking == True:
                step = subprocess.Popen(command,shell=shell_env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                output, error = step.communicate()
                for output_line in output.decode().split('\n'):
                    info_message(output_line)
                for error_lines in error.decode().split('\n'):
                    critical_message(error_lines)
                return step
            elif blocking == False:
                # TODO: not implemented yet                
                pass
        except Exception as derp:
            yellow_bold_print("[-] Interpreter Message: exec_command() failed!")
            return derp




def cls():

	#exec_command(ls)

	#THIS WILL WORK UNTIL THE ABOVE FUNC CAN BE MADE TO FUNCTION
	os.system("clear")
	
	
	# much smoother printing, but doesn't clear screen properly
	
	#process = Popen(['clear', '-x'], stdout=PIPE, stderr=PIPE)
	#stdout, stderr = process.communicate()
	
	
def space():
	
	print('\r\n' * 3)
	
	
	
	
	
	
	
if __name__ == "__main__":

	cls()
