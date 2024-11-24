from time import time

class Match:
    def __init__(self, home_team: str, away_team: str):
        self.home_team: str = home_team
        self.away_team: str = away_team
        self.score_home_team: int = 0
        self.score_away_team: int = 0
        self.match_start_time_ms = int(time() * 1000) # in MS since epoch
    
    def update_score(self, home_team_score: int, away_team_score: int):
        raise NotImplementedError("Not yet implemented")
    
    def get_total_score(self) -> int:
        raise NotImplementedError("Not yet implemented")
    