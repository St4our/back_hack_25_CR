from fastapi import APIRouter

from api.services.municipality import  MunicipalityService

router = APIRouter(
    prefix="/get_municipalities"
)

@router.get('')
async def route():
    return await MunicipalityService().get_all_municipalities()