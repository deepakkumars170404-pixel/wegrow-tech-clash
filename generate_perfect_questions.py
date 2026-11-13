# -*- coding: utf-8 -*-
"""
generate_perfect_questions.py
Builds the complete questions dataset for WeGrow Tech Clash Tournament:
- Round 1: The Bidding MCQ (20 questions, simple English, balanced A/B/C/D, balanced option lengths)
- Round 2: Tech Mythbusters (Fact or Fiction?) (20 questions, 10 Fact / 10 Fiction, exciting misconceptions)
- Round 3: Odd One Out (The Imposter) (20 questions, tough technical conceptual logic, balanced 0/1/2/3)
- Round 4: Tech Detective (Who Am I?) (20 questions, 3 progressive clues)
- Round 5: Future or Fired? (10 questions, exactly 10 debate topics as requested)
- Round 6: The Tech Millionaire (20 questions, balanced A/B/C/D, uniform option length, no loopholes)
- Round 7: Rapid Fire Clash (20 questions, fast questions, balanced A/B/C/D)
"""

import json

rounds = []

# ==================== ROUND 1: 20 IT FOUNDATION MCQs ====================
# Balanced: 5 A, 5 B, 5 C, 5 D. Option lengths uniform (approx 20-35 chars). Simple English.
r1_items = [
    {
        "q": "When you type 'google.com' in a browser, where does the computer look first for the IP address?",
        "options": ["Internet Service Provider", "Local DNS Cache in OS/Browser", "Google Central Data Center", "Undersea Fiber Optic Cable"],
        "ans": 1,
        "ansText": "Local DNS Cache in OS/Browser",
        "expl": "The operating system checks its local cache first to avoid slow network lookups."
    },
    {
        "q": "What core benefit does HTTPS provide compared to regular unencrypted HTTP?",
        "options": ["Doubles file download rate", "Guarantees zero PC viruses", "Encrypts data during transit", "Provides unlimited storage"],
        "ans": 2,
        "ansText": "Encrypts data during transit",
        "expl": "HTTPS uses SSL/TLS encryption so third parties on the network cannot read your data."
    },
    {
        "q": "Why does data remain saved on an SSD when your PC is turned off, but disappears from RAM?",
        "options": ["SSD uses non-volatile NAND", "RAM has a built-in battery", "SSD connects directly to CPU", "Windows restores it at boot"],
        "ans": 0,
        "ansText": "SSD uses non-volatile NAND",
        "expl": "RAM requires continuous electrical power, while SSD NAND flash traps charge permanently."
    },
    {
        "q": "In HTTP status codes, what does the first digit '4' mean in a '404 Not Found' error?",
        "options": ["Network hardware failure", "Server internal error", "Redirect to another URL", "Client-side request error"],
        "ans": 3,
        "ansText": "Client-side request error",
        "expl": "4xx codes indicate client-side errors, meaning the requested URL does not exist."
    },
    {
        "q": "Where does 'Cloud Computing' physically operate in the real world?",
        "options": ["Atmospheric radio waves", "Global data center server farms", "Cellular satellite towers", "Personal Wi-Fi home routers"],
        "ans": 1,
        "ansText": "Global data center server farms",
        "expl": "Cloud computing runs inside massive, climate-controlled enterprise data centers."
    },
    {
        "q": "During ticket flash sales, why do payments sometimes succeed but seats fail to confirm?",
        "options": ["Computer ran out of RAM", "Browser cookie got deleted", "Database row locking conflicts", "Internet provider shut down"],
        "ans": 2,
        "ansText": "Database row locking conflicts",
        "expl": "When thousands try to book the same row simultaneously, database transactions conflict."
    },
    {
        "q": "What is the primary difference between traditional programming and Machine Learning?",
        "options": ["Humans write rules; ML learns rules", "ML requires zero computer memory", "Traditional code has zero bugs", "ML works without any training data"],
        "ans": 0,
        "ansText": "Humans write rules; ML learns rules",
        "expl": "Traditional code requires manual rules, while ML extracts mathematical patterns from data."
    },
    {
        "q": "Why did JSON become more popular than XML for transferring data in modern web APIs?",
        "options": ["Invented directly by Apple", "Works only on Linux servers", "Requires no internet connection", "Lightweight and native to JavaScript"],
        "ans": 3,
        "ansText": "Lightweight and native to JavaScript",
        "expl": "JSON avoids verbose tags and maps directly to native JavaScript data structures."
    },
    {
        "q": "What does browser 'Incognito Mode' actually do on your computer?",
        "options": ["Blocks government monitoring", "Stops local history and cookies", "Changes your real IP address", "Encrypts all outgoing traffic"],
        "ans": 1,
        "ansText": "Stops local history and cookies",
        "expl": "Incognito only prevents local session saving; websites and networks can still see your IP."
    },
    {
        "q": "Which data structure does a browser use to manage the Back and Forward history buttons?",
        "options": ["FIFO First-In First-Out Queue", "Relational Database Table", "LIFO Call Stack Data Structure", "Binary Search Tree Index"],
        "ans": 2,
        "ansText": "LIFO Call Stack Data Structure",
        "expl": "Navigating pages pushes URLs onto a stack; the Back button pops the most recent page."
    },
    {
        "q": "What mechanism allows a single CPU core to run music, coding, and web browsing together?",
        "options": ["Time-sliced multitasking in OS", "Hardware overclocking booster", "Multiple optical laser heads", "Virtual power supply doubling"],
        "ans": 0,
        "ansText": "Time-sliced multitasking in OS",
        "expl": "The OS scheduler switches execution contexts every millisecond to create concurrency."
    },
    {
        "q": "Which database type is best designed for social network friends and mutual connections?",
        "options": ["Flat CSV text document", "Microsoft Excel workbook", "Relational SQL database", "Graph database like Neo4j"],
        "ans": 3,
        "ansText": "Graph database like Neo4j",
        "expl": "Graph databases store nodes and edge relationships directly for fast traversal."
    },
    {
        "q": "What is the main role of an API (Application Programming Interface) in software development?",
        "options": ["Replaces the operating system", "Enables two apps to communicate", "Cools down the motherboard", "Displays graphics on monitor"],
        "ans": 1,
        "ansText": "Enables two apps to communicate",
        "expl": "APIs define the standard contracts and endpoints for different services to exchange data."
    },
    {
        "q": "Why is an IPv6 address needed when IPv4 has been used for decades?",
        "options": ["IPv4 was hacked completely", "IPv6 makes Wi-Fi 10x faster", "World ran out of IPv4 addresses", "IPv4 cannot send text messages"],
        "ans": 2,
        "ansText": "World ran out of IPv4 addresses",
        "expl": "IPv4 supports ~4.3 billion addresses; IPv6 provides 340 undecillion addresses."
    },
    {
        "q": "In Git, what is the exact difference between 'git fetch' and 'git pull'?",
        "options": ["Fetch downloads; pull also merges", "Fetch deletes all local changes", "Pull only works on GitHub repos", "They are 100% identical commands"],
        "ans": 0,
        "ansText": "Fetch downloads; pull also merges",
        "expl": "'git fetch' downloads remote commits; 'git pull' downloads and immediately merges them."
    },
    {
        "q": "What is the function of a 'Compiler' in languages like C, C++, and Java?",
        "options": ["Runs the app inside a browser", "Translates code to machine binaries", "Increases your internet bandwidth", "Cleans the computer cooling fan"],
        "ans": 1,
        "ansText": "Translates code to machine binaries",
        "expl": "Compilers translate human-readable source code into CPU machine instructions."
    },
    {
        "q": "Which layer of the OSI model handles physical routing across international IP networks?",
        "options": ["Application Layer (Layer 7)", "Data Link Layer (Layer 2)", "Network Layer (Layer 3)", "Presentation Layer (Layer 6)"],
        "ans": 2,
        "ansText": "Network Layer (Layer 3)",
        "expl": "Layer 3 handles logical packet addressing, routing, and path determination (IPv4/IPv6)."
    },
    {
        "q": "What happens during a 'Buffer Overflow' security vulnerability in software?",
        "options": ["Monitor screen turns off", "Hard drive gets formatted", "Battery discharges quickly", "Data overwrites adjacent memory"],
        "ans": 3,
        "ansText": "Data overwrites adjacent memory",
        "expl": "Writing past allocated memory boundaries can overwrite return addresses and inject shellcode."
    },
    {
        "q": "Why do modern microprocessors include multiple CPU cores instead of just 1 very high GHz core?",
        "options": ["Preventing excessive heat & power", "Dual cores double monitor sizes", "Single cores cannot run 64-bit OS", "Motherboards require 4 sockets"],
        "ans": 0,
        "ansText": "Preventing excessive heat & power",
        "expl": "Pushing clock speed generates unmanageable heat; parallel cores improve efficiency."
    },
    {
        "q": "In web architecture, what is the primary role of a 'Load Balancer'?",
        "options": ["Compresses CSS and JavaScript", "Distributes traffic across servers", "Scans user photos for viruses", "Charges user credit cards safely"],
        "ans": 1,
        "ansText": "Distributes traffic across servers",
        "expl": "Load balancers spread incoming network requests across multiple backend instances."
    }
]

