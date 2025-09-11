import pandas as pd
import spacy
from rapidfuzz import process

class PlacementChatbot:
    def __init__(self):
        # Load NLP model
        self.nlp = spacy.load("en_core_web_sm")
        self.df_companies = None
        self.df_branches = None
        
        # Load data
        self.load_data()
    
    def load_data(self):
        try:
            self.df_companies = pd.read_csv("data/placement_companies_2024.csv")
            self.df_branches = pd.read_csv("data/placement_branches_2024.csv")
            
            # Clean data
            if self.df_companies is not None:
                self.df_companies["Company"] = self.df_companies["Company"].str.strip()
            if self.df_branches is not None:
                self.df_branches["Branch"] = self.df_branches["Branch"].str.strip()
                
        except FileNotFoundError:
            self.df_companies = None
            self.df_branches = None
    
    def answer_question(self, query):
        if self.df_companies is None or self.df_branches is None:
            return "Placement CSV files not found."
        
        query_lower = query.lower()
        doc = self.nlp(query_lower)
        tokens = [token.text for token in doc if not token.is_stop]
        
        # Fuzzy match company
        company_list = [c.lower() for c in self.df_companies["Company"].tolist()]
        result_company = process.extractOne(query_lower, company_list, score_cutoff=60)
        company_match = None
        if result_company:
            idx = company_list.index(result_company[0])
            company_match = self.df_companies["Company"].iloc[idx]
        
        # Fuzzy match branch
        branch_list = [b.lower() for b in self.df_branches["Branch"].tolist()]
        result_branch = process.extractOne(query_lower, branch_list, score_cutoff=60)
        branch_match = None
        if result_branch:
            idx = branch_list.index(result_branch[0])
            branch_match = self.df_branches["Branch"].iloc[idx]
        
        # Package/Salary/CTC queries
        if any(word in tokens for word in ["package", "salary", "ctc"]):
            if company_match:
                salary = self.df_companies.loc[self.df_companies["Company"] == company_match, "Salary_LPA"].values[0]
                return f"The package offered by {company_match} is {salary} LPA."
            elif branch_match and ("average" in tokens or "avg" in tokens):
                return f"Average salary in {branch_match} is {self.df_branches.loc[self.df_branches['Branch'] == branch_match, 'Average_Salary_LPA'].values[0]} LPA."
            elif branch_match and ("highest" in tokens or "max" in tokens):
                return f"Highest salary in {branch_match} is {self.df_branches.loc[self.df_branches['Branch'] == branch_match, 'Highest_Salary_LPA'].values[0]} LPA."
            elif branch_match and ("lowest" in tokens or "min" in tokens):
                return f"Lowest salary in {branch_match} is {self.df_branches.loc[self.df_branches['Branch'] == branch_match, 'Lowest_Salary_LPA'].values[0]} LPA."
        
        # Highest package queries
        if "highest" in tokens or "max" in tokens:
            if company_match:
                return f"Highest salary at {company_match} is {self.df_companies.loc[self.df_companies['Company'] == company_match, 'Salary_LPA'].values[0]} LPA."
            elif branch_match:
                return f"Highest salary in {branch_match} is {self.df_branches.loc[self.df_branches['Branch'] == branch_match, 'Highest_Salary_LPA'].values[0]} LPA."
        
        # Average salary queries
        if "average" in tokens or "avg" in tokens:
            if branch_match:
                return f"Average salary in {branch_match} is {self.df_branches.loc[self.df_branches['Branch'] == branch_match, 'Average_Salary_LPA'].values[0]} LPA."
        
        # Lowest salary queries
        if "lowest" in tokens or "min" in tokens:
            if branch_match:
                return f"Lowest salary in {branch_match} is {self.df_branches.loc[self.df_branches['Branch'] == branch_match, 'Lowest_Salary_LPA'].values[0]} LPA."
        
        # Offers/placements queries
        if "offer" in tokens or "placed" in tokens or "placement" in tokens:
            if company_match:
                offers = self.df_companies.loc[self.df_companies["Company"] == company_match, "Number_of_Offers"].values[0]
                return f"{company_match} made {offers} offers."
            elif branch_match:
                row = self.df_branches.loc[self.df_branches["Branch"] == branch_match].iloc[0]
                return f"{branch_match} branch got {row['Offers']} offers and {row['Students_Placed']} students placed."
        
        # Total offers query
        if "total" in tokens and "offers" in tokens:
            total_offers = self.df_companies["Number_of_Offers"].sum()
            return f"Total offers across all companies: {total_offers}"
        
        return "Sorry, I could not find an exact match for your question."
