import os , sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from xgboost import XGBRegressor

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('models','model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
        
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Model Training Start")
            logging.info("Split training and test arr")
            
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            
            models = {
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "KNN Regressor": KNeighborsRegressor(),
                "XGBoost" : XGBRegressor(),
                "CatBoost" : CatBoostRegressor(verbose=False),
                "AdaBoost": AdaBoostRegressor()
                }
            
            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test = X_test, y_test = y_test, models = models)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                raise CustomException("NO BEST MODEL FOUND")
            logging.info(f"Best performing model is : \n *************{best_model_name}*************")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            predicted = best_model.predict(X_test)
            r2_scores=  r2_score(y_test, predicted)
            
            return f"Model name: {best_model_name} with r2 score of :{r2_scores}"
        
        except Exception as e:
            raise CustomException(e,sys)