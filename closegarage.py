import asyncio
import logging

from aiohttp import ClientSession

from pymyq import login
from pymyq.account import MyQAccount
from pymyq.errors import MyQError, RequestError
from pymyq.garagedoor import STATE_CLOSED, STATE_OPEN

_LOGGER = logging.getLogger()

EMAIL = "<email>"
PASSWORD = "<password>"
ISSUE_COMMANDS = True
#LOGLEVEL = logging.DEBUG
LOGLEVEL = logging.WARNING

def closegarage():
	asyncio.get_event_loop().run_until_complete(main())


def print_info(number: int, device):
    """Print the device information

    Args:
        number (int): [description]
        device ([type]): [description]
    """
    print(f"      Device {number + 1}: {device.name}")
    print(f"      Device Online: {device.online}")
    print(f"      Device ID: {device.device_id}")
    print(
        f"      Parent Device ID: {device.parent_device_id}",
    )
    print(f"      Device Family: {device.device_family}")
    print(
        f"      Device Platform: {device.device_platform}",
    )
    print(f"      Device Type: {device.device_type}")
    print(f"      Firmware Version: {device.firmware_version}")
    print(f"      Open Allowed: {device.open_allowed}")
    print(f"      Close Allowed: {device.close_allowed}")
    print(f"      Current State: {device.state}")
    print("      ---------")


async def print_garagedoors(account: MyQAccount):  # noqa: C901
    """Print garage door information and open/close if requested

    Args:
        account (MyQAccount): Account for which to retrieve garage doors
    """
    print(f"  GarageDoors: {len(account.covers)}")
    print("  ---------------")
    

    
    
    
    
    
    
    if len(account.covers) != 0:
        for idx, device in enumerate(account.covers.values()):
            print_info(number=idx, device=device)

            if ISSUE_COMMANDS:
                try:
                    open_task = None
                    close_task = None
                    if device.open_allowed:
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

                    #if open_task is not None and not isinstance(open_task, bool):
                        #opened = await open_task

                    if close_task is not None and not isinstance(open_task, bool):
                        closed = await close_task

                except RequestError as err:
                    _LOGGER.error(err)
        print("  ------------------------------")




async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=LOGLEVEL)
    async with ClientSession() as websession:
        try:
            # Create an API object:
            print(f"{EMAIL} {PASSWORD}")
            api = await login(EMAIL, PASSWORD, websession)

            for account in api.accounts.values():
                print(f"Account ID: {account.id}")
                print(f"Account Name: {account.name}")

                # Get all devices listed with this account – note that you can use
                # api.covers to only examine covers or api.lamps for only lamps.
                await print_garagedoors(account=account)

        except MyQError as err:
            _LOGGER.error("There was an error: %s", err)


asyncio.get_event_loop().run_until_complete(main())
