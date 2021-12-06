from melee_gym import MeleeEnv
from stable_baselines.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines.common.callbacks import CallbackList, CheckpointCallback, EveryNTimesteps
from stable_baselines import PPO2, HER, DQN
import csv_callback

env = DummyVecEnv([lambda: MeleeEnv(cpu=False)])
#env = VecNormalize(env, norm_obs=True, norm_reward=True)

nsg = 4
logs_path = "C:/Users/Ian/OneDrive/Desktop/CS238/libmelee/logs/"

#model = PPO2.load('models/PPO2_pretrain_rl_long', env)
model = HER('MlpPolicy',env,DQN,n_sampled_goal=nsg, \
            goal_selection_strategy='future', verbose=1, \
            buffer_size=int(1e8), learning_rate=1e-3, gamma=0.95, \
            batch_size=256, policy_kwargs=dict(layers=[256,256,256]))

win_ct = 0

for i in range(100):
    print(f'EPOCH: {i}')
    env = DummyVecEnv([lambda: MeleeEnv(cpu=False)])
    model = HER.load(logs_path + "her_v1", env=env)
    try:
        model.learn(total_timesteps=8000)
        print("Success. Saving...")
        model.save(logs_path + "her_v1")
        if env.accomplished:
            win_ct += 1
    except:
        print("Timeout Occurred.")
    print(f'Running Average: {win_ct / (i+1)}')
    env.close()
    print("Done")
    input("Press Enter to continue...")

#env.save(logs_path + "vec_normalize.pkl")


obs = env.reset()

for i in range(500):
    print("testing:" + str(i))
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
