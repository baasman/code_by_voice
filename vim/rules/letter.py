from dragonfly import MappingRule, CompoundRule, Key, IntegerRef, RuleRef, Text, Repetition, Alternative, Dictation
from ..choices.letter import letterChoice

class LetterRule(MappingRule):
    mapping = {
        "<letter>": Key("%(letter)s"),

        # jedi
        "complete": Key('c-p'),
        "[<n>] up": Key("up:%(n)d"),
        "[<n>] down": Key("down:%(n)d"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),
    }
    extras = [
        letterChoice("letter"),
        IntegerRef("n", 1, 100),
    ]

letter = RuleRef(rule=LetterRule(), name='letter')

letter_sequence = Repetition(
    Alternative([letter]),
    min=1, max=12, name="letter_sequence")


class LetterSequenceRule(CompoundRule):
    spec = "<letter_sequence>"
    extras = [letter_sequence]

    def _process_recognition(self, node, extras):
        letter_sequence = extras["letter_sequence"]
        for letter in letter_sequence:
            letter.execute()
        Key("shift:up, ctrl:up").execute()
