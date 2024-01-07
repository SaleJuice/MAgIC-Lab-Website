import os, json, shutil, datetime, validators
import pandas as pd


structure = """
<!DOCTYPE html>
<html>

<head><!--This is the head part for importation of css js and others.-->
    <meta charset="utf-8">
    <meta http-equiv="Content-Type">
    <meta content="text/html">

    <meta name="keywords" lang="en" content="MAgIC Lab">
    <meta name="description" content="Multi-Agent & Intelligent Control Lab">

    <title>MAgIC Lab</title>

    <link href="./css/font.css" rel="stylesheet" type="text/css">
    <link href="./css/master.css" rel="stylesheet" type="text/css">
    <link href="./css/style.css" rel="stylesheet" type="text/css">
</head>

<body id="body"><!--This is the body part, include of page.-->
    <div id="page"><!--This is the page part, include of top, content, bottom.-->
        <div id="top"><!--This is the top part.-->
            <div class="breadcrumb">
                <a href="https://www.shanghaitech.edu.cn" target="_blank"><span>ShanghaiTech University</span></a>
                <a href="https://sist.shanghaitech.edu.cn" target="_blank"><span>School of Information Science and Techonology</span></a>
                <a href="https://star-center.shanghaitech.edu.cn" target="_blank"><span>STAR Center</span></a>
                <a href="index.html" target="_self"><span>Multi-Agent & Intelligent Control Lab</span></a>
            </div>
        </div>

        <div id="middle"><!--This is the middle part, include of header, menubar, content, footer.-->
            <div id="header"><!--This is the header part.-->
                <div class="logo">
                    <img class="university" src="./assets/image/university.svg">
                    <img class="lab" src="./assets/image/lab.png">
                    <img class="center" src="./assets/image/center.png">
                </div>
            </div>

            <hr><!--This is a horizontal rule.-->

            <div id="menubar"><!--This is the menubar part.-->
                <a href="index.html">HOME</a>
                <a href="people.html">PEOPLE</a>
                <a href="research.html">RESEARCH</a>
                <a href="publication.html">PUBLICATION</a>
                <a href="course.html">COURSE</a>
                <a href="gallery.html">GALLERY</a>
                <a href="contact.html">CONTACT</a>
            </div>

            <hr><!--This is a horizontal rule.-->

            You can put your content in here.
            
        </div>

        <div id="bottom"><!--This is the bottom part.-->
            <div class="copyright">
                <p>
                    Copyright © 2020-2022 Multi-Agent & Intelligent Control (MAgIC) Lab
                </p>
            </div>
        </div>
    </div>
</body>

</html>
"""


def generate_news_page():
    path = "./assets/news/"
    news = pd.DataFrame(columns=['id', 'date', 'title', 'description', 'links'])
    
    for idx in os.listdir(path):
        with open(os.path.join(path, idx, "info.json"), "r") as fp:
            info = json.load(fp)
        info['id'] = idx
        news = news._append(info, ignore_index=True)
    news.sort_values(by='date', ascending=False, inplace=True)
    news.reset_index(drop=True, inplace=True)
    
    intro = """
    <div id="content">
        <h1>Multi-Agent & Intelligent Control Lab</h1><br>
        <img alt="The group photos of members are placed here." src="./assets/image/group.jpg"><br>
        <p>
            Welcome to the Multi-Agent & Intelligent Control (MAgIC) Lab.
            MAgIC Lab was founded in September 2020 and is located in Room 1D-208A of ShanghaiTech Automation and Robotics (STAR) Center, School of Information Science and Technology (SIST), ShanghaiTech University, Shanghai, China.
            Our lab focuses on the advanced control theory for multi-agent systems, including  adaptive control, intelligent control and data-driven control, and their practical applications on UAVs, bionic robots, manipulators and active noise attenuation.
            We welcome anyone interested in MAgIC Lab.
        </p>
          
        <p>  
            Prof. Yang Wang is an assistant professor at ShanghaiTech University. She received her Ph.D. at Imperial College London in 2019 and founded the MAgIC Lab in 2020.
        </p>
    </div><br>"""

    content = ""
    content += """<h1>News</h1><br>"""
    
    for i, info in news.iterrows():
        content += f"""
        <div class="news">
            <div class="picture">
                <img alt="cover" src="{os.path.join(path, info['id'], "1.jpg")}">
            </div>
            <div class="info">
                <p class="date">{info['date']}</p>
                <p class="title">{info['title']}</p>
                <p class="describe">{info['description']}</p>
                <a href="{info['links'][list(info['links'].keys())[0]]}" target="_blank">{list(info['links'].keys())[0]}</a>
            </div>
        </div><br>"""

    with open("output/index.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", intro+"""<div id="content">"""+content+"""</div>"""))

