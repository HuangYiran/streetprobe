from self_defined_function import load_json_to_pd, load_jsonlist_to_pd

import pandas as pd
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help = 'JSON file name')
parser.add_argument('output', help = 'output file name, ended with .pkl. we save the data as pkl')

def main():
    args = parser.parse_args()
    df = transform(args.file)
    df.to_pickle(args.out)

def transform(file):
    """
    parameters:
    ____________
    file: type of string
        the filename of the data
    
    returns:
    out: type of DataFrame
        return DataFrame transformed from JSON data.
    """
    with open(file) as f:
        load_dict = json.load(f)
    out = []
    for li in load_dict:
        out.append(load_json_to_pd(li))
    df = pd.concat(out, axis = 0)
    return df

if __name__ == '__main__':
    main()