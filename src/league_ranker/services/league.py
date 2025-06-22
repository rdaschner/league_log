from collections import defaultdict
from league_ranker.models.match import MatchResult

class LeagueService:
    def __init__(self):
        self.points = defaultdict(int)

    async def add_match(self, match: MatchResult):
        if match.score1 > match.score2:
            self.points[match.team1] += 3
        elif match.score1 < match.score2:
            self.points[match.team2] += 3
        else:
            self.points[match.team1] += 1
            self.points[match.team2] += 1

    async def rank(self):
        sorted_teams = sorted(self.points.items(), key=lambda x: (-x[1], x[0]))
        rankings = []
        last_score = None
        rank = 0
        skip = 0

        for i, (team, score) in enumerate(sorted_teams):
            if score != last_score:
                rank = i + 1 - skip
                last_score = score
            else:
                skip += 1

            suffix = "pt" if score == 1 else "pts"
            rankings.append(f"{rank}. {team}, {score} {suffix}")
        return rankings
