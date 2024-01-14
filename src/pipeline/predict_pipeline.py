import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            #model_path=os.path.join("artifacts","model.pkl")
            #preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\proprocessor.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        X1: float,
        X2: float,
        X3: float,
        X4: float,
        X5: float,
        X6: float,
        X7: float,
        X8: float):

        self.X1 = X1

        self.X2 = X2

        self.X3 = X3

        self.X4 = X4

        self.X5 = X5

        self.X6 = X6

        self.X7 = X7
        
        self.X8 = X8

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "X1": [self.X1],
                "X2": [self.X2],
                "X3": [self.X3],
                "X4": [self.X4],
                "X5": [self.X5],
                "X6": [self.X6],
                "X7": [self.X7],
                "X8": [self.X8]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)