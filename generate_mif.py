import argparse, os

# Get command line arguments
parser = argparse.ArgumentParser(description='Generate Memory Initialization File (mif) from 153.6 KB of data')
parser.add_argument('-m', '--mif', default='.', help='Use to specify where to output mif file. If not used, mif file will output to CWD.',
					metavar='path')
parser.add_argument('-f', '--file', help='Use to generate a mif file from a provided file. If not used, mif file will use random data.',
					metavar='path_to_file')
args = parser.parse_args()

# if no file specified, generate random data
if args.file is None:
	data = os.urandom(320*240*2)
else:
	print("Getting data from file")

# open initial_data.mif
mif = open('initial_data.mif', 'w')

# write width, depth, address_radix, and data_radix to mif file
mif.write("WIDTH=128;\n")
mif.write("DEPTH=9600;\n\n")
mif.write("ADDRESS_RADIX=HEX;\n")
mif.write("DATA_RADIX=HEX;\n\n")
mif.write("CONTENT BEGIN\n")

# write data to mif file
for n in range(0, 9600):
	mif.write("\t")
	mif.write('{:04X}'.format(n))
	mif.write('  :   ')
	for m in range(0, 16):
		mif.write('{:02X}'.format(data[(n*16)+m]))
	mif.write(';\n')

# close initial_data.mif
mif.write("END;\n")
mif.close()
