from dragonfly import *

from vim.rules.buffer import BufferRule
from vim.rules.normal_navigation import NormalModeKeystrokeRule
from vim.rules.insert_mode import _InsertModeEnabler, _InsertModeDisabler
from vim.rules.insert_commands import InsertRules
from vim.rules.window import WindowRule
from vim.rules.tabs import TabRule
from vim.rules.letter import LetterSequenceRule
from vim.rules.command_mode import CommandModeStartRule, CommandModeFinishRule, CommandModeCommands
from vim.plugins.netrw import NetrwRule
from vim.plugins.csv import CSVRule
from vim.plugins.fugutive import FugitiveRule
from vim.plugins.easymotion import EasyMotionRule
from vim.plugins.nerdtree import NERDTreeRule


try:
    import pkg_resources
    pkg_resources.require("dragonfly >= 0.6.5beta1.dev-r99")
except ImportError:
    pass

print 'gvim grammer accessed'

release = Key("shift:up, ctrl:up")

normal_mode_multiple = [
    RuleRef(rule=NormalModeKeystrokeRule())
]

normal_mode_single = Alternative(normal_mode_multiple)
normal_mode_multiple_action = Repetition(normal_mode_single, min=1, max=16,
                                         name='normal_mode_multiple_action')

class NormalModeRepeatRule(CompoundRule):

    spec     = "<normal_mode_multiple_action> [[[and] repeat [that]] <n> times]"
    extras   = [
            normal_mode_multiple_action,
            IntegerRef("n", 1, 100),
        ]
    defaults = {
            "n": 1,
        }
    def _process_recognition(self, node, extras):
        normal_mode_sequence = extras["normal_mode_multiple_action"]
        count = extras["n"]
        for i in range(count):
            for action in normal_mode_sequence:
                action.execute()
        release.execute()

# ---------------------------

normal_single_rules = [
    RuleRef(rule=BufferRule()),
    RuleRef(rule=NetrwRule()),
    RuleRef(rule=CSVRule()),
    RuleRef(rule=NERDTreeRule()),
    RuleRef(rule=FugitiveRule()),
    RuleRef(rule=EasyMotionRule()),
    RuleRef(rule=WindowRule()),
    RuleRef(rule=TabRule())
]

normal_single_action = Alternative(normal_single_rules,
                                   name='normal_mode_single_action')

class NormalModeSingleAction(CompoundRule):
    spec = "<normal_mode_single_action>"
    extras = [ normal_single_action ]
    def _process_recognition(self, node, extras):
        action = extras["normal_mode_single_action"]
        action.execute()
        release.execute()

# ------------------------------------

insert_single_rules = [
    RuleRef(rule=InsertRules())
]

insert_single_action = Alternative(insert_single_rules,
                                   name='insert_mode_single_action')

class InsertModeSingleAction(CompoundRule):
    spec = "<insert_mode_single_action>"
    extras = [ insert_single_action ]
    def _process_recognition(self, node, extras):
        print extras
        action = extras["insert_mode_single_action"]
        action.execute()
        release.execute()

class InsertModeEnable(_InsertModeEnabler):

    def _process_recognition(self, node, extras):
        InsertModeBootstrap.disable()
        normalModeGrammar.disable()
        InsertModeGrammar.enable()

        for string in extras['command'].split(','):
            key = Key(string)
            key.execute()

        super(self.__class__, self)._process_recognition(node, extras)
        print '\n(Insert Mode)'


class InsertModeDisable(_InsertModeDisabler):

    def _process_recognition(self, node, extras):
        InsertModeGrammar.disable()
        InsertModeBootstrap.enable()
        normalModeGrammar.enable()

        Key("escape").execute()
        if extras["command"] == "cancel":
            Key("u").execute()
            print "Insert command canceled"

        super(self.__class__, self)._process_recognition(node, extras)
        print '\n(Normal mode)'


# ------------------------------------

class CommandModeEnabler(CommandModeStartRule):
    def _process_recognition(self, node, extras):
        commandModeBootstrap.disable()
        normalModeGrammar.disable()
        commandModeGrammar.enable()
        super(self.__class__, self)._process_recognition(node, extras)
        print "\n(EX MODE)"

class CommandModeDisabler(CommandModeFinishRule):
    def _process_recognition(self, node, extras):
        commandModeGrammar.disable()
        commandModeBootstrap.enable()
        normalModeGrammar.enable()
        super(self.__class__, self)._process_recognition(node, extras)
        print "\n(NORMAL)"

# global vim context
gvim_context = AppContext(executable="gvim")
# gvim_context = AppContext(executable="VirtualBox")

# normal mode
normalModeGrammar = Grammar("gvim", context=gvim_context)
normalModeGrammar.add_rule(NormalModeRepeatRule())
normalModeGrammar.add_rule(NormalModeSingleAction())
normalModeGrammar.load()

# insert mode
InsertModeBootstrap = Grammar("InsertMode Bootstrap", context=gvim_context)
InsertModeBootstrap.add_rule(InsertModeEnable())
InsertModeBootstrap.load()

InsertModeGrammar = Grammar("InsertMode grammar", context=gvim_context)
InsertModeGrammar.add_rule(InsertModeDisable())
InsertModeGrammar.add_rule(LetterSequenceRule())
InsertModeGrammar.add_rule(InsertModeSingleAction())
InsertModeGrammar.load()
InsertModeGrammar.disable()

commandModeBootstrap = Grammar("Command Mode bootstrap", context=gvim_context)
commandModeBootstrap.add_rule(CommandModeEnabler())
commandModeBootstrap.load()

commandModeGrammar = Grammar("Command Mode grammar", context=gvim_context)
commandModeGrammar.add_rule(CommandModeDisabler())
commandModeGrammar.add_rule(CommandModeCommands())
commandModeGrammar.load()
commandModeGrammar.disable()

def unload():
    global normalModeGrammar
    if normalModeGrammar: normalModeGrammar.unload()
    normalModeGrammar = None

    global InsertModeGrammar
    if InsertModeGrammar: InsertModeGrammar.unload()
    InsertModeGrammar = None

    global commandModeGrammar
    if commandModeGrammar: commandModeGrammar.unload()
    commandModeGrammar = None
