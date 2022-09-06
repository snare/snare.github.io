from voltron.view import TerminalView
from voltron.plugin import ViewPlugin


class ExampleView(TerminalView):
    def render(self, *args, **kwargs):
        # Perform the request
        res = self.client.perform_request('registers')
        if res.is_success:
            # Process the registers and set the body to the formatted list
            reg_list =  ['rax','rbx','rcx','rdx','rbp','rsp','rdi','rsi','rip',
                         'r8','r9','r10','r11','r12','r13','r14','r15']
            lines = map(lambda x: '{:3}: {:016X}'.format(x, res.registers[x]), reg_list)
            self.body = '\n'.join(lines)
        else:
            self.body = "Failed to get registers: {}".format(res)

        # Set the title and info
        self.title = '[example]'
        self.info = 'some infoz'

        # Let the parent do the rendering
        super(ExampleView, self).render()


class ExampleViewPlugin(ViewPlugin):
    name = 'example'
    view_class = ExampleView
