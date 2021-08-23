from pathlib import Path
import re
import pandas as pd


txt = Path('output.txt.html').read_text()
txt = txt.replace('&quot;', '"')

ss = re.search('\"posts\":\[(.+?),\"tags\":\[{\"id\":70,\"name\":\"hobby\"', txt).group(1)

#print(ss)

splitted = ss.split("},{")

#print(splitted)

for x in range(len(splitted)):
    print(x, "------------")
    print(splitted[x])
    print(x, "------------")

#df = pd.read_json(ss)

#print(df.to_string()) 
