# src/league_ranker/api.py
from fastapi import FastAPI, UploadFile, File
from league_ranker.services.league import LeagueService
from league_ranker.models.match import MatchResult
from typing import List
from pydantic import BaseModel

app = FastAPI()

class MatchInput(BaseModel):
    matches: List[str]

@app.post("/rank")
async def rank_teams(input_data: MatchInput):
    league = LeagueService()
    try:
        for line in input_data.matches:
            match = MatchResult.from_string(line)
            await league.add_match(match)
        return {"ranking": await league.rank()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e) or "Invalid input format")

from fastapi import UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

@app.post("/rank-file")
async def rank_teams_from_file(file: UploadFile = File(...)):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Only text files are supported.")

    try:
        contents = await file.read()
        lines = contents.decode("utf-8").splitlines()

        league = LeagueService()
        for line in lines:
            if not line.strip():
                continue
            match = MatchResult.from_string(line)
            await league.add_match(match)

        return JSONResponse(content={"ranking": await league.rank()})

    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="Could not decode uploaded file.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e) or "Invalid match data.")