rounds.append({
    "id": 1,
    "name": "Round 1: The Bidding MCQ",
    "type": "mcq",
    "description": "IT Foundation Essentials • 4 Balanced Options • 20 Questions",
    "questions": r1_items
})

# ==================== ROUND 2: 20 TECH MYTHBUSTERS (FACT OR FICTION?) ====================
# Exciting, fast, clean! 10 Fact (ans: 0), 10 Fiction / Myth (ans: 1).
r2_items = [
    {
        "q": "Leaving your smartphone plugged into the charger overnight will overcharge and destroy the battery.",
        "statement": "Leaving your smartphone plugged in overnight will overcharge and destroy the battery.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Modern smartphones have smart Power Management ICs that automatically cut current at 100%."
    },
    {
        "q": "RAM memory permanently loses all stored data the moment computer power is switched off.",
        "statement": "RAM memory permanently loses all stored data the moment power is switched off.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "RAM is volatile memory; capacitors discharge in milliseconds without continuous electrical refresh."
    },
    {
        "q": "Browsing in 'Incognito Mode' completely hides your activity from your Wi-Fi owner, college, and ISP.",
        "statement": "Browsing in 'Incognito Mode' completely hides your browsing activity from your Wi-Fi owner, college, and ISP.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Incognito only clears local history on your device; network routers, college proxies, and ISPs still log requests."
    },
    {
        "q": "A processor with 4.0 GHz clock speed is always faster than a processor with 3.2 GHz clock speed.",
        "statement": "A processor with 4.0 GHz clock speed is always faster than a processor with 3.2 GHz clock speed.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Architecture, IPC (Instructions Per Cycle), cache size, and core count matter far more than raw GHz."
    },
    {
        "q": "Over 95% of international internet traffic travels through undersea subsea fiber cables, not satellites.",
        "statement": "Over 95% of international internet traffic travels through undersea subsea fiber cables, not satellites.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "Hundreds of high-capacity fiber cables cross ocean floors carrying virtually all global intercontinental data."
    },
    {
        "q": "More camera Megapixels (e.g. 108 MP vs 12 MP) automatically guarantees superior photo quality.",
        "statement": "More camera Megapixels automatically guarantees superior photo quality.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Sensor physical size, lens aperture, optical stabilization, and computational ISP software matter much more."
    },
    {
        "q": "Symmetric encryption like AES-256 is computationally much faster to execute than asymmetric RSA encryption.",
        "statement": "Symmetric encryption like AES-256 is computationally much faster to execute than asymmetric RSA encryption.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "AES uses fast bitwise CPU instructions, while RSA requires heavy modular arithmetic on giant prime numbers."
    },
    {
        "q": "Mac computers and Apple iPhones are 100% immune to viruses and cannot be infected by malware.",
        "statement": "Mac computers and Apple iPhones are 100% immune to viruses and cannot be infected by malware.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "While sandboxing helps, macOS and iOS have documented zero-day exploits, adware, and targeted spyware like Pegasus."
    },
    {
        "q": "Turning on Dark Mode on an OLED screen genuinely saves battery power.",
        "statement": "Turning on Dark Mode on an OLED screen genuinely saves battery power.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "OLED pixels produce their own light; displaying true black physically shuts those individual LEDs completely off."
    },
    {
        "q": "Emptying the Recycle Bin or Trash permanently erases data so it can never be recovered.",
        "statement": "Emptying the Recycle Bin permanently erases data so it can never be recovered.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "The OS only marks that disk space as available for overwrite; the raw magnetic/NAND bits remain until overwritten."
    },
    {
        "q": "The name 'Bluetooth' was named after a 10th-century Scandinavian Viking King named Harald Bluetooth.",
        "statement": "The name 'Bluetooth' was named after a 10th-century Scandinavian Viking King named Harald Bluetooth.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "King Harald united Scandinavian tribes; engineers named the protocol to unite gadgets without wires."
    },
    {
        "q": "Putting a wet smartphone into a bowl of dry uncooked rice is the best way to fix water damage.",
        "statement": "Putting a wet smartphone into a bowl of dry uncooked rice is the best way to fix water damage.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Rice is slow to absorb moisture and deposits starch dust into ports; silica gel packets and airflow work far better."
    },
    {
        "q": "HTML is an official computer programming language that compiles logic into executable code.",
        "statement": "HTML is an official computer programming language that compiles logic into executable code.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "HTML is a HyperText Markup Language defining document structure; it has no variables, functions, or loops."
    },
    {
        "q": "Over 90% of the world's top 500 supercomputers and cloud servers run on the Linux operating system.",
        "statement": "Over 90% of the world's top 500 supercomputers and cloud servers run on the Linux operating system.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "100% of the world's top 500 supercomputers and majority of global cloud servers run Linux distributions."
    },
    {
        "q": "A longer passphrase of simple words (e.g. 'purple elephant jumps high') is harder to brute force than a short complex password (e.g. 'P@ss1').",
        "statement": "A longer passphrase of simple words is harder to brute force than a short complex password.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "Mathematical password entropy scales exponentially with length; 25+ characters takes centuries to brute force."
    },
    {
        "q": "Deleting all browser cookies will also log you out of your desktop games like Steam and Discord.",
        "statement": "Deleting all browser cookies will also log you out of your desktop games like Steam and Discord.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Desktop applications store their authentication tokens in their own app data folders, not in browser cookie jars."
    },
    {
        "q": "Python is an interpreted language and can never be converted or compiled into standalone binary code.",
        "statement": "Python is strictly an interpreted language and can never be converted into standalone binary code.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Tools like Cython, Nuitka, PyInstaller, and Mojo compile Python into native C/machine code binaries."
    },
    {
        "q": "The term 'Bug' in software engineering literally came from a real moth trapped inside a computer relay in 1947.",
        "statement": "The term 'Bug' in computer science came from a real moth trapped inside a computer relay switch.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "Grace Hopper's team found an actual moth in the Harvard Mark II computer and taped it into their logbook."
    },
    {
        "q": "Closing all background apps on modern iOS and Android smartphones will drastically speed up your phone.",
        "statement": "Force-closing all background apps on modern iOS and Android will drastically speed up your phone.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 1,
        "ansText": "FICTION / MYTH",
        "expl": "Background apps are frozen in RAM; killing them forces the CPU to reload all assets from storage, using MORE battery."
    },
    {
        "q": "The very first domain name ever registered on the commercial internet in 1985 was 'Symbolics.com'.",
        "statement": "The very first commercial '.com' domain name registered in internet history was 'Symbolics.com'.",
        "options": ["FACT", "FICTION / MYTH"],
        "ans": 0,
        "ansText": "FACT",
        "expl": "Symbolics.com was registered on March 15, 1985, years before google.com or apple.com existed."
    }
]

