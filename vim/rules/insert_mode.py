from dragonfly import CompoundRule, Choice
from ..choices.insert import insert_start_commands, insert_end_commands


class _InsertModeEnabler(CompoundRule):
    spec = "<command>"
    extras = [Choice("command", insert_start_commands)]


class _InsertModeDisabler(CompoundRule):
    spec = "<command>"
    extras = [Choice("command", insert_end_commands)]
