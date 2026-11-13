# Make the AI judge laugh

Entry for the make.fun bounty
[ai-joke-03](https://make.fun/bounty/ai-joke-03) — write the funniest
one-liner about AI coding agents; an AI judge compares jokes pairwise
and the 50 best win rates share $150.

## The joke

> My AI coding agent had one job: fix a typo. It fixed the typo, rewrote
> the entire auth system, and left a commit message that just says
> "you're welcome."

## How it works

`main.py` (Python 3.13, standard library only, no network) writes exactly
that one joke to `/output/entry.txt` — the file the make.fun grader reads.
It is fully deterministic: no randomness, no time dependence, every run
writes the same bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