rounds.append({
    "id": 2,
    "name": "Round 2: Tech Mythbusters (Fact or Fiction?)",
    "type": "fact_fiction",
    "description": "Buzz Fast • FACT or FICTION? • Bust Real-World Tech Myths • 20 Questions",
    "questions": r2_items
})

# ==================== ROUND 3: 20 SIMPLE ODD ONE OUT (THE IMPOSTER) ====================
# Simple, relatable, crystal clear for college students! Balanced answers (5 of 0, 5 of 1, 5 of 2, 5 of 3).
r3_items = [
    {
        "items": ["Microsoft Excel", "Google Chrome", "Mozilla Firefox", "Microsoft Edge"],
        "ans": 0,
        "ansText": "Microsoft Excel",
        "expl": "Microsoft Excel is an office spreadsheet tool; the other three are web browsers."
    },
    {
        "items": ["Python", "HTML", "Java", "C++"],
        "ans": 1,
        "ansText": "HTML",
        "expl": "HTML is a document markup structure language; the other three are programming languages."
    },
    {
        "items": ["Keyboard", "Computer Mouse", "Computer Monitor", "Microphone"],
        "ans": 2,
        "ansText": "Computer Monitor",
        "expl": "Computer Monitor is an output display screen; the other three are user input devices."
    },
    {
        "items": ["Instagram", "WhatsApp", "Facebook", "Linux Operating System"],
        "ans": 3,
        "ansText": "Linux Operating System",
        "expl": "Linux is a computer operating system; the other three are social media and messaging apps."
    },
    {
        "items": ["RAM Memory", "SSD Drive", "Hard Disk Drive", "USB Pen Drive"],
        "ans": 0,
        "ansText": "RAM Memory",
        "expl": "RAM is temporary volatile memory that erases on shutdown; the other three are permanent storage."
    },
    {
        "items": ["Windows 11", "Adobe Photoshop", "Apple macOS", "Android OS"],
        "ans": 1,
        "ansText": "Adobe Photoshop",
        "expl": "Adobe Photoshop is a photo editing application; the other three are operating systems."
    },
    {
        "items": ["CPU Processor", "Graphics Card", "Google Search", "Motherboard"],
        "ans": 2,
        "ansText": "Google Search",
        "expl": "Google Search is an online web service; the other three are physical computer hardware parts."
    },
    {
        "items": ["YouTube", "Netflix", "Amazon Prime", "Calculator App"],
        "ans": 3,
        "ansText": "Calculator App",
        "expl": "Calculator App is a basic math utility; the other three are online video streaming platforms."
    },
    {
        "items": ["HDMI Cable", "Wi-Fi", "Bluetooth", "Mobile Hotspot"],
        "ans": 0,
        "ansText": "HDMI Cable",
        "expl": "HDMI Cable is physical wired display hardware; the other three are wireless networking signals."
    },
    {
        "items": ["WhatsApp", "Microsoft Word", "Telegram", "Signal"],
        "ans": 1,
        "ansText": "Microsoft Word",
        "expl": "Microsoft Word is a document word processor; the other three are instant messaging apps."
    },
    {
        "items": ["Google Pay", "PhonePe", "Spotify Music", "Paytm"],
        "ans": 2,
        "ansText": "Spotify Music",
        "expl": "Spotify is an audio music streaming app; the other three are UPI digital payment wallets."
    },
    {
        "items": ["ChatGPT", "Google Gemini", "Claude AI", "VLC Media Player"],
        "ans": 3,
        "ansText": "VLC Media Player",
        "expl": "VLC is a video and music player tool; the other three are conversational AI chatbots."
    },
    {
        "items": ["Nike Shoes", "Apple Inc", "Samsung", "Xiaomi"],
        "ans": 0,
        "ansText": "Nike Shoes",
        "expl": "Nike is a sports apparel and footwear company; the other three are global smartphone tech makers."
    },
    {
        "items": ["Bit", "Kilogram", "Byte", "Gigabyte"],
        "ans": 1,
        "ansText": "Kilogram",
        "expl": "Kilogram is a physical weight metric; the other three are digital computer data storage units."
    },
    {
        "items": ["Audio Speaker", "Headphones", "Webcam Camera", "Projector Screen"],
        "ans": 2,
        "ansText": "Webcam Camera",
        "expl": "Webcam Camera is a video input device; the other three are audio/visual output devices."
    },
    {
        "items": ["Git", "GitHub", "GitLab", "MS Paint"],
        "ans": 3,
        "ansText": "MS Paint",
        "expl": "MS Paint is a simple drawing program; the other three are software source code version control tools."
    },
    {
        "items": ["PDF Document", "MP3 Audio", "WAV Audio", "AAC Audio"],
        "ans": 0,
        "ansText": "PDF Document",
        "expl": "PDF Document is a text and page reading format; the other three are audio sound file formats."
    },
    {
        "items": ["Amazon", "Wikipedia", "Flipkart", "Myntra"],
        "ans": 1,
        "ansText": "Wikipedia",
        "expl": "Wikipedia is a free online encyclopedia; the other three are e-commerce shopping stores."
    },
    {
        "items": ["Swiggy", "Zomato", "Google Maps", "Uber Eats"],
        "ans": 2,
        "ansText": "Google Maps",
        "expl": "Google Maps is a navigation GPS tool; the other three are food delivery apps."
    },
    {
        "items": ["JPEG Image", "PNG Image", "GIF Image", "MP4 Video"],
        "ans": 3,
        "ansText": "MP4 Video",
        "expl": "MP4 is a video recording format; the other three are static graphic image file formats."
    }
]

