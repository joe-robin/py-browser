# py-browser

A browser built while following [Web Browser Engineering](https://browser.engineering/). You write the code. Cursor is a coach, not a copilot for this repo.

## Setup

```bash
# once, if uv is not installed
curl -LsSf https://astral.sh/uv/install.sh | sh

uv sync
```

Run (after Chapter 1 has an entry point):

```bash
uv run python url.py http://example.org/
```

Chapter 2 needs Tk on the OS, not from pip:

```bash
sudo apt install python3-tk   # Debian/Ubuntu
uv run python -m tkinter      # should open a test window
```

Later chapters add packages with `uv add` (`dukpy` at Ch 9; Skia/SDL at Ch 11).

## How learning works

- You type every line of the browser.
- Ask for a JS → Python syntax refresher before a new section.
- Ask for a review when you want one.
- Do not copy from the book’s `labN.py` solution files.
