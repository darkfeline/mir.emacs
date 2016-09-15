import asyncio
import logging
import sys

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level='DEBUG')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_key())
    loop.close()


async def get_key():
    for line in sys.stdin:
        for char in line:
            await process_char(char)


async def process_char(char):
    sys.stdout.write(char)

if __name__ == '__main__':
    main()
