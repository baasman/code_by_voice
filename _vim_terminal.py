from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)


class TerminalEnabler(CompoundRule):
    spec = "Enable terminal grammar"  # Spoken command to enable the Python grammar.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        vimTerminalBootstrap.disable()
        terminalGrammer.enable()
        print "terminal grammar enabled!"


class TerminalDisabler(CompoundRule):
    spec = "disable terminal grammar"  # spoken command to disable the Python grammar.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        terminalGrammer.disable()
        vimTerminalBootstrap.enable()
        print "terminal grammar disabled"


class TerminalCommands(MappingRule):

    extras = [
            Dictation('text')
    ]

    mapping = {
        "terminal up": Key("up"),

        "terminal python": Text("python") + Key('enter'),
        "terminal python three": Text("python3") + Key('enter'),
        "terminal ipython": Text("ipython") + Key('enter'),
        "terminal python quit": Text("quit()") + Key('enter'),

        # pip stuff
        "terminal pip": Text("pip3"),
        "terminal pip install": Text("pip3 install "),
        "terminal pip list": Text("pip3 list") + Key('enter'),

        # directory stuff
        "terminal change": Text("cd "),
        "terminal directory": Text("ls") + Key("enter"),
        "terminal back": Text("cd ..") + Key("enter"),
        "[sudo] terminal move": Text("mv  "),
        "[sudo] terminal make directory": Text("mkdir "),
        "terminal open vim": Text("vim") + Key("enter"),

        # general unix commands
        "terminal top": Text("top") + Key("enter"),
        "terminal quit": Key("q"),
        "terminal search": Key("c-r"),

        # grep unix commands
        "terminal grep <text>": Text("grep -nr %(text)s .") + Key("enter"),

        # interaction
        "paste from register": Key("c-w, quote, k"),

        # debugger options
        "debug next": Text("n") + Key("enter"),
        "debug quit": Text("quit()") + Key("enter"),
        "debug continue": Text("c") + Key("enter"),

        # process stuff
        "terminal close process": Key("c-c"),
        "terminal go background": Key('c-z'),
        "terminal go foreground": Text('fg') + Key("enter"),

        # misc
        "terminal activate environment windows": Text("venv\\Scripts\\activate") + Key("enter"),
        "terminal activate environment unix": Text("source venv/bin/activate") + Key("enter"),
        "terminal set ex": Text("setx "),

        "terminal exit mode": Key("c-w, q, exclamation"),
        "terminal normal mode": Key("c-w, N"),
        "terminal insert mode": Key("i"),
        "terminal bash": Text("c:\\cygwin64\\bin\\bash\\bash.exe --login -i") + Key("enter"),

        "window left": Key("c-w,h"),
        "window right": Key("c-w,l"),
        "window up": Key("c-w,k"),
        "window down": Key("c-w,j"),

        "terminal tabulator next": Key("c-w") + Text(":tabn") + Key('enter'),
        "terminal tabulator previous": Key("c-w") + Text(":tabp") + Key('enter'),

    }

# The main Python grammar rules are activated here
vimTerminalBootstrap = Grammar("vim terminal bootstrap")
vimTerminalBootstrap.add_rule(TerminalEnabler())
vimTerminalBootstrap.load()

terminalGrammer = Grammar("terminal grammar")
terminalGrammer.add_rule(TerminalCommands())
terminalGrammer.add_rule(TerminalDisabler())
terminalGrammer.load()
terminalGrammer.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global terminalGrammer
    if terminalGrammer: terminalGrammer.unload()
    terminalGrammer = None
