class EventHandler:
    def __init__(self):
        self._handlers = {
            "on_mouse_move": []
        }

    def on_mouse_move(self, panel, x, y):
        for handler in self._handlers["on_mouse_move"]:
            handler(panel, x, y)

    def __call__(self, handler):
        name = handler.__name__
        if not name in self._handlers:
            raise KeyError("Unknown event type.")
        self._handlers[name].append(handler)
