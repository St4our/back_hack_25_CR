from fastapi import APIRouter

from api.services.municipality import MunicipalityService

router = APIRouter(
    prefix="/municipality"
)

@router.get('')
async def route(
    id: int
):
    return await MunicipalityService().get_municipality(
        id=id
    )