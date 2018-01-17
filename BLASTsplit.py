#Final working version for writing multiple BLAST hits from one file, to multiple query-named files

with open('filename') as f:
    querylist=[]
    for line in f:
        if line.startswith('# Query'):
            querylist.append(line.split()[2])
for query in querylist:
    with open(query, 'w') as g:
        with open('filename') as f:
            for line in f:
                if line.startswith(query):
                    print(line)
                    g.write(line)
