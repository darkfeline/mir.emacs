class Buffer:

    """A text buffer."""

    def __init__(self):
        self._buffer = []

    def __len__(self):
        return len(self._buffer)

    def __getitem__(self, i):
        return self._buffer(i)

    def insert_char(self, i, s):
        self._buffer.insert(i, s)


class Window:

    """curses Window + Buffer."""

    WIDTH = 80
    HEIGHT = 24

    def __init__(self, cwindow, buffer):
        self.cwindow = cwindow
        self.buffer = buffer

    def refresh(self):
        """Refresh window to match buffer."""
        cwindow = self.cwindow
        buffer = self.buffer
        length = len(buffer)
        for i, coord in enumerate(
                (y, x)
                for y in range(self.HEIGHT)
                for x in range(self.WIDTH)):
            if i >= length:
                break
            y, x = coord
            cwindow.adch(y, x, buffer[i])
        cwindow.refresh()
