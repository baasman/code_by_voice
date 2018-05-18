from dragonfly import MappingRule, Key, Text, IntegerRef
from ..config import leader
from ..choices.letter import letterChoice
from ..choices.find import findChoice
from ..choices.motion import motionChoice


class EasyMotionRule(MappingRule):
    mapping = {
        "queasy <motion>": Key("{}, {}, %(motion)s".format(leader, leader)),
        "queasy <find>": Key("{}, {}, %(find)s".format(leader, leader)),
        "<letter>": Key("%(letter)s"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        motionChoice('motion'),
        letterChoice("letter"),
        findChoice('find')
    ]
    defaults = {
        'n': 1,
    }
