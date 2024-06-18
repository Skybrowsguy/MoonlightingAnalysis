import pandas as pd
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%d %B %Y")

def find_overlap(range1_start, range1_end, range2_start, range2_end):
    # Find the latest start date
    latest_start = max(range1_start, range2_start)
    # Find the earliest end date
    earliest_end = min(range1_end, range2_end)
    
    # Calculate the overlap
    if latest_start <= earliest_end:
        overlap_days = (earliest_end - latest_start).days + 1  # Including both start and end date
        return overlap_days, latest_start, earliest_end
    else:
        return 0, None, None

def find_all_overlaps(df):
    overlaps = []
    n = len(df)
    for i in range(n):
        for j in range(i + 1, n):
            company1 = df.iloc[i]['Company']
            company2 = df.iloc[j]['Company']
            range1_start = df.iloc[i]['DOJ']
            range1_end = df.iloc[i]['DOR']
            range2_start = df.iloc[j]['DOJ']
            range2_end = df.iloc[j]['DOR']
            overlap_days, overlap_start, overlap_end = find_overlap(range1_start, range1_end, range2_start, range2_end)
            if overlap_days > 0:
                overlaps.append((company1, company2, overlap_days, overlap_start, overlap_end))
    return overlaps

# Read the Excel file
file_path = '<file path>'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Convert date columns to datetime
df['DOJ'] = pd.to_datetime(df['DOJ'], format='%d %B %Y')
df['DOR'] = pd.to_datetime(df['DOR'], format='%d %B %Y')

# Find all overlaps
overlaps = find_all_overlaps(df)

# Print the overlaps
for company1, company2, overlap_days, overlap_start, overlap_end in overlaps:
    print(f"Overlap between {company1} and {company2} is from {overlap_start.strftime('%d %B %Y')} to {overlap_end.strftime('%d %B %Y')} with a total of {overlap_days} days.")
