from fpdf import FPDF

class Resume:
    def __init__(self):
        # Initialize attributes as empty dictionaries or lists
        self.personal_info = {}
        self.education = []
        self.experience = []
        self.skills = []

    def get_personal_info(self):
        # Collect personal information from the user
        self.personal_info['name'] = input("Enter your full name: ")
        self.personal_info['email'] = input("Enter your email address: ")
        self.personal_info['phone'] = input("Enter your phone number: ")

    def get_education(self):
        # Collect educational information from the user
        while True:
            edu = {}
            edu['uni_name'] = input("Enter your university's name: ")
            edu['uni_major'] = input("Enter your major: ")
            edu['uni_year'] = input("Enter your years of education: ")
            edu['uni_grade'] = input("Enter your university grade out of 100: ")
            self.education.append(edu)

            more = input("Do you want to add another entry for education? (yes/no): ")
            if more.lower() != 'yes':
                break

    def get_experience(self):
        # Collect professional experience from the user
        while True:
            exp = {}
            exp['exp_name'] = input("Enter the title of your experience: ")
            exp['exp_desc'] = input("Write a description about your experience: ")
            exp['exp_year'] = input("Enter the year of your experience: ")
            self.experience.append(exp)

            more = input("Do you want to add another entry for experience? (yes/no): ")
            if more.lower() != 'yes':
                break

    def get_skills(self):
        # Collect skills from the user
        while True:
            skill = input("Enter the name of a skill you have: ")
            self.skills.append(skill)

            more = input("Do you want to add another skill? (yes/no): ")
            if more.lower() != 'yes':
                break

    def generate_pdf(self):
        # Generate a PDF of the resume
        pdf = FPDF()
        pdf.add_page()

        # Add title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Resume", ln=True, align='C')

        # Add personal information
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "Personal Information", ln=True)
        for key, value in self.personal_info.items():
            pdf.cell(0, 10, f"{key.capitalize()}: {value}", ln=True)

        # Add education information
        pdf.cell(0, 10, "", ln=True)  # Add a blank line
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Education", ln=True)
        pdf.set_font("Arial", size=10)
        for edu in self.education:
            pdf.cell(0, 10, f"{edu['uni_major']} - {edu['uni_grade']}/100   {edu['uni_name']}   {edu['uni_year']}", ln=True)

        # Add experience information
        pdf.cell(0, 10, "", ln=True)  # Add a blank line
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Experience", ln=True)

        page_width = pdf.w - 20

        for exp in self.experience:
            pdf.set_font("Arial", size=12)
            pdf.cell(page_width - 30, 10, exp['exp_name'], align='L')  # Experience name
            pdf.cell(30, 10, exp['exp_year'], align='R', ln=True)  # Year

            # Add experience description on the next line
            pdf.set_font("Arial", size=10)
            pdf.cell(0, 10, exp['exp_desc'])
            pdf.cell(0, 10, "", ln=True)

        # Add skills
        pdf.cell(0, 10, "", ln=True)  # Add a blank line
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Skills", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, ", ".join(self.skills), ln=True)

        # Save the PDF
        pdf.output("resume.pdf")
        print("PDF generated successfully as 'resume.pdf'.")


if __name__ == "__main__":
    my_resume = Resume()

    my_resume.get_personal_info()
    my_resume.get_education()
    my_resume.get_experience()
    my_resume.get_skills()

    my_resume.generate_pdf()
