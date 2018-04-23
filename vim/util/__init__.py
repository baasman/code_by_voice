from dragonfly import Grammar, CompoundRule


class PythonEnabler(CompoundRule):
    spec = "Enable Python"  # Spoken command to enable the Python grammar.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        pythonBootstrap.disable()
        pythonGrammar.enable()
        print "Python grammar enabled"


class PythonDisabler(CompoundRule):
    spec = "switch language"  # spoken command to disable the Python grammar.

    def _process_recognition(self, node, extras):  # Callback when command is spoken.
        pythonGrammar.disable()
        pythonBootstrap.enable()
        print "Python grammar disabled"


pythonBootstrap = Grammar("python bootstrap")
pythonBootstrap.add_rule(PythonEnabler())
pythonBootstrap.load()

pythonGrammar = Grammar("python grammar")
pythonGrammar.load()
pythonGrammar.disable()

def unload():
    global pythonGrammar
    if pythonGrammar: pythonGrammar.unload()
    pythonGrammar = None