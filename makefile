all: right left

right: right.c
	gcc right.c -framework Cocoa -framework ApplicationServices -o right

left: left.c
	gcc left.c -framework Cocoa -framework ApplicationServices -o left
