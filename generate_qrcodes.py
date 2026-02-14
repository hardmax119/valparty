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

guests_js_string = guests_array_match.group(1)

# Clean up the JavaScript string to make it valid JSON
# Remove comments and ensure proper JSON format
guests_js_string = re.sub(r"//.*?
", "
", guests_js_string) # Remove single-line comments
guests_js_string = re.sub(r",\s*\]", "]", guests_js_string) # Remove trailing commas before ]

try:
    guests_data = json.loads(guests_js_string)
except json.JSONDecodeError as e:
    print(f"Error decoding guests data from index.html: {e}")
    print("Attempted to parse this string:")
    print(guests_js_string)
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
    filename_safe_name = display_name.replace(" ", "_").replace("/", "-").replace(":", "").replace("&", "and")
    qr_filename = os.path.join(QR_CODES_DIR, f"{filename_safe_name}_table_{guest['table']}.png")
    
    img = qrcode.make(qr_url)
    img.save(qr_filename)
    
    print(f"Generated QR code for {display_name} (Table {guest['table']}): {qr_url}")

print(f"
All QR codes have been generated and saved to the '{QR_CODES_DIR}' directory.")
print("To run this script, you need Python installed and the 'qrcode' library.")
print("If you don't have 'qrcode' installed, run: pip install qrcode")
