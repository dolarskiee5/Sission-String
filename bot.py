import asyncio, pyrogram

api_id ="20056548"
api_hash ="07e939cade2848503d89dd3881d42748"
async def main():
 async with pyrogram.Client(
  name="app",
  api_id=api_id,
  api_hash=api_hash,
 ) as app:
  ss = await app.export_session_string()
  await app.send_message("me", ss)
  print(ss)
asyncio.run(main())
