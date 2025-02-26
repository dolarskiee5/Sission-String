import asyncio, pyrogram
api_id =28592635
api_hash ="01fa31877697fd17413d2bfbbac944bc"
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
