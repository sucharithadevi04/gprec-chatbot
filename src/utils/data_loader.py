import pandas as pd

def load_placement_data():
    try:
        data = pd.read_csv("data/placement_data.csv")
    except FileNotFoundError:
        data = None
    return data

def load_companies_and_branches():
    try:
        df_companies = pd.read_csv("data/placement_companies_2024.csv")
        df_branches = pd.read_csv("data/placement_branches_2024.csv")
    except FileNotFoundError:
        df_companies = None
        df_branches = None
    return df_companies, df_branches
