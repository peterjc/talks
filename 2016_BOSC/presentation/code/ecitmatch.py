from Bio import Entrez
citation_1 = {
      "journal_title": "proc natl acad sci u s a",
      "year": "1991", "volume": "88", "first_page": "3248",
      "author_name": "mann bj", "key": "citation_1"}
record = Entrez.ecitmatch(db="pubmed", bdata=[citation_1])
print(record.readline())
