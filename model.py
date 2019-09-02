# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.preprocessing import StandardScaler
import pickle

def model():
    data= pd.read_csv('house_price_data_4.csv')

    X = data.iloc[:, :2]
    print ('X shape ='%X.shape)

    #Converting words to integer values
    def convert_to_int(word):
        word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                    'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
        return word_dict[word]

    X['size'] = X['size'].apply(lambda x : convert_to_int(x))

    y = data.iloc[:,3]
    print('y=' %y)

    #Splitting Training and Test Set
    #Since we have a very small dataset, we will train our model with all availabe data.

    from sklearn.linear_model import LinearRegression

    #Fitting model with trainig data
    regressor= LinearRegression()
    regressor.fit(X, y)

    # Saving model 
    pickle.dump(regressor, open('house_price_model.pkl', 'wb'))
    return (output)