rounds.append({
    "id": 3,
    "name": "Round 3: Odd One Out (The Imposter)",
    "type": "imposter",
    "description": "Fun & Fast • Spot the Imposter • 20 Questions",
    "questions": r3_items
})

# ==================== ROUND 4: 20 TECH DETECTIVE (WHO AM I?) ====================
# Progressive 3-clue reveals: Clue 1 (300 pts), Clue 2 (200 pts), Clue 3 (100 pts)
r4_items = [
    {
        "clue1": "I began in 1994 as an online bookstore operating from a Seattle garage.",
        "clue2": "Today, a huge portion of the global internet runs on my hyperscale cloud servers.",
        "clue3": "My logo features a smile arrow pointing from letter 'A' to 'Z'.",
        "ansText": "Amazon (AWS)",
        "expl": "Jeff Bezos founded Amazon, growing it into the world's leading e-commerce and cloud provider."
    },
    {
        "clue1": "My creator wrote me over a Christmas holiday in 1989 as a hobby project.",
        "clue2": "My name does not come from a snake, but from BBC comedy 'Monty Python'.",
        "clue3": "Today, I am the #1 programming language for Data Science and Machine Learning.",
        "ansText": "Python Programming Language",
        "expl": "Guido van Rossum developed Python, famous for clean indentation and rich libraries."
    },
    {
        "clue1": "I was created in 1995 in just 10 days by a programmer named Brendan Eich.",
        "clue2": "Part of my name was chosen for marketing hype; I share no engine design with my namesake.",
        "clue3": "Today, over 98% of all websites in the world depend on me for interactive logic.",
        "ansText": "JavaScript",
        "expl": "JavaScript powers browser interactivity alongside HTML and CSS across the web."
    },
    {
        "clue1": "I started in 1997 as a mail-order DVD rental service that beat Blockbuster.",
        "clue2": "My streaming service accounts for approximately 15% of all global downstream internet traffic.",
        "clue3": "My TV and mobile apps greet viewers with an unmistakable 'Tudum' sound.",
        "ansText": "Netflix",
        "expl": "Reed Hastings and Marc Randolph pioneered video streaming and recommendation algorithms."
    },
    {
        "clue1": "I was created by Linus Torvalds to manage the Linux operating system source code.",
        "clue2": "My core vocabulary includes Commit, Push, Pull, Branch, and Rebase.",
        "clue3": "My cloud counterpart features a mascot that is half-cat, half-octopus called Octocat.",
        "ansText": "Git / GitHub",
        "expl": "Git is the distributed version control system used by software developers globally."
    },
    {
        "clue1": "My original research project name at Stanford in 1996 was 'Backrub'.",
        "clue2": "My name is a misspelling of the mathematical number 1 followed by 100 zeros (Googol).",
        "clue3": "Searching for information anywhere on the web has turned my brand into a common English verb.",
        "ansText": "Google Search",
        "expl": "Larry Page and Sergey Brin founded Google, indexing the web via PageRank algorithms."
    },
    {
        "clue1": "I was unveiled in January 2007 by Steve Jobs as an iPod, a phone, and an internet communicator.",
        "clue2": "I discarded physical plastic keypads in favor of a capacitive multi-touch glass screen.",
        "clue3": "My aluminum body features a logo of an apple with a single bite taken out.",
        "ansText": "Apple iPhone",
        "expl": "The iPhone launched modern mobile computing and the global smartphone app economy."
    },
    {
        "clue1": "I reached 100 million active users in just 60 days, breaking all software growth records.",
        "clue2": "I was developed in San Francisco by an AI research laboratory led by Sam Altman.",
        "clue3": "The last three letters of my name stand for 'Generative Pre-trained Transformer'.",
        "ansText": "ChatGPT",
        "expl": "ChatGPT democratized conversational generative AI and large language models worldwide."
    },
    {
        "clue1": "I was introduced in 2008 in a cryptography whitepaper by Satoshi Nakamoto.",
        "clue2": "My protocol has an absolute mathematical hard cap of 21 million total units.",
        "clue3": "I am recognized as the original decentralized cryptocurrency secured by proof-of-work.",
        "ansText": "Bitcoin",
        "expl": "Bitcoin established peer-to-peer electronic cash without central banks or intermediaries."
    },
    {
        "clue1": "I am represented by a friendly blue whale carrying stacked shipping containers.",
        "clue2": "I solved the famous developer complaint: 'It works on my local machine, but breaks on the server!'",
        "clue3": "I standardized software containerization and runtime image packaging across the cloud.",
        "ansText": "Docker",
        "expl": "Solomon Hykes launched Docker, isolating application binaries and dependencies cleanly."
    },
    {
        "clue1": "I was founded in 2004 in a Harvard dorm room under the domain 'TheFacebook.com'.",
        "clue2": "I later acquired Instagram, WhatsApp, and VR company Oculus into my portfolio.",
        "clue3": "My parent holding company officially rebranded in 2021 as 'Meta'.",
        "ansText": "Facebook (Meta)",
        "expl": "Mark Zuckerberg's social networking platform connects over 3 billion monthly active users."
    },
    {
        "clue1": "I was conceived in the 1970s at IBM Research under the initial project name 'SEQUEL'.",
        "clue2": "My core operations revolve around four keywords: SELECT, INSERT, UPDATE, and DELETE.",
        "clue3": "I am the standard language powering relational database queries for half a century.",
        "ansText": "SQL (Structured Query Language)",
        "expl": "SQL remains the timeless universal query dialect for databases and data pipelines."
    },
    {
        "clue1": "I spent my early decades engineering specialized graphics chips for PC 3D video gamers.",
        "clue2": "When the Generative AI boom arrived, my Tensor Core chips became mandatory infrastructure.",
        "clue3": "My CEO Jensen Huang famously delivers product keynotes wearing a black leather jacket.",
        "ansText": "NVIDIA",
        "expl": "NVIDIA pioneered GPU accelerated computing and powers modern AI model training."
    },
    {
        "clue1": "I am named after 10th-century King Harald of Denmark who united Scandinavian tribes.",
        "clue2": "Just like the king, I unite gadgets over short-range radio signals without wires.",
        "clue3": "My blue logo combines two ancient Nordic runes: Hagall (H) and Bjarkan (B).",
        "ansText": "Bluetooth",
        "expl": "Bluetooth was standardized for short-range personal area device networking."
    },
    {
        "clue1": "My official operating system mascot is an amicable, chubby penguin named Tux.",
        "clue2": "Over 90% of the world's public cloud servers, supercomputers, and Android phones run on my kernel.",
        "clue3": "I am the most successful open-source operating system project in history.",
        "ansText": "Linux",
        "expl": "Linus Torvalds released the Linux kernel in 1991, reshaping enterprise computing."
    },
    {
        "clue1": "I was founded in San Francisco in 2009 under the initial name 'UberCab'.",
        "clue2": "Without owning a single vehicle fleet, I became the largest ride-hailing company on Earth.",
        "clue3": "My primary Indian rival in the mobility sector is Ola.",
        "ansText": "Uber",
        "expl": "Travis Kalanick and Garrett Camp pioneered algorithmic ride dispatching via GPS smartphones."
    },
    {
        "clue1": "When Microsoft released me in 1985, critics dismissed me as a simple bookkeeping grid.",
        "clue2": "Today, even multinational banks run a massive percentage of their financial logic on me.",
        "clue3": "VLOOKUP, Pivot Tables, and a recognizable emerald green icon are my signatures.",
        "ansText": "Microsoft Excel",
        "expl": "Excel remains the world's most enduring and widely used computational spreadsheet software."
    },
    {
        "clue1": "I was founded by Andy Rubin in 2003 and acquired by Google in 2005.",
        "clue2": "My legacy versions were named after treats like Cupcake, KitKat, and Oreo.",
        "clue3": "Today, I power over 70% of all smartphones globally symbolized by a green robot.",
        "ansText": "Android OS",
        "expl": "Android is Google's open-source mobile platform dominating global smartphone usage."
    },
    {
        "clue1": "I was invented in 1989 at CERN in Switzerland by British scientist Sir Tim Berners-Lee.",
        "clue2": "I linked research documents across computer networks using hyperlinked HTML pages.",
        "clue3": "Almost every legacy website address in the world opened with three repeated letters: 'WWW'.",
        "ansText": "World Wide Web (WWW)",
        "expl": "Tim Berners-Lee released the Web royalty-free, igniting the modern digital information age."
    },
    {
        "clue1": "I disrupted the music industry by offering legal streaming access for a flat monthly fee.",
        "clue2": "I was founded in Stockholm, Sweden in 2006 by Daniel Ek and Martin Lorentzon.",
        "clue3": "My brand is recognized by three curved soundwaves inside a vibrant lime green circle.",
        "ansText": "Spotify",
        "expl": "Spotify revolutionized global music streaming economics and personalized audio playlists."
    }
]

