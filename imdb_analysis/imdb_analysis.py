import pandas as pd
import numpy as np
import json

data = '/Users/tony/PycharmProjects/puma/imdb_analysis/data_v1.json'

with open(data, 'r') as f:
    json_object = json.load(f)

#print(json_object)

print(json_object[1]['genre'][0])

for i in range(len(json_object)):
    print(json_object[i]['genre'])