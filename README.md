# multiplehooks
Small library that monkey patches multiple pre + post invoke hooks on discord.py. Open-sourced version of what's used in [Kolumbao](https://kolumbao.com/).

This overrides the given bot's `_before_invoke`, `before_invoke`, `_after_invoke`, `after_invoke` attributes, so be careful if you override these yourself.

## Installation
To install the package to your Python installation, clone the repository locally then run the following command in the repository's directory.
```bash
py setup.py install
```

You can now use the library!

## Usage
```python
from discord.ext import commands
from multiplehooks import before, after

# Initialize the bot
bot = commands.Bot("prefix")

# Setup
before(bot)
after(bot)

# Done!
```

## Issues
If you encounter any problems, check out [current issues](https://github.com/starsflower/multiplehooks/issues) or [make a new issue](https://github.com/starsflower/multiplehooks/issues/new).
