# town-hall-rsvp
Scan Arkansas gov's site for valid LEARNS town hall rsvp links

The Arkansas state governor has been holding RSVP required "town hall" meetings
to push the agenda of the LEARNS act, a dubious piece of "education" legislation,
rooted in fears of some folks kids going to school with "those people".

While they claim the links are public -- and they are -- they don't publish them. 
Only certain people get the links.

Here's a python3 script that scans a list of Arkansas cities to see if the URL returns a 404,
otherwise it prints the assumed valid URL.

Initial release doesn't include retries; this is very brute force and could perhaps use adjusted timeouts, etc.

Of course you could just Google:  https://www.google.com/search?q=site:governor.arkansas.gov+town+hall+rsvp&rlz=1CDGOYI_enUS736US736&hl=en-US&prmd=imnv&filter=0&biw=428&bih=739&dpr=3&dlnr=1&sei=ojebZPfFAteuqtsPquaD6AY

But the script can be modified for your own needs. Have phun.