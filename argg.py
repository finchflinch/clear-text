#learning argparse
#skip

import argparse
parser = argparse.ArgumentParser()

#positional arguements
#arg2
parser.add_argument("square", help="display a square of a given number", type=int)

#arg 2
# parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true", type=int)
parser.add_argument("-v", "--verbose", help="increase verbosity",  action="count", default=0)
args = parser.parse_args()

ans = args.square**2
if args.verbose == 2:
    print("square of {} is {}".format(args.square, ans))
elif args.verbose == 1:
    print("{}^2 == {}".format(args.square, ans))
else:
    print(ans)

# print(args.square**2)
