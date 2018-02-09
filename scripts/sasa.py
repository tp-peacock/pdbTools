import os
import re
import argparse
import bioptools
import exploder

def args():
	parser = argparse.ArgumentParser(description='sasa.py. Produces pdb files with contact residues given dummy chains for highlighting in vmd.')
	parser.add_argument('-f', '--file', type=str, help='input pdb file', required=True)
	parser.add_argument('-e', '--expl', action='store_true', help='produces exploded structure of original pdb', required=False) 
	return parser.parse_args()


def chainContacts(pdbfile):
	tmpfile = "tmp.ca"
	#bioptools.chaincontacts(['-x','D','-y','A',pdbfile,tmpfile])
	bioptools.chaincontacts([pdbfile,tmpfile])
	return tmpfile

def cleanUp(rubbish):
	if os.path.isfile(rubbish):
		os.remove(rubbish)
	elif os.path.isdir(rubbish):
		shutil.rmtree(rubbish)

def readContacts(tmpfile):
	file = open(tmpfile,'r')
	contacts = []
	for line in file:
		if "chain" in line.lower():
			sline = line.strip().split(" ")
			sline = [elem for elem in sline if elem.strip()]			
			res1 = sline[1]+sline[3]
			res2 = sline[6]+sline[8] 
			contacts.append([res1,res2])
	file.close()
	for c in contacts:
		print c
	return contacts

def rewritePDB(pdb,contacts):

	pdbatoms = bioptools.pdbatoms(pdb).split("\n")
	atoms = []
	for atom in pdbatoms:
		split_atom = atom.split(" ")
   
		space_count = re.findall('\s+', atom)

		split_atom = [elem for elem in split_atom if elem.strip()]
		if len(split_atom) < 12:
			continue

		for c in contacts:
			if split_atom[4] == c[0][0] and split_atom[5] == c[0][1:]:
				split_atom[4] = "Y"
			elif split_atom[4] == c[1][0] and split_atom[5] == c[1][1:]:
				split_atom[4] =  "Z"

		pdbatom_out = "".join([val for pair in zip(split_atom, space_count) for val in pair])
		atoms.append(pdbatom_out)

	with open(os.path.splitext(pdb)[0]+"highlight.pdb", "w") as outfile:
		for a in atoms:
			outfile.write(a+"\n")


if __name__ == "__main__":
	args = args()

	tmpfile = chainContacts(args.file)
	contacts = readContacts(tmpfile)

	if args.expl:
		efile = exploder.explode(args.file,2)
		rewritePDB(efile, contacts)
	else:
		rewritePDB(args.file, contacts)

	cleanUp(tmpfile)