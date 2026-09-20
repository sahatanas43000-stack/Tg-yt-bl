# Fix notes

This version keeps the existing bot features and updates the YouTube/deployment path.

- Uses current yt-dlp with its default YouTube client selection instead of forcing old clients.
- Installs yt-dlp's default dependencies and Deno for current YouTube JS challenge handling.
- Keeps an optional `YOUTUBE_COOKIE_FILE` environment variable; cookies are NOT bundled.
- Removes the duplicate Flask startup path: deploy `bot.py` directly.
- Keeps the existing 80 MB limit, quality buttons, MP3, premium/referral/quota system, force-join, broadcasts and admin commands.
