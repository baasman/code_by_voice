from dragonfly import MappingRule, Key, Text


class BufKillRule(MappingRule):
    exported = True
    mapping = {
            "kill buffer": Key('colon') + Text('B') + Text('D') + Key('enter'),
    }
    extras = []
 
