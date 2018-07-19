import sys
from random import randint


def dice_generator(beg, end, times=1):
    result = list()
    for _ in range(0, times):
            result.append(randint(beg, end))
    return result


def main():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if len(sys.argv) > 3:
            times = int(sys.argv[3])
        else:
            times = 1
    except:
        print("You have to input 2 or 3 integers!")

        results = dice_generator(a, b, times)
    for n in results:
        print(n)


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()