from typing import List
from .match import Match

class ScoreBoard:
    def __init__(self):
        self.matches: List[Match] = []
    
    # Start a new match
    def start_match(self, home_team: str, away_team: str):
        match = Match(home_team, away_team)
        self.matches.append(match)
    
    def update_score(self, home_team: str, away_team: str, score_home: int, score_away: int):
        match = self._find_match(home_team, away_team)
        if match:
            match.update_score(score_home, score_away)
        else:
            raise ValueError(f"No match found between {home_team} and {away_team}.")

    
    def finish_match(self, home_team: str, away_team: str):
        match = self._find_match(home_team, away_team)
        if match:
            self.matches.remove(match)
        else:
            raise ValueError(f"No match found between {home_team} and {away_team}.")


    def generate_summary(self) -> List[str]:
        return sorted(
            self.matches,
            key=lambda match: (match.get_total_score(), -match.match_start_time_ms),
            reverse=True
        )

    
    def _find_match(self, home_team: str, away_team: str) -> Match:
        for match in self.matches:
            if match.home_team == home_team and match.away_team == away_team:
                return match
        return None

        
        