rounds.append({
    "id": 4,
    "name": "Round 4: Tech Detective (Who Am I?)",
    "type": "detective",
    "description": "3 Progressive Clues (300/200/100 Pts) • Buzz Early to Win • 20 Questions",
    "questions": r4_items
})

# ==================== ROUND 5: 10 FUTURE OR FIRED DEBATES ====================
# Exactly 10 questions as requested!
r5_items = [
    {
        "topic": "AI coding assistants (Claude, Copilot) will eliminate 70% of entry-level developer roles within 5 years.",
        "reality": "FIRED ❌ (Evolution, Not Extinction)",
        "expl": "AI automates boilerplate code, but complex system design, security, and domain problem-solving require human engineers."
    },
    {
        "topic": "In the future, nobody will need to write code because No-Code drag-and-drop tools will build all enterprise apps.",
        "reality": "FIRED ❌ (Partial Myth)",
        "expl": "No-Code handles simple marketing websites; custom enterprise logic, scalability, and algorithmic security always demand code."
    },
    {
        "topic": "With high-speed 5G and fiber cloud, local PC hard drives will disappear in favor of 100% Cloud PCs.",
        "reality": "FUTURE ✅ (Accelerating Reality)",
        "expl": "Services like Windows 365 and Shadow PC prove dumb terminals with cloud virtualization are cost-effective and secure."
    },
    {
        "topic": "Browsing in 'Incognito Mode' guarantees absolute anonymity from internet service providers and network monitors.",
        "reality": "FIRED ❌ (Dangerous Myth)",
        "expl": "Incognito only discards local device history; upstream ISPs, corporate routers, and government authorities still log traffic."
    },
    {
        "topic": "Because of its beginner-friendly syntax, Python will completely replace languages like Java, C++, and JavaScript.",
        "reality": "FIRED ❌ (Impossible)",
        "expl": "Browsers strictly execute JavaScript; high-performance game engines require C++/Rust. Python's interpreted runtime is too slow."
    },
    {
        "topic": "A university degree is no longer necessary to land top software engineering careers; GitHub portfolios and skill suffice.",
        "reality": "FUTURE ✅ (Validated Trend)",
        "expl": "Silicon Valley giants and startups have dropped strict degree mandates in favor of verified open-source and coding competence."
    },
    {
        "topic": "Brain-computer interfaces like Neuralink will allow humans to type and interact with computers using thought alone.",
        "reality": "FUTURE ✅ (Clinical Reality)",
        "expl": "Paralyzed human trial participants have already successfully controlled computer cursors and played chess using neural implants."
    },
    {
        "topic": "Traditional passwords will be entirely obsolete within 5 years, replaced by biometric Passkeys.",
        "reality": "FUTURE ✅ (Standard Rollout)",
        "expl": "The FIDO alliance (Google, Apple, Microsoft) is actively phasing out master passwords in favor of cryptographic device passkeys."
    },
    {
        "topic": "People will stop clicking 10 blue search links on Google, turning exclusively to direct conversational AI answers.",
        "reality": "FUTURE ✅ (Major Paradigm Shift)",
        "expl": "Perplexity and ChatGPT Search showcase that users prefer concise verified synthesis over wading through ad-bloated links."
    },
    {
        "topic": "AI software developers will soon produce 100% bug-free software that never crashes.",
        "reality": "FIRED ❌ (Philosophical Myth)",
        "expl": "Software requirements change constantly; edge cases, runtime anomalies, and shifting user expectations ensure bugs always exist."
    }
]

