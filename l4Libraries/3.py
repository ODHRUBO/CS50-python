import sys

if len(sys.argv) < 2:
    print("Too few argument")
elif len(sys.argv) > 2:
    print("Too many argument")
else:
    print("hello,my name is ",sys.argv[1])