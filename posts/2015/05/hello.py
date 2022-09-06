import voltron
from voltron.plugin import CommandPlugin
from voltron.command import VoltronCommand


class HelloCommand(VoltronCommand):
    def invoke(self, *args):
        print('ohai ^_^')


class HelloCommandPlugin(CommandPlugin):
    name = 'hello'
    command_class = HelloCommand