def generate_research_page():
    content = ""
    content += """
    <h1>Research</h1>

        <img src="assets/research/research_map.png">
        <p>
            Understanding and control of complex dynamic systems is of crucial importance in many branches of science, engineering and industry. The ushering in of the big-data era, ably supported by exponential advances in computation ability, has provided new potential to revolutionize the modelling, sensing and control of such complex interactive dynamics. Our lab particularly interested in the dynamic agent that interacting with each other and their fluidic environment, such as quadrotor and robotic fish.
        </p>

        <br>
        <br>
        <br>

        <h2>Control Engineering</h2>

            <br>

            <div class="research">
                <div class="info">
                    <p class="title">
                        Hydrodynamic-Interactive Systems
                    </p>
                    <img src="./assets/research/fish.jpg">
                    <video width="450" controls>
                        <source src="./assets/publication/iros23exploring/video.mp4" type="video/mp4">
                    </video>
                    <video width="450" controls>
                        <source src="./assets/publication/icra24dynamic/video.mp4" type="video/mp4">
                    </video>
                    <p class="describe">
                        Robotic fish has gained substantial attention in robotics field in past decades due to their unique benefits, including concealment, flexibility, and energy efficiency. Notable advancements have been achieved in various aspects of this domain, including the realm of electromechanical construction  underwater perception and control However, the problem of dynamic modelling  for the robotic fish, although plays a crucial role in motion planning and control, remains unsolved and challenging due to its inherently high-dimensional and non-linear nature, particularly when operating in complicated environments with background flow.
                    </p>
                </div>
            </div>

            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    Aerodynamic-Interactive Robotic Systems
                </p>
                <img src="assets/research/uav.png">
                <video width="900" controls>
                    <source src="./assets/research/ICRA24_1477_VI_i.mp4" type="video/mp4">
                </video>
                <p class="describe">
                    In contemporary times, Unmanned Aerial Vehicles (UAVs) play a crucial role in various scenarios. Particularly, UAVs have proven to be highly valuable when employed in various specialized tasks such as search and rescue operations, survey missions, and environmental monitoring. One critical aspect among these is ensuring the safe near ground flight of UAVs. Aside from the UAV’s nonlinear characteristics and limited platform size, the intricate interactions between rotor airflow and the ground may result in flight instability or even catastrophic failure. This phenomenon, known as the Ground Effect (GE), poses a great challenge that must be addressed to achieve safe near-ground maneuver including autonomous landings on vertical oscillating platforms.
                </p>
            </div>
            </div>
            
            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                AcousticField-Interactive System
                </p>
                <img src="assets/research/anc.png">
                <video width="900" controls>
                    <source src="./assets/research/ICRA24_0518_VI_i.mp4" type="video/mp4">
                </video>
                <p class="describe">
                    The active control of noises or disturbances has achieved great success in modern robotics, industrial processes, and automation systems. As a promising technique, active noise control (ANC) aims to mitigate unwanted noises by virtue of generating anti-noise sound waves that destructively interfere with coming-forth unwanted sound noises.
                </p>
            </div>
            </div>

            <br>

        <h2>Theoretical Works</h2>

            <br>

            <div class="research">
                <div class="info">
                    <p class="title">
                        Output Regulation (Disturbance Rejection)
                    </p>
                    <img src="assets/research/or.png">
                    <p class="describe">
                        
                    </p>
                </div>
            </div>

            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    IM-based Solution (IFAC2023)
                </p>
                <img src="assets/research/im.png">
                <p class="describe">

                </p>
            </div>
            </div>
            
            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    UIO-based Solution (IFAC2023)
                </p>
                <img src="assets/research/uio.png">
                <p class="describe">

                </p>
            </div>
            </div>

            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    ILC-Embedded MRAC (CDC2024)
                </p>
                <img src="assets/research/ilc_mrac.png">
                <p class="describe">
                        
                </p>
            </div>
            </div>

            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    ILC with output Constraints(IFAC2023)
                </p>
                <img src="assets/research/ilc_oc.png">
                <p class="describe">
                        
                </p>
            </div>
            </div>

            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    Formation Control (ACC2023)
                </p>
                <img src="assets/research/fc_1.png">
                <video width="450" controls>
                    <source src="./assets/research/GCL.mp4" type="video/mp4">
                </video>
                <video width="450" controls>
                    <source src="./assets/research/MyCL.mp4" type="video/mp4">
                </video>
                <p class="describe">
                        
                </p>
            </div>
            </div>

            <br>

            <div class="research">
            <div class="info">
                <p class="title">
                    Formation Control (ROBIO2023)
                </p>
                <img src="assets/research/fc_2.png">
                <video width="450" controls>
                    <source src="./assets/research/E_GCL.mp4" type="video/mp4">
                </video>
                <video width="450" controls>
                    <source src="./assets/research/E_MyCL.mp4" type="video/mp4">
                </video>
                <p class="describe">
                        
                </p>
            </div>
            </div>

            <br>
    """
    with open("output/research.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", """<div id="content">"""+content+"""</div>"""))

