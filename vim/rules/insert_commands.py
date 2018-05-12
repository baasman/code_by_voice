from dragonfly import MappingRule, Key, Text, IntegerRef, Dictation
from vim.choices.letter import WordChoice


class InsertRules(MappingRule):
    mapping = {
        # "[<n>] up": Key("up:%(n)d"),
        # "[<n>] down": Key("down:%(n)d"),
        # "[<n>] left": Key("left:%(n)d"),
        # "[<n>] right": Key("right:%(n)d"),
        "slap": Key("enter"),

        "(scratch|delete)": Key("c-w"),
        "tab": Key("tab"),
        "backspace": Key("backspace"),
        "(scratch|delete) line": Key("c-u"),

        "<text>": Text("%(text)s"),

        "insert breakpoint": Text('import pdb; pdb.set_trace()'),

        # ctrlp commands
        # TODO: this should be own mode
        "open tabulator": Key('c-t'),
        "open vertical split": Key('c-v'),
        "open horizontal split": Key('c-x'),
        "switch buffer": Key('c-b'),
        "switch file": Key('c-f'),

        # common python words

    }
    extras = [
        Dictation('text')
    ]


class CommonInsertWordsRule(MappingRule):
    mapping = {
        "<word>": Key("%(word)s"),
    }
    extras = [
        WordChoice("word"),
    ]
