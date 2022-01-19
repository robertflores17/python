import os
import pandas as pd
import numpy as np

# TODO: Change the filename and the date
df = pd.read_csv("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\Projects\\2022\\Jan '22\\Project_Sites_Vulns_012022.csv")
df['Vulnerable Since'] = pd.to_datetime(df['Vulnerable Since'], format='%Y/%m/%d')
df['Vulnerability Published Date'] = pd.to_datetime(df['Vulnerability Published Date'], format='%Y/%m/%d')
critical = pd.to_datetime('2021-12-20')
severe = pd.to_datetime('2021-11-20')
moderate = pd.to_datetime('2021-10-20')

conditions = [
    (df['Vulnerability CVSSv3 Score'] >= 7.5) & (df['Vulnerable Since'] > critical),
    (df['Vulnerability CVSSv3 Score'] >= 7.5) & (df['Vulnerable Since'] <= critical),
    (df['Vulnerability CVSSv3 Score'] >= 3.5) & (df['Vulnerability CVSSv3 Score'] < 7.5) & (df['Vulnerable Since'] > severe),
    (df['Vulnerability CVSSv3 Score'] >= 3.5) & (df['Vulnerability CVSSv3 Score'] < 7.5) & (df['Vulnerable Since'] <= severe),
    (df['Vulnerability CVSSv3 Score'] >= 0) & (df['Vulnerability CVSSv3 Score'] < 3.5) & (df['Vulnerable Since'] > moderate),
    (df['Vulnerability CVSSv3 Score'] >= 0) & (df['Vulnerability CVSSv3 Score'] < 3.5) & (df['Vulnerable Since'] <= moderate)
]
values = ['Critical', 'Critical_Past_Due', 'Severe', 'Severe_Past_Due', 'Moderate', 'Moderate_Past_Due']
df['Kratos_Vuln_Severity'] = np.select(conditions, values)

ls = [
    (df["Asset Location"].str.contains('Roseville')),
    (df["Asset Location"].str.contains('Sacramento')),
    (df["Asset Location"].str.contains('Dallastown')),
    (df["Asset Location"].str.contains('Orlando')),
    (df["Asset Location"].str.contains("Chantilly - SI"))
]
asset_group = ['Roseville', 'Sacramento', 'Dallastown', 'Orlando', 'Chantilly - SI']
df['Asset Group'] = np.select(ls, asset_group)
df['Vulnerable Since'] = df['Vulnerable Since'].dt.date
df['Vulnerability Published Date'] = df['Vulnerability Published Date'].dt.date
df = df[['Kratos_Vuln_Severity',
         'Asset Group',
         'Vulnerable Since',
         'Vulnerability Title',
         'Vulnerability Solution',
         'Vulnerability Proof',
         'Asset Names',
         'Asset IP Address',
         'Asset OS Name',
         'Asset OS Version',
         'Asset Risk Score',
         'Service Port',
         'Service Protocol',
         'Vulnerability Age',
         'Vulnerability CVSSv3 Score',
         'Vulnerability Published Date']]

#os.makedirs("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\Projects\\2022\\Jan '22\\XLSX")
# TODO: Change the filename
df.to_excel("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\Projects\\2022\\Jan '22\\XLSX\\Project_Sites_Vulns_012022.xlsx", index=False)