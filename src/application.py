from execute_domain \
    import Execution


class Application:
    def __init__(self, mode):
        self.mode = None

        # making calls
        self.set_mode(mode)

    def execute(self):
        if not self.is_mode_empty():
            self.get_mode().execute()

    def clean(self):
        pass

    def is_mode_empty(self) -> bool:
        return self.mode is None

    def get_mode(self) -> Execution:
        return self.mode

    def set_mode(
            self,
            value: Execution
    ) -> None:
        self.mode = value
