from dragonfly import MappingRule, Key, Text

class WindowRule(MappingRule):
    name = "gvim_window"
    mapping = {
          # window navigation commands
          "window left": Key("c-w,h"),
          "window right": Key("c-w,l"),
          "window up": Key("c-w,k"),
          "window down": Key("c-w,j"),
          "increase window vertical": Key("colon") + Text('res +10') + Key('enter'),

          # window creation commands
          "window split": Key("c-w,s"),
          "window vertical split": Key("c-w,v"),
    }
    extras = [
    ]
