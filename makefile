all: right

right: right.c
	gcc right.c -framework Cocoa -framework ApplicationServices -o right
