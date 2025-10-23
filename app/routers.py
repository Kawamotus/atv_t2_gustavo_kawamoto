from fastapi import APIRouter, HTTPException
from app.services import ExternalAPI

router = APIRouter(prefix="/data", tags=["data"])

api_service = ExternalAPI()


@router.get("/")
def get_all_data():
    return api_service.get_all()


@router.get("/{item_id}")
def get_data_by_id(item_id: int):
    data = api_service.get_by_id(item_id)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    return data


@router.post("/")
def create_data(item: dict):
    return api_service.create(item)