def generate_people_page():
    path = "./assets/people/"
    people = pd.DataFrame(columns=['id', 'given name', 'family name', 'email', 'office', 'interests', 'page', 'identity', 'goto', 'come', 'leave'])

    for person in os.listdir(path):
        with open(os.path.join(path, person, "info.json"), "r") as fp:
            info = json.load(fp)
        info['id'] = person
        people = people._append(info, ignore_index=True)
    people.sort_values(by='come', ascending=True, inplace=True)
    people.reset_index(drop=True, inplace=True)

    nowadays = datetime.datetime.now().strftime('%Y/%m')

    present = people[(people['leave'] >= nowadays) | (people['leave'] == "")]
    pi = present[present['identity'] == 'pi']
    phd = present[present['identity'] == 'phd']
    master = present[present['identity'] == 'master']
    undergraduate = present[present['identity'] == 'undergraduate']

    former = people[(people['leave'] < nowadays) & (people['leave'] != "")]
    
    content = ""
    content += f"""<h1>People</h1><br>"""

    content += f"""<h2>Lab Director</h2><br>"""

    for i, info in pi.iterrows():
        content += f"""
        <div class="people">
            <div class="picture">
                <img alt="photo" src="{os.path.join(path, info['id'], "photo.jpg")}">
            </div>
            <div class="info">
                <p class="office">{info['office']}</p>
                <p class="name">{info['given name']+" "+info['family name']}</p>
                <p class="interests">{", ".join(info['interests'])}</p>
                <a href="mailto:{info['email']}">email</a>
                <a href="{info['page']}" target="_blank">page</a>
                <a href="{os.path.join(path, info['id'], "cv.pdf")}" target="_blank">CV</a>
            </div>
        </div><br>"""

    content += """<br>"""

    content += f"""<h2>PhD Students</h2><br>"""

    for i, info in phd.iterrows():
        content += f"""
        <div class="people">
            <div class="picture">
                <img alt="photo" src="{os.path.join(path, info['id'], "photo.jpg")}">
            </div>
            <div class="info">
                <p class="office">{info['office']}</p>
                <p class="name">{info['given name']+" "+info['family name']}</p>
                <p class="interests">{", ".join(info['interests'])}</p>
                <a href="mailto:{info['email']}">email</a>
                <a href="{info['page']}" target="_blank">page</a>
                <a href="{os.path.join(path, info['id'], "cv.pdf")}" target="_blank">CV</a>
            </div>
        </div><br>"""
        
    content += """<br>"""

    content += f"""<h2>Master Students</h2><br>"""

    for i, info in master.iterrows():
        content += f"""
        <div class="people">
            <div class="picture">
                <img alt="photo" src="{os.path.join(path, info['id'], "photo.jpg")}">
            </div>
            <div class="info">
                <p class="office">{info['office']}</p>
                <p class="name">{info['given name']+" "+info['family name']}</p>
                <p class="interests">{", ".join(info['interests'])}</p>
                <a href="mailto:{info['email']}">email</a>
                <a href="{info['page']}" target="_blank">page</a>
                <a href="{os.path.join(path, info['id'], "cv.pdf")}" target="_blank">CV</a>
            </div>
        </div><br>"""
        
    content += """<br>"""

    content += f"""<h2>Undergraduate Students</h2><br>"""

    for i, info in undergraduate.iterrows():
        content += f"""
        <div class="people">
            <div class="picture">
                <img alt="photo" src="{os.path.join(path, info['id'], "photo.jpg")}">
            </div>
            <div class="info">
                <p class="office">{info['office']}</p>
                <p class="name">{info['given name']+" "+info['family name']}</p>
                <p class="interests">{", ".join(info['interests'])}</p>
                <a href="mailto:{info['email']}">email</a>
                <a href="{info['page']}" target="_blank">page</a>
                <a href="{os.path.join(path, info['id'], "cv.pdf")}" target="_blank">CV</a>
            </div>
        </div><br>"""
        
    content += """<br>"""

    content += f"""<h2>Former</h2><br>"""

    for i, info in former.iterrows():
        content += f"""
        <div class="people">
            <div class="picture">
                <img alt="photo" src="{os.path.join(path, info['id'], "photo.jpg")}">
            </div>
            <div class="info">
                <p class="office">{info['office']}</p>
                <p class="name">{info['given name']+" "+info['family name']}</p>
                <p class="interests">{", ".join(info['interests'])}</p>
                <a href="mailto:{info['email']}">email</a>
                <a href="{info['page']}" target="_blank">page</a>
                <a href="{os.path.join(path, info['id'], "cv.pdf")}" target="_blank">CV</a>
            </div>
        </div><br>"""
        
    content += """<br>"""
    
    with open("output/people.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", """<div id="content">"""+content+"""</div>"""))

