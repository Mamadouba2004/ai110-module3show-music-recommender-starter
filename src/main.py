"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from recommender import load_songs, recommend_songs

_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "songs.csv")

def main() -> None:
    songs = load_songs(_DATA_PATH)

    profiles = [
        {"name": "High-Energy Pop", "genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False},
        {"name": "Chill Lofi", "genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True},
        {"name": "Deep Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.9, "likes_acoustic": False},
        {"name": "Genre Trap (metal+happy)", "genre": "metal", "mood": "happy", "energy": 0.5},
        {"name": "Acoustic Paradox", "genre": "classical", "mood": "melancholic", "energy": 0.2, "likes_acoustic": True},
        {"name": "Energy Cliff (mellow pop)", "genre": "pop", "mood": "happy", "energy": 0.5},
    ]

    for profile in profiles:
        name = profile.pop("name")
        print(f"\n=== {name} ===")
        recommendations = recommend_songs(profile, songs, k=3)
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"  Because: {explanation}")


if __name__ == "__main__":
    main()
