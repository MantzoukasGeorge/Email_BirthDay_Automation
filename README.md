# Birthday Email Automation

A Python script that checks a list of birthdays and automatically sends a personalized "Happy Birthday" email to anyone whose birthday is today.

## How It Works

1. Reads the list of people from `birthdays.csv`.
2. Compares each person's birth month and day with today's date.
3. For every match, picks one of the letter templates in `letter_templates/` at random.
4. Replaces the `[NAME]` placeholder with the person's name.
5. Sends the email through Gmail's SMTP server over an encrypted (TLS) connection.

## Project Structure

```
Email_BirthDay_Automation/
├── main.py                  # Main script
├── birthdays.example.csv    # Sample data (copy to birthdays.csv)
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11 or newer
- A Gmail account with 2-Step Verification enabled
- A Gmail **App Password** (your regular Gmail password will not work)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Email_BirthDay_Automation.git
cd Email_BirthDay_Automation
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Create a Gmail App Password

1. Turn on 2-Step Verification for your Google account.
2. Go to <https://myaccount.google.com/apppasswords>.
3. Create a new app password and copy the 16-character code.

### 4. Set the environment variables

The script reads your credentials from two environment variables, so they are never stored in the code.

| Variable | Value |
|----------|-------|
| `email`  | Your Gmail address |
| `pass`   | Your Gmail App Password |

**Windows (PowerShell):**

```powershell
$env:email = "your.address@gmail.com"
$env:pass = "your-app-password"
```

**macOS / Linux:**

```bash
export email="your.address@gmail.com"
export pass="your-app-password"
```

These commands only last for the current terminal session. To make them permanent, add them to your system environment variables or to your IDE's run configuration.

### 5. Add your birthdays

Copy the sample file and replace the sample rows with your own data:

```bash
# Windows
copy birthdays.example.csv birthdays.csv
# macOS / Linux
cp birthdays.example.csv birthdays.csv
```

The file uses this format:

```csv
name,email,year,month,day
John,john.smith@example.com,1985,03,14
```

`birthdays.csv` is listed in `.gitignore`, so your personal data stays on your computer.

### 6. Run the script

```bash
python main.py
```

## Customizing the Letters

Edit or add files in `letter_templates/`. Use `[NAME]` wherever the recipient's name should appear. If you change the number of templates, update the `randint(1, 3)` range in `main.py` to match.

## Running It Automatically Every Day

The script only checks the current date, so it needs to run once a day:

- **Windows:** Create a daily task in **Task Scheduler** that runs `python main.py` from the project folder.
- **macOS / Linux:** Add a cron job, for example:
  ```
  0 9 * * * cd /path/to/Email_BirthDay_Automation && /path/to/.venv/bin/python main.py
  ```
- **Cloud:** Use a service such as PythonAnywhere to schedule a daily task.

## Security Notes

- Credentials come from environment variables and are never hard-coded.
- The SMTP connection is encrypted with TLS, and the server's certificate is verified.
- `.gitignore` excludes IDE settings (which can store environment variables in plain text), the virtual environment, and the real `birthdays.csv`.

## Built With

- [Python](https://www.python.org/)
- [pandas](https://pandas.pydata.org/) for reading the CSV file
- `smtplib`, `ssl` and `email` from the Python standard library
