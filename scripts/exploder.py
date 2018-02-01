#Testing with BiopTools
import sys
import os
import shutil
import operator
import subprocess
import bioptools
import argparse

from numpy import mean

def args():
	parser = argparse.ArgumentParser(description='exploder.py. Will provide a pdb file with separated chain structure.')
	parser.add_argument('-f', '--file', type=str, help='input pdb file', required=True)
	parser.add_argument('-m', '--mult', type=float, default = 2.0, help='multiplier that controls how far chains are separated', required=False)
	return parser.parse_args()


def separateStructure(pdb_dir,base_name):
	directory = pdb_dir+"/tmp_dir"
	if not os.path.exists(directory):
		os.makedirs(directory)
	else:
		print "Error! "+directory+" exists and cannot be overwritten."
		sys.exit()
	
	cwd = os.getcwd()
	os.chdir(directory)
	shutil.copy2("../"+base_name,directory)	
	chains = bioptools.pdbsplitchains(base_name)
	cleanUp(base_name)
	
	sepfiles = os.listdir(directory)
	os.chdir(cwd)

	return directory, sepfiles

def cleanUp(rubbish):
	if os.path.isfile(rubbish):
		os.remove(rubbish)
	elif os.path.isdir(rubbish):
		shutil.rmtree(rubbish)

def getCentralRes(pdbfile):
	return bioptools.pdbcentralres(pdbfile).split("\n")[0].strip()

def getChain(centroidID):
	return centroidID[0]

def getAtomID(centroidID):
	return centroidID[1:]

def getAtoms(pdbfile):
	pdbatoms = bioptools.pdbatoms(pdbfile).split("\n")
	atoms = []
	for atom in pdbatoms:
		split_atom = atom.split(" ")
		split_atom = [elem for elem in split_atom if elem.strip()]
		if len(split_atom) < 12:
			continue
		atoms.append(split_atom)
	return atoms


def getCentroid(pdbfile):
	centroidID = getCentralRes(pdbfile)
	
	atoms = getAtoms(pdbfile)

	chain = getChain(centroidID)
	atomid = getAtomID(centroidID)
	residueX = []
	residueY = []
	residueZ = []
	for atom in atoms:
		 if  atom[4] == chain and atom[5] == atomid:
			residueX.append(float(atom[6]))
	 		residueY.append(float(atom[7]))
		 	residueZ.append(float(atom[8]))

	centroid = (mean(residueX), mean(residueY), mean(residueZ))
	print centroidID, centroid

	return centroid

def getDistance(point1, point2):
	return map(operator.sub, point2, point1)

def translateRes(dist, mult, file):
	x = dist[0]*mult
	y = dist[1]*mult
	z = dist[2]*mult
	outfile = os.path.splitext(file)[0]+"trans.pdb"
	bioptools.pdbtranslate([x,y,z,file,outfile])
	return outfile

def appendFiles(masterfile,files):
	m = open(masterfile, "w")

	for file in files:
		f = open(file,"r")
   		for line in f:
   			if "MASTER" in line:
   				continue
   			if "END" in line:
   				continue
			m.write(line)
		f.close()
	m.close()

def explode(pdbfile, mult):
	pdb_dir = os.path.dirname(pdbfile)
	base_name = os.path.basename(pdbfile)

	cleanUp(pdb_dir+"/tmp_dir")

	tmpdircontent = separateStructure(pdb_dir,base_name)
	tmpdir = tmpdircontent[0]
	
	cres = getCentralRes(pdbfile)
	centroid = getCentroid(pdbfile)

	
	transfiles = []

	for file in tmpdircontent[1:][0]:
		pathfile = tmpdir+"/"+file
		res = getCentralRes(pathfile)
		if getChain(cres) == getChain(res):
			centrefile = pathfile
			transfiles.append(centrefile)
			continue
		else:
			rescentre = getCentroid(pathfile)
			dist = getDistance(centroid,rescentre)
			tfile = translateRes(dist, mult, pathfile)
			transfiles.append(tfile)

	outfile = os.path.splitext(pdbfile)[0]+"exploded.pdb"
	appendFiles(outfile, transfiles)

	cleanUp(tmpdir)


if __name__ == "__main__":

	args = args()
	pdbfile = args.file
	mult = args.mult
	explode(pdbfile, mult)


