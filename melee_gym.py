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

  def __init__(self, ai=0, cpu=0, training_iterations=1000000):
    super(MeleeEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(26)
    # Example for using image as input:
    self.observation_space = spaces.Dict(
        {
            "observation": spaces.Box(np.array([0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0, 0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0]), #player 1(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable), player 2(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable)
                        np.array([4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1, 4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1])), #player 1(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable), #player 2(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable)
            "achieved_goal": spaces.Box(np.array([0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0, 0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0]), #player 1(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable), player 2(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable)
                        np.array([4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1, 4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1])),
            "desired_goal": spaces.Box(np.array([0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0, 0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0]), #player 1(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable), player 2(stock, percent, x, y, facing, on_ground, off_stage, action, jumps_left, invulnerable)
                        np.array([4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1, 4, 1000, 1000, 1000, 1, 1, 1, 500, 10, 1])),
        })

    self.melee_characters = [melee.enums.Character.BOWSER, melee.enums.Character.CPTFALCON, melee.enums.Character.DK, melee.enums.Character.DOC, melee.enums.Character.FALCO, melee.enums.Character.FOX, melee.enums.Character.GAMEANDWATCH, melee.enums.Character.GANONDORF, melee.enums.Character.JIGGLYPUFF, melee.enums.Character.LINK, melee.enums.Character.LUIGI, melee.enums.Character.MARIO, melee.enums.Character.MARTH, melee.enums.Character.MEWTWO, melee.enums.Character.NESS, melee.enums.Character.PEACH, melee.enums.Character.PICHU, melee.enums.Character.PIKACHU, melee.enums.Character.ROY, melee.enums.Character.SAMUS, melee.enums.Character.YLINK, melee.enums.Character.YOSHI, melee.enums.Character.ZELDA]

    #download Slippi (https://slippi.gg/) and insert path here to dolphin (might be in your temp) here (I can send you a link to the iso when you get here so you do not need to download it elsewhere)
    self.console = melee.Console(path="D:/Slippi Dolphin")

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
    self.cpu_level = 1
    self.reward = -1
    self.desired_goal = np.array([0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0, 0, 0, -1000, -1000, 0, 0, 0, 0, 0, 0])

    self.cpu_char = self._get_random_char()

    self.training_iterations = training_iterations
    self.interation = 0
    self.obs = None

  def compute_reward(self, achieved_goal, desired_goal, info={}):
      reward = achieved_goal[0] - achieved_goal[10]
      return reward

  def _get_random_char(self):
      return self.melee_characters[random.randint(0, len(self.melee_characters) - 1)]

  def step(self, action):
    # Execute one time step within the environment
    obs = self._next_observation()

    self._take_action(action)
    self.gamestate = self.console.step()

    self.reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'])

    if self.gamestate.menu_state not in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
        return obs, self.reward, True, {}

    obs = self._next_observation()

    if self.obs is not None:
        self.obs = obs
        self.reward = self.compute_reward(obs['achieved_goal'], obs['desired_goal'])
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
        if(self.ai == 0 or self.ai == 1):
            melee.menuhelper.MenuHelper.menu_helper_simple(self.gamestate,
                                                           self.controller,
                                                           melee.enums.Character.KIRBY,
                                                           melee.enums.Stage.RANDOM_STAGE,
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
                                                       melee.enums.Stage.RANDOM_STAGE,
                                                       "",
                                                       cpu_level=self.cpu_level,
                                                       autostart=True,
                                                       swag=True)

        if self.gamestate.menu_state not in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
            self.gamestate = self.console.step()



    return self._next_observation()

  def _next_observation(self):

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
             int(self.gamestate.players[2].invulnerable)])  #19

      return OrderedDict([
            ('observation', obs),
            ('achieved_goal', obs),
            ('desired_goal', self.desired_goal.copy())
        ])

  def get_gamestate(self):
      return self.gamestate

  def get_obs(self):
      return self.obs

  def render(self, mode='human', close=False):
    # Render the environment to the screen
    pass
