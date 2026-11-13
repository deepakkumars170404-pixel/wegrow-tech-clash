import json

# 30 Tough & Smart Tech Connections without simple giveaways
r2_tough = [
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🔥", "label": "FIRE"}, {"icon": "🧱", "label": "WALL"}],
        "ansText": "Firewall",
        "expl": "FIRE + WALL = Firewall! The foundational security gate monitoring & filtering inbound/outbound packets."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🐱", "label": "CAT"}, {"icon": "🎣", "label": "FISHING"}],
        "ansText": "Phishing",
        "expl": "CAT (Catfish) + FISHING = Phishing! Social engineering attack deceptive fraudulent trap."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🖊️", "label": "PEN"}, {"icon": "🚗", "label": "DRIVE"}],
        "ansText": "Pendrive",
        "expl": "PEN + DRIVE = Pendrive! Portable solid-state USB flash storage."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🍪", "label": "COOKIE"}, {"icon": "🌐", "label": "WEB"}],
        "ansText": "Browser Cookie",
        "expl": "COOKIE + WEB = Browser Cookie! Client-side state tokens tracking authenticated sessions."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🟦", "label": "BLUE"}, {"icon": "🦷", "label": "TOOTH"}],
        "ansText": "Bluetooth",
        "expl": "BLUE + TOOTH = Bluetooth! Short-range wireless standard named after Danish King Harald Bluetooth."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "☕", "label": "JAVA (Coffee)"}, {"icon": "📜", "label": "SCRIPT"}],
        "ansText": "JavaScript",
        "expl": "JAVA + SCRIPT = JavaScript! The universal multi-paradigm runtime powering modern web engines."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🪲", "label": "BUG"}, {"icon": "🔨", "label": "HAMMER / FIX"}],
        "ansText": "Debugging",
        "expl": "BUG + HAMMER/FIX = Debugging! Tracing execution stacks to eliminate flaws in source code."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🐙", "label": "OCTOPUS"}, {"icon": "🐱", "label": "CAT"}],
        "ansText": "GitHub (Octocat)",
        "expl": "OCTOPUS + CAT = Octocat! Official mascot representing Git version control repository host GitHub."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "☁️", "label": "CLOUD"}, {"icon": "💻", "label": "COMPUTING"}],
        "ansText": "Cloud Computing",
        "expl": "CLOUD + COMPUTING = Cloud Computing! Elastic compute, virtual machines, and managed storage."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🐍", "label": "PYTHON"}, {"icon": "🐼", "label": "PANDAS"}],
        "ansText": "Pandas Dataframe",
        "expl": "PYTHON + PANDAS = Pandas! High-performance Python data structures and analytics toolkit."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🧱", "label": "BLOCK"}, {"icon": "🔗", "label": "CHAIN"}],
        "ansText": "Blockchain",
        "expl": "BLOCK + CHAIN = Blockchain! Cryptographically linked distributed ledger providing Byzantine fault tolerance."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🤖", "label": "ROBOT / BOT"}, {"icon": "💬", "label": "CHAT"}],
        "ansText": "Chatbot / ChatGPT",
        "expl": "CHAT + BOT = Chatbot! Large Language Models and natural language conversational agents."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🗄️", "label": "DATA"}, {"icon": "⚾", "label": "BASE"}],
        "ansText": "Database",
        "expl": "DATA + BASE = Database! Organized persistence store ensuring ACID compliance and query planning."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🐧", "label": "PENGUIN"}, {"icon": "💻", "label": "TERMINAL"}],
        "ansText": "Linux OS (Tux)",
        "expl": "PENGUIN + TERMINAL = Linux! Unix-like monolithic kernel symbolized by Tux the penguin."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🧠", "label": "NEURAL (Brain)"}, {"icon": "🕸️", "label": "NETWORK"}],
        "ansText": "Neural Network",
        "expl": "NEURAL + NETWORK = Artificial Neural Network! Weighted layers of perceptrons driving Deep Learning."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🔑", "label": "KEY"}, {"icon": "📋", "label": "BOARD"}],
        "ansText": "Keyboard",
        "expl": "KEY + BOARD = Keyboard! Mechanical and matrix hardware sending scan codes via USB/HID."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🥧", "label": "PIE"}, {"icon": "📊", "label": "CHART"}],
        "ansText": "Pie Chart",
        "expl": "PIE + CHART = Pie Chart! Circular polar projection showing category proportions of 360 degrees."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🪟", "label": "TABLE"}, {"icon": "🌟", "label": "AU (Gold)"}],
        "ansText": "Tableau",
        "expl": "TABLE + AU = Tableau! Visual business intelligence and drag-and-drop data dashboarding tool."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "💧", "label": "DROP"}, {"icon": "📦", "label": "BOX"}],
        "ansText": "Dropbox",
        "expl": "DROP + BOX = Dropbox! Cloud sync pioneer leveraging delta sync block compression algorithms."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🔍", "label": "SEARCH"}, {"icon": "⚙️", "label": "ENGINE"}],
        "ansText": "Search Engine",
        "expl": "SEARCH + ENGINE = Search Engine! Spiders crawling, tokenizing inverted indexes, and ranking results."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🐘", "label": "ELEPHANT"}, {"icon": "📊", "label": "BIG DATA"}],
        "ansText": "Apache Hadoop",
        "expl": "ELEPHANT + BIG DATA = Apache Hadoop! Distributed MapReduce computation and HDFS cluster storage."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🎭", "label": "PRIVATE (Mask)"}, {"icon": "🌐", "label": "NETWORK"}],
        "ansText": "VPN",
        "expl": "PRIVATE + NETWORK = VPN! Virtual Private Network encapsulating encrypted packet payloads."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🚦", "label": "LOAD (Traffic)"}, {"icon": "⚖️", "label": "BALANCER"}],
        "ansText": "Load Balancer",
        "expl": "LOAD + BALANCER = Load Balancer! Layer 4/Layer 7 reverse proxy distributing incoming connections."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🗑️", "label": "GARBAGE"}, {"icon": "♻️", "label": "COLLECTION"}],
        "ansText": "Garbage Collection",
        "expl": "GARBAGE + COLLECTION = Garbage Collection (GC)! Mark-and-sweep automatic heap memory management."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🐳", "label": "WHALE"}, {"icon": "📦", "label": "CONTAINER"}],
        "ansText": "Docker",
        "expl": "WHALE + CONTAINER = Docker! OS-level virtualization packaging apps inside cgroups & namespaces."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🌳", "label": "TREE (Git)"}, {"icon": "🌿", "label": "BRANCH"}],
        "ansText": "Git Branch",
        "expl": "TREE + BRANCH = Git Branch! Lightweight movable pointer to independent commit DAG histories."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🕸️", "label": "MULTI (Web)"}, {"icon": "🧵", "label": "THREAD"}],
        "ansText": "Multi-Threading",
        "expl": "MULTI + THREAD = Multi-Threading! Concurrency paradigm where threads share parent address space."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🔒", "label": "LOCK (Secure)"}, {"icon": "🌐", "label": "WEB (HTTP)"}],
        "ansText": "HTTPS / SSL",
        "expl": "LOCK + WEB = HTTPS! Symmetric session encryption negotiated via asymmetric TLS handshakes."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🌊", "label": "SEA (C)"}, {"icon": "➕➕", "label": "PLUS PLUS"}],
        "ansText": "C++",
        "expl": "SEA (C) + PLUS PLUS = C++! High-performance compiled systems language created by Bjarne Stroustrup."
    },
    {
        "q": "Identify the Core Technology by Connecting the Visual Clues:",
        "cards": [{"icon": "🍃", "label": "LEAF"}, {"icon": "🗄️", "label": "DATABASE"}],
        "ansText": "MongoDB",
        "expl": "LEAF + DATABASE = MongoDB! Document-oriented NoSQL database represented by a green leaf logo."
    }
]

with open('D:/WEGROW/14.Game/public/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update Round 2 without options
data[1]['questions'] = r2_tough

with open('D:/WEGROW/14.Game/public/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('Round 2 updated with 30 tough visual connections without multiple-choice options!')
