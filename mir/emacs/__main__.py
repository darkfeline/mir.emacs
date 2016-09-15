import asyncio
import curses
import logging

from mir.emacs import buffer

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level='DEBUG')

    cwindow = curses.initscr()
    buf = buffer.Buffer()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(get_key(buffer.Window(cwindow, buf)))
    except Exception:
        logger.exception('Uncaught exception')
    finally:
        loop.close()


async def get_key(window):
    cwindow = window.cwindow
    buf = window.buffer
    while True:
        char = cwindow.getkey()
        if char == 'q':
            break
        else:
            await process_char(buf, char)


async def process_char(buf, char):
    buf.insert_char(len(buf), char)

if __name__ == '__main__':
    main()
