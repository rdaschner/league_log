# src/league_ranker/main.py
import argparse
import asyncio
from league_ranker.services.league import LeagueService
from league_ranker.models.match import MatchResult

async def run_cli(file_path: str):
    league = LeagueService()
    with open(file_path, "r") as f:
        for line in f:
            match = MatchResult.from_string(line.strip())
            await league.add_match(match)
    results = await league.rank()
    print("\n".join(results))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to match data file")
    args = parser.parse_args()

    asyncio.run(run_cli(args.file))

if __name__ == "__main__":
    main()
