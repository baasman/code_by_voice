from dragonfly import Choice, MappingRule, Key, RuleRef, Text, Dictation, IntegerRef
from ..choices.letter import letterChoice


class CommandModeStartRule(MappingRule):
    mapping = {
        "exec": Key("colon"),
        "exec shell": Text(":!"),
        "exec read": Text(":r "),
        "exec read shell": Text(":r!"),
        "exec save as": Text(":sav "),
        "exec rename": Text(":Rename "),
        "exec move": Text(":Move "),
        "exec lock": Text(":ldo "),
        "exec fix": Text(":cdo "),
        "exec buffers": Text(":bufdo "),
        "exec windows": Text(":windo "),
        "exec call": Text(":call "),
        "exec echo": Text(":echom "),
        "exec set": Text(":set "),
        "exec let": Text(":let "),
        "exec CD": Text(":cd "),
        "exec local CD": Text(":lcd "),
        "exec sort": Text(":sort "),
        "exec source": Text(":source "),

        "exec tab": Text(":tabe "),
        "exec file": Text(":e "),
        "exec split": Text(":sp "),

        # TODO: Should have its own bootstrap and mode, maybe?
        "exec search": Text("/"),
        "exec (restrict | include)": Text(":g//") + Key('left'),
        "exec exclude": Text(":v//") + Key('left'),

        "exec subvert": Text(":Subvert///") + Key('left:2'),
    }


class CommandModeFinishRule(MappingRule):
    mapping = {
        "okay | kay": Key("escape"),
        "cancel | oops": Key("escape, u"),
    }


class CommandModeCommands(MappingRule):
    mapping = {
        "read": Text("r "),
        "help": Text("help "),
        "file glob": Text("*/**"), # see `starstar`

        # Ex mode commands (see :exu for complete list):
        "X delete": Key("d"),
        "X append": Key("a"),
        "X change": Key("c"),
        "X insert": Key("i"),
        "X join": Key("j"),
        "X copy": Key("c, o"),
        "X move": Key("m"),
        "X put": Key("p"),
        "X yank": Key("y"),
        "X sub": Text("s/"),

        # Basic readline:
        "go start": Key("home"),
        "go end": Key("end"),

        # languages
        "python": Text('python'),

        "up": Key("up"),
        "down": Key("down"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),
        "[<n>] word left": Key("s-left:%(n)d"),
        "[<n>] word right": Key("s-right:%(n)d"),
        "scratch": Key("c-w"),
        "scratch all": Key("c-u"),

        # Pasting info in:
        "paste sys": Key("c-r, asterisk"),
        "paste file": Key("c-r, percent"),
        "paste search": Key("c-r, slash"),

        "paste word": Key("c-r, c-w"), # 'iw' under cursor
        "paste big word": Key("c-r, c-a"), # 'iW' under cursor
        "paste selection": Key("c-y"), # modeless selection

        "shift left": Key("c-t"),
        "shift right": Key("c-d"),

        # Completion:
        "[<n>] match down": Key("c-n"),
        "[<n>] match up": Key("c-p"),

        # TODO: Ranges
        "range all": Key("home, percent, end"),
    }
    extras = [
        letterChoice("letter"),
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }
