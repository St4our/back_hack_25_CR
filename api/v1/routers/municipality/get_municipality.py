from fastapi import APIRouter

from api.services.municipality import MunicipalityService

router = APIRouter(
    prefix="/municipalities"
)

@router.get('')
async def route(
    id: int
):
    return await MunicipalityService().get_municipality(
        id=id
    )