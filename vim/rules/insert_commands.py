from dragonfly import MappingRule, Key, Text, IntegerRef, Dictation, Function
from vim.choices.letter import WordChoice

def format(format_function):
    def _format(dictation):
        text = format_function(dictation)
        Text(text).execute()
    return Function(_format)


@format
def snake_case(dictation):
    response = '_'.join(str(dictation).split(' '))
    return response


@format
def snake_case_function(dictation):
    return '_'.join(str(dictation).split(' ')) + "()"


@format
def camel_case(dictation):
    print(''.join([i.capitalize() for i in str(dictation)]))
    return ''.join([i.capitalize() for i in str(dictation)])


@format
def camel_case_rest(dictation):
    return ''.join([word.capitalize() if idx != 0 else word
                    for idx, word in enumerate(str(dictation))])


@format
def upper(dictation):
    return str(dictation).upper()


@format
def one_word(dictation):
    return str(dictation).replace(' ', '')

class InsertRules(MappingRule):
    mapping = {
        "[<n>] up": Key("up:%(n)d"),
        "[<n>] down": Key("down:%(n)d"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),
        "slap": Key("enter"),

        "(scratch|delete)": Key("c-w"),
        "tab": Key("tab"),
        "backspace": Key("backspace"),
        "(scratch|delete) line": Key("c-u"),

        "<text>": Text("%(text)s"),

        "insert breakpoint": Text('import pdb; pdb.set_trace()'),

        # ctrlp commands
        "open tabulator": Key('c-t'),
        "open vertical split": Key('c-v'),
        "open horizontal split": Key('c-x'),
        "switch buffer": Key('c-b'),
        "switch file": Key('c-f'),

        # formatting
        'snake <dictation>': snake_case,
        'snake function <dictation>': snake_case_function,
        'camel <dictation>': camel_case,
        'camel rest <dictation>': camel_case_rest,
        'upper <dictation>': upper,
        'one word <dictation>': one_word,
    }
    extras = [
        Dictation('text'),
        Dictation('dictation'),
        IntegerRef("n", 1, 100),
    ]


class CommonInsertWordsRule(MappingRule):
    mapping = {
        "<word>": Key("%(word)s"),
    }
    extras = [
        WordChoice("word"),
    ]
