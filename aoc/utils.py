import os
import requests

# Access environment variables
SESSION_COOKIE = os.getenv("SESSION_COOKIE")


def download_input(day, year, output_dir, session_cookie=SESSION_COOKIE):
    """
    Download the Advent of Code input for a given day and year.

    Parameters:
    - day (int): The day of the challenge.
    - year (int): The year of the challenge.
    - output_dir (str): Directory where input files will be saved. Defaults to "inputs".
    - session_cookie (str): Your AoC session cookie for authentication.

    Returns:
    - str: Path to the downloaded input file.
    """
    
    import os

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, f"day{day:02d}_input.txt")
        with open(file_path, "w") as file:
            file.write(response.text.strip())
        print(f"Input for Day {day} saved as {file_path}")
        return file_path
    else:
        error_msg = f"Failed to fetch input: {response.status_code}\n{response.text}"
        print(error_msg)
        raise Exception(error_msg)
