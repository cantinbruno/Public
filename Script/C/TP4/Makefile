CC = gcc
CFLAGS = -Wall -ansi -pedantic
OFLAGS = -lm

all: part3 part2 part1

part1 : part1.c
	$(CC) $(CFLAGS) $(OFLAGS) -o $@ $<

part2 : part2.c
	$(CC) $(CFLAGS) $(OFLAGS) -o $@ $<

part3 : part3.c complex.c
	$(CC) $(CFLAGS) -o $@ $? $(OFLAGS)

clean:
	rm ./*.exe
