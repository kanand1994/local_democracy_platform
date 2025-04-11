# app/visualization.py
from fastapi import APIRouter, Query, Response, HTTPException
from services.visualization_service import VisualizationService

router = APIRouter()
visualization_service = VisualizationService()

@router.get("/visualization/impact")
async def impact():
    return visualization_service.policy_impact()

@router.get("/visualization/impact/chart")
async def impact_chart(type: str = Query("age_groups", enum=["age_groups", "neighborhoods"])):
    data = visualization_service.policy_impact()
    if type not in data:
        raise HTTPException(status_code=400, detail="Invalid chart type")

    img_bytes = visualization_service.generate_bar_chart(data[type], f"Policy Impact by {type.replace('_', ' ').title()}")
    return Response(content=img_bytes, media_type="image/png")