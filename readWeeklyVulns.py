import pandas as pd
import numpy as np
import openpyxl

# TODO: Change the filename and the date
df = pd.read_csv("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\2022\\Jan '22\\Weekly_012122.csv")
df['Vulnerable Since'] = pd.to_datetime(df['Vulnerable Since'], format='%Y/%m/%d')
df['Vulnerability Published Date'] = pd.to_datetime(df['Vulnerability Published Date'], format='%Y/%m/%d')
critical = pd.to_datetime('2021-12-21')
severe = pd.to_datetime('2021-11-21')
moderate = pd.to_datetime('2021-10-21')

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
df['Vulnerable Since'] = df['Vulnerable Since'].dt.date
df['Vulnerability Published Date'] = df['Vulnerability Published Date'].dt.date
df = df[['Kratos_Vuln_Severity',
        'Vulnerable Since',
        'Vulnerability Title',
        'Vulnerability Solution',
        'Vulnerability Proof',
        'Asset Names',
        'Asset IP Address',
        'Asset OS Name',
        'Asset OS Version',
        'Asset Location',
        'Asset Owner',
        'Asset Risk Score',
        'Exploit Count',
        'Service Port',
        'Service Protocol',
        'Site Name',
        'Vulnerability Age',
        'Vulnerability CVSSv3 Score',
        'Vulnerability Published Date']]

df.to_excel("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\2022\\Jan '22\\XLSX\\Weekly_012122.xlsx", index=False)