import asyncio, pyrogram
api_id =masukkan api id
api_hash ="masukkan api hash"
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
