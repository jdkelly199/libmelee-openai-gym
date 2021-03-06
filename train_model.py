import gym

#from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN
from stable_baselines.gail import ExpertDataset
from melee_gym import MeleeEnv
from stable_baselines.common.callbacks import CallbackList, CheckpointCallback, EveryNTimesteps

import progress_bar
import csv_callback

import os
import numpy as np

def main():
  # The algorithms require a vectorized environment to run

  env = MeleeEnv()

  #load blank model or saved model
  #model = DQN('MlpPolicy', env, verbose=1)
  model = DQN.load('D:\libmelee\models\DQN_pretrain_ian_100.zip', env)

  #Use to train over multiple data files (cannot pretrain mutliple times so have to keep loading the model)
  # dataset = None
  #my_dir = 'D:/libmelee/expert_data'
  #for item in os.listdir(my_dir):
  #  print(os.path.join(my_dir, item))
  #  if os.path.isfile(os.path.join(my_dir, item)):
  #    dataset = ExpertDataset(expert_path=os.path.join(my_dir, item), traj_limitation=-1, batch_size=64)
  #    model.pretrain(dataset, n_epochs=1000)
  #    model.save('D:\libmelee\PPO2_pretrain_mult')
  #    model = PPO2.load('D:\libmelee\models\PPO2_pretrain_mult', env)

  #dataset = ExpertDataset(expert_path='D:/libmelee/expert_data/expert_kirby_ian.npz', traj_limitation=-1, batch_size=16)
  #model.pretrain(dataset, n_epochs=1000)
  #model.save(make run_dc)
  
  # RL learning steps
  learn_steps = 1000000

  #callbacks
  csv_callback_function = csv_callback.CSVCallback(env=env)
  checkpoint_callback = CheckpointCallback(save_freq = int(learn_steps/10), save_path='./models/DQN/heur',
                                           name_prefix='rl_model_test')
  with progress_bar.ProgressBarManager(learn_steps) as progress_callback:
    model.learn(total_timesteps=learn_steps, callback=[progress_callback, checkpoint_callback, csv_callback_function])

  model.save("D:\libmelee\models\DQN_heur")
  obs = env.reset()

  for i in range(20000):
    print("test")
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()

if __name__ == '__main__':
  main()