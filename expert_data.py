from stable_baselines.gail import generate_expert_traj
from melee_gym import MeleeEnv
import melee

env = MeleeEnv(ai=1, cpu=1)

def get_action(_obs):

    controller = env.get_gamestate().players[1].controller_state

    print(controller)

    if(controller.button[melee.enums.Button.BUTTON_A]):
        if (abs(0.5 - controller.main_stick[1]) > abs(0.5 - controller.main_stick[0]) and controller.main_stick[1] > 0.5):
            # Up
            return 6
        elif (abs(0.5 - controller.main_stick[1]) > abs(0.5 - controller.main_stick[0]) and controller.main_stick[1] < 0.5):
            # Down
            return 7
        elif (abs(0.5 - controller.main_stick[0]) > abs(0.5 - controller.main_stick[1]) and controller.main_stick[0] > 0.5):
            # Left
            return 8
        elif (abs(0.5 - controller.main_stick[0]) > abs(0.5 - controller.main_stick[1]) and controller.main_stick[0] < 0.5):
            # Right
            return 9
        else:
            # Neural
            return 5
    elif (controller.button[melee.enums.Button.BUTTON_B]):
        if (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
                controller.main_stick[1] > 0.5):
            # Up
            return 11
        elif (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
              controller.main_stick[1] < 0.5):
            # Down
            return 12
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] > 0.5):
            # Left
            return 13
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] < 0.5):
            # Right
            return 14
        else:
            # Neural
            return 10
    elif (controller.button[melee.enums.Button.BUTTON_X]):
        if (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
                controller.main_stick[1] > 0.5):
            # Up
            return 16
        elif (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
              controller.main_stick[1] < 0.5):
            # Down
            return 17
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] > 0.5):
            # Left
            return 18
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] < 0.5):
            # Right
            return 19
        else:
            # Neural
            return 15
    elif (controller.button[melee.enums.Button.BUTTON_Y]):
        if (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
                controller.main_stick[1] > 0.5):
            # Up
            return 21
        elif (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
              controller.main_stick[1] < 0.5):
            # Down
            return 22
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] > 0.5):
            # Left
            return 23
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] < 0.5):
            # Right
            return 24
        else:
            # Neural
            return 20
    elif (controller.button[melee.enums.Button.BUTTON_L]):
        if (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
              controller.main_stick[1] < 0.5):
            # Down
            return 26
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] > 0.5):
            # Left
            return 27
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] < 0.5):
            # Right
            return 28
        else:
            # Neural
            return 25
    elif (controller.button[melee.enums.Button.BUTTON_R]):
        if (abs(0.5 - controller.main_stick[1]) > abs(
                0.5 - controller.main_stick[0]) and
              controller.main_stick[1] < 0.5):
            # Down
            return 30
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] > 0.5):
            # Left
            return 31
        elif (abs(0.5 - controller.main_stick[0]) > abs(
                0.5 - controller.main_stick[1]) and
              controller.main_stick[0] < 0.5):
            # Right
            return 32
        else:
            # Neural
            return 29
    elif (controller.button[melee.enums.Button.BUTTON_Z]):
        #grab
        return 33

    #no button
    elif (abs(0.5 - controller.main_stick[1]) > abs(
            0.5 - controller.main_stick[0]) and
            controller.main_stick[1] > 0.5):
        # Up
        return 1
    elif (abs(0.5 - controller.main_stick[1]) > abs(
            0.5 - controller.main_stick[0]) and
          controller.main_stick[1] < 0.5):
        # Down
        return 2
    elif (abs(0.5 - controller.main_stick[0]) > abs(
            0.5 - controller.main_stick[1]) and
          controller.main_stick[0] > 0.5):
        # Left
        return 3
    elif (abs(0.5 - controller.main_stick[0]) > abs(
            0.5 - controller.main_stick[1]) and
          controller.main_stick[0] < 0.5):
        # Right
        return 4
    else:
        # Neural
        return 0

generate_expert_traj(get_action, 'expert_data/expert_kirby_ian', env, n_episodes=100)
