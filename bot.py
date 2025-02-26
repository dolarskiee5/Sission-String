import asyncio, pyrogram

api_id ="26758806"
api_hash ="37995a8d6e7ae01de1fb7595c6cebeb6"
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
