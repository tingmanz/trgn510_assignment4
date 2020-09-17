#!/usr/bin/python

import sys
import re
import pandas as pd
import csv

if sys.argv[1].startswith("-f"):
	col_number = int(sys.argv[1][2]) - 1
	input_file = sys.argv[2]
else:
	col_number = 0
	input_file = sys.argv[1]

name_dict = {}
with open("Homo_sapiens.GRCh37.75.gtf", "r") as f:
	for line in f:
		if not line.startswith('#'):
			if line.split("\t")[2] == "gene":
				gene_id = re.findall(r'ENSG[0-9]{11}', line)[0]
				gene_name = line.split("\t")[8].split("\"")[3]
				name_dict[gene_id] = gene_name

expression = pd.read_csv(input_file, quoting=csv.QUOTE_NONE)
hugo_list = []
for i in range(len(expression)):
	gene_id = expression.iloc[i, col_number][1:16]
	if gene_id in name_dict.keys():
		hugo_list.append('"' + name_dict[gene_id] + '"')
	else:
		hugo_list.append("\"Unknown\"")
	
expression.iloc[:, col_number] = hugo_list
print(expression.to_csv(quoting=csv.QUOTE_NONE,index=False,line_terminator='\n'))
