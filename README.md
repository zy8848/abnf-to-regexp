
This is new readme file adapted based on `README.rst`.
# Development
Check out the repository.
In the repository root, create the virtual environment:
```
python3 -m venv venv3
```
Activate the virtual environment (in this case, on Linux):
```
source venv3/bin/activate
```
Install the development dependencies:
```
pip3 install -e .[dev]
```
# abnf-to-regexp usage


In `abnf_test/input_abnf`, we put several files containing abnf rules for testing. To converting these files into regexp, you can use the following command:
```
python abnf_to_regexp/main.py -i abnf_test/input_abnf/rfc5234.txt -o abnf_test/output_py/rfc5234.py --format python-nested
```
In this example, we take `abnf_test/input_abnf/rfc5234.txt` as input abnf file, and the output is a python file which contains regexp for that abnf file.

The logic for removing the cycle in abnf is in commit `ed8b4cf37fef5ae2504020672c845d4504d479ae`.

This repo is only for converting, it doesn't include script for extracting abnf from rfc documents.
