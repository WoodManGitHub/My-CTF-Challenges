# osu/date-a-live

by jimchen5209

> [!NOTE]
> This is solved after the CTF ended, and the flag is unofficial, sent by community.

## Summary

> My friend is a huge fan of the Date A Live series, and promised me to make a good mapset of the songs. Maybe he isn't a good mapper, though.
> Wrap the secret you got to `osu{...}` format. Note: Flag length (without `osu{}`) is 10.

## Files Provided

- `osu_date-a-live.tar.gz`
  - `sweet ARMS - Date a Live.osz`

## File Analysis

The file contains a beatmap set with 10 beatmaps.

## Challenge Solving

As mentioned, it's related to the Date A Live series, the order is the OPs and EDs of five season anime.

Orders with star difficulty rated in osu! (stable and lazer looks the same, but I taked it with stable).

1. Season 1 OP: `sweet ARMS - Date a Live (sahuang) [Easy].osu`  (★0.68)
2. Season 1 ED: `Nomizu Iori - SAVE MY HEART (TV Size) (sahuang) [4K EZ].osu` (★1.01)
3. Season 2 OP: `sweet ARMS - Trust in you (sahuang) [Easy].osu` (★1.14)
4. Season 2 ED: `Sadohara Kaori - Day to Story (TV Size) (sahuang) [Easy].osu` (★0.51)
5. Season 3 OP: `sweet ARMS - I swear (sahuang) [Easy].osu` (★0.83)
6. Season 3 ED: `Yamazaki Erii - Last Promise (sahuang) [Easy].osu` (★0.52)
7. Season 4 OP: `Tomita Miyu - OveR (sahuang) [EasY].osu` (★0.53)
8. Season 4 ED: `sweet ARMS - S.O.S (TV Size) (sahuang) [Easy].osu` (★0.51)
9. Season 5 OP: `Tomita Miyu - Paradoxes (TV Size) (sahuang) [Easy].osu` (★1.14)
10. Season 5 ED: `sweet ARMS - Hitohira (TV Size) (sahuang) [Easy].osu` (★1.17)

The star difficulty is hiding ASCII letters in DEC, remove the decimal point in the difficulty and find the corresponding letter.

1. `068` -> `D`
2. `101` -> `e`
3. `114` -> `r`
4. `051` -> `3`
5. `083` -> `S`
6. `052` -> `4`
7. `053` -> `5`
8. `051` -> `3`
9. `114` -> `r`
10. `117` -> `u`

## Flag

`osu{Der3S453ru}`

## Sources

- [List of Date A Live episodes - Wikipedia](https://en.wikipedia.org/wiki/List_of_Date_A_Live_episodes)
- [Date A Live season 1 - Wikipedia](https://en.wikipedia.org/wiki/Date_A_Live_season_1)
- [Date A Live season 2 - Wikipedia](https://en.wikipedia.org/wiki/Date_A_Live_season_2)
- [Date A Live season 3 - Wikipedia](https://en.wikipedia.org/wiki/Date_A_Live_season_3)
- [Date A Live season 4 - Wikipedia](https://en.wikipedia.org/wiki/Date_A_Live_season_4)
- [Date A Live season 5 - Wikipedia](https://en.wikipedia.org/wiki/Date_A_Live_season_5)
- [ASCII Table (7-bit) - ASCII Code](https://www.ascii-code.com/ASCII)


