from dragonfly import Choice


def motionChoice(name="motion"):
    return Choice(name, {
        "up": "k",
        "whiskey": "w",
        "back": "b",
        "whiskey end": "e",
        "big end [whiskey]": "E",
        "down": "j",
        "left": "h",
        "right": "l",
        "whiskey": "w",
        "back": "b",
        "whiskey end": "e",
        "big end [whiskey]": "e",
    })

