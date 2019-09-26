"""

NYCdeaths.py

New York City Leading Causes of Death

https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/data

"""

import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.
import datetime
import urllib.request
import io


welcome = "Hi! This database contains leading causes of death by sex and ethnicity in New York City in 2007-2014."

Ethnicity = [
"Non-Hispanic White",
"Non-Hispanic Black",
"Hispanic",
"Asian and Pacific Islander",
"Not Stated/Unknown",
"Other Race/ Ethnicity"]

url ="https://raw.githubusercontent.com/jhjhjhsu/death/master/New_York_City_Leading_Causes_of_Death.csv"


#user selections: year, sex, ethnicity

print(welcome)
print()
year = input("Which year would you like to look up from 2007-2014? ")
year = str(year)
sex = input ("Which sex would you like to look up? (1=Male, 2= Female) ")
if sex == "1":
    sex = "Male"
elif sex == "2":
    sex = "Female"
else:
    print (error) #need edits
print()
print (*Ethnicity, sep = "\n")
print()
ethnicity = input("Which ethnicity would you like to look up? ")



#access data with selected year

try:
    fileFromUrl = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error, file = sys.stderr)
    sys.exit(1)

sequenceOfBytes = fileFromUrl.read() #Read whole file into one big sequenceOfBytes.
fileFromUrl.close()

try:
    s = sequenceOfBytes.decode("utf-8")    #s is a string, decoding
except UnicodeError as error:
    print(error, file = sys.stderr)
    sys.exit(1)

fileFromString = io.StringIO(s)
lines = csv.reader(fileFromString)   #or lines = csv.reader(s.splitlines())
SelectedYear = [line for line in lines if line[0] == year] #select year of choice
fileFromString.close()

#filter data by sex and ethnicity
FilteredList = []
for x in SelectedYear:
   if SelectedYear[2] == sex and SelectedYear[3] == ethnicity:
        FilteredList.append(x)
FilteredList.sort(key = FilteredList[4])
        

#print leading causes of death
#need to print header
print (f"In {year}, the leading causes of death for {ethnicity} {sex} in New York City are:")
for FilteredList in range (11):
    print (FilteredList[2], FilteredList[4])


sys.exit(0)
