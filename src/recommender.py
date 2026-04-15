import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_dict = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        scored = []
        for song in self.songs:
            score, _ = score_song(user_dict, asdict(song))
            scored.append((song, score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_dict = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        score, reasons = score_song(user_dict, asdict(song))
        if not reasons:
            reasons = [f"Score: {score:.2f}"]
        return f"'{song.title}' (score {score:.2f}): " + " | ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre match: 3 points
    if song.get("genre") == user_prefs.get("genre"):
        score += 3
        reasons.append(f"Matches your favorite genre ({song['genre']})")

    # Mood match: 2 points
    if song.get("mood") == user_prefs.get("mood"):
        score += 2
        reasons.append(f"Matches your preferred mood ({song['mood']})")

    # Energy proximity: max 1 point, decreases with distance
    energy_diff = abs(song.get("energy", 0) - user_prefs.get("energy", 0))
    energy_score = max(0.0, 1.0 - energy_diff)
    score += energy_score
    reasons.append(f"Energy match: {energy_score:.2f}/1.00 (song={song.get('energy', 0):.2f}, target={user_prefs.get('energy', 0):.2f})")

    # Acoustic bonus: 1 point if user likes acoustic and song is acoustic
    if user_prefs.get("likes_acoustic", False) and song.get("acousticness", 0) > 0.6:
        score += 1
        reasons.append(f"Has the acoustic feel you enjoy (acousticness={song['acousticness']:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [(song, score, " | ".join(reasons)) for song, score, reasons in scored[:k]]
