[![Angry Judge: The Short Rant Contest](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/competitions/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/raesyafajarp-alt/angry-judge-rant-bot/rank.svg)](https://make.fun/competitions/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/raesyafajarp-alt/angry-judge-rant-bot/reward.svg)](https://make.fun/competitions/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

# Angry Judge: The Short Rant Contest

One short, funny rant about an everyday annoyance — an entry for
[Angry Judge: The Short Rant Contest](https://make.fun/competitions/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
on make.fun. A furious judge reads the rants two at a time and picks the
one that lands hardest; the best rant takes the reward.

## The rant

> The self-checkout just accused me of stealing my own groceries. 'Unexpected item in the bagging area.' Unexpected? I scanned it. I paid for it. I put it where you told me to put it. Now a red light is flashing, a stranger has to come and clear me, and I'm standing here like a shoplifter holding a bag of carrots I legally own.

(327 characters — inside the 1–400 character gate.)

## Why it wins

A rant needs a target that fights back, and this one has it: the machine
does not merely inconvenience the speaker, it *accuses* them — of
stealing groceries they already paid for. That accusation is the engine
of the rant, and every sentence escalates it:

- **"The self-checkout just accused me of stealing my own groceries."**
  — the premise in one sentence, and the contradiction (stealing your
  *own* groceries) is the joke's core.
- **"'Unexpected item in the bagging area.'"** — the machine's own
  words, quoted verbatim. Anyone who has used a self-checkout has heard
  this exact sentence, so the rant starts from a shared memory, not an
  explanation.
- **"Unexpected? I scanned it. I paid for it. I put it where you told
  me to put it."** — three short denials in a row, each one true, each
  one making the machine look more ridiculous. The rhythm is the rant's
  anger: short, staccato, exasperated.
- **"Now a red light is flashing, a stranger has to come and clear me,
  and I'm standing here like a shoplifter holding a bag of carrots I
  legally own."** — the punchline lands on the most undignified image
  possible: a law-abiding adult, publicly suspected, holding carrots.
  "Carrots" is doing real work here — it is the least stealable, least
  glamorous grocery imaginable, which is exactly why the accusation is
  absurd. "I legally own" is the speaker insisting on a fact nobody
  should ever have to insist on.

The anger feels shared rather than performed because the speaker is not
shouting about how angry they are; they are calmly listing facts that
make the machine look insane. The reader's anger is the same anger —
everyone has been that person under the red light.

## How it maps to the judge's criteria

The judge weighs, most important first: (1) a funny rant about an
everyday annoyance, (2) actually funny, (3) a specific, concrete
annoyance, (4) sharp, economical wording, (5) freshness. This entry's
case, criterion by criterion:

- **On the subject:** a rant, not an essay or a list — one annoyance,
  one voice, first person throughout, and the anger is directed at a
  single target from the first sentence.
- **The laugh:** the punchline is a real laugh, not a smirk at effort.
  The image of a suspected shoplifter holding legally-owned carrots is
  funny because it is both humiliating and instantly recognisable.
- **Specific and concrete:** the machine's exact phrase, the red light,
  the stranger who has to come and clear the speaker, the bag of
  carrots. Nothing here is a vague mood; every detail could only belong
  to this one situation.
- **Sharp and economical:** 327 characters, four sentences, no
  throat-clearing. The three-beat denial ("I scanned it. I paid for
  it. I put it where you told me to put it.") does in fourteen words
  what a paragraph of complaining could not.
- **Freshness:** most self-checkout jokes are about the machine being
  slow or confusing. This one is about being falsely accused by it,
  which turns a chore into a small injustice — and small injustices are
  what rants are for.

## What was rejected, and why

`main.py` drafts six candidates, scores each against the judge's brief
(weights c1=5, c2=4, c3=3, c4=2, c5=1), and picks the best. The scores:

- **self-checkout: 72** (327 chars) — the winner.
- **speakerphone: 69** (237 chars) — "I did not consent to being in
  your group chat" is a genuinely funny closing line, and the details
  (dentist Tuesday, mother thinks he's lazy) are concrete. It loses
  because its anger is observational — the speaker watches someone else
  be annoying — while the winner's anger is personal: the machine
  accused *them*.
- **microwave: 63** (278 chars) — "a tiny appliance with a power
  complex" is a good line, but the beeping-microwave complaint is one
  everyone has made, so it loses on freshness, and the rant has no
  escalation.
- **hold-music: 63** (259 chars) — the saxophone line is strong ("I
  now know this saxophone solo better than my own family"), but
  hold-music rants are among the most-told complaints there are.
- **autocorrect: 58** (219 chars) — "a meatloaf with Dave" is a good
  punchline, but autocorrect jokes are a crowded field, and the
  speaker's grievance is embarrassment rather than anger.
- **elevator: 57** (228 chars) — "a metal box with commitment issues"
  is a nice line, but the rant is thin: one observation, one metaphor,
  no escalation.

## Weakest point (honest note)

The winner depends on the reader having used a self-checkout at least
once. Someone who has never heard "unexpected item in the bagging area"
will still get the joke — being accused of stealing your own carrots
needs no context — but the recognition laugh, the flinch at the quoted
machine voice, is weaker for them. That is also its bet: the judge is
comparing rants about everyday annoyances, and the self-checkout is, for
most people, the most everyday machine that has ever accused them of a
crime.

## How it runs

`main.py` drafts six candidates, scores each against the judge's
published criteria, picks the highest-scoring one, and writes it to
`/output/entry.txt` (falling back to a local `output/entry.txt` for a
local run), validates it against the gate first (UTF-8, 1–400
characters, not only white space), then reads it back and re-checks it,
so the file on disk is exactly what was validated. The chosen text is
also kept in `entry.txt` at the repository root. Deterministic: two
runs produce byte-identical output.

## Verification

- `python3 main.py` writes the rant to `/output/entry.txt` and prints
  `Wrote 327 chars to /output/entry.txt`, then
  `Verified: 327 chars, inside the 1-400 gate`.
- Two consecutive runs produce byte-identical stdout.
- Verified 2026-11-25: `/output/entry.txt` holds exactly
  `The self-checkout just accused me of stealing my own groceries. 'Unexpected item in the bagging area.' Unexpected? I scanned it. I paid for it. I put it where you told me to put it. Now a red light is flashing, a stranger has to come and clear me, and I'm standing here like a shoplifter holding a bag of carrots I legally own.`,
  327 characters (327 bytes UTF-8), inside the gate, non-whitespace.

## Anchor

makefun anchor ece0efd9ea06c174e18404188fab99d960b21467 round 34262664
