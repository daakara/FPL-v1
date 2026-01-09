"""
Domain Models for FPL Analytics
"""
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum


class Position(Enum):
    """Player positions"""
    GOALKEEPER = 1
    DEFENDER = 2
    MIDFIELDER = 3
    FORWARD = 4


class AnalysisType(Enum):
    """Types of analysis"""
    BASIC = "basic"
    ADVANCED = "advanced"
    PREDICTIVE = "predictive"


@dataclass
class Player:
    """Player data model"""
    id: int
    web_name: str
    team: int
    element_type: int
    now_cost: float
    total_points: int
    form: float
    selected_by_percent: float
    points_per_game: float
    minutes: int
    goals_scored: int = 0
    assists: int = 0
    clean_sheets: int = 0
    goals_conceded: int = 0
    bonus: int = 0
    bps: int = 0
    ict_index: float = 0.0
    influence: float = 0.0
    creativity: float = 0.0
    threat: float = 0.0
    expected_goals: float = 0.0
    expected_assists: float = 0.0
    expected_goal_involvements: float = 0.0


@dataclass
class Team:
    """Team data model"""
    id: int
    name: str
    short_name: str
    strength: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int


@dataclass
class Fixture:
    """Fixture data model"""
    id: int
    event: int
    team_h: int
    team_a: int
    team_h_score: Optional[int]
    team_a_score: Optional[int]
    finished: bool
    kickoff_time: Optional[str]
    team_h_difficulty: int
    team_a_difficulty: int


@dataclass
class FDRData:
    """Fixture Difficulty Rating data"""
    team_id: int
    team_name: str
    next_5_fixtures: List[int]
    avg_difficulty: float
    home_fixtures: int
    away_fixtures: int


@dataclass
class UserTeam:
    """User team data model"""
    entry_id: int
    entry_name: str
    player_first_name: str
    player_last_name: str
    summary_overall_points: int
    summary_overall_rank: int
    current_event: int
    total_transfers: int
    bank: float
    value: float


@dataclass
class PlayerPick:
    """Player pick in user team"""
    element: int
    position: int
    multiplier: int
    is_captain: bool
    is_vice_captain: bool
