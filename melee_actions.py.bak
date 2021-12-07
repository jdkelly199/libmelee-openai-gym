import melee

enum_buttons = [melee.enums.Button.BUTTON_A, melee.enums.Button.BUTTON_B, melee.enums.Button.BUTTON_X,
                melee.enums.Button.BUTTON_Y, melee.enums.Button.BUTTON_Z, melee.enums.Button.BUTTON_L,
                melee.enums.Button.BUTTON_R]


def perform_action(action, controller):
    #Buttons - No Button(Direction), A(Direction), B(Direction), X(Direction), Y(Direction), L(Direction - Up), R(Direction - Up), Z(Grab)
    enum_buttons = [melee.enums.Button.BUTTON_A, melee.enums.Button.BUTTON_B, melee.enums.Button.BUTTON_X, melee.enums.Button.BUTTON_Y, melee.enums.Button.BUTTON_Z, melee.enums.Button.BUTTON_L, melee.enums.Button.BUTTON_R]
    #Direction - Neutral, Up, Down, Left, Right

    # No Button
    if(action >= 0 and action <= 4):
        for button in enum_buttons:
            controller.release_button(button)

        if(action == 0):
            #Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif(action == 1):
            #Up
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=1)
        elif (action == 2):
            #Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 3):
            #Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 4):
            #Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

    # Button_A
    if (action >= 5 and action <= 9):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_A:
                controller.press_button(button)
            else:
                controller.release_button(button)

        if (action == 5):
            # Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif (action == 6):
            # Up
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=1)
        elif (action == 7):
            # Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 8):
            # Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 9):
            # Right
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

    # Button_B
    if (action >= 10 and action <= 14):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_B:
                controller.press_button(button)
            else:
                controller.release_button(button)

        if (action == 10):
            # Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif (action == 11):
            # Up
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=1)
        elif (action == 12):
            # Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 13):
            # Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 14):
            # Right
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

    # Button_X
    if (action >= 15 and action <= 19):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_X:
                controller.press_button(button)
            else:
                controller.release_button(button)

        if (action == 15):
            # Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif (action == 16):
            # Up
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=1)
        elif (action == 17):
            # Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 18):
            # Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 19):
            # Right
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

    # Button_Y
    if (action >= 20 and action <= 24):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_Y:
                controller.press_button(button)
            else:
                controller.release_button(button)

        if (action == 20):
            # Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif (action == 21):
            # Up
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=1)
        elif (action == 22):
            # Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 23):
            # Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 24):
            # Right
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

            """
    # Button_L
    if (action >= 25 and action <= 28):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_L:
                controller.press_shoulder(button, 0)
            else:
                controller.release_button(button)

        if (action == 25):
            # Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif (action == 26):
            # Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 27):
            # Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 28):
            # Right
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

    # Button_R
    if (action >= 29 and action <= 32):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_R:
                controller.press_shoulder(button, 0)
            else:
                controller.release_button(button)

        if (action == 29):
            # Neural
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)
        elif (action == 30):
            # Down
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=-1)
        elif (action == 31):
            # Left
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)
        elif (action == 32):
            # Right
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)
    """

    # Button_Z
    if (action == 25):
        for button in enum_buttons:
            if button == melee.enums.Button.BUTTON_Z:
                controller.press_button(button)
            else:
                controller.release_button(button)

        controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=0, y=0)

def get_action(controller):

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
        return 25

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
