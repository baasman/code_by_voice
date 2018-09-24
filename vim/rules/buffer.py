from dragonfly import MappingRule, Key, Text, Dictation


class BufferRule(MappingRule):
    mapping = {
        "file save": Key("colon, w, exclamation, enter"),
        "file save all": Key("colon, w, a, exclamation, enter"),
        "file quit": Key("colon, q, exclamation, enter"),
        "file quit all": Key("colon, q, a, exclamation, enter"),
        "file done": Key("colon, x, exclamation, enter"),
        "file done all": Key("colon, x, a, exclamation, enter"),
        "file reload": Key("colon, e, exclamation, enter"),
        "file open [<text>]": Key("colon, e") + Text(" <text>"),

        "buffer next": Key('colon, b, n, e, x, t, enter'),
        "buffer previous": Key('colon, b, p, r, e, v, i, o, u, s, enter'),
        "buffer show all": Key('colon, l, s'),
    }
    extras = [
        Dictation("text"),
    ]
    defaults = {
        "text": "",
    }

