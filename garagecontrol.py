import asyncio

from aiohttp import ClientSession

from pymyq import login
from pymyq.account import MyQAccount
from pymyq.errors import MyQError, RequestError
from pymyq.garagedoor import STATE_CLOSED, STATE_OPEN

EMAIL = "<email>"
PASSWORD = "<pass>"


def opengarage():
	asyncio.get_event_loop().run_until_complete(open())


async def open() -> None:
	async with ClientSession() as websession:
		try:
			api = await login(EMAIL, PASSWORD, websession)
			for account in api.accounts.values():
				for idx, device in enumerate(account.covers.values()):
					try:
						open_task = await device.open(wait_for_state=False)
					except:
						pass
		except:
			pass


def closegarage():
	asyncio.get_event_loop().run_until_complete(close())


async def close() -> None:
	async with ClientSession() as websession:
		try:
			api = await login(EMAIL, PASSWORD, websession)
			for account in api.accounts.values():
				for idx, device in enumerate(account.covers.values()):
					try:
						close_task = await device.close(wait_for_state=False)
					except:
						pass
		except:
			pass
