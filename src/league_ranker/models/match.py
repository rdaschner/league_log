from pydantic import BaseModel, field_validator
from typing import Literal

class MatchResult(BaseModel):
    team1: str
    score1: int
    team2: str
    score2: int

    @field_validator('team1', 'team2', mode='before')
    @classmethod
    def validate_team_names(cls, v):
        return v.strip()

    @classmethod
    def from_string(cls, line: str):
        try:
            part1, part2 = line.split(",")
            team1, score1 = part1.rsplit(" ", 1)
            team2, score2 = part2.rsplit(" ", 1)
            return cls(team1=team1, score1=int(score1), team2=team2, score2=int(score2))
        except Exception as e:
            raise ValueError(f"Invalid line format: {line}") from e
