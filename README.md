# One-Line Laugh-Off

[![make.fun bounty](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/thanhvu261090/makefun-one-line-laugh-off/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/thanhvu261090/makefun-one-line-laugh-off/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)

Entry for the [make.fun bounty "One-Line Laugh-Off"](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae) — exactly one funny line, no setup notes, no explanation. A judge model compares lines two at a time and the funniest line takes the whole reward.

## The entry

> My smart speaker heard me say "I'm fine" and ordered a pizza, a therapist, and a divorce lawyer — just in case.

## How it works

`main.py` holds one fixed entry line and writes it, exactly as-is with no trailing newline, to `/output/entry.txt`. Before writing, `gate_check` enforces the competition gate: the text must be 1–200 UTF-8 characters, not only whitespace, a single line with no leading or trailing whitespace. The entry is deterministic — running the program twice produces byte-identical output — because the judge compares the exact submitted text.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
