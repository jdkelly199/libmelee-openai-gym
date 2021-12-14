# libmelee-openai-gym
Custom OpenAI Gym Environment implementation for RL training of a Kirby Bot with libmelee

Once you pull the repo you will need to install Slippi @ slippi.gg and a SSBM iso from somewhere online.
Then you will need to change the path to your dolphin emulator on line 28 of the custom openAI gym environment to your dolphin emulatior executable path downloaded with slippi.

Running train_model.py will train a model. We have implemeneted stable-baselines here, but you can use whatever is compatable with openAI gym.

The custom openAI gym envronment utalizing libmelee is in melee_gy.py

To learn more about libmelee, checkout its git page: https://github.com/altf4/libmelee
