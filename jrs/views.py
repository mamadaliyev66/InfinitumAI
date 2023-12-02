from django.shortcuts import render, redirect
from .forms import PDFUploadForm
import PyPDF2
import os
def home(request):
    return render(request,"jrs/index.html")

# def upload(request):
#     return render(request,"getcv.html")



def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            uploaded_pdf = form.save()
            # Extract text from the uploaded PDF
            pdf_text = extract_text_from_pdf(uploaded_pdf.pdf_file)
            # Delete the uploaded PDF file
            delete_uploaded_pdf(uploaded_pdf.pdf_file.path)
            # Redirect to display the extracted text
            skills=[]
            for i in range(0,len(programming_languages)):
                if programming_languages[i].lower() in pdf_text.lower():
                    skills.append(programming_languages[i])
            print(skills)
            return result(request, pdf_text=skills)
    else:
        print("invalid")

        form = PDFUploadForm()
    return render(request, 'jrs/getcv.html', {'form': form})
def extract_text_from_pdf(pdf_file):
    pdf_text = ''
    try:
        # Get the file path from the FieldFile object
        pdf_file_path = pdf_file.path
        with open(pdf_file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            for page_number in range(num_pages):
                page = reader.pages[page_number]
                pdf_text += page.extract_text()
    except Exception as e:
        print("Error extracting text from PDF:", e)



    return pdf_text

def delete_uploaded_pdf(pdf_path):
    try:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
    except Exception as e:
        print("Error deleting PDF:", e)

def result(request, pdf_text):
    return render(request, 'jrs/result.html', {'Skills': pdf_text})
programming_languages = [
    # Software Development
    "Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Swift", "Kotlin", "PHP", "Rust", "Go", "SQL", "HTML", "CSS",
    "React", "Angular", "Vue.js", "Node.js", "Django", "Flask", "ASP.NET", "Spring", "Hibernate", "Express.js", "Ruby on Rails",
    "jQuery", "Bootstrap", "Ember.js", "Meteor.js", "Laravel", "Symfony", "CakePHP", "CodeIgniter", "Zend Framework", "Grails",

    # Networking
    "Cisco", "Juniper", "TCP/IP", "DNS", "LAN/WAN", "VPN", "Firewalls", "Load Balancing", "Wireshark", "SDN (Software Defined Networking)",
    "NAT (Network Address Translation)", "BGP (Border Gateway Protocol)", "OSPF (Open Shortest Path First)", "MPLS (Multiprotocol Label Switching)",

    # Cybersecurity
    "Encryption", "Firewall", "Intrusion Detection Systems", "SIEM (Security Information and Event Management)", "Penetration Testing",
    "Vulnerability Assessment", "Ethical Hacking", "Security Auditing", "Antivirus", "Cyber Threat Intelligence", "Digital Forensics",
    "Identity and Access Management (IAM)", "Web Application Firewall (WAF)", "Endpoint Protection", "Security Information & Event Management (SIEM)",

    # Database Administration
    "MySQL", "PostgreSQL", "Oracle", "MongoDB", "SQL Server", "SQLite", "Cassandra", "Redis", "MariaDB", "DB2", "Amazon RDS", "DynamoDB",
    "Data Warehousing", "Database Replication", "Database Sharding", "Database Clustering",

    # IT Support
    "Troubleshooting", "Ticketing Systems", "Remote Desktop", "Customer Service", "Hardware Support", "Active Directory", "Group Policy",
    "ITIL (Information Technology Infrastructure Library)", "Remote Monitoring and Management (RMM)", "Patch Management",

    # Cloud Computing
    "AWS (Amazon Web Services)", "Microsoft Azure", "Google Cloud Platform", "Kubernetes", "Docker", "Serverless Architecture",
    "IaaS (Infrastructure as a Service)", "PaaS (Platform as a Service)", "SaaS (Software as a Service)", "FaaS (Function as a Service)",
    "Cloud Storage (e.g., Amazon S3, Azure Blob Storage, Google Cloud Storage)", "Elasticsearch", "Cloud Security", "Cloud Networking",

    # Business Analysis
    "Requirements Analysis", "Process Modeling", "Business Process Improvement", "UML (Unified Modeling Language)", "SWOT Analysis",
    "Root Cause Analysis", "Use Case Diagrams", "Activity Diagrams", "Entity Relationship Diagrams (ERD)", "Gantt Charts", "Fishbone Diagrams",

    # Project Management
    "Agile Methodology", "Scrum", "Kanban", "Lean", "Waterfall Model", "PRINCE2", "PMI (Project Management Institute)", "PERT (Program Evaluation and Review Technique)",
    "Critical Path Method (CPM)", "Earned Value Management (EVM)", "Risk Management", "Stakeholder Management", "Project Planning Tools (e.g., MS Project, Primavera)",

    # AI and Machine Learning
    "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Pandas", "NumPy", "NLTK (Natural Language Toolkit)", "OpenCV", "Apache Spark", "Hadoop",
    "BigML", "RapidMiner", "AutoML", "Reinforcement Learning", "Generative Adversarial Networks (GANs)", "Transfer Learning", "Computer Vision APIs",

    # Web Development
    "Adobe Dreamweaver", "Sublime Text", "Atom", "WebStorm", "Notepad++", "NetBeans", "Visual Studio Code", "Brackets", "Eclipse", "IntelliJ IDEA",
    "WebAssembly", "WebSockets", "GraphQL", "OAuth", "RESTful APIs", "SOAP", "WebRTC", "Progressive Web Apps (PWA)", "Web Accessibility Standards (WCAG)",

    # Quality Assurance
    "Selenium", "JUnit", "TestNG", "Cucumber", "Postman", "LoadRunner", "JMeter", "Appium", "Robot Framework", "Mocha", "Chai", "Jest", "Cypress",
    "Codeception", "Sikuli", "SoapUI", "Katalon Studio", "Visual Studio Test Professional", "TestRail", "Zephyr", "Applitools", "Tricentis Tosca",

    # UI/UX Design
    "Adobe XD", "Sketch", "Figma", "InVision", "Axure RP", "Marvel", "Zeplin", "Balsamiq", "Moqups", "Adobe Illustrator", "Adobe Photoshop",
    "User Flows", "Wireframing", "Prototyping", "Usability Testing", "Information Architecture", "User Persona", "Design Thinking",

    # Miscellaneous
    "Linux", "Unix", "Windows Server", "MacOS", "Git", "SVN (Subversion)", "Mercurial", "Bash Scripting", "PowerShell", "Continuous Integration (CI)",
    "Continuous Deployment (CD)", "Jenkins", "TeamCity", "Travis CI", "CircleCI", "Version Control Systems", "Agile Tools (e.g., Jira, Trello, Asana)",

    "Illustrator", "Graphic Designer", "UI/UX Designer", "Motion Graphics Designer",

    # Content Creation & Copywriting
    "Copywriter", "Content Writer", "Content Strategist", "Editor/Proofreader",

    # Digital Marketing & Advertising
    "Digital Marketer", "Social Media Manager", "SEO Specialist", "PPC Specialist",

    # Video & Multimedia Production
    "Videographer/Video Editor", "Motion Designer", "Audio Engineer",

    # Web & User Experience (UX) Roles
    "Web Designer", "Front-end Developer", "User Experience (UX) Designer",

    # Photography
    "Photographer","Photography","Illustration",

    # Miscellaneous
    "Creative Director", "Brand Strategist", "Marketing Coordinator", "Art Director", "Visual Designer",
    "Interactive Designer"

]
