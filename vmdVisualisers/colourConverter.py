import argparse
import struct

def args():
	parser = argparse.ArgumentParser(description='converts rgb or hex to VMD colour format')
	parser.add_argument('-rgb', '--rgb', type=str, help='rgb colour format', required=False)
	parser.add_argument('-hex', '--hex', type=str, help='hex colour format', required=False)
	return parser.parse_args()


if __name__ == "__main__":

	args = args()
	vmdcol = []

	if args.rgb:
		rgbcol = args.rgb.split(",")

	if args.hex:
		if args.hex[0] == '#':
			args.hex = args.hex[1:]
		rgbcol = struct.unpack('BBB',args.hex.decode('hex'))
	
	for i in range(len(rgbcol)):
		vmdcol.append(round(float(rgbcol[i])/255.0,2))

	print vmdcol[0], vmdcol[1], vmdcol[2]