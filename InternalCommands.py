import gdb
import GDBDataInterface
import matplotlib.pyplot as plt


class Plot(gdb.Command):
    def __init__(self):
        super(Plot, self).__init__("plot", gdb.COMMAND_OBSCURE)

    def invoke(self, arguments: str, from_tty: bool) -> None:
        legend = []
        plt.legend = legend
        for argument in arguments.split():
            self.extractor = GDBDataInterface(argument)
            data = self.extractor()