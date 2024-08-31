import pandas as pd
import numpy as np


tech_nace_codes = {
    '6201', '6202', '6203', '6209', '2611', '2612', '2620', '2630', '5821', '5829', '6311', '6312', '7219'
}

df = pd.read_excel("data.xlsx")

tech_comp_indexes = []
for index, row in df.iterrows():
    codes = row['nace_codes']
    if isinstance(codes, str):
        lst = codes.split(',')
        for num in lst:
            if num in tech_nace_codes:
                tech_comp_indexes.append(index)
                break
    elif str(codes) in tech_nace_codes:
        tech_comp_indexes.append(index)

columns_to_normalize = [
    'Taxable turnover 2019', 'Taxable turnover 2020Q1',
    'Taxable turnover 2020Q2', 'Taxable turnover 2020Q3',
    'National taxes 2020Q3', 'Labour taxes 2020Q3',
    'Employee count 2020Q3', 'Debt'
]

norm_df = df.copy()

for col in columns_to_normalize:
    values = norm_df.loc[tech_comp_indexes, col].values.astype(float)
    normalized_values = (values - np.min(values)) / (np.max(values) - np.min(values))
    norm_df.loc[tech_comp_indexes, col] = normalized_values
    norm_df.loc[~norm_df.index.isin(tech_comp_indexes), col] = 0

norm_df['Overall_Score'] = norm_df[columns_to_normalize].sum(axis=1)
df['overall_score'] = norm_df['Overall_Score']
sorted_df = df.sort_values(by='overall_score', ascending=False)
top_300_df = sorted_df.head(300)
top_300_df.to_excel('result.xlsx', index=False)
