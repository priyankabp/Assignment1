# importing numpy array
import numpy as np

# importing pandas
import pandas as pd

# list of columns to read from the USCereals.csv file
colnames = ['cereals', 'mfr', 'calories', 'protein', 'fat', 'sodium', 'fibre', 'carbo', 'sugars', 'shelf', 'potassium']

# reading the specific columns given in 'colnames' list from the csv file using pandas
data = pd.read_csv('USCereals.csv', usecols=colnames)
# printing all data in structured format
#print(data)

# read cereals names from the dataset
cerealsTitle = data.cereals.tolist()
# storing the list of cereals titles in 'np_cerealsTitle' numpy aarray
np_cerealsTitle = np.array(cerealsTitle)

# read cereals calories from the dataset
cerealsCalories = data.calories.tolist()
# storing the list of cereals calories content in 'np_cerealsCalories' numpy aarray
np_cerealsCalories = np.array(cerealsCalories)

# read cereals protein from the dataset
cerealsProtein = data.protein.tolist()
# storing the list of cereals protein content in 'np_cerealsProtein' numpy aarray
np_cerealsProtein = np.array(cerealsProtein)

# read cereals fat from the dataset
cerealsFat = data.fat.tolist()
# storing the list of cereals fat content in 'np_cerealsFat' numpy aarray
np_cerealsFat = np.array(cerealsFat)

# read cereals sodium from the dataset
cerealsSodium = data.sodium.tolist()
# storing the list of cereals sodium content in 'np_cerealsSodium_mg' numpy aarray because it vslue is in milligrams
np_cerealsSodium_mg = np.array(cerealsSodium)

# read cereals fibre from the dataset
cerealsFibre = data.fibre.tolist()
# storing the list of cereals fibre content in 'np_cerealsFibre' numpy aarray
np_cerealsFibre = np.array(cerealsFibre)

# read cereals carbo from the dataset
cerealsCarbo = data.carbo.tolist()
# storing the list of cereals carbo content in 'np_cerealsCarbo' numpy aarray
np_cerealsCarbo = np.array(cerealsCarbo)

# read cereals sugar from the dataset
cerealsSugar = data.sugars.tolist()
# storing the list of cereals sugar content in 'np_cerealsSugar' numpy aarray
np_cerealsSugar = np.array(cerealsSugar)

# read cereals shelf from the dataset
cerealsShelf = data.shelf.tolist()
# storing the list of cereals shelf content in 'np_cerealsShelf' numpy aarray
np_cerealsShelf = np.array(cerealsShelf)

# read cereals potassium from the dataset
cerealsPotassium = data.potassium.tolist()
# storing the list of cereals potassium content in 'np_cerealsPotassium' numpy aarray
np_cerealsPotassium = np.array(cerealsPotassium)

# Metric 1 - Total calories per serving calculated using carbo,fats,proteins
# According to Science
# Fat:	1 gram = 9 Calories
# Protein:	1 gram = 4 Calories
# Carbohydrates: 	1 gram = 4 Calories

# Converting fats in grams to calories
np_cerealsFat_cal = np_cerealsFat * 9
# Converting proteins in grams to calories
np_cerealsProtein_cal = np_cerealsProtein * 4
# Converting carbohydrates in grams to calories
np_cerealsCarbo_cal = np_cerealsCarbo * 4

# Calculating the total calories per serving using fat, carbo and proteins
totalCaloriesPerServing = np_cerealsFat_cal + np_cerealsProtein_cal + np_cerealsCarbo_cal

# formating lists of string and vlues to print in tabular format
fmt = '{:<10}{:<1}{:<40}{:<1}{:<25}{:<1}'

# goto new line
print('\n\n')
print('Metric 1           : Total calories per serving calculated using carbohydrates,fats,proteins')
print('According to Science')
print('Fat                : 1 gram = 9 Calories')
print('Protein            : 1 gram = 4 Calories')
print('Carbohydrates      : 1 gram = 4 Calories')
print('Formula            : Total Calories Per Serving = Fats(in calories) + Proteins(in calories) + Carbohydrates(in calories)')
print('Reference document : https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwi1is_Kk7HUAhWBcz4KHTZ4DgkQFggqMAE&url=http%3A%2F%2Fwww2.bakersfieldcollege.edu%2Flcarter%2FAssignments%2FSample%2520Food%2520Label%2520Calculations.doc&usg=AFQjCNFkBZwgyobarHrempezQD2-zs4y4A&sig2=y3GVaFN8VKhrcHnhgwi1Lg')
print('The following table shows the "Total Calories per Serving" calculated using carbohydrates,proteins and fats.')
print('\n')
# Column names
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
print(fmt.format('Serial.No','|',' Cereal Name','|','Total Calories Per Serving','|'))
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
# Using 'forloop' to iterate over the list of cereals names and their corresponding total calories per serving
# calculated using fat,carbo and proteins.
for i, (cerealName, totalCalories) in enumerate(zip(np_cerealsTitle, totalCaloriesPerServing)):
    print(fmt.format(i, '|', ' '+ cerealName, '|', totalCalories, ' |'))
    print(fmt.format('----------', '|', '----------------------------------------', '|', '--------------------------',
                     '|'))

