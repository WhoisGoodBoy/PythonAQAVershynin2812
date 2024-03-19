from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--a', help='first argument to parse', default=15)
parser.add_argument('--b', help='second argument to parse', default=30)
args = parser.parse_args()
dicted_args = args.__dict__
print(type(dicted_args['a']))