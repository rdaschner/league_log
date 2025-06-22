from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import argparse
import asyncio
import sys

from .services.league import LeagueService
from .models.match import MatchResult
from dotenv import load_dotenv; load_dotenv()


app = FastAPI()  # FastAPI instance for serving

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


# ---------- CLI SUPPORT ----------
async def run_cli(filename: str):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    league = LeagueService()
    for line in lines:
        try:
            match = MatchResult.from_string(line)
            await league.add_match(match)
        except ValueError as e:
            print(f"Skipping invalid line: {line} ({e})")

    print("\nLeague Ranking:")
    for line in await league.rank():
        print(line)

def cli_entry():
    parser = argparse.ArgumentParser(description="League Ranking Tool")
    parser.add_argument("--file", "-f", help="Path to input file with match results")
    args = parser.parse_args()

    if args.file:
        asyncio.run(run_cli(args.file))
    else:
        print("Use FastAPI by running: uvicorn main:app --reload")
        print("Or run with --file path/to/input.txt to use CLI")

if __name__ == "__main__":
    cli_entry()
