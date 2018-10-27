from dragonfly import (Grammar, CompoundRule, Dictation, Text, Key, AppContext, MappingRule)


class PythonEnabler(CompoundRule):
    spec = "Enable Python"

    def _process_recognition(self, node, extras):
        pythonBootstrap.disable()
        pythonGrammar.enable()
        print "Python grammar enabled!"


class PythonDisabler(CompoundRule):
    spec = "disable python"

    def _process_recognition(self, node, extras):
        pythonGrammar.disable()
        pythonBootstrap.enable()
        print "Python grammar disabled"


class PythonControlStructures(MappingRule):
    mapping = {
        "if": Text("if cond:") + Key("enter"),
        "for loop": Text("for i in iter:") + Key("enter"),
        "function": Text("def function():") + Key("enter"),
        "class": Text("class cls(object):") + Key("enter"),
        "init": Text("def __init__(self):") + Key("enter"),
        "main": Text("if __name__ == '__main__':") + Key("enter"),

    }


class PythonUsefulCommands(MappingRule):
    mapping = {
        "import pandas": Text("import pandas as pd") + Key("enter"),
        "import numpy": Text("import numpy as np") + Key("enter"),
        "import plot": Text("import matplotlib.pyplot as plt") + Key("enter"),

        # pandas
        "pandas": Text("pd"),
        "pandas head": Text(".head()"),

        # numpy
        "numpy": Text("np"),

        # matplotlib
        "show plot": Text("plt.show()"),
    }


# The main Python grammar rules are activated here
pythonBootstrap = Grammar("python bootstrap")
pythonBootstrap.add_rule(PythonEnabler())
pythonBootstrap.load()

pythonGrammar = Grammar("python grammar")
pythonGrammar.add_rule(PythonControlStructures())
pythonGrammar.add_rule(PythonUsefulCommands())
pythonGrammar.add_rule(PythonDisabler())
pythonGrammar.load()
pythonGrammar.disable()


# Unload function which will be called by natlink at unload time.
def unload():
    global pythonGrammar
    if pythonGrammar: pythonGrammar.unload()
    pythonGrammar = None
