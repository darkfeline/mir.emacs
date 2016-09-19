import asyncio
import curses
import logging

from mir.emacs import buffer as buffer_mod
from mir.emacs import window as window_mod

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level='DEBUG')

    cwindow = curses.initscr()
    curses.noecho()
    curses.nonl()
    curses.raw()
    buffer = buffer_mod.Buffer()
    window = window_mod.CursesWindow(cwindow, buffer)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(get_key(window))
    except Exception:
        logger.exception('Uncaught exception')
    finally:
        loop.close()


async def get_key(window):
    buffer = window.buffer
    while True:
        char = window.getkey()
        if char == 'q':
            break
        if char == 'w':
            pass
        else:
            await process_char(buffer, char)
            window.refresh()


async def process_char(buffer, char):
    buffer.insert_char(len(buffer), char)
