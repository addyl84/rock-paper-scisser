let x = 0
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        # . # . #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        . # # # #
        . # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
    basic.showLeds(`
        # # # # #
        # # . . #
        . . # # #
        . . . . #
        . . . . #
        `)
    x = randint(1, 3)
    if (x == 1) {
        basic.showLeds(`
            . . . . .
            # . # . #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    if (x == 2) {
        basic.showLeds(`
            . . # # #
            . # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    }
    if (x == 3) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            `)
    }
    if (x == 4) {
        basic.showLeds(`
            # # # # #
            # # . . #
            . . # # #
            . . . . #
            . . . . #
            `)
    }
})
