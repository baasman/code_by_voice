from dragonfly import MappingRule, Key, Text, RuleRef, Alternative, Repetition, CompoundRule
from ..choices.letter import letterChoice

general_rule = MappingRule(
    name = "general",
    mapping = {
        "cancel": Key("c-c"),
        "kay": Key("enter"),
        "left": Key("left"),
        "right": Key("right"),
        "up": Key("up"),
        "down": Key("down"),
    },
)

file_extensions_rule = MappingRule(
    name = "file extensions",
    mapping = {
        "dot jay": Text(".json"),
        "dot pie": Text(".py"),
    },
    extras = [
    ],
)


commands = MappingRule(
    name = "cmd-commands",
    mapping = {
        "P. W. D.": Text("dir\n"),
        "CD dot dot": Text("cd ..\n"),
		"CD double dot": Text("cd ..\n"),
		"CD triple dot": Text("cd ../..\n"),

        "make directory ": Text("mkdir "),

        "remove directory": Text('rd -r ')
    },
    extras = [
    ],
)


class LetterRule(MappingRule):
    mapping = {
        "<letter>": Key("%(letter)s"),

    }
    extras = [
        letterChoice("letter"),
    ]

letter = RuleRef(rule = LetterRule(), name='letter')

letter_sequence = Repetition(
    Alternative([letter]),
    min=1,max=12, name="letter_sequence")

class LetterSequenceRule(CompoundRule):
    spec     = "<letter_sequence>"
    extras   = [ letter_sequence ]
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        letter_sequence = extras["letter_sequence"]
        # An integer repeat count.
        for letter in letter_sequence:
            letter.execute()
        Key("shift:up, ctrl:up").execute()
