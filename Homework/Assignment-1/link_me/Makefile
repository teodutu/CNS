CC = gcc
CFLAGS = -fPIC
LDFLAGS = -shared

.PHONY: run clean

run: libmumu.so
	LD_LIBRARY_PATH=. ./link_me

libmumu.so: mumu.c
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

clean:
	rm -f libmumu.so
