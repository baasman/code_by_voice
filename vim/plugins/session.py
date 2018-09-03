from dragonfly import MappingRule, Key, Text


class SessionRules(MappingRule):
    exported = True
    mapping = {
        # this is not yet working
        "session save": Text(':SaveSession') + Key('enter'),
        "session new session": Key('colon') + Text('SaveSession '),
        "session open": Key('colon') + Text('OpenSession') + Key('enter')
    }
    extras = []
    default = {}
