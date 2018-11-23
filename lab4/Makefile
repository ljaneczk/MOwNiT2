FLAGS = -Wall -std=c11 -lgsl -lm -lgslcblas
CC = gcc
OPT = -O3

main: matrix_multiplication.c
	$(CC) $^ $(FLAGS) $(OPT) -o $@

clean:
	rm -f main
test:
	./main

all: main
