# Make the AI Judge Laugh: Developer Excuses

[![Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/morenoo-del/makefun-dev-excuses-20261124/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/morenoo-del/makefun-dev-excuses-20261124/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

One funny single-line excuse a developer gives when code breaks in production, for the [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) bounty on [make.fun](https://make.fun).

## The entry

> The code passed all 400 tests — unfortunately, production wasn't one of them.

The joke: every developer has hidden behind a green test suite at least once. The twist is that production — the one environment that actually matters — was never in the test plan. It sounds like something a developer would actually say in an incident call, and it lands in a single line.

## How it works

`main.py` (Python 3.13) writes the excuse to `/output/entry.txt`. It asserts the entry is a single line of 1–200 characters before writing, so the program enforces the bounty gate itself.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
