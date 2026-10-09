"""
python_string_methods.py

Demonstrates commonly used Python string methods in real-world software engineering,
including sanitization, formatting, parsing, searching, and validation.
"""


def demonstrate_string_methods():
    print("=" * 60)
    print(" 1. TRIMMING & SANITIZATION")
    print("=" * 60)
    user_input = "  \n  hello_user@example.com \t \r "
    # strip() removes leading and trailing whitespace
    cleaned_email = user_input.strip()
    print(f"Original input : {repr(user_input)}")
    print(f"Cleaned email  : {repr(cleaned_email)}")

    # lstrip() and rstrip() remove characters from a specific side
    raw_path = "///var/logs/app.log///"
    print(f"Trimmed left   : {repr(raw_path.lstrip('/'))}")
    print(f"Trimmed right  : {repr(raw_path.rstrip('/'))}")

    print("\n" + "=" * 60)
    print(" 2. SPLITTING & JOINING")
    print("=" * 60)
    # split() separates a string into a list based on a delimiter
    csv_line = "Jacob,Software Engineer,Engineering,Active"
    fields = csv_line.split(",")
    print(f"CSV Line       : {csv_line}")
    print(f"Parsed Fields  : {fields}")

    # join() concatenates an iterable of strings using a specified separator
    tags = ["python", "backend", "string-processing"]
    tag_string = ", ".join(tags)
    print(f"Joined Tags    : {tag_string}")

    # splitlines() splits text by line breaks (useful for log/file processing)
    multiline_log = "Error 404\nWarning 200\nInfo 100"
    print(f"Split Lines    : {multiline_log.splitlines()}")

    print("\n" + "=" * 60)
    print(" 3. CASE CONVERSIONS & NORMALIZATION")
    print("=" * 60)
    raw_header = "X-api-TOKEN-Key"
    # lower() and upper() for standardization
    print(f"Lowercase      : {raw_header.lower()}")
    print(f"Uppercase      : {raw_header.upper()}")

    # title() and capitalize() for display names
    title_text = "python programming for backend developers"
    print(f"Title Case     : {title_text.title()}")
    print(f"Capitalized    : {title_text.capitalize()}")

    print("\n" + "=" * 60)
    print(" 4. SEARCHING & CHECKING PREFIXES / SUFFIXES")
    print("=" * 60)
    filename = "report_2026_q3.pdf"

    # startswith() and endswith() accept single strings or tuples of strings
    is_pdf = filename.endswith(".pdf")
    is_doc = filename.endswith((".doc", ".docx", ".pdf"))
    is_report = filename.startswith("report_")
    print(f"Filename       : {filename}")
    print(f"Ends with .pdf : {is_pdf}")
    print(f"Valid Document : {is_doc}")
    print(f"Starts with 'report_': {is_report}")

    # find() returns the lowest index (-1 if not found), index() raises ValueError if missing
    log_msg = "[ERROR] Database connection timed out."
    error_idx = log_msg.find("ERROR")
    print(f"Find 'ERROR'   : Index {error_idx}")

    print("\n" + "=" * 60)
    print(" 5. REPLACING & TRANSLATING")
    print("=" * 60)
    template = "Hello, {user_name}! Your account balance is {amount}."
    # replace() substitutes occurrences of a substring
    formatted = template.replace("{user_name}", "Jacob").replace("{amount}", "$150.00")
    print(f"Replaced String: {formatted}")

    # maketrans() and translate() for bulk character replacement / mapping
    dirty_text = "Phone: +1 (555) 019-2834"
    # Remove parentheses, spaces, and hyphens
    trans_table = str.maketrans("", "", " ()-")
    sanitized_phone = dirty_text.translate(trans_table)
    print(f"Original Phone : {dirty_text}")
    print(f"Cleaned Phone  : {sanitized_phone}")

    print("\n" + "=" * 60)
    print(" 6. STRING VALIDATION (CHARACTER CHECKS)")
    print("=" * 60)
    user_id = "109482"
    alphanumeric_code = "ABC123"
    padded_str = "   "

    # isdigit(), isalpha(), isalnum(), isspace()
    print(f"'{user_id}' isdigit()    : {user_id.isdigit()}")
    print(f"'{alphanumeric_code}' isalnum(): {alphanumeric_code.isalnum()}")
    print(f"'{padded_str}' isspace()  : {padded_str.isspace()}")

    print("\n" + "=" * 60)
    print(" 7. PADDING & ALIGNMENT")
    print("=" * 60)
    code = "42"
    # zfill() pads string on the left with zeros to fit specified length
    padded_code = code.zfill(6)
    print(f"Zero Padded    : {padded_code}")

    # ljust(), rjust(), center() for aligned output
    header = "SUMMARY"
    print(f"Centered       : '{header.center(20, '-')}'")
    print(f"Left Justified : '{header.ljust(15, '.')}'")
    print(f"Right Justified: '{header.rjust(15, '.')}'")


if __name__ == "__main__":
    demonstrate_string_methods()
