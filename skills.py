skills_list = [

# Programming Languages
"python","java","c++","c","c#","javascript","typescript","go","rust","kotlin","swift","php","ruby","scala","matlab","r",

# Web Development
"html","css","react","angular","vue","node","nodejs","express","django","flask","spring","bootstrap","jquery","rest api","graphql",

# Data Science / AI
"machine learning","deep learning","data science","data analysis","nlp","natural language processing","computer vision",
"tensorflow","pytorch","keras","scikit-learn","pandas","numpy","matplotlib","seaborn","opencv","xgboost",

# Databases
"sql","mysql","postgresql","mongodb","oracle","sqlite","firebase","redis","cassandra",

# Cloud & DevOps
"aws","azure","google cloud","docker","kubernetes","jenkins","git","github","gitlab","ci cd","terraform","ansible",

# Cybersecurity
"cybersecurity","network security","penetration testing","ethical hacking","cryptography","firewall","siem",

# Networking
"networking","tcp/ip","dns","dhcp","routing","switching","vpn","linux administration",

# Mobile Development
"android","ios","react native","flutter","xamarin","kotlin android",

# Data Tools
"excel","power bi","tableau","hadoop","spark","big data","etl","data warehouse",

# Business / Management
"project management","business analysis","product management","marketing","sales","finance","accounting","management",
"strategic planning","operations","supply chain","crm","erp",

# Soft Skills
"communication","leadership","teamwork","problem solving","critical thinking","time management","decision making",
"adaptability","creativity","negotiation","presentation","public speaking","collaboration","conflict resolution",

# Research / Writing
"research","technical writing","report writing","documentation","content writing",

# Customer / HR
"customer service","recruitment","human resources","training","mentoring"
]


def extract_skills(text):

    detected = []

    for skill in skills_list:
        if skill in text:
            detected.append(skill.title())

    return detected