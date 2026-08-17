# Description 

Assets of the "Introduction to programming" course, ENS Louis-Lumière. 
Author: D. Poirier-Quinot, 2026


# Teacher's notes

- After giving students time to work alone on each script, present the correction. Show script correction, hide comments, and pick a random student (using ./tools/random_student_select.py) to read and explain the script.


# Compile slides

Use VSCode / VSCodium with its Marp extension.


# Install modules 

```bash
pip install -r requirements.txt
```

Make sure to use the correct python to install package

```python
import sys
print(sys.executable)
```

then e.g.
/Users/pyrus/.pyenv/versions/3.13.0/envs/.venv/bin/python -m pip install pygame


# Sound device issue

Might need to force sound device ID on some machines

```python
#  force sound device ID
print(sd.query_devices())
OUTPUT_DEVICE_INDEX = 7
sd.default.device = (None, OUTPUT_DEVICE_INDEX)
```