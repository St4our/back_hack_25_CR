from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from adminka_fast_api.services.fighter import FighterService
from db.database import get_db
from fastapi import Query

router = APIRouter(prefix="/fighters")

# Route to get all fighters with optional filtering
@router.get("/all")
async def get_all_fighters(
    db: AsyncSession = Depends(get_db),
    name: str = Query(None),
    municipality_id: int = Query(None)
):
    return await FighterService(db).get_all_fighters(name=name, municipality_id=municipality_id)

# Route to get a single fighter by ID
@router.get("/{id}")
async def get_fighter(id: int, db: AsyncSession = Depends(get_db)):
    return await FighterService(db).get_fighter(id=id)

# Route to create a new fighter
@router.post("/create")
async def create_fighter(
    user_id: int,
    name: str,
    birth_death_years: str,
    municipality_id: int,
    short_info: str,
    photo_path: str,
    db: AsyncSession = Depends(get_db)
):
    return await FighterService(db).create(
        user_id=user_id,
        name=name,
        birth_death_years=birth_death_years,
        municipality_id=municipality_id,
        short_info=short_info,
        photo_path=photo_path
    )

# Route to delete a fighter
@router.delete("/{id}")
async def delete_fighter(id: int, db: AsyncSession = Depends(get_db)):
    return await FighterService(db).delete(id=id)

# Route to update a fighter's information
@router.put("/{id}")
async def update_fighter(
    id: int,
    name: str,
    birth_death_years: str,
    short_info: str,
    photo_path: str,
    db: AsyncSession = Depends(get_db)
):
    return await FighterService(db).update(
        id=id,
        name=name,
        birth_death_years=birth_death_years,
        short_info=short_info,
        photo_path=photo_path
    )
