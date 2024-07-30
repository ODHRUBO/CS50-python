import sys

if len(sys.argv) < 2:
    sys.exit("Too few argument")
elif len(sys.argv) > 2:
    sys.exit("Too many argument")

#print name tags
print("hello,my name is ",sys.argv[1])