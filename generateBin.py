import argparse, os

# get file size from command line
parser = argparse.ArgumentParser(description='Generates random binary of user-inputted size')
parser.add_argument('size', metavar='size', type=float,
                    help='Size in KB of binary file to be generated')
args = parser.parse_args()

# generate random data
data = os.urandom(int(args.size*1000))

# write data to file
file = open('data.bin', 'wb')
file.write(data)
file.close()
