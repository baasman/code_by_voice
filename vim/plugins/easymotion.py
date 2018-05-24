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
        motionChoice('motion'),
        letterChoice("letter"),
        findChoice('find')
    ]
