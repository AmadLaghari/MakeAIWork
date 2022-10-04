import numpy as np
from tensorflow.python.keras.engine.sequential import Sequential
from tensorflow.python.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from cgi import print_directory
import numpy as np
import pandas as pd
from matplotlib import pyplot 
from tensorflow import keras
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
import tensorflow as tf
optim = tf.keras.optimizers.Adam()
import gym 
import random


dataframe = pd.read_csv('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/Lidar/lidar.samples', header = None, sep = ' ')
dataframe.to_csv('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/Lidar/lidar.samples', header = None, index=False)
#print (np.array(dataframe))
#print (df.shape)



# Dataframe conversion
numpyarray = np.array(dataframe)
arr_distances = []
arr_steering = []
total = []
for x in numpyarray:
    distancesLidar = float(x[0].split(',')[0]), float(x[0].split(',')[1]), float(x[0].split(',')[2]), float(x[0].split(',')[3]), float(x[0].split(',')[4]), float(x[0].split(',')[5]), float(x[0].split(',')[6]), float(x[0].split(',')[7]), float(x[0].split(',')[8]), float(x[0].split(',')[9]), float(x[0].split(',')[10]), float(x[0].split(',')[11]), float(x[0].split(',')[12]), float(x[0].split(',')[13]), float(x[0].split(',')[14]), float(x[0].split(',')[15])
    steeringSonar =  float(x[0].split(',')[16])
    data_np = np.asarray(distancesLidar, np.float32)
    s = tf.convert_to_tensor(data_np, np.float32)
    arr_distances.append(distancesLidar)
    arr_steering.append(steeringSonar)
    total.append((distancesLidar, steeringSonar))


# Validation data 0 - 299
# val_arr_distances = np.array(arr_distances[0:699])
# val_arr_steering = np.array(arr_steering[0:699])


# #Tensorflow input, layers en output
# inputs = keras.Input(shape=(16,), name="distances_input")
# x = keras.layers.Dense(64, activation="relu", name="layer_1")(inputs)
# x = keras.layers.Dense(128, activation="relu", name="layer_2")(x)
# x = keras.layers.Dense(256, activation="relu", name="layer_3")(x)
# x = keras.layers.Dense(64, activation="relu", name="layer_4")(x)
# x = keras.layers.Dense(16, activation="relu", name="layer_5")(x)
# output = keras.layers.Dense(1, name="predictions")(x)
# model = keras.Model(inputs=inputs, outputs=output, name="16_layer_mlp")

env = gym.make('ALE/Skiing-v0')
states = env.arr_distances
actions = env.arr_steering

def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1,states)))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

model = build_model(states, actions)

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, 
                  nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

dqn = build_agent(model, actions)
dqn.compile(tf.keras.optimizers.Adam()(lr=1e-3), metrics=['mse'])
dqn.fit( nb_steps=50000, visualize=False, verbose=1)

scores = dqn.test( nb_episodes=100, visualize=False)
print(np.mean(scores.history['episode_reward']))


dqn.save('C:/Users/amad_/makeaiwork/simulations/car/control_client/Opdracht/AI/model_lidar_rl')