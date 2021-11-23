#include <stdlib.h>
#include <stdio.h>

int seeds[] = { -1315103649, -696731225, 1030243117, -1215499853, 1139093643,
	1833309849, 1771331713, -1112691348, 542904738, 1701160368 };

char flag_enc[] = "\xdb\x20\x98\xc1\x08\x84\x5e\xda\xa3\xb4\x57\xe3\xb0\xe5"
	"\xcc\xe6\x8f\x27\xfe\x20\x82\x41\xb8\x1e\x07\xa7\x45\xb2\xe4\x11\xda"
	"\x7b\xd2\xd4\x8e\x48\xb6\xac\xac\x7c\xd9";

char flag[42];


int main()
{
	struct random_data data;
	char buff[128];
	int rand;

	for (size_t i = 0; i != sizeof(seeds) / sizeof(*seeds); ++i) {
		initstate_r(seeds[i], buff, 0x80, &data);
  		srandom_r(seeds[i], &data);

		for (int j = 0; j != 41; ++j) {
			random_r(&data, &rand);
			flag[j] = flag_enc[j] ^ rand;
		}

		printf("seed %zu: flag = %s\n", i, flag);
	}

	return 0;
}
