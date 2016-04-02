#!/usr/bin/python3.4

import argparse
import shutil
from Bio import Entrez
Entrez.email = "studentka_tnp@mail.ru"


parser = argparse.ArgumentParser(description="It's take 2 args: query, taxon"
                                             "Output: Asswsion, taxon, title")

parser.add_argument("query",
                    type=str,
                    help="Input your query for search")

parser.add_argument("taxon",
                    type=str,
                    nargs='?',
                    help='Input taxon for search')

args = parser.parse_args()
taxon = args.taxon
query = args.query

if args.taxon == None:
    term = query + " AND GSE[Entry Type] "
else:
    term = query + " AND GSE[Entry Type] AND " + taxon + '[Organism]'

handle = Entrez.esearch(db="gds", term=term)
record = Entrez.read(handle)

for i in record["IdList"]:
    result = Entrez.esummary(db='gds', id=i)
    search = Entrez.read(result)[0]
    print(search["Accession"], "\t", search["taxon"], "\t", search["title"])
