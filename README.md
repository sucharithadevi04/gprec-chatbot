# GPRE Campus Assistant

A Streamlit-based web application that serves as a comprehensive campus assistant for GPREC (G. Pullaiah College of Engineering) students. The application includes features like campus navigation, placement information, faculty contact details, and an intelligent chatbot for placement-related queries.

## Features

1. **Home** - Overview of the application
2. **Campus Map** - Interactive map with building locations and navigation
3. **FAQ** - Frequently asked questions about the college
4. **Placements** - Placement statistics and visualizations
5. **Placement Chatbot** - NLP-powered chatbot for placement queries
6. **Contact** - Faculty contact information by department

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gpre.git
cd gpre
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages and download spaCy model:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

1. Make sure all the required data files are present in the `src/data` directory:
   - placement_data.csv
   - placement_companies_2024.csv
   - placement_branches_2024.csv
   - faculty_data.json (optional)
   - faq.json (optional)

2. Run the application:
```bash
cd src
streamlit run main.py
```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Project Structure

```
gpre/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── components/
    │   ├── campus_map.py  # Campus map and navigation
    │   ├── contact.py     # Faculty contact information
    │   ├── faq.py         # FAQ section
    │   ├── home.py        # Home section
    │   └── placements.py  # Placement statistics
    ├── utils/
    │   ├── data_loader.py # Data loading utilities 
    │   └── chatbot.py     # Placement chatbot logic
    └── data/
        ├── placement_data.csv
        ├── placement_companies_2024.csv
        ├── placement_branches_2024.csv
        ├── faculty_data.json
        └── faq.json
```

## Contributing

Feel free to open issues and pull requests for any improvements.

## License

This project is licensed under the G Pullareddy Collecge of Engineering students (Charitha Ambarkar & Team). 
