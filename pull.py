# pulls several csv docs and pandas reads them and loads them into momory
#combines them into a single data frame and the saves that as a csv file to the hd for easy mainpulation

import pandas as pd

ok_01_dennis_baker_url = "https://drive.google.com/uc?id=11b9v60FwcKnhNC-Xj85Gb9jfsBdKdry1"
ok_01_kevin_hern_url = "https://drive.google.com/uc?id=15AxRWKNPShj-4WUSI6boppHFIGG5SxLL"
ok_02_brandon_wade_url = "https://drive.google.com/uc?id=1W3x0_psyoLZuZnahL3P3IfDBWwFJas01"
ok_03_frank_lucas_url = "https://drive.google.com/uc?id=1smBYR4oI3mYK38hoq8clsDDFCg_sLFOd"
ok_04_tom_cole_url = "https://drive.google.com/uc?id=1hdgvoSoZMuFcdFEgEiYZywDixmAbaKxG"
ok_05_madison_horn_url = "https://drive.google.com/uc?id=1VN8C15xH7etBKHuqsAxdGsBaZD76TXVB"
ok_05_stephanie_bice_url = "https://drive.google.com/uc?id=1hykdSP9A2YEmmGwjAuDaQuy1Z58XiWjz"

df_dennis_baker = pd.read_csv(ok_01_dennis_baker_url, low_memory=False)
df_kevin_hern = pd.read_csv(ok_01_kevin_hern_url, low_memory=False)
df_brandon_wade = pd.read_csv(ok_02_brandon_wade_url, low_memory=False)
df_frank_lucas = pd.read_csv(ok_03_frank_lucas_url, low_memory=False)
df_tom_cole = pd.read_csv(ok_04_tom_cole_url, low_memory=False)
df_madison_horn = pd.read_csv(ok_05_madison_horn_url, low_memory=False)
df_stephanie_bice = pd.read_csv(ok_05_stephanie_bice_url, low_memory=False)

df_combined_data = pd.concat([
    df_dennis_baker,
    df_kevin_hern,
    df_brandon_wade,
    df_frank_lucas,
    df_tom_cole,
    df_madison_horn,
    df_stephanie_bice
], ignore_index=True)

map_dict = {
    'HERN FOR CONGRESS': {'party': 'Republican', 'district': 'OK-01', 'candidate_name': 'Kevin Hern'},
    'BICE FOR CONGRESS': {'party': 'Republican', 'district': 'OK-05', 'candidate_name': 'Stephanie Bice'},
    'COLE FOR CONGRESS': {'party': 'Republican', 'district': 'OK-04', 'candidate_name': 'Tom Cole'},
    'OKLAHOMANS FOR MADISON': {'party': 'Republican', 'district': 'OK-02', 'candidate_name': 'Madison Horn'},
    'LUCAS FOR CONGRESS': {'party': 'Republican', 'district': 'OK-03', 'candidate_name': 'Frank Lucas'},
    'DENNIS BAKER FOR CONGRESS': {'party': 'Democratic', 'district': 'OK-01', 'candidate_name': 'Dennis Baker'},
    'OKLAHOMA FOR BRANDON': {'party': 'Democratic', 'district': 'OK-05', 'candidate_name': 'Brandon Wade'}
}

df_combined_data['party'] = df_combined_data['committee_name'].map(lambda x:map_dict.get(x, {}).get('party'))
df_combined_data['district'] = df_combined_data['committee_name'].map(lambda x:map_dict.get(x, {}).get('district'))
df_combined_data['candidate_name'] = df_combined_data['committee_name'].map(lambda x:map_dict.get(x, {}).get('candidate_name'))


df_combined_data.to_csv('combined_data_output.csv', index=False)

# this is a change 