# this file just contains the code on how to extract x random papers to train instead of using all 
# 2.9M papers based on the compute available 

import json 
import random 

input_file = 'arxiv.json'
output_file = 'arxiv_sample_500k.json'
sample_size = 500

required_keys = ['id', 'authors', 'title', 'categories', 'abstract']

reservoir = []


with open(input_file, 'r') as f: 

    for i, line in enumerate(f):

        paper = line.strip()

        if i < sample_size:

            reservoir.append(paper)

        else: 
            j = random.randint(0, i)
            if j < sample_size:
                reservoir[j] = paper

with open(output_file, 'w') as out:

    for paper in reservoir:

        paper = json.loads(paper)

        new_paper = {key : paper.get(key, None) for key in required_keys}

        new_paper = json.dumps(new_paper)

        out.write(new_paper + "\n")

print('Done creating sample file with 500 papers')