# Metric 2 - % Calories from fat
# We have fat calculated in calories per gram in 'np_cerealsFat_cal'
# We have total calories per serving in 'totalCaloriesPerServing'
percentageCaloriesFromFat = np_cerealsFat_cal / totalCaloriesPerServing * 100
print('\n')
# Column names
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
print(fmt.format('Serial.No','|',' Cereal Name','|','% Calories from Fat',' |'))
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
# Using 'forloop' to iterate over the list of cereals names and their corresponding total calories per serving
# calculated using fat,carbo and proteins.
for i, (cerealName, perCaloriesFromFat) in enumerate(zip(np_cerealsTitle, percentageCaloriesFromFat)):
    print(fmt.format(i, '|', ' '+ cerealName, '|', perCaloriesFromFat, ' |'))
    print(fmt.format('----------', '|', '----------------------------------------', '|', '--------------------------',
                     '|'))

# Metric 3 - % Calories from protein
# We have proteins calculated in calories per gram in 'np_cerealsProtein_cal'
# We have total calories per serving in 'totalCaloriesPerServing'
percentageCaloriesFromProtein = np_cerealsProtein_cal / totalCaloriesPerServing * 100
print('\n')
# Column names
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
print(fmt.format('Serial.No','|',' Cereal Name','|','% Calories from Protein',' |'))
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
# Using 'forloop' to iterate over the list of cereals names and their corresponding total calories per serving
# calculated using fat,carbo and proteins.
for i, (cerealName, perCaloriesFromProtein) in enumerate(zip(np_cerealsTitle, percentageCaloriesFromProtein)):
    print(fmt.format(i, '|', ' '+ cerealName, '|', perCaloriesFromProtein, ' |'))
    print(fmt.format('----------', '|', '----------------------------------------', '|', '--------------------------',
                     '|'))

# Metric 4 - % Calories from carbo
# We have carbohydrates calculated in calories per gram in 'np_cerealsCarbo_cal'
# We have total calories per serving in 'totalCaloriesPerServing'
percentageCaloriesFromCarbo = np_cerealsCarbo_cal / totalCaloriesPerServing * 100
print('\n')
# Column names
print(fmt.format('----------','|','----------------------------------------','|','------------------------------','|'))
print(fmt.format('Serial.No','|',' Cereal Name','|','% Calories from Carbohydrates',' |'))
print(fmt.format('----------','|','----------------------------------------','|','------------------------------','|'))
# Using 'forloop' to iterate over the list of cereals names and their corresponding total calories per serving
# calculated using fat,carbo and proteins.
for i, (cerealName, perCaloriesFromCarbo) in enumerate(zip(np_cerealsTitle, percentageCaloriesFromCarbo)):
    print(fmt.format(i, '|', ' '+ cerealName, '|', perCaloriesFromCarbo, '     |'))
    print(fmt.format('----------', '|', '----------------------------------------', '|', '------------------------------',
                     '|'))


# Metric 5 - % Calories from sugar
# Calculate sugar in calories per gram
np_cerealsSugar_cal = np_cerealsSugar * 4
# We have total calories per serving in 'totalCaloriesPerServing'
percentageCaloriesFromSugar = np_cerealsSugar_cal / totalCaloriesPerServing * 100
print('\n')
# Column names
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
print(fmt.format('Serial.No','|',' Cereal Name','|','% Calories from Sugar',' |'))
print(fmt.format('----------','|','----------------------------------------','|','--------------------------','|'))
# Using 'forloop' to iterate over the list of cereals names and their corresponding total calories per serving
# calculated using fat,carbo and proteins.
for i, (cerealName, perCaloriesFromSugar) in enumerate(zip(np_cerealsTitle, percentageCaloriesFromSugar)):
    print(fmt.format(i, '|', ' '+ cerealName, '|', perCaloriesFromSugar, ' |'))
    print(fmt.format('----------', '|', '----------------------------------------', '|', '--------------------------',
                     '|'))


# Metric 6 - sodium/potassium ratio of Na/K <1 is protective
# We have sodium in milligrams in 'np_cerealsSodium_mg'

# Converting Potassium from grams to milligrams
np_cerealsPotassium_mg = np_cerealsPotassium * 1000
# Calculating sodium/potassium (Na/K) ratio
sodiumPotassiumRatio = np_cerealsSodium_mg / np_cerealsPotassium_mg

# formating lists of string and vlues to print in tabular format
fmt = '{:<10}{:<1}{:<40}{:<1}{:<25}{:<1}{:<30}{:<1}'

# Check if the values of ratio are <1 or >1 and store the list in 'protectiveOrNot'.
# If value is <1 then add value 'yes' to arraylist , if >1 then add 'no'
protectiveOrNot = ['yes' if float(x) < 1 else 'no' for x in sodiumPotassiumRatio]
print('\n')
# Column names
print(fmt.format('----------','|','----------------------------------------','|','-------------------------','|','-------------------------------','|'))
print(fmt.format('Serial.No','|',' Cereal Name','|',' Na/K Ratio','|',' Ratio of Na/K <1 is Protective','|'))
print(fmt.format('----------','|','----------------------------------------','|','-------------------------','|','-------------------------------','|'))
# Using 'forloop' to iterate over the list of cereals names and their corresponding total calories per serving
# calculated using fat,carbo and proteins.
for i, (cerealName, Na_K_Ratio,protectiveOrNot) in enumerate(zip(np_cerealsTitle, sodiumPotassiumRatio,protectiveOrNot)):
    print(fmt.format(i, '|', ' '+ cerealName, '|', Na_K_Ratio, '|',' ' + protectiveOrNot,' |'))
    print(fmt.format('----------', '|', '----------------------------------------', '|', '-------------------------',
                     '|','-------------------------------','|'))
