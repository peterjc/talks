from Bio.PDB.mmtf import MMTFParser
# read structure from file
structure = MMTFParser.get_structure("PDB/4CUP.mmtf")
# read structure from PDB
structure = MMTFParser.get_structure_from_url("4CUP")