#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

number1 = 0
length = len(argv)
for i in range(1, length):
    number1 += int(argv[i])
print('{}'.format(number1))
