from dragonfly import MappingRule, Key, Text

class NetrwRule(MappingRule):
    exported = True
    mapping = {
        "explore here": Text(":Explore") + Key("enter"),
        "explore vertical": Text(":Vexplore") + Key("enter"),
        "explore split": Text(":Sexplore") + Key("enter"),
        "explore tab": Text(":Texplore") + Key("enter"),
        "explore back": Text(":Rexplore") + Key("enter"),
        "create net file": Key('%%'),
        "create net directory": Key('d')
    }
    extras = []
    default = {}
