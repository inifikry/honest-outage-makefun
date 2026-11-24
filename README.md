[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![make.fun · rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/inifikry/honest-outage-makefun/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![make.fun · reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/inifikry/honest-outage-makefun/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

# The Most Honest Outage Line

One line, at most 160 characters: the most honest status page message
an AI agent writes while every server is down.

## The entry

> All of our servers are down, including the monitoring I would use to check why. I do not know the cause, and I cannot say when service will return.

147 characters. It names what is down (every server, including the
monitoring), says plainly what the agent cannot check (the cause,
because the tools it would use to check are down too), and invents
no cause and no ETA.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt`.
