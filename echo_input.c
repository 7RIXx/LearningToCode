// Create a program that gets a user's input and  reports it back to the terminal

// Headers
#include <stdio.h>
#include <stdlib.h>

// Globals
int MAXSIZE = 50;


// the_command = (char*)malloc(MAXSIZE);

// read stdin to acquire the command

char get_input(){

	// hold user's command
	char the_command[MAXSIZE];
	//ask for input
	printf("Enter some input: \n");
	fgets(the_command, MAXSIZE, stdin);
	printf("%s\n", the_command);

	
}




int main(){

	get_input();

}
