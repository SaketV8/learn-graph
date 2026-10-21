import os
import re

BASE_DIR = "."          # root folder (where day-1, day-2 exist)
OUTPUT_FILE = "EVERYTHING_ALL_AT_ONCE.md"


def extract_day_number(folder_name):
    match = re.search(r'\d+', folder_name)
    return int(match.group()) if match else float('inf')


def generate_readme():
    # get all folders that contain .cpp files, sorted by number then name
    folders = sorted(
        [
            f for f in os.listdir(BASE_DIR)
            if os.path.isdir(f) and any(x.endswith(".cpp") for x in os.listdir(f))
        ],
        key=lambda f: (extract_day_number(f), f)
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as md:

        md.write("# 🌸 Recursion Practice\n\n")

        for folder in folders:
            # Heading
            md.write(f"## 📂 {folder}\n\n")

            folder_path = os.path.join(BASE_DIR, folder)

            files = sorted([
                f for f in os.listdir(folder_path)
                if f.endswith(".cpp")
            ])

            for file in files:
                file_path = os.path.join(folder_path, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                # Collapsible block
                md.write("<details>\n")
                md.write(f"<summary>📄 {file}</summary>\n\n")
                # md.write(f"<summary>{file}</summary>\n\n")
                md.write(f"\n<h3 align=\"center\"> ⚡ {file} </h3>\n\n")
                md.write("```cpp\n")
                md.write(code)
                md.write("\n```\n")
                md.write("</details>\n\n")

        print("README.md generated successfully! ^_^")


if __name__ == "__main__":
    generate_readme()