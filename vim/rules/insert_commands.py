from dragonfly import MappingRule, Key, Text, IntegerRef, Dictation


class InsertRules(MappingRule):
    mapping = {
        # "[<n>] up": Key("up:%(n)d"),
        # "[<n>] down": Key("down:%(n)d"),
        # "[<n>] left": Key("left:%(n)d"),
        # "[<n>] right": Key("right:%(n)d"),
        "slap": Key("enter"),

        "(scratch|delete)": Key("c-w"),
        "tab": Key("tab"),
        "backspace": Key("backspace"),
        "(scratch|delete) line": Key("c-u"),

        "<text>": Text("%(text)s"),

        "insert debug": Text('import ipdb; ipdb.set_trace()')
    }
    extras = [
        Dictation('text')
    ]
