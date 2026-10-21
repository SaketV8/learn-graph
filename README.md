<h1 align="center">Learn Graph</h1>

solving DSA questions on graphs to increase my chances of cracking interviews (-_-)

### [🌸 Everything All At Once (～￣▽￣)～](./EVERYTHING_ALL_AT_ONCE.md)

<details>
<summary><h2> 🚁 Run locally on your machine </h2> </summary>


### Prerequisites

- **WSL (Ubuntu)** if you're on Windows. Run this in PowerShell as admin, then restart:
  ```powershell
  wsl --install
  ```
- **g++ (C++17)** and **Python 3**. Run these inside WSL:
  ```bash
  sudo apt update
  sudo apt install build-essential python3
  g++ --version   # check it works
  ```
- **VS Code** with the **WSL** and **C/C++** extensions

### Setup

1. Clone the repo inside WSL and open it in VS Code:
   ```bash
   git clone <repo-url> learn-graph
   cd learn-graph
   code .
   ```
2. Create `input.txt` and `output.txt` in the root folder (they're gitignored).
3. Add the `cpp-run` task. It's already in `.vscode/tasks.json`; if it's missing, create that file with:
   ```json
   {
       "version": "2.0.0",
       "tasks": [
           {
               "label": "cpp-run",
               "type": "process",
               "command": "bash",
               "args": [
                   "-c",
                   "printf '[ COMPILING ]\\n\\n' > output.txt && g++ -std=c++17 '${file}' -o '${fileDirname}/${fileBasenameNoExtension}' > compile.log 2>&1; if [ $? -ne 0 ]; then printf '[ COMPILETIME ERROR ]\\n\\n' >> output.txt && cat compile.log >> output.txt; else printf '[ RUNNING ]\\n\\n' > output.txt && start=$(date +%s%3N) && timeout 10s '${fileDirname}/${fileBasenameNoExtension}' < input.txt >> output.txt 2>&1; code=$?; end=$(date +%s%3N); runtime=$((end-start)); if [ $code -eq 124 ]; then printf '\\n[ TLE (Time Limit Exceeded) ]\\n' >> output.txt; elif [ $code -eq 139 ]; then printf '\\n[ RUNTIME ERROR (Segmentation Fault) ]\\n' >> output.txt; elif [ $code -eq 134 ]; then printf '\\n[ RUNTIME ERROR (Abort) ]\\n' >> output.txt; elif [ $code -ne 0 ]; then printf '\\n[ RUNTIME ERROR (Exit Code: %s) ]\\n' \"$code\" >> output.txt; else printf '\\n\\n[ COMPLETED ]\\n' >> output.txt; fi; printf '\\n[ FINISHED in %s ms ]\\n' \"$runtime\" >> output.txt; fi"
               ],
               "presentation": {
                   "reveal": "never"
               },
               "problemMatcher": []
           }
       ]
   }
   ```
4. Add the keybinding that runs this task: `Ctrl+Shift+P` → **Preferences: Open Keyboard Shortcuts (JSON)** and paste:
   ```json
   [
       {
           "key": "ctrl+shift+f12",
           "command": "workbench.action.tasks.runTask",
           "args": "cpp-run"
       }
   ]
   ```

### Run

- Open any `.cpp` file, put your input in `input.txt`, and press `Ctrl+Shift+F12`.
- `output.txt` shows the output, plus compile errors, TLE (10s), runtime errors, and how long it ran.

</details>

<details>
<summary><h2> 🏗️ Build the all-in-one page </h2> </summary>

```bash
python3 build.py
```

This regenerates `EVERYTHING_ALL_AT_ONCE.md` with the code from every folder.

To run it automatically before every commit, install the [lefthook](https://github.com/evilmartians/lefthook) git hook once (needs Node.js):

```bash
npm i -g lefthook
lefthook install
```

The hook (`lefthook.yml`) runs `python3 build.py` and adds the regenerated `EVERYTHING_ALL_AT_ONCE.md` to the commit.

</details>