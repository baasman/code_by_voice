from dragonfly import MappingRule, Key, Text

# this is replaced by a insert start command
class TerminalRule(MappingRule):
    exported = True
    mapping = {
        "open terminal": Text(":term") + Key("enter"),
    }
    extras = []
    defaults = {}

# this is replaced by the _vim_terminal grammar
class TerminalCommandsRule(MappingRule):
    mapping = {
        "terminal directory": Text("dir") + Key("enter"),
        "terminal up": Key("up"),
        "terminal python": Text("python "),
        "terminal change": Text("cd  "),

        # window navigation commands
        "window left": Key("c-w,h"),
        "window right": Key("c-w,l"),
        "window up": Key("c-w,k"),
        "window down": Key("c-w,j"),
    }
    extras = []
    defaults = {}
