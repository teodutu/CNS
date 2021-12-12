#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

int fd;
char flag[32];

int stop(int a)
{
	if (a != 0x4ABADA55) {
		puts("What do you think you're doing?");
		exit(-1);
	}
	fd = open("./flag", 0);
	puts("-> secret vault opened");
	fflush(stdout);
	return 0;
}

int right(int a, int b)
{
	if (a != 0xD15EA5ED || b != 0x4B1DDE9) {
		puts("You should really reconsider!");
		exit(-1);
	}
	read(fd, flag, 32);
	puts("-> vault contents transferred");
	fflush(stdout);
	return 0;
}

int there(void)
{
	printf("You got the flag: %s\n", flag);
	fflush(stdout);
	return 0;
}

ssize_t play(void)
{
	char buf[40];
	puts("Welcome to our Retired Old Programmers message board!");
	puts("Please leave a message: ");
	return read(0, buf, 160);
}

int main(int argc, char* argv[])
{
	play();
	puts("Thank you!");
	return 0;
}
