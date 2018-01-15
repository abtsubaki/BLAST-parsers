#final working script for filtering BLAST tabular data by alignment length, identity and e value

bad_words = ['#']

with open('filename') as oldfile, open('filenametemp', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

#import file with headers

import pandas as pd
data = pd.read_table('filenametemp', sep='\t', header=None)
data.columns = ["query acc.", "subject acc.", "evalue", "% identity", "mismatches", "gap opens", "q. start", "q. end", "s. start", "s. end", "alignment length"]
data = data.set_index('query acc.')

#filter by alignment length of 100bp and identity of 96% and sort by evalue
answer = data[(data['alignment length'] >= 100) & (data['% identity'] >= 96)].sort_values('evalue')

#write to output file
answer.to_csv('outputfile', sep='\t')
