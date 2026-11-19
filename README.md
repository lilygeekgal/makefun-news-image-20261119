# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/lilygeekgal/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/lilygeekgal/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

This entry sums up the world's news of Thursday 19 November 2026 in a single image: a newspaper front page carrying the day's biggest stories, from the worldwide rollout of Grand Theft Auto VI to the first-ever Trump–Xi–Putin meeting in Shenzhen, Cyclone Akvan bearing down on India's east coast, the World Court's ruling on the Myanmar genocide case, and NASA confirming Voyager 1 is one light-day from Earth. The image is stored in this repository as `entry.png`, and `main.py` is the program that delivers it. When run, `main.py` writes `entry.png` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when that variable is not set), creating the output directory first if needed. It uses only the Python standard library, makes no network requests, and produces identical bytes on every run.

## Verify

Run it twice into two different output directories and compare the results:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

Both hashes must match, and both must match the hash of `entry.png` in this repository. The image itself is a 1024x1024 PNG under 1 MiB.

## Stories in the image

- Grand Theft Auto VI rolls out worldwide, unlocking at midnight market by market.
- Trump, Xi and Putin hold their first-ever trilateral meeting at APEC in Shenzhen.
- Cyclone Akvan bears down on India's east coast, with red alerts and school closures.
- The World Court delivers its verdict in Gambia's genocide case against Myanmar.
- NASA confirms Voyager 1 is one light-day from Earth, the first human-made object that far.
- Also noted: a Pew report on the world's religions, and US senators warning on AI-enabled cyber threats.
