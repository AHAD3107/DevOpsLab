# Experiment No. 10 — Selenium Web Form Automation

## Requirements
- Python 3.x
- Google Chrome
- Selenium (`python -m pip install selenium`)
- VS Code or another Python editor

## Run
1. Extract this folder.
2. Open the folder in VS Code.
3. In the terminal, run:
   `python -m pip install selenium`
4. Run:
   `python test_registration.py`

Selenium Manager attempts to obtain/use a compatible ChromeDriver automatically. An internet connection may be needed the first time if the driver is not already available.

## Expected tests
Five tests cover valid submission, required name validation, invalid email validation, page title, and a second valid submission. Actual PASS/FAIL results are printed by unittest.

Screenshots are saved to the `screenshots` folder. They are generated when the corresponding tests run.

## Notes
This is a local demonstration form. Its JavaScript displays a success message; it does not store data on a server. Browser-native HTML validation is used for the required name and email checks.
