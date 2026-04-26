# KMP Algorithm

This program implements the Knuth-Morris-Pratt (KMP) algorithm to determine whether a given pattern appears as a substring inside a text. It also uses the failure function (LPS array) to improve efficiency by avoiding unnecessary comparisons.

## How the algorithm works

The KMP algorithm searches for a pattern inside a text in linear time.

First, it computes the **failure function** (also called **LPS: Longest Prefix Suffix**), which stores the length of the longest proper prefix of the pattern that is also a suffix for each position.

During the search:

- The text is scanned from left to right.
- If characters match, both pointers move forward.
- If a mismatch occurs, the algorithm uses the LPS values to skip redundant comparisons instead of restarting from the beginning.

This makes the algorithm efficient, with time complexity:

O(n + m)

Where:

- n = length of the text
- m = length of the pattern

---

## Pseudocode

### Compute LPS Array

1. Initialize an array `lps` with zeros.
2. Compare characters inside the pattern.
3. Store prefix/suffix matches in the array.
4. Continue until the full pattern is processed.

### Search Process

1. Compare text and pattern characters.
2. If they match, move both indices.
3. If mismatch:
   - Use LPS to move the pattern index.
   - Do not move backward in the text.
4. If all pattern characters match, the pattern is found.

---

## Environment

The program was developed using:

- Python 3.12
- Visual Studio Code

---

## How to run

1. Download the project.
2. Open a terminal inside the project folder.
3. Run the program:

 ```
   python main.py
   ```
Or for the tracing version:
 ```
   python exercise.py
   ```

## Example Input.
 ```
    Enter text: "abababaab"
    Enter pattern: "ababaa"
   ```
## Example Output.
 ```
    Pattern FOUND.
   ```

## Exercise 3.4.6 Results.
### Pattern.
 ```
    "ababaa".
   ```
### Text tested.
    1. `abababaab` -> Pattern FOUND.
    2. `abababbaa` -> Pattern NOT found.

## Outputs
For String #1.

Input.
<img width="259" height="139" alt="image" src="https://github.com/user-attachments/assets/bcc57752-33f0-41ec-90f9-09a6db9e4e4b" />
Tracing process.
<img width="332" height="622" alt="image" src="https://github.com/user-attachments/assets/51a6ce90-c087-4c48-8d44-92233dba17ff" />
Output.
<img width="257" height="28" alt="image" src="https://github.com/user-attachments/assets/a89fa0dc-5680-4be6-8b84-53983c329187" />

For String #2.

Input.
<img width="257" height="141" alt="image" src="https://github.com/user-attachments/assets/5e82e340-4518-42e8-a675-2cae97e4555f" />
Tracing process.
<img width="333" height="736" alt="image" src="https://github.com/user-attachments/assets/f66c1991-775c-4582-97c6-75c491cb3084" />
<img width="323" height="181" alt="image" src="https://github.com/user-attachments/assets/7e5b5d5a-d46d-4c6f-9d32-396caff0d39e" />
Output.
<img width="167" height="32" alt="image" src="https://github.com/user-attachments/assets/0074652a-76d8-4153-b308-9331362a2e18" />

## Files Included

 - `kmp.py` → KMP algorithm implementation.
 - `main.py` → Basic execution program.
 - `exercise.py` → Step-by-step tracing version.
 - `lexer.py` → Token recognition using KMP.
 - `README.md` → Project documentation.

