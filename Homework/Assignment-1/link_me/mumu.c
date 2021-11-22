#include <unistd.h>

int array_sum(int *arr, size_t len)
{
	int sum = 0;
	for (size_t i = 0; i != len; ++i)
		sum += arr[i];
	return sum;
}

void string_xor_with_key(char *str, size_t len, char key)
{
	for (size_t i = 0; i != len; ++i)
		str[i] ^= key;
}

int main()
{
	return 0;
}
