import sys
import subprocess
	
def pdbsymm(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbsymm',toolarg])
def pdbselect(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbselect',toolarg])
def pdbhadd(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbhadd',toolarg])
def pdbflip(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbflip',toolarg])
def pdbcter(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbcter',toolarg])

def chaincontacts(toolarg):
	toolarg = ['/home/tom/phd/bioptools/src/chaincontacts'] + toolarg
	return subprocess.check_output(toolarg)


def pdbgetresidues(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbgetresidues',toolarg])
def pdbfindresrange(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbfindresrange',toolarg])
def pdbtranslate(toolarg):
	#toolarg should be in format ["x", "y", "z", "infile", "outfile"]
	#if outfile blank, will return to STDOUT
	if len(toolarg) == 4:
		return subprocess.call(['/home/tom/phd/bioptools/src/pdbtranslate',"-x ",str(toolarg[0]),"-y ",str(toolarg[1]),"-z ",str(toolarg[2]),toolarg[3]])
	elif len(toolarg) == 5:
		return subprocess.call(['/home/tom/phd/bioptools/src/pdbtranslate',"-x ",str(toolarg[0]),"-y ",str(toolarg[1]),"-z ",str(toolarg[2]),toolarg[3],toolarg[4]])
	else:
		print "Error in pdbtranslate: wrong number of arguments"
		sys.exit()
def setpdbnumbering(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/setpdbnumbering',toolarg])
def pdbtorsions(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbtorsions',toolarg])
def pdbrenum(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbrenum',toolarg])
def pdbrotate(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbrotate',toolarg])
def pdbgetzone(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbgetzone',toolarg])
def pdbfit(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbfit',toolarg])
def pdbhstrip(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbhstrip',toolarg])
def pdbaddhet(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbaddhet',toolarg])
def pdbsolv(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbsolv',toolarg])
def pdbpatchbval(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbpatchbval',toolarg])
def pdbpatchnumbering(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbpatchnumbering',toolarg])
def pdbsphere(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbsphere',toolarg])
def pdb2xyz(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdb2xyz',toolarg])
def pdbsecstr(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbsecstr',toolarg])
def scorecons(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/scorecons',toolarg])
def pdbhbond(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbhbond',toolarg])
def pdb2pir(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdb2pir',toolarg])
def pdbatomcount(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbatomcount',toolarg])
def pdbatoms(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbatoms',toolarg])
def pdbmakepatch(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbmakepatch',toolarg])
def pdborder(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdborder',toolarg])
def pdb2ms(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdb2ms',toolarg])
def pdbcalcrms(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbcalcrms',toolarg])
def pdbconect(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbconect',toolarg])
def pdbheader(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbheader',toolarg])
def pdborigin(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdborigin',toolarg])
def pdbdummystrip(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbdummystrip',toolarg])
def pdbsumbval(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbsumbval',toolarg])
def pdbcount(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbcount',toolarg])
def sixft(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/sixft',toolarg])
def pdb2pdbml(toolarg):
	return subprocess.call(['/home/tom/phd/bioptools/src/pdb2pdbml',toolarg])
def pdbatomsel(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbatomsel',toolarg])
def pdbavbr(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbavbr',toolarg])
def pdbcheckforres(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbcheckforres',toolarg])
def pdbml2pdb(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbml2pdb',toolarg])
def pdbchain(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbchain',toolarg])
def pdblistss(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdblistss',toolarg])
def naccess2bval(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/naccess2bval',toolarg])
def distmat(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/distmat',toolarg])
def pdbhetstrip(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbhetstrip',toolarg])
def pdbsplitchains(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbsplitchains',toolarg])
def pdbcentralres(toolarg):
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbcentralres',toolarg])
def pdbgetchain(toolarg):
	#toolarg should be in form ["chain","file"] e.g. toolarg = ["A", "example.pdb"]
	return subprocess.check_output(['/home/tom/phd/bioptools/src/pdbgetchain',toolarg[0],toolarg[1]])
