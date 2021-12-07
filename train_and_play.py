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

#model = PPO2.load('models/PPO2_pretrain_rl_long', env)
model = HER('MlpPolicy',env,DQN,n_sampled_goal=nsg, \
            goal_selection_strategy='future', verbose=1, \
            buffer_size=int(1e8), learning_rate=1e-3, gamma=0.99, \
            batch_size=256, policy_kwargs=dict(layers=[256,256,256]))

#model = HER.load('D:\libmelee-openai-gym\models\her_no_pre_model_test_400000_steps.zip', env=env)


learn_steps = 10000000
#callbacks
csv_callback_function = csv_callback.CSVCallback(env=env)
checkpoint_callback = CheckpointCallback(save_freq = int(learn_steps/100), save_path='./models',
                                       name_prefix='her_less_sparse_rl')
with progress_bar.ProgressBarManager(learn_steps) as progress_callback:
    model.learn(total_timesteps=learn_steps, callback=[progress_callback, checkpoint_callback, csv_callback_function])

logs_path = "D:/libmelee-openai-gym/models/"
model.save(logs_path + "her_final_v1")
#env.save(logs_path + "vec_normalize.pkl")


obs = env.reset()

for i in range(3000):
    print("testing:" + str(i))
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
