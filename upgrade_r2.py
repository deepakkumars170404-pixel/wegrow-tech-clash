import json

r2_conn = [
    {
        "q": "Connect the Visual Clues to Find the Tech Security Barrier:",
        "cards": [{"icon": "🔥", "label": "FIRE"}, {"icon": "🧱", "label": "WALL"}],
        "options": ["Proxy Gateway", "Firewall", "Antivirus Shield", "Network Switch"],
        "ans": 1,
        "ansText": "Firewall",
        "expl": "FIRE + WALL = Firewall! A network security barrier monitoring and filtering traffic."
    },
    {
        "q": "Connect the Visual Clues to Find the Portable Storage Device:",
        "cards": [{"icon": "🖊️", "label": "PEN"}, {"icon": "🚗", "label": "DRIVE"}],
        "options": ["Hard Disk Drive", "Pendrive (USB Drive)", "RAM Memory Stick", "MicroSD Card"],
        "ans": 1,
        "ansText": "Pendrive",
        "expl": "PEN + DRIVE = Pendrive! Portable solid-state USB flash storage."
    },
    {
        "q": "Connect the Visual Clues to Find the Cyber Social Engineering Attack:",
        "cards": [{"icon": "🐱", "label": "CAT"}, {"icon": "🎣", "label": "FISHING"}],
        "options": ["Ransomware Attack", "Phishing Attack", "Trojan Horse", "Spyware Bot"],
        "ans": 1,
        "ansText": "Phishing",
        "expl": "CAT (Catfish) + FISHING = Phishing! Deceptive attack tricking users into revealing credentials."
    },
    {
        "q": "Connect the Visual Clues to Find the Web Session Tracker:",
        "cards": [{"icon": "🍪", "label": "COOKIE"}, {"icon": "🌐", "label": "WEB"}],
        "options": ["Browser Cache", "Browser Cookie", "Session Token", "Local Storage"],
        "ans": 1,
        "ansText": "Browser Cookie",
        "expl": "COOKIE + WEB = Browser Cookie! Small text files stored by browsers to remember sessions."
    },
    {
        "q": "Connect the Visual Clues to Find the Short-Range Wireless Protocol:",
        "cards": [{"icon": "🟦", "label": "BLUE"}, {"icon": "🦷", "label": "TOOTH"}],
        "options": ["Wi-Fi Direct", "Bluetooth", "NFC Tag", "Infrared Beam"],
        "ans": 1,
        "ansText": "Bluetooth",
        "expl": "BLUE + TOOTH = Bluetooth! Named after 10th-century Danish King Harald Bluetooth."
    },
    {
        "q": "Connect the Visual Clues to Find the #1 Web Scripting Language:",
        "cards": [{"icon": "☕", "label": "JAVA (Coffee)"}, {"icon": "📜", "label": "SCRIPT"}],
        "options": ["TypeScript", "JavaScript", "CoffeeScript", "Python"],
        "ans": 1,
        "ansText": "JavaScript",
        "expl": "JAVA + SCRIPT = JavaScript! The universal language powering web interactivity."
    },
    {
        "q": "Connect the Visual Clues to Find the Code Defect Repair Process:",
        "cards": [{"icon": "🪲", "label": "BUG"}, {"icon": "🔨", "label": "FIX / HAMMER"}],
        "options": ["Code Compiling", "Debugging", "Refactoring", "Unit Testing"],
        "ans": 1,
        "ansText": "Debugging",
        "expl": "BUG + FIX = Debugging! Finding and resolving defects in computer program code."
    },
    {
        "q": "Connect the Visual Clues to Find the World Leading Code Repository Platform:",
        "cards": [{"icon": "🐙", "label": "OCTOPUS"}, {"icon": "🐱", "label": "CAT"}],
        "options": ["GitLab", "Bitbucket", "GitHub (Octocat)", "SourceForge"],
        "ans": 2,
        "ansText": "GitHub (Octocat)",
        "expl": "OCTOPUS + CAT = Octocat, the famous official mascot of GitHub!"
    },
    {
        "q": "Connect the Visual Clues to Find the On-Demand Hyperscale Infrastructure:",
        "cards": [{"icon": "☁️", "label": "CLOUD"}, {"icon": "💻", "label": "COMPUTING"}],
        "options": ["Cloud Computing", "Web Hosting", "Mainframe Server", "Edge Gateway"],
        "ans": 0,
        "ansText": "Cloud Computing",
        "expl": "CLOUD + COMPUTING = Cloud Computing! On-demand delivery of servers, databases, and storage."
    },
    {
        "q": "Connect the Visual Clues to Find the Modern PC Operating System:",
        "cards": [{"icon": "🪟", "label": "WINDOW"}, {"icon": "1️⃣1️⃣", "label": "ELEVEN"}],
        "options": ["Windows 10", "Windows 11", "macOS Sonoma", "Ubuntu Linux"],
        "ans": 1,
        "ansText": "Windows 11",
        "expl": "WINDOW + 11 = Windows 11! Microsoft's flagship desktop operating system."
    },
    {
        "q": "Connect the Visual Clues to Find the Top Python Data Science Library:",
        "cards": [{"icon": "🐍", "label": "PYTHON"}, {"icon": "🐼", "label": "PANDAS"}],
        "options": ["NumPy", "Pandas", "Matplotlib", "Scikit-Learn"],
        "ans": 1,
        "ansText": "Pandas",
        "expl": "PYTHON + PANDAS = Pandas! The foundational Python library for data manipulation and analysis."
    },
    {
        "q": "Connect the Visual Clues to Find the Leading Biometric Wearable:",
        "cards": [{"icon": "🍎", "label": "APPLE"}, {"icon": "⌚", "label": "WATCH"}],
        "options": ["Galaxy Watch", "Apple Watch", "Fitbit Charge", "Garmin Forerunner"],
        "ans": 1,
        "ansText": "Apple Watch",
        "expl": "APPLE + WATCH = Apple Watch! Running watchOS with heart-rate and health tracking."
    },
    {
        "q": "Connect the Visual Clues to Find the Decentralized Ledger Technology:",
        "cards": [{"icon": "🧱", "label": "BLOCK"}, {"icon": "🔗", "label": "CHAIN"}],
        "options": ["Smart Contract", "Blockchain", "Crypto Wallet", "Distributed Hash"],
        "ans": 1,
        "ansText": "Blockchain",
        "expl": "BLOCK + CHAIN = Blockchain! Cryptographically linked chain of immutable blocks."
    },
    {
        "q": "Connect the Visual Clues to Find the Conversational AI Assistant:",
        "cards": [{"icon": "🤖", "label": "ROBOT"}, {"icon": "💬", "label": "CHAT"}],
        "options": ["Web Scraper", "Chatbot / ChatGPT", "Search Bot", "Voice Modulator"],
        "ans": 1,
        "ansText": "Chatbot / ChatGPT",
        "expl": "CHAT + BOT = Chatbot! Conversational AI interface such as OpenAI's ChatGPT."
    },
    {
        "q": "Connect the Visual Clues to Find the Structured Electronic Data Store:",
        "cards": [{"icon": "🗄️", "label": "DATA"}, {"icon": "⚾", "label": "BASE"}],
        "options": ["File Folder", "Database", "Spreadsheet", "Data Lakehouse"],
        "ans": 1,
        "ansText": "Database",
        "expl": "DATA + BASE = Database! Organized repository for structured retrieval and storage."
    },
    {
        "q": "Connect the Visual Clues to Find the Open-Source Kernel Represented by Tux:",
        "cards": [{"icon": "🐧", "label": "PENGUIN"}, {"icon": "💻", "label": "TERMINAL"}],
        "options": ["FreeBSD", "Linux OS (Tux)", "Unix System V", "Solaris"],
        "ans": 1,
        "ansText": "Linux OS (Tux)",
        "expl": "PENGUIN + TERMINAL = Linux! Tux the penguin is the official mascot created by Linus Torvalds."
    },
    {
        "q": "Connect the Visual Clues to Find the Core Architecture of Deep Learning:",
        "cards": [{"icon": "🧠", "label": "NEURAL (Brain)"}, {"icon": "🕸️", "label": "NETWORK"}],
        "options": ["Decision Tree", "Neural Network", "Support Vector Machine", "Random Forest"],
        "ans": 1,
        "ansText": "Neural Network",
        "expl": "NEURAL + NETWORK = Artificial Neural Network! Modeling brain synaptic connections for AI."
    },
    {
        "q": "Connect the Visual Clues to Find the Essential Alphanumeric Input Hardware:",
        "cards": [{"icon": "🔑", "label": "KEY"}, {"icon": "📋", "label": "BOARD"}],
        "options": ["Motherboard", "Keyboard", "Circuit Breadboard", "Touchpad"],
        "ans": 1,
        "ansText": "Keyboard",
        "expl": "KEY + BOARD = Keyboard! Hardware device transmitting alphanumeric keystroke codes."
    },
    {
        "q": "Connect the Visual Clues to Find the Circular Statistical Chart:",
        "cards": [{"icon": "🥧", "label": "PIE"}, {"icon": "📊", "label": "CHART"}],
        "options": ["Bar Graph", "Pie Chart", "Scatter Plot", "Histogram"],
        "ans": 1,
        "ansText": "Pie Chart",
        "expl": "PIE + CHART = Pie Chart! Circular statistical graphic divided into proportional slices."
    },
    {
        "q": "Connect the Visual Clues to Find the Enterprise Visual Analytics Platform:",
        "cards": [{"icon": "🪟", "label": "TABLE"}, {"icon": "🌟", "label": "AU (Gold)"}],
        "options": ["Power BI", "Tableau", "Looker Studio", "Qlik Sense"],
        "ans": 1,
        "ansText": "Tableau",
        "expl": "TABLE + AU = Tableau! World famous data visualization and dashboarding software."
    },
    {
        "q": "Connect the Visual Clues to Find the Pioneer Cloud File Sync Service:",
        "cards": [{"icon": "💧", "label": "DROP"}, {"icon": "📦", "label": "BOX"}],
        "options": ["Google Drive", "OneDrive", "Dropbox", "Mega Cloud"],
        "ans": 2,
        "ansText": "Dropbox",
        "expl": "DROP + BOX = Dropbox! Cloud storage service founded by Drew Houston and Arash Ferdowsi."
    },
    {
        "q": "Connect the Visual Clues to Find the System That Indexes World Information:",
        "cards": [{"icon": "🔍", "label": "SEARCH"}, {"icon": "⚙️", "label": "ENGINE"}],
        "options": ["Web Browser", "Search Engine (Google)", "Web Server", "Domain Registry"],
        "ans": 1,
        "ansText": "Search Engine (Google)",
        "expl": "SEARCH + ENGINE = Search Engine! Crawling and indexing billions of web pages."
    },
    {
        "q": "Connect the Visual Clues to Find the Big Data Framework Symbolized by a Yellow Elephant:",
        "cards": [{"icon": "🐘", "label": "ELEPHANT"}, {"icon": "📊", "label": "BIG DATA"}],
        "options": ["Apache Spark", "Apache Hadoop", "Apache Kafka", "Elasticsearch"],
        "ans": 1,
        "ansText": "Apache Hadoop",
        "expl": "ELEPHANT + BIG DATA = Apache Hadoop! Doug Cutting named it after his son's toy yellow elephant."
    },
    {
        "q": "Connect the Visual Clues to Find the Encrypted Identity Tunnel:",
        "cards": [{"icon": "🎭", "label": "PRIVATE (Mask)"}, {"icon": "🌐", "label": "NETWORK"}],
        "options": ["Firewall Shield", "VPN (Virtual Private Network)", "Proxy Server", "Tor Relay"],
        "ans": 1,
        "ansText": "VPN",
        "expl": "PRIVATE + NETWORK = VPN! Encrypts traffic and hides your IP address on public Wi-Fi."
    },
    {
        "q": "Connect the Visual Clues to Find the Traffic Distribution System:",
        "cards": [{"icon": "🚦", "label": "LOAD (Traffic)"}, {"icon": "⚖️", "label": "BALANCER"}],
        "options": ["Reverse Proxy", "Load Balancer", "API Gateway", "Firewall Router"],
        "ans": 1,
        "ansText": "Load Balancer",
        "expl": "LOAD + BALANCER = Load Balancer! Distributes network traffic across healthy server clusters."
    },
    {
        "q": "Connect the Visual Clues to Find Automatic Memory Reclaim in Java/Python:",
        "cards": [{"icon": "🗑️", "label": "GARBAGE"}, {"icon": "♻️", "label": "COLLECTION"}],
        "options": ["Memory Leak", "Garbage Collection", "Buffer Overflow", "Stack Tracing"],
        "ans": 1,
        "ansText": "Garbage Collection",
        "expl": "GARBAGE + COLLECTION = Garbage Collection (GC)! Automatic memory management freeing dead RAM objects."
    },
    {
        "q": "Connect the Visual Clues to Find the World Container Platform (Blue Whale):",
        "cards": [{"icon": "🐳", "label": "WHALE"}, {"icon": "📦", "label": "CONTAINER"}],
        "options": ["Kubernetes", "Docker", "Podman", "Vagrant"],
        "ans": 1,
        "ansText": "Docker",
        "expl": "WHALE + CONTAINER = Docker! Standard packaging for applications and dependencies."
    },
    {
        "q": "Connect the Visual Clues to Find the Git Feature to Work on Parallel Features:",
        "cards": [{"icon": "🌳", "label": "GIT TREE"}, {"icon": "🌿", "label": "BRANCH"}],
        "options": ["Git Commit", "Git Branch", "Git Merge", "Git Stash"],
        "ans": 1,
        "ansText": "Git Branch",
        "expl": "GIT TREE + BRANCH = Git Branch! Allows teams to develop isolated features without touching main."
    },
    {
        "q": "Connect the Visual Clues to Find Parallel Execution Inside a Single Process:",
        "cards": [{"icon": "🕸️", "label": "MULTI (Web)"}, {"icon": "🧵", "label": "THREAD"}],
        "options": ["Multi-Processing", "Multi-Threading", "Asynchronous Loop", "Task Scheduling"],
        "ans": 1,
        "ansText": "Multi-Threading",
        "expl": "MULTI + THREAD = Multi-Threading! Concurrent execution threads sharing memory within a process."
    },
    {
        "q": "Connect the Visual Clues to Find the Secure Web Protocol with Green Padlock:",
        "cards": [{"icon": "🔒", "label": "LOCK (Secure)"}, {"icon": "🌐", "label": "WEB (HTTP)"}],
        "options": ["HTTP Protocol", "HTTPS / SSL", "FTP Protocol", "SSH Gateway"],
        "ans": 1,
        "ansText": "HTTPS / SSL",
        "expl": "LOCK + WEB = HTTPS! HyperText Transfer Protocol Secure encrypted via SSL/TLS certificates."
    }
]

with open('D:/WEGROW/14.Game/public/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data[1]['questions'] = r2_conn

with open('D:/WEGROW/14.Game/public/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('Round 2 successfully upgraded to 30 Visual Connections Puzzles with Options!')
