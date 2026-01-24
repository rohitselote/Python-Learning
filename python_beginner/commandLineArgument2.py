# another package called arg parrse
import argparse
parser=argparse.ArgumentParser(
    description='This program prints the name of my  dog'
)

# parser.add_argument('-c','--color',metavar='color' ,required=True,help='the color to search for')
#python commandLineArgument2.py -c red

parser.add_argument('-c','--color',metavar='color' ,required=True,choices={'red','yellow'},help='the color to search for')

args = parser.parse_args()

print(args.color)
