import gym
from gym import spaces
import numpy as np
import melee
import random
import melee_actions
from collections import OrderedDict

class MeleeEnv(gym.GoalEnv):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, ai=0, cpu=0, enemy_level=1, training_iterations=1000000):
    super(MeleeEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(21)
    # Example for using image as input:
    self.observation_space = spaces.Box(
        np.array([0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0, 0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0, -1]),
        # player 1(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable), player 2(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable)
        np.array([4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1, 4, 1000, 1000, 1000, 1, 1, 1, 500, 10,
                  1, 1]))  # player 1(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable), #player 2(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable)

    self.melee_characters = [melee.enums.Character.CPTFALCON]

    #download Slippi (https://slippi.gg/) and insert path here to dolphin (might be in your temp) here (I can send you a link to the iso when you get here so you do not need to download it elsewhere)
    self.console = melee.Console(path="D:/Slippi Dolphin")#"C:/Users/Ian/OneDrive/Desktop/CS238/Slippi Dolphin")

    self.ai = ai
    self.cpu = cpu

    if(self.ai == 0 or self.ai == 2):
        self.controller = melee.Controller(console=self.console, port=1)
    else:
        self.controller = melee.Controller(console=self.console, port=1, type=melee.ControllerType.GCN_ADAPTER)

    if (self.cpu == 0):
        self.cpu_controller = melee.Controller(console=self.console, port=2)
    else:
        self.cpu_controller = melee.Controller(console=self.console, port=2, type=melee.ControllerType.GCN_ADAPTER)

    self.dolphin = False
    self.cpu_level = enemy_level
    self.reward = -1
    self.accomplished = False

    self.cpu_char = self._get_random_char()

    self.training_iterations = training_iterations
    self.interation = 0
    self.obs = None

  def compute_reward(self, obs):
      reward = self.reward = (obs[0] * 300 - obs[1]) - (obs[10] * 300 - obs[11]) + (((-250 * int(obs[20] != 0) + obs[3] * int(obs[20] != 0)) + (-1 * (abs(obs[2] - obs[12]) + abs(obs[3] - obs[13])))) * (1/2)**(self.interation / (self.training_iterations / 2)))
      return reward

  def isAccomplished(self):
      return self.accomplished

  def getStockAdvantage(self):
      return self.obs['observation'][0] - self.obs['observation'][10]

  def _get_random_char(self):
      return self.melee_characters[random.randint(0, len(self.melee_characters) - 1)]

  def step(self, action):
    # Execute one time step within the environment
    obs = self._next_observation()

    self._take_action(action)
    self.gamestate = self.console.step()

    self.reward = self.compute_reward(obs)

    if self.gamestate.menu_state not in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
        return obs, self.reward, True, {}

    obs = self._next_observation()

    if self.obs is not None:
        self.obs = obs
        self.reward = self.compute_reward(obs)
    else:
        self.obs = "New Game"
        self.reward = -1

    self.interation += 1

    return obs, self.reward, False, {}

  def _take_action(self, action):
      melee_actions.perform_action(action, self.controller)

  def reset(self):
    # Reset the state of the environment to an initial state
    self.obs = None
    """
    #reset functionality
    if self.dolphin:
        try:
            self.console.stop()
        except:
            print("had the exception")
        self.dolphin = False
        self.console = melee.Console(path="C:/Users/Ian/OneDrive/Desktop/CS238/Slippi Dolphin")
        if(self.ai == 0 or self.ai == 2):
            self.controller = melee.Controller(console=self.console, port=1)
        else:
            self.controller = melee.Controller(console=self.console, port=1, type=melee.ControllerType.GCN_ADAPTER)
        if (self.cpu == 0):
            self.cpu_controller = melee.Controller(console=self.console, port=2)
        else:
            self.cpu_controller = melee.Controller(console=self.console, port=2, type=melee.ControllerType.GCN_ADAPTER)
    """

    if(not self.dolphin):
        self.console.run()
        self.console.connect()

        self.controller.connect()
        self.controller.release_all()
        # controller_human.connect()
        self.cpu_controller.connect()

        self.dolphin = True

    self.cpu_char = self._get_random_char()
    self.gamestate = self.console.step()

    #if (self.reward > -1) and (self.cpu_level < 9):
    #    self.cpu_level += 1
    #    print(self.reward, self.cpu_level)


    while self.gamestate.menu_state not in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
        self.gamestate = self.console.step()
        if(self.ai == 0 or self.ai == 1):
            melee.menuhelper.MenuHelper.menu_helper_simple(self.gamestate,
                                                           self.controller,
                                                           melee.enums.Character.KIRBY,
                                                           melee.enums.Stage.FINAL_DESTINATION,
                                                           "",
                                                           autostart=False,
                                                           swag=True)
        else:
            melee.menuhelper.MenuHelper.menu_helper_simple(self.gamestate,
                                                           self.controller,
                                                           melee.enums.Character.KIRBY,
                                                           melee.enums.Stage.RANDOM_STAGE,
                                                           "",
                                                           cpu_level=9,
                                                           autostart=False,
                                                           swag=True)


        melee.menuhelper.MenuHelper.menu_helper_simple(self.gamestate,
                                                       self.cpu_controller,
                                                       self.cpu_char,
                                                       melee.enums.Stage.FINAL_DESTINATION,
                                                       "",
                                                       cpu_level=self.cpu_level,
                                                       autostart=True,
                                                       swag=True)




    return self._next_observation()

  def _next_observation(self):

      recovery_obs = 0
      if self.gamestate.players[1].position.x >= 90 or (self.gamestate.players[1].position.x > 0 and self.gamestate.players[1].position.y < 0):
          recovery_obs = 1
      if self.gamestate.players[1].position.x <= -90 or (self.gamestate.players[1].position.x < 0 and self.gamestate.players[1].position.y < 0):
          recovery_obs = -1

      obs = np.array([int(self.gamestate.players[1].stock), #0
             int(self.gamestate.players[1].percent),        #1
             int(self.gamestate.players[1].position.x),     #2
             int(self.gamestate.players[1].position.y),     #3
             int(self.gamestate.players[1].facing),         #4
             int(self.gamestate.players[1].on_ground),      #5
             int(self.gamestate.players[1].off_stage),      #6
             int(self.gamestate.players[1].action._value_), #7
             int(self.gamestate.players[1].jumps_left),     #8
             int(self.gamestate.players[1].invulnerable),   #9
             int(self.gamestate.players[2].stock),          #10
             int(self.gamestate.players[2].percent),        #11
             int(self.gamestate.players[2].position.x),     #12
             int(self.gamestate.players[2].position.y),     #13
             int(self.gamestate.players[2].facing),         #14
             int(self.gamestate.players[2].on_ground),      #15
             int(self.gamestate.players[2].off_stage),      #16
             int(self.gamestate.players[2].action._value_), #17
             int(self.gamestate.players[2].jumps_left),     #18
             int(self.gamestate.players[2].invulnerable),   #19
             int(recovery_obs)])  #20

      return obs

  def get_gamestate(self):
      return self.gamestate

  def get_obs(self):
      return self.obs

  def get_iter(self):
      return self.interation

  def close(self):
      self.console.stop()
      self.dolphin = False

  def render(self, mode='human', close=False):
    # Render the environment to the screen
    pass