def generate_publication_page():
    path = "./assets/publication/"
    publication = pd.DataFrame(columns=['id', 'date', 'title', 'authors', 'press', 'links', 'is_accepted', 'is_journal', 'cover'])

    for folder_name in os.listdir(path):
        with open(os.path.join(path, folder_name, 'info.json'), 'r') as fp:
            info = json.load(fp)
        info['id'] = folder_name
        l = [item for item in os.listdir(os.path.join(path, folder_name)) if item.startswith('cover.')]
        info['cover'] = None if len(l) == 0 else l[0]
        publication = publication._append(info, ignore_index=True)  # FIXME to use more elegant way
    publication.sort_values(by='date', ascending=False, inplace=True)
    publication.reset_index(drop=True, inplace=True)

    
    recent_publication = publication[(publication['date'] >= '2021-01')]
    early_publication = publication[(publication['date'] < '2021-01')]

    accepted_publication = recent_publication[(recent_publication['is_accepted'] == 'True')]
    under_review_publication = recent_publication[(recent_publication['is_accepted'] == 'False')]

    journal_publication = accepted_publication[(accepted_publication['is_journal'] == 'True')]
    conference_publication = accepted_publication[(accepted_publication['is_journal'] == 'False')]


    content = ""
    content += """<h1>Publication</h1><br>"""

    content += """<h2>Under Review</h2><br>"""
    for i, info in under_review_publication.iterrows():
        content += f"""<div class="publication">"""
        if info['cover'] is not None:
            content += f"""<div class="picture"> <img alt="cover" src="{os.path.join(path, info['id'], info['cover'])}"> </div>"""
        content += f"""<div class="info">"""
        content += f"""<p class="others">{info['press']}</p>"""
        content += f"""<p class="title">{info['title']}</p>"""
        content += f"""<p class="author">{", ".join(info['authors'])}</p>"""
        for key, value in info['links'].items():
            if validators.url(value):
                content += f"""<a href="{value}" target="_blank">{key}</a>"""
            else:
                content += f"""<a href="{os.path.join(path, info['id'], value)}" target="_blank">{key}</a>"""
        content += """</div></div><br>"""
    
    content += """<h2>Conference</h2><br>"""
    for i, info in conference_publication.iterrows():
        content += f"""<div class="publication">"""
        if info['cover'] is not None:
            content += f"""<div class="picture"> <img alt="cover" src="{os.path.join(path, info['id'], info['cover'])}"> </div>"""
        content += f"""<div class="info">"""
        content += f"""<p class="others">{info['press']}</p>"""
        content += f"""<p class="title">{info['title']}</p>"""
        content += f"""<p class="author">{", ".join(info['authors'])}</p>"""
        for key, value in info['links'].items():
            if validators.url(value):
                content += f"""<a href="{value}" target="_blank">{key}</a>"""
            else:
                content += f"""<a href="{os.path.join(path, info['id'], value)}" target="_blank">{key}</a>"""
        content += """</div></div><br>"""
    
    content += """<h2>Journal</h2><br>"""
    for i, info in journal_publication.iterrows():
        content += f"""<div class="publication">"""
        if info['cover'] is not None:
            content += f"""<div class="picture"> <img alt="cover" src="{os.path.join(path, info['id'], info['cover'])}"> </div>"""
        content += f"""<div class="info">"""
        content += f"""<p class="others">{info['press']}</p>"""
        content += f"""<p class="title">{info['title']}</p>"""
        content += f"""<p class="author">{", ".join(info['authors'])}</p>"""
        for key, value in info['links'].items():
            if validators.url(value):
                content += f"""<a href="{value}" target="_blank">{key}</a>"""
            else:
                content += f"""<a href="{os.path.join(path, info['id'], value)}" target="_blank">{key}</a>"""
        content += """</div></div><br>"""
    
    content += """<h2>Early</h2><br>"""
    for i, info in early_publication.iterrows():
        content += f"""<div class="publication">"""
        if info['cover'] is not None:
            content += f"""<div class="picture"> <img alt="cover" src="{os.path.join(path, info['id'], info['cover'])}"> </div>"""
        content += f"""<div class="info">"""
        content += f"""<p class="others">{info['press']}</p>"""
        content += f"""<p class="title">{info['title']}</p>"""
        content += f"""<p class="author">{", ".join(info['authors'])}</p>"""
        for key, value in info['links'].items():
            if validators.url(value):
                content += f"""<a href="{value}" target="_blank">{key}</a>"""
            else:
                content += f"""<a href="{os.path.join(path, info['id'], value)}" target="_blank">{key}</a>"""
        content += """</div></div><br>"""

    with open("output/publication.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", """<div id="content">"""+content+"""</div>"""))

