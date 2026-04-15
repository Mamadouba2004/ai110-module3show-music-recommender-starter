# Reflection: Profile Comparisons

## High-Energy Pop vs. Chill Lofi

These two profiles are near-opposites and the results show it clearly. The pop+happy user gets bright, fast songs like Sunrise City and Gym Hero — both loud, upbeat tracks built for dancing or a good mood. The lofi+chill user gets slow, quiet, acoustic tracks like Midnight Coding and Library Rain — background music built for studying or winding down. What's interesting is that the Chill Lofi profile scores *higher* overall (6.98 vs 5.98) because it matches on genre, mood, energy, AND acoustic preference all at once. The pop profile only matched three signals. This makes sense: the more ways a song fits your taste, the higher it should score.

## Deep Intense Rock vs. Genre Trap (metal+happy)

Both profiles want high-energy, hard-sounding music — but the results are very different. The rock+intense user gets Storm Runner as a clear #1 (score 5.99), which is exactly right: it's loud, fast, and aggressive. The metal+happy user gets Neon Rage at the top — but Neon Rage is an *intense* metal song, not a happy one. The user asked for happy music and got the opposite mood. Why? Because the genre match (metal = 3 points) was worth more than two happy songs with no genre match. This exposed the biggest weakness in the scoring: genre loyalty can override mood accuracy when there's no song in the catalog that matches both.

## Acoustic Paradox vs. Energy Cliff (mellow pop)

Both profiles ask for low-to-medium energy, but the acoustic classical user and the mellow pop user get very different 2nd and 3rd place results. The classical user's top pick (Sonata No. 3) is perfect — it matches all four signals. But 2nd and 3rd place are ambient and country songs with no genre or mood match at all — they only ranked because they're acoustic and low-energy. The mellow pop user's results feel more intuitive: Sunrise City at #1 is correct (it's pop+happy), but Gym Hero at #2 is a high-energy workout song that doesn't fit "mellow" at all. It won purely because genre (pop = 3 points) outweighed the energy mismatch. Both profiles show the same root issue: when the catalog doesn't have enough songs in a genre, the system falls back on partial matches that don't feel right.

## Overall Takeaway

The profiles that worked best (Chill Lofi, Deep Intense Rock) were the ones where the catalog had multiple songs matching both genre and mood. The profiles that failed (Genre Trap, Acoustic Paradox, Energy Cliff) all shared the same problem: the catalog had at most one song matching the genre, so the system had nowhere to go after the top result. This taught me that a recommender is only as good as its data — the scoring logic can be perfect, but if the catalog is too small or too unbalanced, the results will always feel off for users with niche tastes.
