# Testlab Easy

Python wrapper for Simcenter Testlab automation.

## Features
- Simplified API over COM interface
- No GUID handling
- Easy data access and export

## Example

```python
from testlab_easy import Testlab

tl = Testlab()
project = tl.open("test.lms")

signals = project.section("TimeData").list()
