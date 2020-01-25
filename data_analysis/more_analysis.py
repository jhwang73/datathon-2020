import pandas as pd
import csv

zip_gentrif_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/zipToGentrif.csv'
zip_gentrif = pd.read_csv(zip_gentrif_file)
# Number of rows
zip_gentrif_rows = zip_gentrif.shape[0]

gentLevel_dict = {0:[], 1:[], 2:[], 3:[]}
for idx in range(zip_gentrif_rows):
	if 0.0 <= zip_gentrif['Prob16_00v'][idx] < 25.0:
		gentLevel_dict[0].append(zip_gentrif['ZIP'][idx])
	elif 25.0 <= zip_gentrif['Prob16_00v'][idx] < 50.0:
		gentLevel_dict[1].append(zip_gentrif['ZIP'][idx])
	elif 50.0 <= zip_gentrif['Prob16_00v'][idx] < 75.0:
		gentLevel_dict[2].append(zip_gentrif['ZIP'][idx])
	else:
		gentLevel_dict[3].append(zip_gentrif['ZIP'][idx])

# with open('zipToGentrifClassif.csv', 'w') as f:
# 	for key in gentLevel_dict.keys():
# 		f.write("%s,%s\n"%(key, gentLevel_dict[key]))

zip_pop_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/ZipcodeToCrimeCountBy100.csv'
zip_pop = pd.read_csv(zip_pop_file)
zip_pop.set_index("zipcode", inplace=True)
print(zip_pop)
crime_dict = {0:0, 1:0, 2:0, 3:0}

for key,val in gentLevel_dict.items():
	crimeCount = 0
	validCount = 0
	for zc in val:
		if zc in zip_pop.index.values:
			crimeCount += zip_pop.loc[zc].tolist()[1]
			validCount += 1
	crime_dict[key] = round(crimeCount/validCount, 2)

with open('gentLevelToPerCapitaDrime.csv', 'w') as f:
	for key in crime_dict.keys():
		f.write("%s,%s\n"%(key, crime_dict[key]))

charges = ["Aggravated Assault", "All other larceny", "All other offenses", "Animal Cruelty", "Arson", "Assisting or promoting prostitution", 
	"Bad checks", "Betting/wagering", "Bribery", "Burglary, Breaking and Entering", "Counterfeiting, forgery", "Credit Card, ATM fraud", "Curfew, loitering, vagrancy violations",
	"Destruction, damage, vandalism", "Disorderly conduct", "Driving under the influence", "Drug equipment violations", "Drug, narcotic violations", "Drunkeness", "Embezzlement", "Extortion, Blackmail", "False pretenses, swindle", "Family offenses, no violence",
	"Forcible fondling", "Forcible rape", "Forcible sodomy", "From coin-operated machine or device", "Gambling equipment violations", "Hacking/Computer Invasion", "Human Trafficking/Commercial Sex Act", "Human Trafficking/Involuntary Servitude",
	"Identity Theft", "Impersonation", "Intimidation", "Kidnapping, abduction", "Liquor law violations", "Motor vehicle theft", "Murder, non-negligent", "Negligent Manslaughter", "Peeping tom", "Pocket-picking", "Pornographs, obscene material",
	"Promoting gambling", "Prostitution", "Purse-snatching", "Robbery", "Runaway", "Shoplifting", "Simple assault", "Statutory rape", "Stolen property offenses", "Theft from building",
	"Theft from motor vehicle", " Theft of motor vehicle parts or accessory", "Trespass of real property", "Weapon law violations", "Welfare fraud", "Wire fraud"]

crime_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/NIBRSPublicView.Jan1-Dec31-FINAL.xlsx'
crime = pd.read_excel(crime_file)

comp_charges = []
for charge in crime['NIBRSDescription']:
	if charge not in comp_charges:
		comp_charges.append(charge)

with open('differentCrimes.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(comp_charges)

# for key,val in gentLevel_dict.items():
# 	crime 
# 	popCount = 0
# 	for zc in val:
# 		popCount += zip_pop.loc[zc]['PopCount']

# 	crimecategory_avgcountpercapita = {}
# 	for category in crime_categories:
# 		for zc in val:
# 			category_crime_count += zip_crime.loc[zc]['CrimeCount']['auto']
# 		crimecategory_avgcountpercapita[category] = category_crime_count / popCount

