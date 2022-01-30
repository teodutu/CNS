#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	srand(time(0));
	printf("%lu\n", (long)rand() | (long)rand() << 32);
	return 0;
}
