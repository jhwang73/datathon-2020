zip_gentrif_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/zipToGentrif.csv'
zip_gentrif = pd.read_csv(zip_gentrif_file)
# Number of rows
zip_gentrif_rows = zip_gentrif.shape[0]

gentLevel_dict = {0:[], 1:[], 2:[], 3:[]}
for idx in range(zip_gentrif_rows):
	if 0.0 <= zip_gentrif['Prob16_00v'][idx] < 25.0:
		gentLevel_dict[0].append(zip_gentrif['ZIP'][idx])
	else if 25.0 <= zip_gentrif['Prob16_00v'][idx] < 50.0:
		gentLevel_dict[1].append(zip_gentrif['ZIP'][idx])
	else if 50.0 <= zip_gentrif['Prob16_00v'][idx] < 75.0:
		gentLevel_dict[2].append(zip_gentrif['ZIP'][idx])
	else:
		gentLevel_dict[3].append(zip_gentrif['ZIP'][idx])

