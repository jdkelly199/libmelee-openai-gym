from melee_gym import MeleeEnv
from stable_baselines.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines.common.callbacks import CallbackList, CheckpointCallback, EveryNTimesteps
from stable_baselines import PPO2, HER, DQN
import csv_callback
import time

env = DummyVecEnv([lambda: MeleeEnv(cpu=False, enemy_level=(2))])
#env = VecNormalize(env, norm_obs=True, norm_reward=True)

nsg = 4
logs_path = "C:/Users/Ian/OneDrive/Desktop/CS238/libmelee/logs/"
#model = PPO2.load('models/PPO2_pretrain_rl_long', env)
model = HER('MlpPolicy',env,DQN,n_sampled_goal=nsg, \
            goal_selection_strategy='future', verbose=1, \
            buffer_size=int(1e8), learning_rate=1e-3, gamma=0.95, \
            batch_size=256, policy_kwargs=dict(layers=[256,256,256]))

model.save(logs_path + "her_v4")
env.close()
time.sleep(1)
win_ct = 0
stock_adv = []

for i in range(100):
    print(f'EPOCH: {i}')
    env = MeleeEnv(cpu=False, enemy_level=((i+200)//100))
    model = HER.load(logs_path + "her_v4", env=env)
    try:
        model.learn(total_timesteps=5000)
        print("Success. Saving...")
        model.save(logs_path + "her_v3")
    except:
        print("Timeout Occurred.")
    if env.isAccomplished():
        win_ct += 1
    stock_adv.append(env.getStockAdvantage())
    print(f'Running Average: {win_ct / (i+1)}')
    print(stock_adv)
    env.close()
    print("Done")
    time.sleep(1)
    if (i%20 == 0):
        input("Press enter to continue...")
#env.save(logs_path + "vec_normalize.pkl")

env = DummyVecEnv([lambda: MeleeEnv(cpu=False, enemy_level=((200)//100))])
for i in range(1000):
    print("testing:" + str(i))
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
env.close()
