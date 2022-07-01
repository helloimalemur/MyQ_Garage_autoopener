import asyncio
import logging

from aiohttp import ClientSession

from pymyq import login
from pymyq.account import MyQAccount
from pymyq.errors import MyQError, RequestError
from pymyq.garagedoor import STATE_CLOSED, STATE_OPEN

_LOGGER = logging.getLogger()

EMAIL = ""
PASSWORD = ""
ISSUE_COMMANDS = True
#LOGLEVEL = logging.DEBUG
LOGLEVEL = logging.WARNING

def closegarage():
	asyncio.get_event_loop().run_until_complete(main())

async def close_garagedoors(account: MyQAccount):  # noqa: C901
    if len(account.covers) != 0:
        for idx, device in enumerate(account.covers.values()):
            if ISSUE_COMMANDS:
                try:
                    open_task = None
                    close_task = None
                    if device.close_allowed:
                        if device.state != STATE_CLOSED:
                            try:
                                #open_task = await device.open(wait_for_state=False)
                                close_task = await device.close(wait_for_state=False)
                            except MyQError as err:
                                _LOGGER.error(
                                    "Error when trying to open %s: %s",
                                    device.name,
                                    str(err),
                                )
                            print(f"Garage door {device.name} is {device.state}")

                    else:
                        print(f"Opening of garage door {device.name} is not allowed.")

                    if close_task is not None and not isinstance(open_task, bool):
                        closed = await close_task

                    #elif close_task is not None and not isinstance(open_task, bool):
                        #closed = await close_task

                except RequestError as err:
                    _LOGGER.error(err)
        print("  ------------------------------")

async def main() -> None:
    logging.basicConfig(level=LOGLEVEL)
    async with ClientSession() as websession:
        try:
            # Create an API object:
            api = await login(EMAIL, PASSWORD, websession)

            for account in api.accounts.values():
                print(f"Account ID: {account.id}")
                print(f"Account Name: {account.name}")

                # Get all devices listed with this account – note that you can use
                # api.covers to only examine covers or api.lamps for only lamps.
                await close_garagedoors(account=account)

        except MyQError as err:
            _LOGGER.error("There was an error: %s", err)

#asyncio.get_event_loop().run_until_complete(main())
