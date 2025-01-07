import asyncio
import websockets
import json

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        order = {
            "header": {"version": "1.1", "timestamp": "2025-01-07T12:00:00Z"},
            "orderId": "order_001",
            "actions": [{"actionType": "MOVE", "parameters": {"targetNodeId": "NodeA"}}]
        }
        await websocket.send(json.dumps(order))
        response = await websocket.recv()
        print(f"Response: {response}")

asyncio.get_event_loop().run_until_complete(client())
