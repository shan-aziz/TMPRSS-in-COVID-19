
from modeller import *
env= environ()
aln= alignment(env)
mdl = model(env, file='3R1I')
aln.append_model(mdl,align_codes='3R1I',atom_files='3R1I.pdb')
aln.append(file='ardh_gene.ali',align_codes='ardh_gene')
aln.align2d()
aln.write(file='PQ.ali',alignment_format='PIR')
aln.write(file='PQ.pap',alignment_format='PAP')
