# trgn510_homework4
In this 4th week assignment, I create a program called ensg2hugo.py that takes a comma-delimited file as an argument and a column number as an input, and print a file where the Ensembl gene name has changed to a HUGO name.

## Installation & Usage
- To install, use `git clone https://github.com/tingmanz/trgn_homework4.git`
- A file named "ensg2hugo.py" that contains the script is necessary for the program. 
- The script is generated that with a gtf file named "Homo_sapiens.GRCh37.75.gtf". This file could be downloaded to our server. 
- There is a .csv for unit test in the repository we got, and we could use 
$ ./ensg2hugo.py -f 2 expres.anal.csv 
and we change the Ensembl gene names in column 2 to HUGO name with -f 2 option. The first column would be used if we don't specify the column number. The column number could be changed to wirk with our csv file with our option. 

## Known Issues
There will be some ensembl names which do not have a match in the dictionary. "Unknown" would be shown in the gene name column in the file.  

## Dependencies
- git 
- sys python package
- re python package
- csv python package
- pandas python package

## Contact
tingmanz@usc.edu

