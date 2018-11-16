import turicreate as tc
import time

from skafossdk import *

ska = Skafos() #initialize Skafos

# read in the actions and items 
actions = tc.SFrame.read_csv('https://s3.amazonaws.com/skafos.example.data/MovieLensDataset/ml-20m/ratings.csv')
items = tc.SFrame.read_csv('https://s3.amazonaws.com/skafos.example.data/MovieLensDataset/ml-20m/movies.csv')


# split the training and validation sets up
ska.log("Spliting up the training and validation data", labels = ['turi_recommender'])
training_data, validation_data = tc.recommender.util.random_split_by_user(actions, 'userId', 'movieId')

# build the recommender
ska.log("Training the recommender", labels = ['turi_recommender'])
model = tc.recommender.create(training_data, 'userId', 'movieId')

# grab the results of the model
ska.log("Obtaining the results", labels = ['turi_recommender'])
results = model.recommend()

# print the validation data
validation_data.print_rows(num_rows=30)

# evaluate the model
ska.log("Evaluating the model on the validation data")
model.evaluate(validation_data)

#ska.engine.save_model(model_name, model_data, tags = ["0.1.0", "latest"], access="private").result()