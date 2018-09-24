from dragonfly import (
    Grammar, 
    CompoundRule,
    Dictation,
    Text,
    Key,
    AppContext,
    MappingRule
)


print 'Ubuntu grammar access'


class FirefoxShortcuts(MappingRule):
    mapping = {
        "bunt new window": Key("c-T"),
        "bunt select all": Key("c-a"),
    }


class GeneralUbuntu(MappingRule):
    mapping = {
        "bunt close window": Key("c-w"),
    }


ubuntuGrammar = Grammar("Ubuntu")
ubuntuGrammar.add_rule(FirefoxShortcuts())
ubuntuGrammar.add_rule(GeneralUbuntu())
ubuntuGrammar.load()


def unload():
    global ubuntuGrammar
    if ubuntuGrammar:
        ubuntuGrammar.unload()
    ubuntuGrammar = None
