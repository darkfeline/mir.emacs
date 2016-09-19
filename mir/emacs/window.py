class CursesWindow:

    """curses Window + Buffer.

    Args:
        cwindow: curses Window object.
        buffer: Buffer instance.

    """

    WIDTH = 80
    HEIGHT = 24

    def __init__(self, cwindow, buffer):
        self._cwindow = cwindow
        self.buffer = buffer

    def getkey(self):
        return self._cwindow.getkey()

    def refresh(self):
        """Refresh window to match buffer."""
        cwindow = self._cwindow
        buffer = self.buffer
        length = len(buffer)
        for i, coord in enumerate(
                (y, x)
                for y in range(self.HEIGHT)
                for x in range(self.WIDTH)):
            if i >= length:
                break
            y, x = coord
            cwindow.addch(y, x, buffer[i])
        cwindow.refresh()
