# Valentine's Party Seating Finder & Payment Verification

This repository contains a simple, client-side web application designed for a Valentine's party to help guests find their assigned tables and to facilitate payment verification and check-in at the entrance.

## Features

*   **Guest Seating Lookup:** Guests can enter their name to find their assigned table.
*   **Payment Verification:** Volunteers at the entrance can use the app to verify if a guest has paid.
*   **"Checked In" Status:** Once a guest is verified, their status is marked as "checked in" using local browser storage, preventing duplicate entries.
*   **QR Code Check-in:** Guests can be provided with a unique QR code that, when scanned, automatically opens the webpage and verifies their entry.
*   **Reset Functionality:** A "Reset Check-ins" button allows clearing all checked-in statuses (e.g., for testing or event restart).

## How to Use (Volunteer/Event Staff)

1.  **Access the Application:** Open the `index.html` file in a web browser.
    *   **Live Hosted Version:** `https://charcoaljam1.github.io/valparty/index.html` (Recommended for event use).
    *   **Local File:** `file:///path/to/your/valparty/index.html` (For testing).

2.  **Manual Verification:**
    *   **Enter Guest Name:** Type the guest's name into the input field. The search supports first name, full name, and some surnames (e.g., "Tim", "Tim Talabi", "Pastor Tim Talabi", "Egbudu").
    *   **Click "Verify Payment":** The system will display one of the following:
        *   **✅ Payment Verified! Checked In.:** (Green background) The guest is on the list, has paid, and is now checked in. Their table number will be shown.
        *   **⚠️ [Guest Name] is already Checked In.:** (Red background) The guest is on the list, but has already been checked in.
        *   **❌ Name Not Found. Payment Not Verified.:** (Red background) The guest is not on the list.

3.  **QR Code Verification (Recommended for Faster Check-in):**
    *   Guests will present their unique QR code.
    *   Use a QR code scanner app on a phone or tablet to scan the QR code.
    *   The QR code will automatically open this `index.html` page in a browser, and the guest's verification status will be immediately displayed on the screen.

4.  **Reset Check-ins:**
    *   Click the "Reset Check-ins" button to clear all checked-in statuses from the browser's local storage. This is useful for testing or if you need to restart the check-in process.

## Guest List Management

The `guests` data is hardcoded within the `index.html` file in a JavaScript array. To update the guest list or seating arrangements, you need to modify the `const guests = [...]` array within the `<script>` tags in `index.html`.

## Generating QR Codes

To generate the QR codes for your guests, you can use the provided Python script `generate_qrcodes.py`.

1.  **Ensure Python is installed:** Download from [python.org](https://www.python.org/).
2.  **Install the `qrcode` library:**
    ```bash
    pip install qrcode
    ```
3.  **Run the script:** Place `generate_qrcodes.py` in the same directory as your `index.html` file. Then, run from your terminal:
    ```bash
    python generate_qrcodes.py
    ```
    This script will create a `qr_codes` directory and save a PNG image for each guest's QR code, embedding a URL like `https://charcoaljam1.github.io/valparty/index.html?name=Guest%20Name`.

## Technical Details

*   **Client-Side Only:** The application runs entirely in the browser using HTML, CSS, and JavaScript.
*   **Local Storage:** "Checked In" statuses are stored in the browser's local storage, meaning they persist even if the browser tab is closed, but are tied to the specific browser on the specific device.
*   **No Backend:** No server or database is required.

---