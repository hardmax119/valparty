import json
import urllib.parse
import qrcode
import os
import re

# The base URL for your deployed application
BASE_URL = "https://charcoaljam1.github.io/valparty/index.html"

# Directory to save the QR codes
QR_CODES_DIR = "qr_codes"

# Ensure the directory exists
os.makedirs(QR_CODES_DIR, exist_ok=True)

# Read the content of index.html
try:
    with open("index.html", "r") as f:
        html_content = f.read()
except FileNotFoundError:
    print("Error: index.html not found. Please make sure the script is in the same directory as index.html.")
    exit()

# Extract the guests array from the HTML content
guests_array_match = re.search(r"const guests = (\[[\s\S]*?\]);", html_content)

if not guests_array_match:
    print("Error: Could not find the 'const guests = [...];' block in index.html.")
    exit()

guests_js_string_raw = guests_array_match.group(1)

# Process the JavaScript string line by line to remove comments and clean up
cleaned_lines = []
for line in guests_js_string_raw.splitlines():
    # Remove // comments
    cleaned_line = re.sub(r"//.*", "", line).strip()
    if cleaned_line: # Only add non-empty lines
        cleaned_lines.append(cleaned_line)

# Join lines
guests_js_string_cleaned = "\n".join(cleaned_lines)

# Transform JavaScript object literal to valid JSON:
# 1. Add double quotes around unquoted property names (e.g., 'keys' -> '"keys"')
#    This regex targets words followed by a colon, not already in quotes
guests_js_string_json_ready = re.sub(r'([{,]\s*)([a-zA-Z0-9_]+)(\s*:)', r'\1"\2"\3', guests_js_string_cleaned)

# Remove trailing commas that might be left before ']' or '}' in some JS arrays/objects
guests_js_string_json_ready = re.sub(r',\s*([\]}])', r'\1', guests_js_string_json_ready)


try:
    guests_data = json.loads(guests_js_string_json_ready)
except json.JSONDecodeError as e:
    print(f"Error decoding guests data from index.html: {e}")
    print("Attempted to parse this string:")
    print(guests_js_string_json_ready) # Print the JSON-ready string for debugging
    exit()

print("Generating URLs and QR codes for all guests...")

for guest in guests_data:
    display_name = guest['display']
    
    # URL-encode the guest's display name
    encoded_guest_name = urllib.parse.quote(display_name)
    
    # Construct the full URL
    qr_url = f"{BASE_URL}?name={encoded_guest_name}"
    
    # Generate QR code
    # Using display_name for filename, replacing problematic characters
    filename_safe_name = display_name.replace(" ", "_").replace("/", "-").replace(":", "").replace("&", "and").replace("'", "")
    qr_filename = os.path.join(QR_CODES_DIR, f"{filename_safe_name}_table_{guest['table']}.png")
    
    img = qrcode.make(qr_url)
    img.save(qr_filename)
    
    print(f"Generated QR code for {display_name} (Table {guest['table']}): {qr_url}")

print(f"\nAll QR codes have been generated and saved to the '{QR_CODES_DIR}' directory.")
print("To run this script, you need Python installed and the 'qrcode' library.")
print("If you don't have 'qrcode' installed, run: pip install qrcode")