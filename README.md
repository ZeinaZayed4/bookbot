# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

**BookBot** is a Python command-line tool for analyzing the text of books or any text files. It provides a quick overview of the content, including total word count and detailed character frequency analysis.

## Features

- Counts total number of words in a text file.
- Calculates the frequency of each character.
- Displays characters sorted by frequency.

## Requirements

- Python 3.6 or higher.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ZeinaZayed4/bookbot
    ```
2. Navigate to the project:
    ```bash
    cd bookbot
    ```

## Usage

Run the script from the commend line with the path to your text file:
```bash
python3 main.py <path_to_book>
```

Example:
```bash
python3 main.py books/mobydick.txt
```

Expected output:
```
============ BOOKBOT ============
Analyzing book found at books/moby_dick.txt...
----------- Word Count ----------
Found 209117 total words
--------- Character Count -------
e: 12901
t: 9273
a: 8746
...
============= END ===============
```
