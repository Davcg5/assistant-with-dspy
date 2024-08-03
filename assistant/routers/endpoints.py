from fastapi import APIRouter

from assistant.routers import dtos
from assistant import factories

router = APIRouter()


@router.post("/advice_lli", tags=["Assistant"])
async def analyze_game_using_lli(request: dtos.AdviceRequest):
    query = request.query
    assistant = factories.get_lli_assistant()
    advice = assistant(query)
    return dtos.AdviceResponse(
        advice=advice,
    )


@router.post("/advice_chroma_db", tags=["Assistant"])
async def analyze_game_using_chromadb(request: dtos.AdviceRequest):
    query = request.query
    assistant = factories.get_chromadb_assistant()
    advice = assistant(query)

    return dtos.AdviceResponse(
        advice=advice,
    )
