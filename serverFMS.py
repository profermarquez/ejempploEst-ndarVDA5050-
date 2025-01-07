import asyncio
import json
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print(f"Message received: {message}")
        response = {
            "header": {"version": "1.1", "timestamp": "2025-01-07T12:00:00Z"},
            "state": "ACKNOWLEDGED"
        }
        await websocket.send(json.dumps(response))

start_server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
