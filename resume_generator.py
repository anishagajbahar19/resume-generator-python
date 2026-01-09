import markdown
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def convert_markdown_to_pdf(markdown_content, resume_file="Resume.pdf"):
    c = canvas.Canvas(resume_file, pagesize=A4)
    width, height = A4

    x = 50
    y = height - 50

    for line in markdown_content.split("\n"):
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(x, y, line)
        y -= 14

    c.save()
    print(f"✅ Resume saved to {resume_file}")


class Resume:
    def __init__(self, name, email, mobile, education, skills,
                 experience, projects, achievements, activities):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.achievements = achievements
        self.activities = activities

    def generate_markdown(self):
        markdown_text = f"{self.name}\n"
        markdown_text += f"Email: {self.email} | Mobile: {self.mobile}\n"
        markdown_text += "-" * 60 + "\n\n"

        markdown_text += "EDUCATION\n"
        for edu in self.education:
            markdown_text += (
                f"- {edu['level']}: {edu['institution']} | "
                f"{edu['field']} | Score: {edu['score']} | "
                f"{edu['duration']}\n"
            )

        markdown_text += "\nSKILLS\n"
        markdown_text += f"{self.skills}\n"

        markdown_text += "\nEXPERIENCE\n"
        for exp in self.experience:
            markdown_text += (
                f"- {exp['job_role']} ({exp['company_name']}): "
                f"{exp['description']}\n"
            )

        markdown_text += "\nPROJECTS\n"
        for proj in self.projects:
            markdown_text += f"- {proj['name']}: {proj['description']}\n"

        markdown_text += "\nACHIEVEMENTS\n"
        for ach in self.achievements:
            markdown_text += f"- {ach}\n"

        markdown_text += "\nOTHER ACTIVITIES\n"
        markdown_text += self.activities + "\n"

        return markdown_text


def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile number: ")

    print("\nEducation:")
    education = []
    while True:
        if input("Add education? (yes/no): ").lower() != "yes":
            break
        level = input("Level (e.g., Graduation): ")
        institution = input("Institution: ")
        field = input("Field of study: ")
        duration = input("Passing year: ")
        score = input("Score: ")
        education.append({
            "level": level,
            "institution": institution,
            "field": field,
            "duration": duration,
            "score": score
        })

    skills = input("\nEnter your skills (comma-separated): ")

    print("\nExperience:")
    experience = []
    while True:
        job_role = input("Job Role (or 'done'): ")
        if job_role.lower() == "done":
            break
        company = input("Company Name: ")
        description = input("Description: ")
        experience.append({
            "job_role": job_role,
            "company_name": company,
            "description": description
        })

    print("\nProjects:")
    projects = []
    while True:
        project_title = input("Project Title (or 'done'): ")
        if project_title.lower() == "done":
            break
        description = input("Description: ")
        projects.append({
            "name": project_title,
            "description": description
        })

    print("\nAchievements:")
    achievements = []
    while True:
        ach = input("Achievement (or 'done'): ")
        if ach.lower() == "done":
            break
        achievements.append(ach)

    activities = input("\nEnter other activities: ")

    return Resume(
        name, email, mobile,
        education, skills,
        experience, projects,
        achievements, activities
    )


if __name__ == "__main__":
    user_resume = get_user_input()
    markdown_text = user_resume.generate_markdown()
    convert_markdown_to_pdf(markdown_text)
