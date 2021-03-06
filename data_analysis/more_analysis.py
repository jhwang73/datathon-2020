import pandas as pd
import csv

zip_gentrif_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/zipToGentrif.csv'
zip_gentrif = pd.read_csv(zip_gentrif_file)
# Number of rows
zip_gentrif_rows = zip_gentrif.shape[0]

gentLevel_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
for idx in range(zip_gentrif_rows):
	if 0.0 == zip_gentrif['Prob16_00v'][idx]:
		gentLevel_dict[0].append(zip_gentrif['ZIP'][idx])
	elif 0.0 < zip_gentrif['Prob16_00v'][idx] < 25.0:
		gentLevel_dict[1].append(zip_gentrif['ZIP'][idx])
	elif 25.0 <= zip_gentrif['Prob16_00v'][idx] < 50.0:
		gentLevel_dict[2].append(zip_gentrif['ZIP'][idx])
	elif 50.0 <= zip_gentrif['Prob16_00v'][idx] < 75.0:
		gentLevel_dict[3].append(zip_gentrif['ZIP'][idx])
	else:
		gentLevel_dict[4].append(zip_gentrif['ZIP'][idx])

with open('zipToGentrifClassif.csv', 'w') as f:
	for key in gentLevel_dict.keys():
		f.write("%s,%s\n"%(key, gentLevel_dict[key]))

zc_total_count_plus = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/ZipcodeToCrimeCount.csv'
zc_total_count = pd.read_csv(zc_total_count_plus)
zc_total_count.set_index("ZIP", inplace=True)
print(zc_total_count)


pop_raw = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/population_zip_harris.csv'
pop = pd.read_csv(pop_raw)
pop.set_index("zip_code", inplace=True)

zc_cat_raw = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/sumCrimeCountByCategorizedCrime_Zipcode.csv'
zc_cat = pd.read_csv(zc_cat_raw)
zc_cat.set_index("zipcode", inplace=True)


zip_pop_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/ZipcodeToCrimeCountBy100.csv'
zip_pop = pd.read_csv(zip_pop_file)
zip_pop.set_index("zipcode", inplace=True)


# for grange, zcs in gentLevel_dict.items():
# 	crime_dict = {0:0, 1:0, 2:0, 3:0, 4:0}
# 	pop_count = 0
# 	total_crime_count = 0
# 	valid_count = 0
# 	for zc in zcs:
# 		if (zc in zc_total_count.index.values):
# 			total_crime_count += zc_total_count.loc[zc].tolist()[0]
			
# 			pop_count += pop.loc[zc]["y-2016"]

# 			valid_count += 1
# 	crime_dict[grange] = round(total_crime_count / (valid_count * pop_count), 2)


# 	file_name = str(grange) + "category.csv"
# 	with open(file_name, 'w') as f:
# 	for key in crime_dict.keys():
# 		f.write("%s,%s\n"%(key, crime_dict[key]))


# for grange,zcs in gentLevel_dict.items():
# 	popCount = 0
# 	for zc in val:
# 		popCount += zip_pop.loc[zc]['PopCount']

# 	crimecategory_avgcountpercapita = {}
# 	for category in crime_categories:
# 		for zc in val:
# 			category_crime_count += zip_crime.loc[zc]['CrimeCount']['auto']
# 		crimecategory_avgcountpercapita[category] = category_crime_count / popCount





zip_pop_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/ZipcodeToCrimeCountBy100.csv'
zip_pop = pd.read_csv(zip_pop_file)
zip_pop.set_index("zipcode", inplace=True)
crime_dict = {0:0, 1:0, 2:0, 3:0, 4:0}

for grange, zcs in gentLevel_dict.items():
	pop_count = 0
	total_crime_count = 0
	valid_count = 0
	for zc in zcs:
		if (zc in zc_total_count.index.values):
			total_crime_count += zc_total_count.loc[zc].tolist()[0]
			
			pop_count += pop.loc[zc]["y-2016"]

			valid_count += 1
	crime_dict[grange] = round((total_crime_count * 1000) / (valid_count * pop_count), 2)

# for key,val in gentLevel_dict.items():
# 	crimeCount = 0
# 	validCount = 0
# 	for zc in val:
# 		if zc in zip_pop.index.values:
# 			crimeCount += zip_pop.loc[zc].tolist()[1]
# 			validCount += 1
# 	crime_dict[key] = round(crimeCount/validCount, 2)

with open('gentLevelToPerCapitaDrime.csv', 'w') as f:
	for key in crime_dict.keys():
		f.write("%s,%s\n"%(key, crime_dict[key]))





# crime_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/NIBRSPublicView.Jan1-Dec31-FINAL.xlsx'
# crime = pd.read_excel(crime_file)

# comp_charges = []
# for charge in crime['NIBRSDescription']:
# 	if charge not in comp_charges:
# 		comp_charges.append(charge)

# with open('differentCrimes.csv', 'w', newline='') as myfile:
# 	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# 	wr.writerow(comp_charges)

