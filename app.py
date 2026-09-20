"""Compatibility health server.
The deployed bot entrypoint is bot.py; bot.py owns its Flask keep-alive server.
"""

from bot import flask_app

app = flask_app

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
