# load the train and test files
# Train the algo
# save the metrics, parameters

import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config['split_data']['test_path']
    train_data_path =config['split_data']['train_path']
    random_state = config['base']['random_state']
    model_dir = config['estimators']['ElasticNet']['params']['alpha']

    alpha = config['estimators']['ElasticNet']['params']['alpha']
    l1_ration = config['estimators']['ElasticNet']['params']['l1_ration']

    target = config['base']['target_col']

    train = pd.read_csv(train_data_path, sep=',')
    test = pd.read_csv(test_data_path, sep=',')

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha,
                     l1_ratio=l1_ration, 
                     random_state=42)
    
    lr.fit(train_x, train_y)
    predicted_qualities = lr.predict(test_x)

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
    print(rmse, mae, r2)


if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
