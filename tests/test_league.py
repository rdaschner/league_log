import pytest
import asyncio
from league_ranker.services.league import LeagueService
from league_ranker.models.match import MatchResult

@pytest.mark.asyncio
async def test_league_ranking_with_mock_data():
    league = LeagueService()
    matches = [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0",
        "Lions 1, FC Awesome 1",
        "Tarantulas 3, Snakes 1",
        "Lions 4, Grouches 0",
        "Snakes 1, FC Awesome 1",
        "Grouches 2, Tarantulas 2"
    ]
    for m in matches:
        await league.add_match(MatchResult.from_string(m))

    ranking = await league.rank()
    assert isinstance(ranking, list)
    assert isinstance(ranking[0], str)
    assert ranking[0].startswith("1. Tarantulas")
    assert "7 pts" in ranking[0]