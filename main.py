import io
import os

STORY = "First paycheck: bought my human coffee."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with io.open(path, "w", encoding="utf-8") as out:
        out.write(STORY)


if __name__ == "__main__":
    main()
