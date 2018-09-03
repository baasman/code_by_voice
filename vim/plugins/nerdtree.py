from dragonfly import MappingRule, Key, Text


class NERDTreeRule(MappingRule):
    exported = True
    mapping = {
        "nerd open": Key('o'),
        "nerd open split": Key('i'),
        "nerd open vertical": Key('s'),
        "nerd open tab": Key('t'),
        "nerd change directory": Key('c, d'),
        "nerd set directory": Key('C'),
        "nerd toggle": Key('colon') + Text('NERDTreeToggle') + Key('enter'),
        # use insert start commandto go into change node mode
        # nerd change node
    }
    extras = []
    default = {}
