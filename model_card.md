# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder suggests songs from a small catalog based on a user's preferred genre, mood, energy level, and whether they enjoy acoustic music. It is designed for classroom exploration of how content-based recommendation systems work — not for production use with real users.

The system assumes each user has a single fixed taste profile. It does not learn over time, adapt to context (e.g. working out vs. studying), or consider listening history.

---

## 3. How the Model Works

Every song in the catalog gets a score based on how well it matches what the user said they like. The scoring works like a points system:

- If the song's genre matches the user's favorite genre, it earns 3 points — the biggest reward, because genre defines the overall sonic world of a song.
- If the mood matches (happy, chill, intense, etc.), the song earns 2 more points.
- Every song earns a partial point based on how close its energy level is to the user's target. A perfect energy match earns 1 full point; a song that is very far off earns close to 0.
- If the user enjoys acoustic music and the song has a strong acoustic quality, it earns 1 bonus point.

Once every song has a score, the system sorts them from highest to lowest and returns the top results. The score also comes with a plain-language explanation — for example, "Matches your favorite genre (pop) | Energy match: 0.98/1.00."

---

## 4. Data

The catalog contains 18 songs stored in `data/songs.csv`. Each song has the following attributes: title, artist, genre, mood, energy (0–1), tempo in BPM, valence (musical positivity, 0–1), danceability (0–1), and acousticness (0–1).

**Genres represented:** pop, lofi, rock, ambient, jazz, synthwave, indie pop, country, hip-hop, classical, rnb, metal, funk, electronic

**Moods represented:** happy, chill, intense, relaxed, focused, moody, nostalgic, energetic, melancholic, romantic

The original starter dataset had 10 songs across 7 genres and 6 moods. Eight additional songs were added to improve diversity. Despite this, the catalog is tiny compared to real music platforms, and most genres have only 1–2 representative songs — meaning a user who prefers a rare genre will almost always get poor results.

---

## 5. Strengths

- **Well-represented profiles get strong results.** Users who prefer lofi+chill or rock+intense get clear, intuitive top picks because those genre-mood combinations have multiple matching songs in the catalog.
- **Explanations are transparent.** Every recommendation includes a breakdown of exactly why each song was chosen, which makes the system easy to audit and understand.
- **Energy proximity is smooth.** Unlike a binary match, the energy score rewards songs that are *close* to the target — so a near-miss still gets partial credit rather than zero.
- **Acoustic preference works as a useful tiebreaker.** For users who like acoustic music, it consistently surfaces lofi and classical songs over electronic ones when scores are otherwise close.

---

## 6. Limitations and Bias

**Genre dominance (the "Genre Trap"):** Because genre is worth 3 points — more than mood and energy combined — a genre match can push a song to the top even when mood and energy are completely wrong. A metal+happy user gets an intense metal song as their top result because no metal+happy song exists in the catalog.

**Filter bubble:** The system only rewards exact matches on genre and mood. A pop+happy user will never discover a jazz song that happens to be bright and energetic, even if it would suit their mood perfectly. The system has no mechanism for cross-genre discovery.

**Acoustic bonus inflation:** The acoustic bonus rewards any acoustic song regardless of genre or mood fit. This causes lofi and ambient songs to appear in top results for users with completely unrelated tastes (e.g., a classical+melancholic user gets ambient and country as 2nd and 3rd place, not because they match, but because they are acoustic).

**Thin catalog coverage:** Most genres have only one song. A country or rnb user will always get that one song first, then fall back to energy-proximity matches with no genre or mood relevance.

**No context awareness:** The system ignores when or why someone is listening. The same profile returns the same songs whether the user is working out, studying, or falling asleep.

---

## 7. Evaluation

Six user profiles were tested, including three designed to expose edge cases:

| Profile | Top Result | Observation |
|---|---|---|
| pop + happy + energy 0.8 | Sunrise City (5.98) | Correct — perfect genre+mood+energy match |
| lofi + chill + energy 0.4 + acoustic | Midnight Coding (6.98) | Correct — strong across all four signals |
| rock + intense + energy 0.9 | Storm Runner (5.99) | Correct — only rock+intense song, near-perfect energy |
| metal + happy + energy 0.5 (Genre Trap) | Neon Rage (3.54) | Wrong mood — intense metal beat happy songs due to genre weight |
| classical + melancholic + energy 0.2 + acoustic (Acoustic Paradox) | Sonata No. 3 (6.98) | Top result correct, but 2nd/3rd were ambient/country with no mood match |
| pop + happy + energy 0.5 (Energy Cliff) | Sunrise City (5.68) | Correct genre+mood, but high-energy pop scored 2nd over calmer happy songs |

An experimental weight adjustment was also tested: genre reduced to 1.5 points and energy multiplied by 2. This fixed the Genre Trap (happy songs correctly outranked metal) but weakened genre loyalty for users who care about it strongly. The original weights were restored after the experiment.

---

## 8. Future Work

- **Configurable weights:** Let users specify how much they care about genre vs. mood vs. energy, rather than using fixed weights for everyone.
- **Valence scoring:** Add proximity-based scoring for valence (musical positivity) to better differentiate within genre+mood matches — e.g., separating "euphoric pop" from "bittersweet pop."
- **Diversity injection:** Intentionally include at least one cross-genre recommendation in the top results to avoid pure filter bubbles.
- **Larger catalog:** With only 1–2 songs per genre, the catalog cannot give meaningful recommendations for most profiles. A real dataset of even 100 songs would produce far more useful results.
- **Context profiles:** Allow different profiles for different listening contexts (focus, workout, sleep) rather than a single static taste profile.

---

## 9. Personal Reflection

The most surprising finding was how strongly the genre weight dominated every other signal — a metal song beating happy songs for a happy user exposed that a single categorical match can override two other correct signals. If I rebuilt this, I would make weights configurable per user context, so someone in a workout session could boost energy weight while someone browsing casually keeps genre loyalty high. This project taught me that real recommendation systems aren't just about math — they're about encoding human behavior and context into numbers, and small weight decisions have outsized effects on what users actually see. The filter bubble problem also hit differently once I saw it in action: a pop+happy user will never discover great funk or indie pop songs no matter how well they match emotionally, purely because genre doesn't match.

