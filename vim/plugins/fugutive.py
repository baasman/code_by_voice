from dragonfly import MappingRule, Key, Text, IntegerRef

class FugitiveRule(MappingRule):
    mapping = {
        # Big picture commands:
        "get status": Text(":Gstatus") + Key("enter"),
        "get diff this": Text(":Gdiff") + Key("enter"),
        "get commit": Text(":Gcommit") + Key("enter"),
        "get push": Text(":Gpush") + Key("enter"),


        # when in g status
        # possible needs own bootstrap
        "status open tabulator": Key('O'),
        "status open split": Key('o'),
        "status view diff": Key('D'),
        "status add file": Key("minus"),
    }
    extras = [
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        'n': 1,
    }
