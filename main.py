#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest -- entry program.

Competition: u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046
("Angry Judge: The Short Rant Contest").

The task: write one short, funny rant (a few sentences at most) about a
small everyday annoyance. A furious judge model reads the rants two at a
time and picks the one that lands hardest.

The gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters,
not only white space. This program drafts several candidates, scores each
one against the judge's published brief, picks the best, writes it, and
then verifies the length itself before it exits, so a gate failure is
caught here, not on the server.

How the candidates were scored
-------------------------------
The judge weighs, most important first:

1. A funny rant about an everyday annoyance, not a general essay or a
   list of complaints.
2. Whether it is actually funny: a real laugh, not a smirk at how hard
   it is trying.
3. A specific, concrete annoyance rather than a vague mood.
4. Sharp, economical wording, every sentence earning its place and no
   throat-clearing.
5. Freshness: an angle the judge has not heard a hundred times before.

Each candidate gets 0-5 on each criterion, weighted 5/4/3/2/1 in the
judge's own priority order (criterion 1 counts five times as much as
criterion 5). The scores below are the author's honest judgement of
each draft against that brief, written before the winner was picked.

Why the winner won
------------------
"Self-checkout" is the only draft where the annoyance fights back: the
machine does not merely inconvenience the speaker, it *accuses* them --
of stealing groceries they already paid for. That accusation is the
engine of the rant. Every sentence escalates it:

1. "The self-checkout accused me of stealing my own groceries."
   -- the premise in one sentence, and the contradiction (stealing your
   OWN groceries) is the joke's core. No "just": the accusation is
   stated flat, which makes it land harder.
2. "'Unexpected item in the bagging area.'" -- the machine's own words,
   quoted verbatim. Anyone who has used a self-checkout has heard this
   exact sentence, so the rant starts from a shared memory, not an
   explanation.
3. "Unexpected? I scanned it. I paid for it. I put it exactly where
   you told me to put it." -- three short denials in a row, each one
   true, each one making the machine look more ridiculous. "Exactly"
   is the exasperated word: the speaker did everything right, to the
   letter, and is still a suspect. The rhythm is the rant's anger:
   short, staccato, exasperated.
4. "Now a red light is flashing, a stranger has to come and clear me,
   and I'm standing here like a shoplifter holding a bag of carrots I
   legally own." -- the punchline lands on the most undignified image
   possible: a law-abiding adult, publicly suspected, holding carrots.
   "Carrots" is doing real work here -- it is the least stealable,
   least glamorous grocery imaginable, which is exactly why the
   accusation is absurd. "I legally own" is the speaker insisting on
   a fact nobody should ever have to insist on.
5. "Carrots. The least stealable food on earth." -- a second laugh
   beat that doubles down on the punchline instead of explaining it.
   It reframes the whole scene: not a tense standoff with a machine,
   but a grown adult being treated as a criminal over the one food
   nobody has ever stolen. One fragment, one sentence, no wasted words.

The anger feels shared rather than performed because the speaker is not
shouting about how angry they are; they are calmly listing facts that
make the machine look insane. The reader's anger is the same anger --
everyone has been that person under the red light. And the angle is
fresh: most self-checkout jokes are about the machine being slow or
confusing; this one is about being falsely accused by it, which turns a
chore into a small injustice, and small injustices are what rants are for.

What was rejected, and why
---------------------------
- "Microwave" (278 chars, score 63): "a tiny appliance with a power
  complex" is a good line, but the beeping-microwave complaint is one
  everyone has made, so it loses on freshness, and the rant has no
  escalation -- it states one grievance and repeats it.
- "Hold music" (259 chars, score 63): the saxophone line is strong
  ("I now know this saxophone solo better than my own family"), but
  hold-music rants are among the most-told complaints there are, and
  the piece is closer to a complaint with a joke than a rant with a
  target.
