# Password Manager

A desktop GUI app for generating, saving and looking up website passwords, built with Python and Tkinter.

## How to Run
1. Make sure Python 3 is installed
2. Install the dependency:
   ```
   pip install pyperclip
   ```
3. Clone the repository
4. Run `python main.py`

## Features
- Save website credentials (website, email/username, password) to a local `data.json` file
- Generate a strong random password with one click; it's automatically copied to your clipboard
- Search for a saved website to see its email and password
- Input validation stops you from saving with empty fields
- Handles a missing or empty data file without crashing

## Data Storage
Credentials are saved in `data.json` in the project folder. See `data_example.json` for the format.
`data.json` is listed in `.gitignore`, so your real passwords are never uploaded to GitHub.

> ⚠️ Passwords are stored as plain text (not encrypted). This is a learning project, so don't use it for real passwords.

## Future Improvements
- Encrypt stored passwords with a master password
- Add a confirmation dialog before saving

## Technologies Used
- Python 3
- Tkinter
- JSON file handling
- pyperclip
