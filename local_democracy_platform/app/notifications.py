# app/notifications.py
from fastapi import APIRouter, WebSocket
from services.notification_service import NotificationService

router = APIRouter()
notification_service = NotificationService()

@router.websocket("/ws/notifications")
async def websocket_notifications(websocket: WebSocket):
    await notification_service.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        notification_service.disconnect(websocket)