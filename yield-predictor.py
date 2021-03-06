import numpy as np
from sklearn import metrics
from sklearn.metrics import r2_score
#Optional - just helps to check if arrays have the correct values
np.set_printoptions(formatter={'float_kind':'{:f}'.format})

#Import data from different regions
buenos_aires = np.genfromtxt('buenos-aires.txt', dtype='float', delimiter=';', skip_header=1, usecols = (1, 2, 3, 4, 5, 6))
tucuman = np.genfromtxt('tucuman.txt', dtype='float', delimiter=';', skip_header=1, usecols = (1, 2, 3, 4, 5, 6))
chaco = np.genfromtxt('chaco.txt',dtype='float', delimiter=';', skip_header=1, usecols = (1, 2, 3, 4, 5, 6))

#Concatenate arrays into one and shuffle rows to make sure training and testing sets include all regions
data = np.concatenate((buenos_aires, tucuman, chaco), axis=0)
np.random.shuffle(data)

#Split the data(80% training - 20% testing) into training and testing sets
split_value = round(len(data)*8/10)
training_data = data[:split_value, :]
test_data = data[split_value:, :]

#Split the columns for lstsqr method - last one is the result
training_items = training_data[:, :-1]
training_yield = training_data[:, -1]
test_items = test_data[:, :-1]
test_yield = test_data[:, -1]
#Least squares calculation
coefficients = np.linalg.lstsq(training_items, training_yield,rcond=-1)[0]

#Testing
predictions = test_items @ coefficients
# print (predictions)
#print(test_yield)

#Measuring error
# print('Mean absolute error: ', metrics.mean_absolute_error(test_yield, predictions))
print('Coefficient of determination: %.2f'
      % r2_score(test_yield, predictions))


#Ask user for data needed to make prediction
repeat = 'yes'
while repeat == 'yes':

    try:
        print('Remember: Data should be real if you want to receive a decent output!')
        temp_input = float(input('Please insert mean temperature(ºC): ' ))
        rainfall_input = float(input('Please insert amount of anual rainfall(mm): '))
        solar_input = float (input('Please insert anual solar output(in MWh/m2): '))
        co_input = float(input('Please insert Organic Carbon presence in soil: '))
        ph_input = float(input('Please insert pH of soil: '))

        #Make a list with valid input
        user_input = list()
        user_input.append(temp_input)
        user_input.append(rainfall_input)
        user_input.append(solar_input)
        user_input.append(co_input)
        user_input.append(ph_input)

        #Make prediction
        user_prediction = user_input @ coefficients

        #Printing results
        print('You entered this values:', temp_input, 'ºC', rainfall_input, 'mm', solar_input, 'in MWh/m2', co_input, 'CO in soil', ph_input, 'soil pH')
        print('Wheat yield prediction:', round(user_prediction))

    except:
        print('Try again. You must enter valid numbers')

    repeat = input('Do you want to make another calculation?(yes/no)')
