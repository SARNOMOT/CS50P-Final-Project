# Resume Creator

#### Video Demo:  https://youtu.be/lHYtkj-moV0

#### Description:

The Resume Creator is a Python-based tool that allows users to easily create professional resumes in PDF format. This program guides users through the process of entering their personal details, education, work experience, and skills, and then formats this information into a neatly organized PDF document.

The key features of the Resume Builder include:

- **Interactive Input**: The program prompts users for their name, contact details, education history, work experience, and skills, ensuring that all necessary information is collected in a user-friendly way.
- **PDF Generation**: Utilizing the `fpdf` library, the program converts the user's input into a well-structured resume in PDF format. The generated PDF includes various formatting elements like headers, bold text for section titles, and dynamic content placement for experience and education details.
- **Customizable Template**: The program can be easily extended to allow for additional customization, such as different fonts, colors, or layouts, making it suitable for different professional contexts.

#### Usage:

To use the Resume Builder, run the `resume.py` file in your Python environment. Follow the prompts to enter your details. Once all the information is entered, the program will generate a `resume.pdf` file in the same directory.

#### Dependencies:

- Python 3.x
- `fpdf` library: Install using `pip install fpdf`

#### Installation:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the program:
    ```bash
    python resume.py
    ```
