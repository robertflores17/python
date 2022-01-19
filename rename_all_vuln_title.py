#! python3

import os

old_name = r"C:\Users\robert.flores\Downloads\VulnerabilityListingExport.csv"
new_name = r"C:\Users\\robert.flores\\Documents\Vulns\Vulns\All Vulns\2022\Jan '22\All_Vulns_1-20-22.csv"

os.rename(old_name, new_name)