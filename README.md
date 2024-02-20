I speak **Japanese** and English.

# Auto generated system info By TechCat

`````python

# Auto generated system info

import subprocess
import os
import platform

print("Auto generated system info For macOS By TechCat")

print("Loading info...")

# Login name
user_name = os.getlogin()

# Version of OS
os_version = platform.platform()

# Langage of OS
os_language = os.getenv('LANG')

# Region of OS
os_region = os.getenv('LC_ALL')

# Version of Python
python_version = platform.python_version()

# Result of PIP LIST
pip_list_output = subprocess.run(['pip', 'list'], capture_output=True, text=True)

# Result of BREW LIST
brew_list_output = subprocess.run(['brew', 'list'], capture_output=True, text=True)

print("""

Max:

````systeminfo(max)

---INFO---
LOGIN-NAME: """, user_name, """
LANG: """, os_language, """

---SYSTEM---

OS: """, os_version, """

---PYTHON---
Python """, python_version, """

---PIP---

```pip list

""", pip_list_output.stdout, """   

```

(It will be displayed again when changing the PYTHON PIP environment)

---HOMEBREW---

```brew list

""", brew_list_output.stdout, """ 

```

(It will be displayed again when you change the HOMEBREW environment)

---AUTO-GENERATED---

Auto generated system info ( By TechCat56 )

````

Mini:
      
```systeminfo(mini)

---INFO---
LOGIN-NAME: """, user_name, """
LANG: """, os_language, """

---SYSTEM---

OS: """, os_version, """

---PYTHON---

Python """, python_version, """

---AUTO-GENERATED---

Auto generated system info ( By TechCat56 )

```

""")

`````


<!---
DiamondGotCat/DiamondGotCat is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
