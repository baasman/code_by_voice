from dragonfly import *
from cmd_rules.rules.general import file_extensions_rule, general_rule, LetterSequenceRule

cmd_context = AppContext(executable="cmd")

grammar = Grammar('cmd', context=cmd_context)


grammar.add_rule(general_rule)
grammar.add_rule(file_extensions_rule)
grammar.add_rule(LetterSequenceRule())
grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None