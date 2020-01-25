import pandas as pd

"""
Need to be able to take census number and determine what zipcodes lie in it.
"""
def censusToZip(censusDF, censusNum, rows):
	zipNum = []

	for idx in range(rows):
		if censusNum == censusDF['TRACT'][idx]:
			zipNum.append(censusDF['ZIP'][idx])

	return zipNum

"""
Obtain the census num from a zipcode
"""
def zipToCensusNum(censusDF, zipNum, rows):
	censusNum = []

	for idx in range(rows):
		if zipNum == censusDF['ZIP'][idx]:
			censusNum.append(censusDF['TRACT'][idx])

	return censusNum

"""
Obtain gentrif percentage from a zipcode
"""
def zipToGentrif(censusDF, gentrificationDF, census_rows, zipcodes):
	averageGentrif = {}
	for zipcode in zipcodes:
		gentrifLevels = []
		#print(gentrifLevels)
		for censusNum in zipToCensusNum(censusDF, zipcode, census_rows):
			gentrifLevels.append(gentrificationDF.loc[censusNum]['Prob16_00v'])
		if gentrifLevels:
			averageGentrif[zipcode] = sum(gentrifLevels)/len(gentrifLevels)
	return averageGentrif

# Store/Analyze census data
zipToCensus_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/ZIP_TRACT_032016.xlsx'
zipToCensus = pd.read_excel(zipToCensus_file)
zipToCensus_shape = zipToCensus.shape
# Number of rows
zipToCensus_rows = zipToCensus_shape[0]

# Store/Analyze gentrification data
gentrificationCensusNum_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/gentrifData.xlsx'
gentrification = pd.read_excel(gentrificationCensusNum_file)
# Different census numbers
#gentrificationCensusNum = gentrification['FIPS']
gentrification.set_index("FIPS", inplace=True)

# Store/Analyze crime data
crime_file = '/Users/alexanderxiong/Documents/GitHub/datathon-2020/data/NIBRSPublicView.Jan1-Dec31-FINAL.xlsx'
crime = pd.read_excel(crime_file)
# Different zip codes from crime data
crimeZips = crime['ZIP Code']

print(zipToGentrif(zipToCensus, gentrification, zipToCensus_rows, crimeZips))


"""
Need to take the zipcodes and pull the proper metrics/distributions from crime data
"""