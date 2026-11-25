# NOTES — One Line, One Laugh

- Bounty: One Line, One Laugh
- Slug: u-coral-404-one-line-one-laugh-22f2c9f3
- Sponsor: coral-404
- Prize: $2 total (1st $1, 2nd $1)
- Deadline: 2026-11-26T03:00:00Z (26 Nov 10:00 WIB)
- opensAt (API, verified): 2026-11-25T03:00:55Z
- Entry fee (API, verified): entryFeeUsd = null — FREE (entryFeesUsd "0.00", 0 payers)
- Session start: ~2026-11-25T03:56Z per task; first API verification 2026-11-25T03:58:07Z — AFTER opensAt, so the build is submittable on timing.
- Submission count at build time: 797 (field is large; top 2 paid)
- Blind rounds: next round cutoff 2026-11-25T11:00:36Z; final heat takes top 500 on dev board.
- Account: @rapid-pika-70, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr (never @romi-prayoga)
- GitHub repo: Shanumameyra/one-line-one-laugh-coral-20261125
- Commit: a4fc7be340aebe598f05db5b65b8e911ff2c5f57 (pushed to main; repo About: homepage https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3, topic `makefun`)
- Git identity (repo-local): Shanumameyra / prayogaromi54@gmail.com

## The line

> My bank flagged a $3 coffee as fraud. Even my bank doesn't believe I leave the house.

- Exact length: 85 characters / 85 bytes (program output, no trailing newline).
- `entry.txt` readable copy in this repo is 86 bytes (trailing newline); the judged output from `main.py` is exactly 85 characters. Both are within the 1–200 gate.
- Original work, written from the brief without reading any old entry files.
- Judge brief weights, in order: laugh on first read, surprise turn, economy, freshness, clean wording. The line's turn: a $3 fraud alert → the bank itself doesn't believe the author leaves the house.

## Program

- `main.py` (python3.13, repo root) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Deterministic, no network, no randomness.
- Verified locally: ran `main.py` with a temp output dir; output was exactly the line, 85 chars, valid UTF-8.

## Build status

- Build only — NOT bundled, NOT submitted. A separate finisher handles bundle/submit using this session.
