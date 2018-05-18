from dragonfly import MappingRule, Key, Text, IntegerRef
from ..config import leader
from ..choices.letter import letterChoice


class EasyMotionRule(MappingRule):
    mapping = {
        "easy whiskey": Key("%s, %s, w" % (leader, leader)),
        "<letter>": Key("%(letter)s"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        letterChoice("letter"),
    ]
    defaults = {
        'n': 1,
    }
