CFLAGS= -Wall -no-pie -O0
LDLIBS = -lm

PRG=point

$(PRG): $(PRG).c
	$(CC) $(CFLAGS) -o $@ $< $(LDLIBS)

clean:
	rm -f $(PRG)
