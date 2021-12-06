from melee_gym import MeleeEnv
from stable_baselines.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines import PPO2, HER, DQN

env = DummyVecEnv([lambda: MeleeEnv(cpu=False)])
#env = VecNormalize(env, norm_obs=True, norm_reward=True)

nsg = 4

#model = PPO2.load('models/PPO2_pretrain_rl_long', env)
model = HER('MlpPolicy',env,DQN,n_sampled_goal=nsg, \
            goal_selection_strategy='future', verbose=1, \
            buffer_size=int(1e8), learning_rate=1e-3, gamma=0.95, \
            batch_size=256, policy_kwargs=dict(layers=[256,256,256]))


model.learn(total_timesteps=100000)

logs_path = "C:/Users/Ian/OneDrive/Desktop/CS238/libmelee/logs/"
model.save(logs_path + "her_v1")
#env.save(logs_path + "vec_normalize.pkl")


obs = env.reset()

for i in range(3000):
    print("testing:" + str(i))
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
