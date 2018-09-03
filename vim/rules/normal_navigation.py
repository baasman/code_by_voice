from dragonfly import (
    MappingRule,
    Key,
    Text,
    Function,
    IntegerRef,
    Dictation
)
from ..choices.letter import letterChoice
from ..config import leader
# from .letter import letter, letter_sequence
#
# def execute_letter(letter):
#     letter.execute()


class NormalModeKeystrokeRule(MappingRule):
    exported = False

    mapping = {
        "[<n>] up": Key("k:%(n)d"),
        "[<n>] down": Key("j:%(n)d"),
        "[<n>] left": Key("h:%(n)d"),
        "[<n>] right": Key("l:%(n)d"),
        "[<n>] go up": Key("c-b:%(n)d"),
        "[<n>] go down": Key("c-f:%(n)d"),

        "[<n>] scroll up": Key("c-y:%(n)d"),
        "[<n>] scroll down": Key("c-e:%(n)d"),

        "hat": Key("caret"),
        "rest": Key("dollar"),
        "match": Key("percent"),
        "doc home": Key("c-home"),
        "doc end": Key("c-end"),

        "lower case": Key("g,u"),
        "upper case": Key("g,U"),
        "swap case": Key("tilde"),

        "visual": Key("v"),
        "visual line": Key("s-v"),
        "visual block": Key("c-v"),
        "visual select all": Key("g,g,V,G"),

        "next occurrence": Key("asterisk"),
        "next": Key("n"),
        "previous": Key("N"),
        "[<n>] back": Key("b:%(n)d"),
        "[<n>] whiskey": Key("w:%(n)d"),
        "[<n>] end": Key("e:%(n)d"),

        "Center": Key("z,dot"),
        "format": Key("g,q"),

        "next paragraph": Key("rbrace"),
        "previous paragraph": Key("lbrace"),
        "a paragraph": Key("a,p"),
        "inner paragraph": Key("i,p"),

        "[<n>] X.": Key("x:%(n)d"),
        "[<n>] backspace": Key("backspace:%(n)d"),

        "[<n>] Pete macro": Key("at,at:%(n)d"),

        "[<n>] join": Key("J:%(n)d"),

        "(delete | D.)": Key("d"),
        "[<n>] (delete | D.) (whiskey|word)": Text("%(n)ddw"),
        "(delete | D.) a (whiskey | word)": Key("d,a,w"),
        "(delete | D.) inner (whiskey | word)": Key("d,i,w"),
        "(delete | D.) a paragraph": Key("d,a,p"),
        "(delete | D.) inner paragraph": Key("d,i,p"),
        "(delete | D.) a (paren|parenthesis|raip|laip)": Key("d,a,rparen"),
        "(delete | D.) inner (paren|parenthesis|raip|laip)": Key("d,i,rparen"),
        "(delete | D.) a (bracket|rack|lack)": Key("d,a,rbracket"),
        "(delete | D.) inner (bracket|rack|lack)": Key("d,i,rbracket"),
        "(delete | D.) a (bracket|race|lace)": Key("d,a,rbrace"),
        "(delete | D.) inner (bracket|race|lace)": Key("d,i,rbrace"),

        "(delete | D.) character": Key("x"),
        "(delete | D.) line": Key("d,d"),
        "(delete | D.) end": Key("d,e"),

        "[<n>] (increment|increase)": Key("c-a:%(n)d"),
        "[<n>] (decrement|decrease)": Key("c-x:%(n)d"),

        "shift (delete | D.)": Key("s-d"),

        "[<n>] undo": Key("u:%(n)d"),
        "[<n>] redo": Key("c-r:%(n)d"),

        # '[<n>] find <letter>': Text('%(n)df') + Function(execute_letter),
        # '[<n>] shift find <letter>': Text('%(n)dF') + Function(execute_letter),
        # 'find [<n>] <letter>': Text('%(n)df') + Function(execute_letter),
        # 'shift find [<n>] <letter>': Text('%(n)dF') + Function(execute_letter),
        #
        # '[<n>] again': Text('%(n)d;'),
        # '[<n>] shift again': Text('%(n)d,'),
        #
        # '[<n>] until <letter>': Text('%(n)dt') + Function(executeLetter),
        # '[<n>] shift until <letter>': Text('%(n)dT') + Function(executeLetter),
        # 'until [<n>] <letter>': Text('%(n)dt') + Function(executeLetter),
        # 'shift until [<n>] <letter>': Text('%(n)dT') + Function(executeLetter),

        "(yank | copy)": Key("y"),
        "(yank | copy) a paragraph": Key("y,a,p"),
        "(yank | copy) inner paragraph": Key("y,i,p"),
        "(yank | copy) inner word": Key("y,i,w"),
        "(yank | copy) a (paren|parenthesis|raip|laip)": Key("y,a,rparen"),
        "(yank | copy) inner (paren|parenthesis|raip|laip)": Key("y,i,rparen"),
        "shift (yank | copy)": Key("Y"),
        "copy line": Key("y,y"),
        "yank end": Key("y,e"),
        "yank rest": Key("y,dollar"),

        # always yank in register k
        "register yank": Key('quote, k, y'),

        "paste": Key("p"),
        "shift paste": Key("P"),

        "replace": Key("r"),
        "shift replace": Key("R"),

        "shift left": Key("langle,langle"),
        "shift right": Key("rangle,rangle"),

        "fuzzy find": Key("backslash,t"),

        # used in Jedi vim
        "go to definition": Key("backslash,d"),

        # Pete is shorthand for repeat
        "[<n>] Pete": Key("dot:%(n)d"),

        "go first line": Key("g,g"),
        "go last line": Key("G"),
        "go old": Key("c-o"),

        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # line navigation
        "go <line>": Key("colon") + Text("%(line)s\n"),

        # searching
        # "search <text>": Key("slash") + Text("%(text)s\n"),
        "search this": Key("asterisk"),
        # "back search <text>": Key("question") + Text("%(text)s\n"),

        "cancel": Key('escape'),

        "last edit": Key("dot"),

        "toggle comment": Key("comma, c, space"),

        "paste clip": Key("quote, plus, g, P"),

        "run selection": Key("%s, k" % leader),

        "run last process": Key("%s, b" % leader),

    }
    extras = [
        # letter,
        # letter_sequence,
        IntegerRef("n", 1, 100),
        IntegerRef("line", 1, 10000),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }
