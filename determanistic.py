import melee
import random
import gym

melee_characters = [melee.enums.Character.BOWSER, melee.enums.Character.CPTFALCON, melee.enums.Character.DK, melee.enums.Character.DOC, melee.enums.Character.FALCO, melee.enums.Character.FOX, melee.enums.Character.GAMEANDWATCH, melee.enums.Character.GANONDORF, melee.enums.Character.JIGGLYPUFF, melee.enums.Character.LINK, melee.enums.Character.LUIGI, melee.enums.Character.MARIO, melee.enums.Character.MARTH, melee.enums.Character.MEWTWO, melee.enums.Character.NESS, melee.enums.Character.PEACH, melee.enums.Character.PICHU, melee.enums.Character.PIKACHU, melee.enums.Character.ROY, melee.enums.Character.SAMUS, melee.enums.Character.YLINK, melee.enums.Character.YOSHI, melee.enums.Character.ZELDA]

console = melee.Console(path="D:/Slippi Dolphin")

controller = melee.Controller(console=console, port=1)
cpu_controller = melee.Controller(console=console, port=2)
#controller_human = melee.Controller(console=console,
                                    #port=2,
                                    #type=melee.ControllerType.GCN_ADAPTER)
console.run()
console.connect()

controller.connect()
#controller_human.connect()
cpu_controller.connect()

random_character = melee_characters[random.randint(0, len(melee_characters) - 1)]
picked_char = False

while True:
    gamestate = console.step()
    # Press buttons on your controller based on the GameState here!
    if gamestate.menu_state in [melee.enums.Menu.IN_GAME, melee.enums.Menu.SUDDEN_DEATH]:
        if (picked_char):
            picked_char = False

        x_dist = gamestate.players[2].position.x - gamestate.players[1].position.x
        y_dist = gamestate.players[2].position.y - gamestate.players[1].position.y

        controller.release_all()

        if(x_dist < 10):
            if(y_dist < 0):
                controller.tilt_analog_unit(melee.enums.Button.BUTTON_B, x=0, y=-1)
            elif(y_dist > 5):
                controller.tilt_analog_unit(melee.enums.Button.BUTTON_B, x=0, y=1)
            else:
                controller.press_button(melee.enums.Button.BUTTON_A)

        if(y_dist > 10):
            controller.press_button(melee.enums.Button.BUTTON_Y)

        if(x_dist - 10 > 0):
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=1, y=0)

        if (x_dist + 10 < 0):
            controller.tilt_analog_unit(melee.enums.Button.BUTTON_MAIN, x=-1, y=0)

        controller.flush()

    else:
        if(not picked_char):
            random_character = melee_characters[random.randint(0, len(melee_characters) - 1)]
            picked_char = True

        melee.menuhelper.MenuHelper.menu_helper_simple(gamestate,
                                                       controller,
                                                       melee.enums.Character.KIRBY,
                                                       melee.enums.Stage.RANDOM_STAGE,
                                                       "",
                                                       autostart=False,
                                                       swag=True)

        melee.menuhelper.MenuHelper.menu_helper_simple(gamestate,
                                                       cpu_controller,
                                                       random_character,
                                                       melee.enums.Stage.RANDOM_STAGE,
                                                       "",
                                                       cpu_level=9,
                                                       autostart=True,
                                                       swag=True)