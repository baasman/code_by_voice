from dragonfly import MappingRule, CompoundRule, Key, IntegerRef, RuleRef, Text, Repetition, Alternative, Dictation
from ..choices.letter import letterChoice

class LetterRule(MappingRule):
    mapping = {
        "<letter>": Key("%(letter)s"),

        # jedi
        "complete": Key('c-space'),
        "[<n>] up": Key("up:%(n)d"),
        "[<n>] down": Key("down:%(n)d"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),

        "<text>": Text("%(text)s"),
    }
    extras = [
        letterChoice("letter"),
        IntegerRef("n", 1, 100),
        Dictation('text')
    ]

letter_sequence = Repetition(
    Alternative([RuleRef(rule = LetterRule())]),
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