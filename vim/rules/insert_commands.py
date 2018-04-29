from dragonfly import MappingRule, Key, Text, IntegerRef, Dictation


class InsertRules(MappingRule):
    mapping = {
        # "[<n>] up": Key("up:%(n)d"),
        # "[<n>] down": Key("down:%(n)d"),
        # "[<n>] left": Key("left:%(n)d"),
        # "[<n>] right": Key("right:%(n)d"),
        "slap": Key("enter"),

        "[<n>] (scratch|delete)": Key("c-w:%(n)d"),
        # "[<n>] slap": Key("enter:%(n)d"),
        "[<n>] tab": Key("tab:%(n)d"),
        "[<n>] backspace": Key("backspace:%(n)d"),
        "(scratch|delete) line": Key("c-u"),

        "<text>": Text("%(text)s"),
    }
    extras = [
        IntegerRef("n", 1, 100),
        Dictation('text')
    ]