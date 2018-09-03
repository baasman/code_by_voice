from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)

print 'Ubuntu grammar access'

class UbuntuShortcuts(MappingRule):
    mapping = {
        "bunt new window": Key("c-T"),
        "bunt select all": Key("c-a"),
    }


# The main Python grammar rules are activated here
ubuntuGrammar = Grammar("Ubuntu")
ubuntuGrammar.add_rule(UbuntuShortcuts())
ubuntuGrammar.load()


def unload():
    global ubuntuGrammar
    if ubuntuGrammar: ubuntuGrammar.unload()
    ubuntuGrammar = None
