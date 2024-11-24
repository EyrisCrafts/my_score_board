
import time
import pytest
from my_score_board.match import Match

def test_initalization():
    start_time = int(time.time() * 1000)
    match = Match(home_team="Germany", away_team="Italy")
    end_time = int(time.time() * 1000)
    assert match.home_team == "Germany"
    assert match.away_team == "Italy"
    assert match.score_home_team == 0
    assert match.score_away_team == 0
    assert match.match_start_time_ms <= end_time and match.match_start_time_ms >= start_time

def test_get_total_score_valid():
    match = Match(home_team="Germany", away_team="Italy")
    assert match.get_total_score() == 0
    
    match.update_score(home_team_score=2, away_team_score=3)
    assert match.get_total_score() == 5
    
def test_get_total_score_negative():
    match = Match(home_team="Germany", away_team="Italy")
    
    with pytest.raises(ValueError):
        match.update_score(home_team_score=-5, away_team_score=-5)
    
    assert match.get_total_score() == 0
    
def test_update_score_valid():
    match = Match(home_team="Germany", away_team="Italy")
    assert match.score_home_team == 0
    assert match.score_away_team == 0
    
    match.update_score(home_team_score=3, away_team_score=5)
    assert match.score_home_team == 3
    assert match.score_away_team == 5
    
def test_update_score_negative():
    match = Match(home_team="Germany", away_team="Italy")
    with pytest.raises(ValueError):
        match.update_score(home_team_score=-5, away_team_score=-5)