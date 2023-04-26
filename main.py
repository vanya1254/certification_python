# import controller
#
# cr = controller.Controller()
# cr.start()
import controller


class Main():

    def __init__(self):
        self.cr = controller.Controller()
        self.cr.start()