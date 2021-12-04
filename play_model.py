from melee_gym import MeleeEnv
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2

env = DummyVecEnv([lambda: MeleeEnv(cpu=False)])

model = PPO2.load('PPO2_pretrain_rl_ian', env)
obs = env.reset()

for i in range(20000):
    print("test")
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()