rounds.append({
    "id": 5,
    "name": "Round 5: Future or Fired? (4-Team Debate)",
    "type": "debate",
    "description": "4-Team Battle • 60-Second Timed Speeches • Industry Reality Verdict • 10 Questions",
    "questions": r5_items
})

# ==================== ROUND 6: 20 THE TECH MILLIONAIRE ====================
# Balanced A/B/C/D (5 each). Uniform option lengths (~20-35 chars each). No loophole!
r6_items = [
    {
        "q": "Why does Netflix stream HD video smoothly in India without lag, even though original servers are in the USA?",
        "options": ["Direct satellite dishes", "CDN edge server caches", "Chrome web accelerator", "Wi-Fi router boosters"],
        "ans": 1,
        "ansText": "CDN edge server caches",
        "expl": "Netflix pre-caches video streams onto local ISP network appliances closer to viewers."
    },
    {
        "q": "Which memory level inside a computer delivers the absolute lowest access latency?",
        "options": ["CPU L1 hardware cache", "High-speed DDR5 RAM", "Fast PCIe NVMe drive", "External flash drive"],
        "ans": 0,
        "ansText": "CPU L1 hardware cache",
        "expl": "CPU SRAM cache sits directly on the processor die with sub-nanosecond clock cycle latency."
    },
    {
        "q": "Why do mobile banking OTP verification codes automatically expire after 5 or 10 minutes?",
        "options": ["SIM card powers down", "SMS storage gets full", "Time-To-Live replay fix", "Telecom regulation rule"],
        "ans": 2,
        "ansText": "Time-To-Live replay fix",
        "expl": "Strict expiration windows prevent attackers from intercepting and re-using captured tokens."
    },
    {
        "q": "What is the technical term when an AI chatbot invents fake historical facts with high confidence?",
        "options": ["Runtime segmentation fault", "Operating system kernel panic", "Browser script memory leak", "Artificial intelligence hallucination"],
        "ans": 3,
        "ansText": "Artificial intelligence hallucination",
        "expl": "LLMs predict the most statistically probable token without an inherent grounded factual truth database."
    },
    {
        "q": "Why does a brand new 1,000 GB external drive show only ~931 GB in Windows Explorer?",
        "options": ["Decimal vs Binary units", "Operating system file tax", "Defective factory sectors", "Hidden backup partition"],
        "ans": 0,
        "ansText": "Decimal vs Binary units",
        "expl": "Hardware makers define 1 GB = 1000^3 bytes, while Windows counts in binary 1024^3 bytes."
    },
    {
        "q": "What benchmark unit measures the operational computation speed of global supercomputers?",
        "options": ["Megahertz Clock Rate", "Floating Point FLOPS", "Gigabytes Per Second", "Revolutions Per Minute"],
        "ans": 1,
        "ansText": "Floating Point FLOPS",
        "expl": "Supercomputers are measured by how many quintillion floating-point calculations they solve per second."
    },
    {
        "q": "When millions order food at midnight on New Year's Eve, what cloud architecture prevents server crash?",
        "options": ["Higher internet bandwidth", "Manual developer overtime", "Auto-scaling load balancer", "Local database backup copies"],
        "ans": 2,
        "ansText": "Auto-scaling load balancer",
        "expl": "Auto-scaling automatically adds server instances dynamically as incoming traffic surges."
    },
    {
        "q": "What cyber attack floods a server with coordinated traffic from thousands of infected botnet devices?",
        "options": ["Social engineering phishing", "Encrypted ransomware hold", "Silent keystroke logger spy", "Distributed denial of service"],
        "ans": 3,
        "ansText": "Distributed denial of service",
        "expl": "DDoS attacks exhaust network bandwidth and connection queues, blocking legitimate users."
    },
    {
        "q": "If you delete a critical tracked file in a Git project, what command restores it from HEAD?",
        "options": ["git restore <filename>", "git revert master branch", "git delete undo file", "git checkout root origin"],
        "ans": 0,
        "ansText": "git restore <filename>",
        "expl": "'git restore' discards local working directory modifications and recovers the clean file from index."
    },
    {
        "q": "Why were keyboard keys arranged in the scrambled 'QWERTY' layout instead of ABCDEF order?",
        "options": ["Military cryptographic code", "Preventing mechanical key jams", "Latin language typing rules", "Accidental manufacturing typo"],
        "ans": 1,
        "ansText": "Preventing mechanical key jams",
        "expl": "Christopher Sholes separated frequently co-occurring letters so mechanical typewriter arms wouldn't jam."
    },
    {
        "q": "How does Google Maps determine live traffic congestion and color road segments red or green?",
        "options": ["Traffic police radios", "Overhead drone cameras", "Crowdsourced mobile GPS", "Highway toll radar beams"],
        "ans": 2,
        "ansText": "Crowdsourced mobile GPS",
        "expl": "Active smartphones send anonymous velocity updates; when phones slow down, routes turn red."
    },
    {
        "q": "What is the official expanded technical acronym of the word 'Wi-Fi'?",
        "options": ["Wireless Fiber Link", "Wide Frequency Internet", "Wired Interface File", "Catchy rhyme (Not an acronym)"],
        "ans": 3,
        "ansText": "Catchy rhyme (Not an acronym)",
        "expl": "The Wi-Fi Alliance hired a marketing agency to coin a consumer name for IEEE 802.11b."
    },
    {
        "q": "Why did Microsoft submerge an entire data center capsule onto the ocean floor in Scotland?",
        "options": ["Seawater cooling efficiency", "Hiding from government taxes", "Providing Wi-Fi to submarines", "Avoiding earthquakes on land"],
        "ans": 0,
        "ansText": "Seawater cooling efficiency",
        "expl": "Project Natick proved underwater servers benefit from natural free chilling and low failure rates."
    },
    {
        "q": "Which NASA computer scientist wrote the asynchronous software that saved Apollo 11's moon landing?",
        "options": ["Marie Curie Physicist", "Margaret Hamilton Engineer", "Ada Lovelace Mathematician", "Katherine Johnson Pioneer"],
        "ans": 1,
        "ansText": "Margaret Hamilton Engineer",
        "expl": "Her priority scheduling dropped radar overload tasks, allowing the computer to focus on descent engines."
    },
    {
        "q": "What was the very first commercial '.com' domain name registered in internet history in 1985?",
        "options": ["Apple.com computer", "Microsoft.com software", "Symbolics.com system", "Google.com search engine"],
        "ans": 2,
        "ansText": "Symbolics.com system",
        "expl": "Symbolics.com was registered on March 15, 1985, by a computer manufacturer in Massachusetts."
    },
    {
        "q": "What was the title of the very first video ever uploaded to YouTube in April 2005?",
        "options": ["Hello World Coding", "My First Video Post", "Google Campus Tour", "Me at the zoo video"],
        "ans": 3,
        "ansText": "Me at the zoo video",
        "expl": "Co-founder Jawed Karim uploaded an 19-second video standing in front of elephants at the zoo."
    },
    {
        "q": "What does a 'Reverse Proxy' like Nginx do in front of an enterprise web application?",
        "options": ["Protects and balances backend", "Generates user passwords", "Formats hard drive partitions", "Increases monitor refresh rate"],
        "ans": 0,
        "ansText": "Protects and balances backend",
        "expl": "Reverse proxies handle SSL termination, caching, and distribute incoming traffic to backend nodes."
    },
    {
        "q": "Why do products you view on Amazon follow you as advertisements on Instagram and news sites?",
        "options": ["Phone microphone listening", "Ad-network tracking cookies", "Instagram owns all retailers", "Pure algorithmic coincidence"],
        "ans": 1,
        "ansText": "Ad-network tracking cookies",
        "expl": "Ad networks use third-party tracking cookies and device fingerprinting to target cross-site ads."
    },
    {
        "q": "Which data structure provides constant O(1) average lookup time for key-value pairs?",
        "options": ["Singly Linked List", "Binary Search Tree", "Hash Table Key Map", "Sorted Array Sequence"],
        "ans": 2,
        "ansText": "Hash Table Key Map",
        "expl": "Hash tables compute a bucket index directly from the key hash, giving instantaneous O(1) lookup."
    },
    {
        "q": "In machine learning, what happens when a model performs 100% on training data but fails on real users?",
        "options": ["Model Underfitting Error", "Data Normalization Shift", "Zero Gradient Vanish", "Model Overfitting Defect"],
        "ans": 3,
        "ansText": "Model Overfitting Defect",
        "expl": "Overfitting occurs when a neural model memorizes noise instead of learning generalizable patterns."
    }
]

