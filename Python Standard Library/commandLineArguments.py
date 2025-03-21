import sys

# print(sys.argv)     # argv -> Argument Variable     | run comand python commandLineArgument -a -b -c
# return value           ['.\\commandLineArguments.py', '-a', '-b', '-c']

if len(sys.argv) == 1:  # python commandLineArgument 12344
    print("USAGE: python commandLineArgument.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
