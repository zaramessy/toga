from .window import Window


class MainWindow(Window):
    pass


class App(object):
    def __init__(self, name, app_id):
        self.main_window = MainWindow()

    def main_loop(self):
        pass
