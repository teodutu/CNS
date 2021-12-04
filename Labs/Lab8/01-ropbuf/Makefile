CFLAGS = -fno-pic -Wall -Wextra -Wno-unused-function -Wno-unused-variable -g -O0  -fno-stack-protector
CFLAGS_EXEC = -fno-pic -Wall -Wextra -Wno-unused-function -Wno-unused-variable -g -O0  -fno-stack-protector -zexecstack
LDFLAGS = -no-pie

all: ropbuf ropbuf_dbg

ropbuf: ropbuf.c
	$(CC) $(CFLAGS_EXEC) $(LDFLAGS) $^ -o $@

ropbuf_dbg: ropbuf.c
	$(CC) $(CFLAGS) $(LDFLAGS) $^ -o $@

clean:
	rm -f ropbuf ropbuf_dbg
	rm -f *.o

.PHONY: all clean
