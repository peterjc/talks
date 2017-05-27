from __future__ import print_function

from Bio import ExPASy, SwissProt

# 'PDOC00965', 'PDOC00022', 'PDOC50853', Chalcone synthases from Orchid

ids = ['PDOC00965', 'PDOC00022', 'PDOC50853']

for id in ids:
    handle = ExPASy.get_sprot_raw(id)
    record = SwissProt.read(handle)
    # Print description
    print("description: %s" % record.description)
    for ref in record.references:
        # Print Author and Title references
        print("authors: %s" % ref.authors)
        print("title: %s" % ref.title)
