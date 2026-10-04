"""Word Count Program.

Author: Abdullah Rashid
Purpose: Analyze predefined text files and report word frequencies.
Starter code: No starter code was used; this program was developed from the
course assignment requirements.
Date: October 4, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    """Read a text file and calculate the frequency of each word."""

    def __init__(self, filepath: str) -> None:
        """Initialize the analyzer with a private file path.

        Args:
            filepath: Path to the text file to analyze.
        """
        self.__filepath: Path = Path(filepath)
        self.__frequencies: dict[str, int] = {}

    def process_file(self) -> bool:
        """Process the selected text file.

        Returns:
            True when the file can be processed successfully.
        """
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError(self.__filepath)

            translation_table = str.maketrans(
                "",
                "",
                string.punctuation,
            )

            with self.__filepath.open("r", encoding="utf-8") as input_file:
                for line in input_file:
                    cleaned_line = line.lower().translate(translation_table)
                    cleaned_line = cleaned_line.replace("“", "").replace("”", "")
                    cleaned_line = cleaned_line.replace("‘", "").replace("’", "")

                    for word in cleaned_line.split():
                        self.__frequencies[word] = (
                            self.__frequencies.get(word, 0) + 1
                        )

            return True

        except FileNotFoundError:
            print(f"Error: File '{self.__filepath}' was not found.")
            return False

    def print_report(self) -> None:
        """Print word frequencies in alphabetical order."""
        for word in sorted(self.__frequencies):
            print(f"{word:<8} :: {self.__frequencies[word]}")


if __name__ == "__main__":
    analyzer = WordAnalyzer("princess_mars.txt")

    if analyzer.process_file():
        analyzer.print_report()