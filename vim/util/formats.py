from dragonfly import MappingRule, Dictation, Function, Text


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
    return '_'.join(str(dictation).split(' ')) + '()'


@format
def camel_case(dictation):
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
