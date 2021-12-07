from melee_gym import MeleeEnv
from stable_baselines.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines import PPO2, HER, DQN
import progress_bar

# from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN
from stable_baselines.gail import ExpertDataset
from melee_gym import MeleeEnv
from stable_baselines.common.callbacks import CallbackList, CheckpointCallback, EveryNTimesteps

import progress_bar
import csv_callback

import os
import numpy as np

env = MeleeEnv(cpu=False)
#env = VecNormalize(env, norm_obs=True, norm_reward=True)

nsg = 4
logs_path = "C:/Users/Ian/OneDrive/Desktop/CS238/libmelee/logs/"

#model = PPO2.load('models/PPO2_pretrain_rl_long', env)
model = HER('MlpPolicy',env,DQN,n_sampled_goal=nsg, \
            goal_selection_strategy='episode', verbose=1, \
            buffer_size=int(1e8), learning_rate=1e-3, gamma=0.9995, \
            batch_size=256, policy_kwargs=dict(layers=[256,256,256]))

learn_steps = 10000000
#callbacks
csv_callback_function = csv_callback.CSVCallback(env=env)
checkpoint_callback = CheckpointCallback(save_freq = int(learn_steps/100), save_path='./models',
                                       name_prefix='her_model_test')
with progress_bar.ProgressBarManager(learn_steps) as progress_callback:
    model.learn(total_timesteps=learn_steps, callback=[progress_callback, checkpoint_callback, csv_callback_function])

obs = env.reset()

for i in range(500):
    print("testing:" + str(i))
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
