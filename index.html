---
layout: none
---

<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Valentine's Seating Finder</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: system-ui, Arial, sans-serif;
      background: linear-gradient(135deg, #ff5f6d, #ffc371);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0;
    }
    .card {
      background: white;
      padding: 2rem;
      border-radius: 16px;
      max-width: 400px;
      width: 100%;
      text-align: center;
      box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    input, button {
      padding: 12px;
      width: 100%;
      border-radius: 8px;
      border: 1px solid #ddd;
      margin-bottom: 1rem;
      font-size: 16px;
    }
    button {
      background: #ff5f6d;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background: #e94b5a;
    }
    .result {
      margin-top: 1rem;
      font-size: 20px; /* Slightly larger for prominence */
      font-weight: bold;
      padding: 15px; /* Add some padding */
      border-radius: 8px; /* Rounded corners */
      transition: all 0.3s ease-in-out; /* Smooth transitions */
    }
    .result.verified {
      background-color: #e6ffe6; /* Light green background */
      color: #006600; /* Dark green text */
      border: 2px solid #006600; /* Green border */
    }
    .result.not-verified {
      background-color: #ffe6e6; /* Light red background */
      color: #cc0000; /* Dark red text */
      border: 2px solid #cc0000; /* Red border */
    }
  </style>
</head>
<body>

  <div class="card">
    <h1>Happy Valentine's Day 💘</h1>
    <p>Enter guest's name for payment verification:</p>
    <input id="name" placeholder="e.g. Tim or Tim Talabi" />
    <button onclick="findSeat()">Verify Payment</button>
    <button onclick="resetCheckIns()" style="background: #ccc; color: #333; margin-top: 10px;">Reset Check-ins</button>
    <div class="result" id="result"></div>
  </div>

  <!-- PASTE YOUR <script> HERE -->
  <script>
    // Initialize checkedIn status from local storage
    let checkedInGuests = JSON.parse(localStorage.getItem('checkedInGuests')) || {};

    const guests = [
      // Table 1
      { keys: ["tim", "tim talabi", "pastor tim talabi"], display: "Pastor Tim Talabi", table: 1, couple: null },
      { keys: ["patrick", "patrick aizebeokhai", "brother patrick aizebeokhai"], display: "Brother Patrick Aizebeokhai", table: 1, couple: "aizebeokhai" },
      { keys: ["lucy", "lucy aizebeokhai", "sister lucy aizebeokhai"], display: "Sister Lucy Aizebeokhai", table: 1, couple: "aizebeokhai" },
      { keys: ["kolawole", "kolawole ajisefinni", "pastor kolawole ajisefinni"], display: "Pastor Kolawole Ajisefinni", table: 1, couple: "ajisefinni" },
      { keys: ["omolade", "omolade ajisefinni", "sister omolade ajisefinni"], display: "Sister Omolade Ajisefinni", table: 1, couple: "ajisefinni" },
      { keys: ["seun", "seun makanjuola", "dcn seun makanjuola"], display: "Dcn Seun Makanjuola", table: 1, couple: "makanjuola" },
      { keys: ["harriet", "harriet makanjuola", "dcns harriet makanjuola"], display: "Dcns Harriet Makanjuola", table: 1, couple: "makanjuola" },
      // Table 2
      { keys: ["bidemi", "bidemi abe", "brother bidemi abe"], display: "Brother Bidemi Abe", table: 2, couple: "abe" },
      { keys: ["bunmi", "bunmi abe", "sister bunmi abe"], display: "Sister Bunmi Abe", table: 2, couple: "abe" },
      { keys: ["olusegun", "olusegun john", "pastor olusegun john"], display: "Pastor Olusegun John", table: 2, couple: "john" },
      { keys: ["serah", "serah john", "sister serah john"], display: "Sister Serah John", table: 2, couple: "john" },
      { keys: ["ricky", "brother ricky"], display: "Brother Ricky", table: 2, couple: null },
      { keys: ["ugo", "sis ugo"], display: "Sis Ugo", table: 2, couple: null },
      { keys: ["peter", "peter egbudu", "brother peter egbudu"], display: "Brother Peter Egbudu", table: 2, couple: "egbudu" },
      { keys: ["egbudu", "sister egbudu"], display: "Sister Egbudu", table: 2, couple: "egbudu" },
      // Table 3
      { keys: ["chuks", "chuks okere", "pastor chuks okere"], display: "Pastor Chuks Okere", table: 3, "couple": "okere" },
      { keys: ["gbemi", "gbemi okere", "sister gbemi okere"], display: "Sister Gbemi Okere", table: 3, "couple": "okere" },
      { keys: ["ololade", "ololade adewumi", "sister ololade adewumi"], display: "Sister Ololade Adewumi", table: 3, "couple": "adewumi" },
      { keys: ["adewumi", "brother adewumi"], display: "Brother Adewumi", table: 3, "couple": "adewumi" },
      { keys: ["idahosa", "brother idahosa"], display: "Brother Idahosa", table: 3, "couple": "idahosa" },
      { keys: ["idahosa", "sister idahosa"], display: "Sister Idahosa", table: 3, "couple": "idahosa" },
      { keys: ["tope", "tope stark", "sister tope stark"], display: "Sister Tope Stark", table: 3, "couple": "stark" },
      { keys: ["stark", "mr stark"], display: "Mr Stark", table: 3, "couple": "stark" },
      // Table 4
      { keys: ["julliet", "julliet ogunkunle", "sister julliet ogunkunle"], display: "Sister Julliet Ogunkunle", table: 4, "couple": "ogunkunle" },
      { keys: ["ogunkunle", "brother ogunkunle"], display: "Brother Ogunkunle", table: 4, "couple": "ogunkunle" },
      { keys: ["omotola", "omotola adelekan", "sister omotola adelekan"], display: "Sister Omotola Adelekan", table: 4, "couple": "adelekan" },
      { keys: ["demola", "demola adelekan", "brother demola adelekan"], display: "Brother Demola Adelekan", table: 4, "couple": "adelekan" },
      { keys: ["folake", "folake adewunmi", "sister folake adewunmi"], display: "Sister Folake Adewunmi", table: 4, "couple": "adewunmi-2" },
      { keys: ["samson", "samson adewunmi", "brother samson adewunmi"], display: "Brother Samson Adewunmi", table: 4, "couple": "adewunmi-2" },
      { keys: ["monica", "sister monica & daughter"], display: "Sister Monica & Daughter", table: 4, "couple": null },
      { keys: ["mohammed", "brother mohammed"], display: "Brother Mohammed", table: 4, "couple": null },
      // Table 5
      { keys: ["funke", "funke adebanwo", "sister funke adebanwo"], display: "Sister Funke Adebanwo", table: 5, "couple": "adebanwo" },
      { keys: ["roland", "roland adebanwo", "brother roland adebanwo"], display: "Brother Roland Adebanwo", table: 5, "couple": "adebanwo" },
      { keys: ["chinyere", "sister chinyere"], display: "Sister Chinyere", table: 5, "couple": null },
      { keys: ["susuti", "dncs susuti"], display: "Dncs Susuti", table: 5, "couple": null },
      { keys: ["elizabeth", "elizabeth ejembi", "sister elizabeth ejembi"], display: "Sister Elizabeth Ejembi", table: 5, "couple": "ejembi" },
      { keys: ["daniel", "daniel ejembi", "brother daniel ejembi"], display: "Brother Daniel Ejembi", table: 5, "couple": "ejembi" },
      { keys: ["johnpaul", "johnpaul akame", "brother johnpaul akame"], display: "Brother Johnpaul Akame", table: 5, "couple": null },
      { keys: ["grandma ejembi"], display: "Grandma Ejembi", table: 5, "couple": null },
      // Table 6
      { keys: ["maxwell", "brother maxwell"], display: "Brother Maxwell", table: 6, "couple": "maxwell" },
      { keys: ["maxwell", "sister maxwell"], display: "Sister Maxwell", table: 6, "couple": "maxwell" },
      { keys: ["kenny", "kenny adunola", "brother kenny adunola"], display: "Brother Kenny Adunola", table: 6, "couple": "adunola" },
      { keys: ["taiwo", "taiwo adunola", "sister taiwo adunola"], display: "Sister Taiwo Adunola", table: 6, "couple": "adunola" },
      { keys: ["florence", "florence roland", "sister florence roland"], display: "Sister Florence Roland", table: 6, "couple": null },
      { keys: ["funto", "sister funto"], display: "Sister Funto", table: 6, "couple": null },
      { keys: ["grace", "grace iyiola", "sister grace iyiola"], display: "Sister Grace iyiola", table: 6, "couple": null },
      { keys: ["atinuke", "sister atinuke"], display: "Sister Atinuke", table: 6, "couple": null },
      // Table 7
      { keys: ["blessing", "blessing omokri", "sister blessing omokri"], display: "Sister Blessing Omokri", table: 7, "couple": "blessing-omokri" },
      { keys: ["blessings husband", "sister blessings husband"], display: "Sister Blessings Husband", table: 7, "couple": "blessing-omokri" },
      { keys: ["sandra", "sandra oni", "sister sandra oni"], display: "Sister Sandra Oni", table: 7, "couple": "oni" },
      { keys: ["oni", "brother oni"], display: "Brother Oni", table: 7, "couple": "oni" },
      { keys: ["ruth", "ruth adesanmi", "sister ruth adesanmi"], display: "Sister Ruth Adesanmi", table: 7, "couple": "adesanmi" },
      { keys: ["adesanmi", "brother adesanmi"], display: "Brother Adesanmi", table: 7, "couple": "adesanmi" },
      { keys: ["paul", "brother paul"], display: "Brother Paul", table: 7, "couple": null },
      { keys: ["sylvester", "brother sylvester"], display: "Brother Sylvester", table: 7, "couple": null },
      // Table 8
      { keys: ["shade", "sister shade"], display: "Sister Shade", table: 8, "couple": null },
      { keys: ["rachel", "rachel george", "sister rachel george"], display: "Sister Rachel George", table: 8, "couple": null },
      { keys: ["nenye", "sister nenye"], display: "Sister Nenye", table: 8, "couple": null },
      { keys: ["cyril", "cyril omogbai", "brother cyril omogbai"], display: "Brother Cyril Omogbai", table: 8, "couple": null }
    ];
  
    function normalize(str) {
      return str.toLowerCase().trim();
    }
  
    function findSeat() {
      const input = normalize(document.getElementById("name").value);
      const resultEl = document.getElementById("result");
      
      // Clear previous classes and content
      resultEl.classList.remove('verified', 'not-verified', 'checked-in');
      resultEl.innerHTML = ''; // Clear content
  
      const guest = guests.find(g =>
        g.keys.some(k => normalize(k) === input)
      );
  
      if (!guest) {
        resultEl.innerHTML = "❌ <strong>Name Not Found. Payment Not Verified.</strong> Please check spelling or see the event organizer.";
        resultEl.classList.add('not-verified');
        return;
      }

      const guestId = guest.display; // Use display name as a unique ID for checking in

      if (checkedInGuests[guestId]) {
          resultEl.innerHTML = `⚠️ <strong>${guest.display} is already Checked In.</strong>`;
          resultEl.classList.add('not-verified'); // Use not-verified style for already checked in
          return;
      }
  
      if (guest.couple) {
        const partner = guests.find(g => g.couple === guest.couple && g.display !== guest.display);
        if (partner) {
          resultEl.innerHTML = `✅ <strong>Payment Verified! Checked In.</strong><br>💑 <strong>${guest.display}</strong> & <strong>${partner.display}</strong><br>💺 You are seated at <strong>Table ${guest.table}</strong>`;
          resultEl.classList.add('verified');
          
          // Mark both guests as checked in
          checkedInGuests[guestId] = true;
          checkedInGuests[partner.display] = true;
          localStorage.setItem('checkedInGuests', JSON.stringify(checkedInGuests));

          return;
        }
      }
  
      resultEl.innerHTML = `✅ <strong>Payment Verified! Checked In.</strong><br>🎉 Welcome <strong>${guest.display}</strong><br>💺 Your table is <strong>Table ${guest.table}</strong>`;
      resultEl.classList.add('verified');

      // Mark single guest as checked in
      checkedInGuests[guestId] = true;
      localStorage.setItem('checkedInGuests', JSON.stringify(checkedInGuests));
    }

    function resetCheckIns() {
        if (confirm("Are you sure you want to reset all checked-in statuses? This cannot be undone.")) {
            localStorage.removeItem('checkedInGuests');
            checkedInGuests = {}; // Reset in-memory state
            const resultEl = document.getElementById("result");
            resultEl.innerHTML = '🔄 All check-in statuses have been reset.';
            resultEl.classList.remove('verified', 'not-verified');
        }
    }

    // Function to get query parameters from the URL
    function getQueryParam(param) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(param);
    }

    // On page load, check for 'name' in URL parameters
    window.onload = function() {
        const guestNameFromURL = getQueryParam('name');
        if (guestNameFromURL) {
            document.getElementById("name").value = guestNameFromURL;
            findSeat();
        }
    };
  </script>


</body>
</html>
