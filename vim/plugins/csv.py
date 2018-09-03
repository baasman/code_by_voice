from dragonfly import MappingRule, Key, Text, IntegerRef

class CSVRule(MappingRule):
    mapping = {
        "align columns": Key("colon, percent") + Text("ArrangeColumn") + Key("enter"),
        "delete column [<n>]": Key("colon") + Text("DeleteColumn %(n)d") + Key("enter"),
        "set header [<n>]": Text(":Header %(n)d") + Key("enter"),
        "highlight column [<n>]": Text(":HiColumn %(n)d") + Key("enter"),
        "highlight column [<n>]": Text(":HiColumn %(n)d") + Key("enter"),
        "analyze column [<n>]": Text(":Analyze %(n)d") + Key("enter"),
    }
    extras = [
        IntegerRef("n", 1, 10),
    ]
    defaults = {
        'n': 1,
    }
