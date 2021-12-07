from melee_gym import MeleeEnv
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import DQN, HER

env = DummyVecEnv([lambda: MeleeEnv(cpu=False)])
nsg = 4
model = HER('MlpPolicy',env,DQN,n_sampled_goal=nsg, \
            goal_selection_strategy='future', verbose=1, \
            buffer_size=int(1e8), learning_rate=1e-3, gamma=0.99, \
            batch_size=256, policy_kwargs=dict(layers=[256,256,256]))
obs = env.reset()

for i in range(20000):
    print("test")
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()