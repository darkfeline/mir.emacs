class Buffer:

    """A text buffer."""

    def __init__(self):
        self._buffer = []

    def __len__(self):
        return len(self._buffer)

    def __getitem__(self, i):
        return self._buffer[i]

    def insert_char(self, i, s):
        self._buffer.insert(i, s)
