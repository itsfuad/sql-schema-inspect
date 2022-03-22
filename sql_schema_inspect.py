"""Extract SQLite CREATE TABLE statements into a schema overview."""

def analyze(text):
    import re
    tables={}
    for match in re.finditer(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([\w]+)\s*\((.*?)\)\s*;',text,re.I|re.S):
        columns=[]
        for segment in match.group(2).split(','):
            words=segment.strip().split()
            if len(words)>1 and words[0].upper() not in ('PRIMARY','FOREIGN','CHECK','CONSTRAINT','UNIQUE'):
                columns.append({'name':words[0],'type':words[1]})
        tables[match.group(1)]=columns
    return {'tables':tables,'count':len(tables)}
