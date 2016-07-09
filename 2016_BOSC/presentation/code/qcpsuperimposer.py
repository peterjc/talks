from Bio.PDB.QCPSuperimposer import QCPSuperimposer
sup = QCPSuperimposer()
# set the coords
# y will be rotated and translated on x
sup.set(x, y)
# do the lsq fit
sup.run()
# get the rmsd
rms = sup.get_rms()