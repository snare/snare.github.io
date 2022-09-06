import voltron
from voltron.plugin import CommandPlugin
from voltron.command import VoltronCommand


class LLDBHelloCommand(VoltronCommand):
    def invoke(self, *args):
        print("Debugger host: {}".format(voltron.debugger.host))
        print("Do an LLDB thing: {}".format(voltron.debugger.host.GetVersionString()))


class LLDBHelloCommandPlugin(CommandPlugin):
    name = 'lldbhello'
    command_class = LLDBHelloCommand