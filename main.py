x = 0

def on_button_pressed_a():
    global x
    basic.show_leds("""
        . . . . .
                # . # . #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . # # # #
                . # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
    """)
    basic.show_leds("""
        # # # # #
                # # . . #
                . . # # #
                . . . . #
                . . . . #
    """)
    x = randint(1, 3)
    if x == 1:
        basic.show_leds("""
            . . . . .
                        # . # . #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    if x == 2:
        basic.show_leds("""
            . . # # #
                        . # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
    if x == 3:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        # # . # #
                        # # . # #
        """)
    if x == 4:
        basic.show_leds("""
            # # # # #
                        # # . . #
                        . . # # #
                        . . . . #
                        . . . . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)
