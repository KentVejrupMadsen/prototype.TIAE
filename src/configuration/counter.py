class Counter:
    def __init__(
            self,
            value: int = 0
    ):
        self.current_value = value

    def increase(
            self,
            value: int = 1
    ) -> None:
        self.set_value(
            self.get_value() + value
        )

    def decrease(
            self,
            value: int = 1
    ) -> None:
        self.set_value(
            self.get_value() - value
        )

    def increment(self) -> None:
        self.increase()

    def decrement(self) -> None:
        self.decrease()

    def get_value(self) -> int:
        return self.current_value

    def set_value(
            self,
            value: int
    ) -> None:
        self.current_value = value

    def pass_boundary(
            self,
            n: int
    ) -> bool:
        if self.get_value() == 0:
            return False

        if self.get_value() % n == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(
            self.current_value
        )