def generate_gallery_page():
    # gallery page
    path = "./assets/gallery/"
    gallery = pd.DataFrame(columns=['id', 'date', 'title', 'description'])
    
    for idx in os.listdir(path):
        with open(os.path.join(path, idx, "info.json"), "r") as fp:
            info = json.load(fp)
        info['id'] = idx
        gallery = gallery._append(info, ignore_index=True)
    gallery.sort_values(by='date', ascending=False, inplace=True)
    gallery.reset_index(drop=True, inplace=True)

    content = ""
    content += """<h1>Gallery</h1><br>"""
    
    for i, info in gallery.iterrows():
        content += f"""
        <div class="activity">
            <div class="info">
                <p class="date">{info['date']}</p>
                <p class="title">{info['title']}</p>
            </div><br>
            <div class="picture">
                <img alt="cover" src="{os.path.join(path, info['id'], "1.jpg")}">
            </div>
        </div><br>"""

    with open("output/gallery.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", """<div id="content">"""+content+"""</div>"""))

def generate_course_page():
    # course page
    path = "./assets/course/"
    course = pd.DataFrame(columns=['id', 'code', 'name', 'description', 'is_opening'])

    for idx in os.listdir(path):
        with open(os.path.join(path, idx, "info.json"), "r") as fp:
            info = json.load(fp)
        info['id'] = idx
        course = course._append(info, ignore_index=True)
    course.sort_values(by='code', ascending=False, inplace=True)
    course.reset_index(drop=True, inplace=True)

    content = ""
    content += """<h1>Course</h1><br>"""

    for i, info in course.iterrows():
        content += f"""
        <div class="course">
            <div class="info">
                <p class="code">{info['code']}</p>
            <p class="name">{info['name']}</p>
            <p class="describe">{info['description']}</p>
            <a href="assets/course/{info['id']}/syllabus.pdf" target="syllabus.pdf">Syllabus</a>
            <a href="assets/course/{info['id']}/slides.zip" download="slides.zip">Slides</a>
            <a href="assets/course/{info['id']}/exam.pdf" target="exam.pdf">Exam</a>
            <a href="assets/course/{info['id']}/project.pdf" target="project.pdf">Project</a>
          </div>
        </div><br>"""

    with open("output/course.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", """<div id="content">"""+content+"""</div>"""))

def generate_contact_page():
    # contact page
    content = ""
    content += """<h1>Contact</h1><br>"""
    with open("output/contact.html", "w") as fp:
        fp.write(structure.replace("You can put your content in here.", """<div id="content">"""+content+"""</div>"""))


if __name__ == '__main__':
    # material copy
    if os.path.exists("./output"):
        shutil.rmtree("./output")
    os.makedirs("./output")

    shutil.copytree("./assets", "./output/assets")
    shutil.copytree("./css", "./output/css")

    generate_news_page()
    generate_research_page()
    generate_people_page()
    generate_publication_page()
    generate_gallery_page()
    generate_course_page()
    generate_contact_page()
    