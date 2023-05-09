import gi

gi.require_version("Notify", "0.7")
from gi.repository import Notify


class Notification:
    def __init__(self) -> None:
        Notify.init("Glasses check")

    def display(self, name: str):
        notification = Notify.Notification.new(
            "Glasses check", f"Put on your glasses, {name}!", "dialog-warning"
        )
        # notification.set_timeout(0)
        notification.set_urgency(2)
        notification.show()
