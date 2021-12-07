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
import time
env = MeleeEnv(cpu=False)
#env = VecNormalize(env, norm_obs=True, norm_reward=True)

nsg = 4
learn_steps = 10000000

model = DQN('MlpPolicy', env, verbose=1)

#callbacks
csv_callback_function = csv_callback.CSVCallback(env=env)
checkpoint_callback = CheckpointCallback(save_freq = int(learn_steps/100), save_path='./models',
                                       name_prefix='dqn_rl')

try:
    with progress_bar.ProgressBarManager(learn_steps) as progress_callback:
        model.learn(total_timesteps=learn_steps, callback=[progress_callback, checkpoint_callback, csv_callback_function])
except:
    env.close()
    time.sleep(5)
    env.reset()

    learn_steps -= env.get_iter()

    csv_callback_function = csv_callback.CSVCallback(env=env)
    checkpoint_callback = CheckpointCallback(save_freq=int(learn_steps / 100), save_path='./models',
                                             name_prefix='dqn_rl_from' + str(env.get_iter()))
    with progress_bar.ProgressBarManager(learn_steps) as progress_callback:
        model.learn(total_timesteps=learn_steps, callback=[progress_callback, checkpoint_callback, csv_callback_function])

logs_path = "D:/libmelee-openai-gym/models/"
model.save(logs_path + "her_final_v1")
#env.save(logs_path + "vec_normalize.pkl")

for i in range(1000):
    print("testing:" + str(i))
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
env.close()
