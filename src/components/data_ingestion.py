import sys
import os
from src.exception import CustomeException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# @dataclass allows directly define a class variable
@dataclass
class DataIngestionConfig:

    train_data_path:str = os.path.join('artifacts',"train.csv")
    test_data_path:str = os.path.join('artifacts',"test.csv")
    raw_data_path:str = os.path.join('artifacts',"data.csv")


class DataIngestion:

    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()

    
    def initiate_data_ingestion(self):

        logging.info("Enter the Data Ingestion Method or Component")

        try:
            df = pd.read_csv("notebook/data/stud.csv")

            logging.info("Read the Dataset as Dataframe")

            os.makedirs(os.path.dirname(self.ingestionConfig.train_data_path),exist_ok=True)

            df.to_csv(self.ingestionConfig.raw_data_path,index=False,header=True)
            logging.info("train test split initiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestionConfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionConfig.test_data_path,index = False,header = True)

            logging.info("Data Ingestion Completed")


            return (self.ingestionConfig.train_data_path,
                    self.ingestionConfig.test_data_path)


        except Exception as e:

            raise CustomeException(e,sys)





if __name__ == "__main__":

    obj=DataIngestion()
    obj.initiate_data_ingestion()

