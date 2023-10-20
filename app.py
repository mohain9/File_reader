from pathlib import Path
import streamlit as st
from PIL import Image

#path settings                      
current_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file= current_dir/"styles"/"main.css"
resume_file= current_dir/"assets"/"cv.pdf"
profile_pic= current_dir/"assets"/"profile-pic.png"

#general settings

page_title ="Digital CV | Mohan"
page_icon = ":wave:"
name= "MohanKumar"
description= """Result-focused and an astute professional spanning 10+ years in IT & ITES domains, delivering positive outcomes in areas of Business Intelligence, Service Delivery, Application Support and more…
Multi linguistic communicator, developed interpersonal skills with European business culture and stakeholders. Capable of defining strategies with deliverable’s.
"""
email="mohain@gmail.com"
social_media={
   # "yooutube": "https://youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/mohankumar-n/",
}
projects= {
    "Dashboards - Live with customer filter and report download": "https://medium.com/@mohain/live-dashboard-using-streamlit-50cd51d62b77"
    "Desktop Application",
}

st.set_page_config(page_title=page_title,page_icon=page_icon)
st.title("Digital ")

#load css, pdf & profile pic
with open (css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open (resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
    profile_pic=Image.open(profile_pic)
    
#hero section
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic, width =230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Download Resume (Deutsch)",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="applicaton/octet-stream",
    )
    st.write("...",email)
    
    
#solical links
st.write("#")
cols=st.columns(len(social_media))
for index,(platform,link) in enumerate(social_media.items()):
    cols [index].write(f"[{platform}]({link})")
    
#experience &qualifications
st.write("#")
st.subheader("Experience & Qualificaitons")
st.write(
    """
    - Developed automated solutions that make it possible to create forecasts, trigger emails and generate live reports. These automations have not only increased efficiency but also enabled real-time weekly customer reports.
    - Extensive knowledge of using tools such as Power BI, Apache Superset, Excel and programming languages such as Python to create meaningful dashboards.
    """
)
# EDUCATION & CREDENTIAL
st.write("#")
st.subheader("EDUCATION & CREDENTIAL")
st.write(
    """
    - Bachelor of Science (Computer science) from Madras University
    - English (C1 equivalent)
    - French (B1 equivalent)
    - German (A1) from Goethe Institue
    - ITIL V3 Foundation from AXELOS

    """
)

#skills
st.write("#")
st.subheader("Hard skills")
st.write(
    """
    - Knowledge in XML, .NET, ASP, VisualBasic...
    - Programming Langue – Python…..
    - Softwares - SAP SuccessFactors, Adobe Photoshop…..
    - BI tools – KNIME, Power BI, TIBCO Spot fire and Superset
    - Ticketing tools - Clear Quest, Cornerstone and JIRA
    - Database – MySQL, MS SQL Server and MongoDB(Beginner)

    """
)



#work history

st.write("#")
st.subheader("CAREER PROGRESSION")
st.write("---")

#Job 1
st.write("BI & Data Analytics Specialist - WebID solutions (Solingen und Hamburg)")
st.write("03/2022 – Present")
st.write(
    """
    - Dashboards for multiple users within using Power BI.
    - Live dashboards for Management team using Apache Superset.
    - Process automation like report generation, email sender…. 
    - Data download, manipulation, refresh and transfer using Python and Excel.
    - Multiple IT related activities on a daily basis.

    """
)

#Job 2
st.write("Project Owner - JuiceUP (Start-up)")
st.write("Dec 2016 – Nov 2018")
st.write(
    """
    - Ideate and implement an automated retail juice vending system 
    - Research the idea, workflow procedure, raise funds for the startup, develop the front design and the back of house setup 
    """
)

#Job 3
st.write("Subject Matter Expert - AXA Technologies Shared Services  (Bangalore and Paris)")
st.write("03/2015 – 09/2016")
st.write(
    """
    - Team Lead for IT support and data analyst teams in India.
    - Service delivery Manager for IRIS platform globally. (France, Poland and Spain)
    - A reliable source of information, proactively managing customer’s functional needs into technical specifications 
    - Experience with cross-functional teams and multiple stakeholders
    - Technical specialist and competence in ITSM process and product management.
    """
)

#Job 4
st.write("BI/Data Analyst")
st.write("03/2013 – 03/2015")
st.write(
    """
    - A client-facing role, driving the end-to-end implementation of Business Intelligence engagement
    - Delivery management (Delivery Director):
        - Bridge between the programmer and the executor during file execution.
        - Plan and control the delivery on each execution of package(files)
        - Monitor the production server to identify incident.
    -	Information security management:
        - Work on Access management using ITIL standards.
        - Create, provision, delete and manage users, groups and roles for different systems using Active Directory.
        - Manage role assignments in development and pre-production servers
    - Document management:
        - Manage and control all process related documents within shared drive, without external software.
    - Incident Management:
        - Handle L1 and L2 incidents within Data Management team.
        - Identify L3 incidents and assign to production technical team members.
        - Introduced best practices and procedures for faster resolution of Incidents
    """
)

#Job 5
st.write("Senior Software Engineer")
st.write("09/2011 – 03/2013")
st.write(
    """
    - Business Intelligence Monitoring and Reporting: 
        - Monitoring the execution of files in production server.
        - Daily reports (SQL Management studio) on the availability of applications.
    - Experience in dealing with system logs, especially network traffic analyzes, payload, event logs, application logs, etc..
    """
)

#Job 6
st.write("Senior Process Associate - I Gate (Bangalore)")
st.write("01/2010 – 09/2011")
st.write(
    """
    - Handling online banking and insurance transactions (only individuals) within Canada. 
    """
)

#Job 7
st.write("Associate - HSBC (Bangalore)")
st.write("11/2008 – 01/2010")
st.write(
    """
    - Handling multiple online banking transactions (individual and corporate) within France.
    """
)

#Job 8
st.write("Associate - Aditya Birla Minacs (Bangalore)")
st.write("07/2008 – 11/2008")
st.write(
    """
    - A typical French call center selling Bank credit cards.
    """
)

#Job 9
st.markdown("Programmer Analyst - ADIVA Systems  (Chennai)")
st.write("01/2005 – 12/2005")
st.write(
    """
    - Developer or programmer, coded in .NET, XML, ASP and JavaScript. Queries in SQL and Python. 
    - Knowledge in runtime analysis and procedures for ensuring the correctness of software components (test, validation, verification) in the environment of parallel and distributed systems.

    """
)

#projects and accomplishments
st.write("#")
st.subheader("A sample Project description")
st.write("---")
for project,link in projects.items():
    st.write(f"[{project}]({link})")



