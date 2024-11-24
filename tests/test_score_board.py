import pytest
from my_score_board.score_board import ScoreBoard


def test_scoreboard_start_match():
    scoreboard = ScoreBoard()
    scoreboard.start_match("Mexico", "Canada")
    assert len(scoreboard.matches) == 1
    assert scoreboard.matches[0].home_team == "Mexico"
    assert scoreboard.matches[0].away_team == "Canada"

def test_scoreboard_update_score():
    scoreboard = ScoreBoard()
    scoreboard.start_match("Spain", "Brazil")
    scoreboard.update_score("Spain", "Brazil", 2, 3)
    match = scoreboard.matches[0]
    assert match.score_home_team == 2
    assert match.score_away_team == 3
    assert match.get_total_score() == 5

def test_scoreboard_update_score_invalid_match():
    scoreboard = ScoreBoard()
    scoreboard.start_match("Spain", "Brazil")
    with pytest.raises(ValueError, match="No match found between Germany and France."):
        scoreboard.update_score("Germany", "France", 1, 0)

def test_scoreboard_finish_match():
    scoreboard = ScoreBoard()
    scoreboard.start_match("Spain", "Brazil")
    scoreboard.finish_match("Spain", "Brazil")
    assert len(scoreboard.matches) == 0

def test_scoreboard_finish_match_invalid_match():
    scoreboard = ScoreBoard()
    scoreboard.start_match("Argentina", "Australia")
    with pytest.raises(ValueError, match="No match found between Mexico and Canada."):
        scoreboard.finish_match("Mexico", "Canada")

def test_scoreboard_generate_summary():
    scoreboard = ScoreBoard()
    scoreboard.start_match("Mexico", "Canada")
    scoreboard.start_match("Spain", "Brazil")
    scoreboard.start_match("Germany", "France")
    scoreboard.start_match("Uruguay", "Italy")
    scoreboard.start_match("Argentina", "Australia")

    scoreboard.update_score("Mexico", "Canada", 0,5)
    scoreboard.update_score("Spain", "Brazil", 10,2)
    scoreboard.update_score("Germany", "France", 2,2)
    scoreboard.update_score("Uruguay", "Italy", 6,6)
    scoreboard.update_score("Argentina", "Australia", 3, 1)
    
    
    summary = scoreboard.generate_summary()
    assert summary[0].home_team == "Uruguay"  
    assert summary[1].home_team == "Spain"

def test_scoreboard_generate_summary_empty():
    scoreboard = ScoreBoard()
    summary = scoreboard.generate_summary()
    assert summary == []