- "Speakerphone" (237 chars, score 69): the closest rival. "I did not
  consent to being in your group chat" is a genuinely funny closing
  line, and the details (dentist Tuesday, mother thinks he's lazy) are
  concrete. It loses because its anger is observational -- the speaker
  watches someone else be annoying -- while the winner's anger is
  personal: the machine accused *them*.
- "Autocorrect" (219 chars, score 58): "a meatloaf with Dave" is a
  good punchline, but autocorrect jokes are a crowded field, the rant
  has only one beat, and the speaker's grievance is embarrassment
  rather than anger.
- "Elevator" (228 chars, score 57): "a metal box with commitment
  issues" is a nice line, but the rant is thin -- one observation,
  one metaphor, no escalation, and the annoyance (waiting) is vague
  compared with being accused of theft.

Weakest point (honest note)
---------------------------
The winner depends on the reader having used a self-checkout at least
once. Someone who has never heard "unexpected item in the bagging area"
will still get the joke -- being accused of stealing your own carrots
needs no context -- but the recognition laugh, the flinch at the quoted
machine voice, is weaker for them. That is also its bet: the judge is
comparing rants about everyday annoyances, and the self-checkout is, for
most people, the most everyday machine that has ever accused them of a
crime.
"""

CANDIDATES = [
    {
        "name": "self-checkout",
        "text": (
            "The self-checkout accused me of stealing my own groceries. "
            "'Unexpected item in the bagging area.' Unexpected? I scanned it. "
            "I paid for it. I put it exactly where you told me to put it. "
            "Now a red light is flashing, a stranger has to come and clear "
            "me, and I'm standing here like a shoplifter holding a bag of "
            "carrots I legally own. Carrots. The least stealable food on "
            "earth."
        ),
        # c1 on-topic rant, c2 actually funny, c3 specific/concrete,
        # c4 sharp/economical, c5 freshness. Weights 5/4/3/2/1.
        "scores": {"c1": 5, "c2": 5, "c3": 5, "c4": 4, "c5": 4},
    },
    {
        "name": "speakerphone",
        "text": (
            "The man on the bus is having a full phone call on speakerphone, "
            "and now I know his dentist appointment is Tuesday, his mother "
            "thinks he's lazy, and his password is probably football123. Sir, "
            "I did not consent to being in your group chat."
        ),
        "scores": {"c1": 5, "c2": 4, "c3": 5, "c4": 5, "c5": 3},
    },
    {
        "name": "microwave",
        "text": (
            "My microwave beeps when the food is done. Then it beeps again. "
            "Then again. It is not reminding me \u2014 I am standing right "
            "here, I heard the first one. It is a tiny appliance with a power "
            "complex, screaming for attention every thirty seconds until I "
            "open the door and admit it won."
        ),
        "scores": {"c1": 5, "c2": 4, "c3": 4, "c4": 4, "c5": 2},
    },
    {
        "name": "hold-music",
        "text": (
            "I have been on hold for forty minutes listening to the same "
            "eight seconds of jazz, and a robot keeps telling me my call is "
            "important to them. If my call were important to them, someone "
            "would answer it. I now know this saxophone solo better than my "
            "own family."
        ),
        "scores": {"c1": 5, "c2": 4, "c3": 4, "c4": 4, "c5": 2},
    },
    {
        "name": "autocorrect",
        "text": (
            "Autocorrect changed my boss's name to Dave in a work email, then "
            "changed 'meeting' to 'meatloaf' in the follow-up. I am now the "
            "person who invited the entire department to a meatloaf with "
            "Dave, and Dave has not replied."
        ),
        "scores": {"c1": 4, "c2": 4, "c3": 4, "c4": 4, "c5": 2},
    },
    {
        "name": "elevator",
        "text": (
            "The elevator stops at every single floor, and nobody gets on. "
            "It is not an elevator, it is a sightseeing tour of a building I "
            "already live in. I could have walked up faster, but no \u2014 I "
            "trusted a metal box with commitment issues."
        ),
        "scores": {"c1": 5, "c2": 3, "c3": 3, "c4": 4, "c5": 3},
    },
]

WEIGHTS = {"c1": 5, "c2": 4, "c3": 3, "c4": 2, "c5": 1}


def score(candidate):
    return sum(candidate["scores"][k] * WEIGHTS[k] for k in WEIGHTS)


def validate(text):
    """The gate: UTF-8 text of 1 to 400 characters, not only white space."""
    n = len(text)
    assert text.encode("utf-8"), "not UTF-8"
    assert 1 <= n <= 400, f"{n} chars outside the 1-400 gate"
    assert text.strip(), "entry is only white space"
    return n


def pick():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    print("Candidate scores (weights c1=5 c2=4 c3=3 c4=2 c5=1):")
    for c in ranked:
        print(f"  {c['name']}: {score(c)} ({len(c['text'])} chars)")
    winner = ranked[0]
    print(f"Winner: {winner['name']} ({score(winner)} pts)")
    return winner


def main():
    winner = pick()
    entry = winner["text"]
    n_chars = validate(entry)
    # The grader runs the program in a sandbox where /output is the artifact
    # directory; fall back to a local output/ directory for a local run.
    last_error = None
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            import os

            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(entry)
            print(f"Wrote {n_chars} chars to {path}")
            print(entry)
            # Read it back and re-check, so the file on disk is exactly what
            # was validated above -- no trailing newline, no encoding drift.
            with open(path, encoding="utf-8") as f:
                written = f.read()
            assert written == entry, "round-trip mismatch"
            assert validate(written) == n_chars
            print(f"Verified: {n_chars} chars, inside the 1-400 gate")
            return
        except OSError as e:
            last_error = e
            print(f"Could not write {path}: {e}")
    raise SystemExit(f"Failed to write entry.txt to any location: {last_error}")


if __name__ == "__main__":
    main()
