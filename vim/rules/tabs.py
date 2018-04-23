from dragonfly import MappingRule, Key

class TabRule(MappingRule):
    name = "gvim_tabs"
    mapping = {
        "tabulator next": Key("g,t"),
        "tabulator previous": Key("g,T"),
    }
    extras = [
    ]
