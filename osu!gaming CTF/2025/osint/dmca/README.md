# osint/dmca

by WoodMan

## Summary

> Peppy once received a DMCA takedown request for osu! due to alleged copyright infringement. The client, however, spelled "osu!" wrong.
> Can you find out the email address of the client who sent the DMCA request? Wrap in `osu{}` and submit.

## Challenge Solving

I searched on DuckDuckGo for: **osu dmca peppy**

After scrolling for a while, I found this document: https://github.com/seedcrack/osu-DMCA-maps-finder/blob/main/notices.txt

From the [first file](https://gist.githubusercontent.com/peppy/079dc3f77e316f9cd40077d411319a72/raw), I noticed a typo in the first line: **Dear OUS!’s designated Agent,**

Wrap the email addresses in the content with **osu{}**.

## Flag

`osu{neowizip@neowiz.com}`

