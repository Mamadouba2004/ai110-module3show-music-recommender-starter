# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommendation systems like Spotify use hybrid approaches combining
collaborative filtering (finding users with similar taste) and content-based
filtering (matching song attributes to a taste profile). This simulation
focuses on content-based filtering — the layer that ensures recommended songs
actually sound right for the user.

Our recommender scores each song against a user's taste profile using a
weighted scoring rule:
- Genre match: 3 points (strongest signal — defines the sonic world)
- Mood match: 2 points (emotional intent)
- Energy proximity: 0–1 points (rewards closeness to target energy)
- Acoustic bonus: 1 point (if user likes acoustic and song is acoustic)

The ranking rule then sorts all scored songs and returns the top k results.

### Features Used

**Song object:** id, title, artist, genre, mood, energy, tempo_bpm,
valence, danceability, acousticness

**UserProfile object:** favorite_genre, favorite_mood, target_energy,
likes_acoustic

## Algorithm Recipe

| Feature | Points | Logic |
|---------|--------|-------|
| Genre match | +3 | Exact string match |
| Mood match | +2 | Exact string match |
| Energy proximity | 0–1 | `max(0, 1 - abs(song.energy - target))` |
| Acoustic bonus | +1 | Only if `likes_acoustic=True` and `acousticness > 0.6` |

**Max possible score: 7.0**

## Data Flow

```mermaid
flowchart TD
    A[User Profile\ngenre · mood · energy · likes_acoustic] --> C[For each song: score_song]
    B[songs.csv\n18 songs] --> C
    C --> D[Genre match? +3 pts]
    D --> E[Mood match? +2 pts]
    E --> F[Energy proximity 0–1 pts]
    F --> G[Acoustic bonus? +1 pt]
    G --> H[Song Score]
    H --> I{More songs?}
    I -- Yes --> C
    I -- No --> J[Sort all scores descending]
    J --> K[Return top k results\nwith explanations]
```

## Potential Biases

This system may over-prioritize genre, causing songs with matching mood
and energy but different genre to rank poorly. It also creates a filter
bubble — a pop+happy user will only ever see pop+happy songs.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

