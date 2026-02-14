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
      font-size: 18px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <div class="card">
    <h1>Happy Valentine's Day 💘</h1>
    <p>Enter your first name or full name to find your seat</p>
    <input id="name" placeholder="e.g. Tim or Tim Talabi" />
    <button onclick="findSeat()">Find My Table</button>
    <div class="result" id="result"></div>
  </div>

  <!-- PASTE YOUR <script> HERE -->
  <script>
    const guests = [
      // Table 1
      { keys: ["tim", "tim talabi", "pastor tim talabi"], display: "Pastor Tim Talabi", table: 1, couple: null },
      { keys: ["patrick", "patrick aizebeokhai"], display: "Brother Patrick Aizebeokhai", table: 1, couple: "aizebeokhai" },
      { keys: ["lucy", "lucy aizebeokhai"], display: "Sister Lucy Aizebeokhai", table: 1, couple: "aizebeokhai" },
      { keys: ["kolawole", "kolawole ajisefinni"], display: "Pastor Kolawole Ajisefinni", table: 1, couple: "ajisefinni" },
      { keys: ["omolade", "omolade ajisefinni"], display: "Sister Omolade Ajisefinni", table: 1, couple: "ajisefinni" },
  
      // Table 2
      { keys: ["bidemi", "bidemi abe"], display: "Brother Bidemi Abe", table: 2, couple: "abe" },
      { keys: ["bunmi", "bunmi abe"], display: "Sister Bunmi Abe", table: 2, couple: "abe" },
      { keys: ["olusegun", "olusegun john"], display: "Pastor Olusegun John", table: 2, couple: "john" },
      { keys: ["serah", "serah john"], display: "Sister Serah John", table: 2, couple: "john" },
      { keys: ["seun", "seun makanjuola"], display: "Deacon Seun Makanjuola", table: 2, couple: "makanjuola" },
      { keys: ["harriet", "harriet makanjuola"], display: "Deaconess Harriet Makanjuola", table: 2, couple: "makanjuola" },
  
      // Table 3
      { keys: ["chuks", "chuks okere"], display: "Pastor Chuks Okere", table: 3, couple: "okere" },
      { keys: ["gbemi", "gbemi okere"], display: "Sister Gbemi Okere", table: 3, couple: "okere" },
      { keys: ["ololade", "ololade adewumi"], display: "Sister Ololade Adewumi", table: 3, couple: "adewumi" },
      { keys: ["adewumi"], display: "Brother Adewumi", table: 3, couple: "adewumi" },
      { keys: ["peter", "peter egbudu"], display: "Brother Peter Egbudu", table: 3, couple: "egbudu" },
      { keys: ["egbudu"], display: "Sister Egbudu", table: 3, couple: "egbudu" },
  
      // Table 4
      { keys: ["julliet", "julliet ogunkunle"], display: "Sister Julliet Ogunkunle", table: 4, couple: "ogunkunle" },
      { keys: ["ogunkunle"], display: "Brother Ogunkunle", table: 4, couple: "ogunkunle" },
      { keys: ["omotola", "omotola adelekan"], display: "Sister Omotola Adelekan", table: 4, couple: "adelekan" },
      { keys: ["demola", "demola adelekan"], display: "Brother Demola Adelekan", table: 4, couple: "adelekan" },
      { keys: ["idahosa sister"], display: "Sister Idahosa", table: 4, couple: "idahosa" },
      { keys: ["idahosa brother"], display: "Brother Idahosa", table: 4, couple: "idahosa" },
  
      // Table 5
      { keys: ["funke", "funke adebanwo"], display: "Sister Funke Adebanwo", table: 5, couple: "adebanwo" },
      { keys: ["roland", "roland adebanwo"], display: "Brother Roland Adebanwo", table: 5, couple: "adebanwo" },
      { keys: ["folake", "folake adewummi"], display: "Sister Folake Adewummi", table: 5, couple: "adewunmi" },
      { keys: ["samson", "samson adewunmi"], display: "Brother Samson Adewunmi", table: 5, couple: "adewunmi" },
      { keys: ["tope", "tope stark"], display: "Sister Tope Stark", table: 5, couple: "stark" },
      { keys: ["stark", "mr stark"], display: "Mr Stark", table: 5, couple: "stark" },
  
      // Table 6
      { keys: ["ricky"], display: "Brother Ricky", table: 6, couple: null },
      { keys: ["monica"], display: "Sister Monica & Daughter", table: 6, couple: null },
      { keys: ["mohammed"], display: "Brother Mohammed", table: 6, couple: null },
      { keys: ["ugo"], display: "Sister Ugo", table: 6, couple: null },
      { keys: ["chinyere", "chinyere dundee"], display: "Sister Chinyere Dundee", table: 6, couple: null },
  
      // Table 7
      { keys: ["max", "maxwell ndugatuda"], display: "Brother Maxwell", table: 7, couple: "maxwell" },
      { keys: ["adati", "adati maxwell"], display: "Sister Maxwell", table: 7, couple: "maxwell" },
      { keys: ["kenny", "kenny adunola"], display: "Brother Kenny Adunola", table: 7, couple: "adunola" },
      { keys: ["taiwo", "taiwo adunola"], display: "Sister Taiwo Adunola", table: 7, couple: "adunola" },
      { keys: ["daniel", "daniel ejembi"], display: "Brother Daniel Ejembi", table: 7, couple: "ejembi" },
      { keys: ["elizabeth", "elizabeth ejembi"], display: "Sister Elizabeth Ejembi", table: 7, couple: "ejembi" },
      { keys: ["jp", "john-paul", "john paul akame"], display: "Brother John-Paul Akame", table: 7, couple: null },
  
      // Table 8
      { keys: ["susuti"], display: "Deaconess Susuti", table: 8, couple: null },
      { keys: ["grandma ejembi"], display: "Grandma Ejembi", table: 8, couple: null },
      { keys: ["florence", "florence roland"], display: "Sister Florence Roland", table: 8, couple: null },
      { keys: ["funto"], display: "Sister Funto", table: 8, couple: null },
      { keys: ["grace", "grace iyiola"], display: "Sister Grace Iyiola", table: 8, couple: null },
      { keys: ["atinuke"], display: "Sister Atinuke", table: 8, couple: null },
  
      // Table 9
      { keys: ["blessing", "blessing omokri"], display: "Sister Blessing Omokri", table: 9, couple: "blessing-omokri" },
      { keys: ["omokri"], display: "Brother Omokri", table: 9, couple: "blessing-omokri" },
      { keys: ["sandra", "sandra oni"], display: "Sister Sandra Oni", table: 9, couple: "oni" },
      { keys: ["oni"], display: "Brother Oni", table: 9, couple: "oni" },
  
      // Table 10
      { keys: ["paul"], display: "Brother Paul", table: 10, couple: null },
      { keys: ["sylvester"], display: "Brother Sylvester", table: 10, couple: null },
      { keys: ["shade"], display: "Sister Shade", table: 10, couple: null },
      { keys: ["rachel", "rachel george"], display: "Sister Rachel George", table: 10, couple: null },
      { keys: ["nenye"], display: "Sister Nenye", table: 10, couple: null }
    ];
  
    function normalize(str) {
      return str.toLowerCase().trim();
    }
  
    function findSeat() {
      const input = normalize(document.getElementById("name").value);
      const resultEl = document.getElementById("result");
  
      const guest = guests.find(g =>
        g.keys.some(k => normalize(k) === input)
      );
  
      if (!guest) {
        resultEl.innerHTML = "❌ Name not found. Please check spelling or see the host.";
        return;
      }
  
      if (guest.couple) {
        const partner = guests.find(g => g.couple === guest.couple && g.display !== guest.display);
        if (partner) {
          resultEl.innerHTML = `💑 <strong>${guest.display}</strong> & <strong>${partner.display}</strong><br>💺 You are seated at <strong>Table ${guest.table}</strong>`;
          return;
        }
      }
  
      resultEl.innerHTML = `🎉 Welcome <strong>${guest.display}</strong><br>💺 Your table is <strong>Table ${guest.table}</strong>`;
    }
  </script>


</body>
</html>
