import pytest
from league_ranker.models.match import MatchResult

def test_parse_match_valid():
    match = MatchResult.from_string("Lions 3, Snakes 3")
    assert match.team1 == "Lions"
    assert match.team2 == "Snakes"
    assert match.score1 == 3
    assert match.score2 == 3

def test_parse_match_invalid():
    with pytest.raises(ValueError):
        MatchResult.from_string("Invalid Format")