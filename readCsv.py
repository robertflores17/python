import pandas as pd
import numpy as np

# TODO: Change the filename and the date
df = pd.read_csv("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\Nov '21\\All_Vulns_11-5-21.csv")
df['CVSSv3'] = df['CVSSv3'].fillna(0)
df['Published On'] = pd.to_datetime(df['Published On'], format='%m/%d/%y')
critical = pd.to_datetime('10/5/2021')
severe = pd.to_datetime('9/5/2021')
moderate = pd.to_datetime('8/5/2021')

conditions = [
    (df['CVSSv3'] >= 7.5) & (df['Published On'] > critical),
    (df['CVSSv3'] >= 7.5) & (df['Published On'] <= critical),
    (df['CVSSv3'] >= 3.5) & (df['CVSSv3'] < 7.5) & (df['Published On'] > severe),
    (df['CVSSv3'] >= 3.5) & (df['CVSSv3'] < 7.5) & (df['Published On'] <= severe),
    (df['CVSSv3'] >= 0) & (df['CVSSv3'] < 3.5) & (df['Published On'] > moderate),
    (df['CVSSv3'] >= 0) & (df['CVSSv3'] < 3.5) & (df['Published On'] <= moderate)
]
values = ['Critical', 'Critical_Past_Due', 'Severe', 'Severe_Past_Due', 'Moderate', 'Moderate_Past_Due']
df['Severity & SLA'] = np.select(conditions, values)

df.to_excel("C:\\Users\\robert.flores\\Documents\\Vulns\\Vulns\\All Vulns\\Nov '21\\XLSX\\All_Vulns_11-5-21-b.xlsx")
