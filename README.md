# AE-SEGY-EBCDIC-Header-Editor-v1.0

A comprehensive and user-friendly Python tool tailored for geophysicists and data engineers, enabling effortless access, viewing, and editing of the EBCDIC header within SEGY files.

This tool simplifies the otherwise complex process of handling SEGY file headers, ensuring quick modifications, quality control, and metadata management without requiring deep knowledge of SEGY internals.

✨ Features

	•	📂 Load SEGY files and access their EBCDIC headers.
	•	🔍 View headers in a structured, readable format.
	•	📝 Edit and update header lines with a simple interface.
	•	💾 Save changes back into SEGY files without corrupting data.
	•	🔄 Preserves binary and trace data while modifying headers.
	•	⚡ Lightweight, standalone Python script – no heavy dependencies.

  📦 Installation
  
	1.	Clone this repository: git clone https://github.com/alaa-emam-geophysicist/AE-SEGY-EBCDIC-Header-Editor-v1.0.git 
    cd AE-SEGY-EBCDIC-Header-Editor-v1.0
    2.	(Optional) Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
	3.	Install dependencies (if any):
    pip install -r requirements.txt

🚀 Usage

  Run the program from the command line:
  python AE_Segy_headerEditing_FreeEdit_v1.0.py
  Follow the prompts to:
	  1.	Select a SEGY file.
	  2.	View and navigate through the EBCDIC header.
	  3.	Edit lines as needed.
	  4.	Save your updated SEGY file.


📘 Example

 ---------------------------------------
 SEGY EBCDIC Header Editor - FreeEdit v1.0
---------------------------------------
Loaded SEGY file: example.sgy

[Header Lines Preview]
C 1 CLIENT COMPANY: TEST ENERGY LTD
C 2 SURVEY AREA: BLOCK 12 NORTH
C 3 ACQUISITION DATE: 2025-01-15
...

Choose an option:
[1] Edit Header Line
[2] Save and Exit
[3] Cancel

📂 Repository Structure

SEGY-EBCDIC-Header-Editor/
│
├── AE_Segy_headerEditing_FreeEdit_v1.0.py   # Main Python script
├── README.md                                # Documentation
├── LICENSE                                  # License file (add your choice)
└── requirements.txt                         # Dependencies (if any)


🛠️ Requirements

	•	Python 3.8+
	•	Standard libraries (no special dependencies unless added later).

🌍 Applications
  
	•	Quality control of SEGY datasets.
	•	Standardizing header metadata across seismic projects.
	•	Quick updates to client/company, survey, and project details in headers.
	•	Teaching and training tool for seismic data management.

  🤝 Contributions
  
  Contributions, issues, and feature requests are welcome!
  Feel free to open an issue or submit a pull request.

👤 Author
  
  Alaa EMAM
  A geophysicist passionate about seismic data, software tools, and simplifying geophysical workflows.

  📬 Contact
  
  Feel free to reach out with feedback, ideas, or improvements!
  GitHub: @alaa-emam-geophysicist