rounds.append({
    "id": 6,
    "name": "Round 6: The Tech Millionaire",
    "type": "millionaire",
    "description": "High Stakes • Balanced A/B/C/D • No Length Clues • 20 Questions",
    "questions": r6_items
})

# ==================== ROUND 7: 20 RAPID FIRE CLASH ====================
# Fast, snappy, balanced!
r7_items = [
    {
        "q": "What does the 'C' stand for in the popular CPU acronym?",
        "options": ["Central", "Circuit", "Control", "Compute"],
        "ans": 0,
        "ansText": "Central",
        "expl": "CPU stands for Central Processing Unit."
    },
    {
        "q": "Which standard internet port does unencrypted HTTP use by default?",
        "options": ["Port 443", "Port 80", "Port 21", "Port 22"],
        "ans": 1,
        "ansText": "Port 80",
        "expl": "HTTP runs on port 80; HTTPS runs on port 443."
    },
    {
        "q": "Which company originally created the Android mobile operating system before Google acquired it?",
        "options": ["Apple Inc", "Microsoft", "Android Inc", "Samsung Co"],
        "ans": 2,
        "ansText": "Android Inc",
        "expl": "Andy Rubin founded Android Inc in 2003, acquired by Google in 2005."
    },
    {
        "q": "What is the standard networking loopback IP address representing 'localhost'?",
        "options": ["192.168.1.1", "10.0.0.1", "0.0.0.0", "127.0.0.1"],
        "ans": 3,
        "ansText": "127.0.0.1",
        "expl": "127.0.0.1 is the standard loopback IP address assigned to localhost."
    },
    {
        "q": "Which binary logic gate outputs True (1) only when BOTH inputs are True (1)?",
        "options": ["AND Gate", "OR Gate", "XOR Gate", "NOT Gate"],
        "ans": 0,
        "ansText": "AND Gate",
        "expl": "AND logic requires all inputs to be high (1) to produce a high output."
    },
    {
        "q": "What does the 'S' stand for in the secure protocol HTTPS?",
        "options": ["System", "Secure", "Socket", "Server"],
        "ans": 1,
        "ansText": "Secure",
        "expl": "HTTPS stands for HyperText Transfer Protocol Secure."
    },
    {
        "q": "Which programming language was created by Sun Microsystems under the motto 'Write Once, Run Anywhere'?",
        "options": ["Python", "C++", "Java", "Ruby"],
        "ans": 2,
        "ansText": "Java",
        "expl": "Java compiles to bytecode running on any Java Virtual Machine (JVM)."
    },
    {
        "q": "What is the primary volatile memory storage used by the CPU to store running process data?",
        "options": ["Hard Drive", "CD-ROM", "USB Drive", "RAM Memory"],
        "ans": 3,
        "ansText": "RAM Memory",
        "expl": "RAM (Random Access Memory) provides high-speed volatile workspace for active programs."
    },
    {
        "q": "What is the smallest unit of digital data in computer science, representing a 0 or 1?",
        "options": ["Bit", "Byte", "Nibble", "Pixel"],
        "ans": 0,
        "ansText": "Bit",
        "expl": "A bit (binary digit) is the fundamental atomic unit of digital computation."
    },
    {
        "q": "Which open-source relational database management system features a dolphin named Sakila in its logo?",
        "options": ["Oracle DB", "MySQL", "SQLite", "MongoDB"],
        "ans": 1,
        "ansText": "MySQL",
        "expl": "MySQL is the widely used open-source relational database represented by a dolphin mascot."
    },
    {
        "q": "What software layer serves as the intermediary between hardware silicon and user application software?",
        "options": ["Web Browser", "Text Editor", "Operating System", "Antivirus Tool"],
        "ans": 2,
        "ansText": "Operating System",
        "expl": "The OS manages hardware abstraction, CPU scheduling, memory, and file systems."
    },
    {
        "q": "In Git version control, which command creates and switches to a brand new isolated branch in one step?",
        "options": ["git branch new", "git merge branch", "git commit branch", "git checkout -b"],
        "ans": 3,
        "ansText": "git checkout -b",
        "expl": "'git checkout -b <name>' or 'git switch -c <name>' creates and checks out the branch."
    },
    {
        "q": "Which standard format is universally used for styling and designing visual presentation on web pages?",
        "options": ["CSS Stylesheet", "JSON Payload", "SQL Query", "C++ Binary"],
        "ans": 0,
        "ansText": "CSS Stylesheet",
        "expl": "Cascading Style Sheets (CSS) controls typography, layouts, colors, and responsive design."
    },
    {
        "q": "What hardware device routes data packets between different computer networks and connects to the internet?",
        "options": ["Sound Card", "Network Router", "Graphics Card", "Power Supply"],
        "ans": 1,
        "ansText": "Network Router",
        "expl": "Routers forward data packets across network boundaries using IP routing tables."
    },
    {
        "q": "What does the popular web programming acronym 'DOM' stand for?",
        "options": ["Data Online Model", "Direct Object Mode", "Document Object Model", "Disk Operating Module"],
        "ans": 2,
        "ansText": "Document Object Model",
        "expl": "The DOM is the programming API representation of HTML document trees in browsers."
    },
    {
        "q": "Which non-volatile solid-state storage technology replaced spinning mechanical magnetic hard disk drives?",
        "options": ["Floppy Disk Drive", "Magnetic Tape Reel", "Optical Laser Disc", "Solid State Drive"],
        "ans": 3,
        "ansText": "Solid State Drive",
        "expl": "SSDs use flash memory with zero moving parts, providing vastly superior I/O speeds."
    },
    {
        "q": "What is the common term for malicious software designed to disrupt, damage, or gain unauthorized access?",
        "options": ["Malware", "Firmware", "Shareware", "Middleware"],
        "ans": 0,
        "ansText": "Malware",
        "expl": "Malware (malicious software) encompasses viruses, ransomware, trojans, and worms."
    },
    {
        "q": "Which cryptographic protocol replaced the insecure Telnet protocol for remote terminal server access?",
        "options": ["FTP Protocol", "SSH Protocol", "SMTP Protocol", "SNMP Protocol"],
        "ans": 1,
        "ansText": "SSH Protocol",
        "expl": "SSH (Secure Shell) encrypts command-line sessions and file transfers across networks."
    },
    {
        "q": "In Python, which built-in data type is immutable and defined using round parentheses ()?",
        "options": ["List array", "Dictionary map", "Tuple sequence", "Set collection"],
        "ans": 2,
        "ansText": "Tuple sequence",
        "expl": "Tuples are ordered, immutable sequences defined using parentheses in Python."
    },
    {
        "q": "Which cloud computing model provides virtualized servers, storage, and networking over the internet?",
        "options": ["SaaS Software", "PaaS Platform", "BaaS Backend", "IaaS Infrastructure"],
        "ans": 3,
        "ansText": "IaaS Infrastructure",
        "expl": "IaaS (Infrastructure as a Service) provides raw compute instances, storage, and networking."
    }
]

rounds.append({
    "id": 7,
    "name": "Round 7: Rapid Fire Clash",
    "type": "rapid",
    "description": "5-Second Buzzes • Fast Elimination • High-Speed Clashes • 20 Questions",
    "questions": r7_items
})

output_path = "D:/WEGROW/14.Game/public/questions.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(rounds, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(rounds)} tournament rounds in {output_path}!")
for r in rounds:
    print(f"- {r['name']}: {len(r['questions'])} questions (type: {r['type']})")
