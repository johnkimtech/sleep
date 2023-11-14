import pandas as pd
import json

def read_json(file_path)->dict:
    with open(file_path, 'r') as f:
        data = json.loads(f.read())
        return data

def translate_cells(df, translation):
    for column, translation in translation.items():
        df[column] = df[column].map(translation)