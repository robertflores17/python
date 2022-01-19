import datetime
import os
import pandas as pd
import numpy as np

# TODO: Change the filename and the date
df = pd.read_csv("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\2022\\Jan '22\\All_Vulns_1-20-22.csv")
df['CVSSv3'] = df['CVSSv3'].fillna(0)
df['Published On'] = pd.to_datetime(df['Published On'], format='%m/%d/%y')
df['Modified On'] = pd.to_datetime(df['Modified On'])
critical = pd.to_datetime('12-20-2021')
severe = pd.to_datetime('11-20-2021')
moderate = pd.to_datetime('10-20-2021')

conditions = [
    (df['CVSSv3'] >= 7.5) & (df['Published On'] > critical),
    (df['CVSSv3'] >= 7.5) & (df['Published On'] <= critical),
    (df['CVSSv3'] >= 3.5) & (df['CVSSv3'] < 7.5) & (df['Published On'] > severe),
    (df['CVSSv3'] >= 3.5) & (df['CVSSv3'] < 7.5) & (df['Published On'] <= severe),
    (df['CVSSv3'] >= 0) & (df['CVSSv3'] < 3.5) & (df['Published On'] > moderate),
    (df['CVSSv3'] >= 0) & (df['CVSSv3'] < 3.5) & (df['Published On'] <= moderate)
]
values = ['Critical', 'Critical_Past_Due', 'Severe', 'Severe_Past_Due', 'Moderate', 'Moderate_Past_Due']
df['Kratos_Vuln_Severity'] = np.select(conditions, values)
df['Published On'] = df['Published On'].dt.date
df['Modified On'] = df['Modified On'].dt.date
df = df[['Kratos_Vuln_Severity', 'Title', 'CVSSv3', 'Risk', 'Published On', 'Modified On', 'Instances']]
#os.makedirs("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\2022\\Jan '22\\XLSX")
df.to_excel("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\2022\\Jan '22\\XLSX\\All_Vulns_1-20-22.xlsx", index=False)
