# This code is unnecessary but i just write this to create a file that has only one sample that helps me to understand the contents in the file of 
# json
import json 


input_path = 'arxiv_sample_500.json'

output_file = 'just_one_sample.json'

store = []
with open(input_path, 'r') as f: 

    for paper in f:

        store.append(paper)
        break 

with open(output_file, 'w') as out:

    for paper in store:
        out.write(paper)







