import json

rounds = [
    {
        "id": 1,
        "name": "Round 1: The Price is Right (Guess the Retail Price)",
        "type": "mcq",
        "description": "Guess the Real Indian MRP/Retail Price • 4 Close Options • 25 Questions",
        "questions": [
            {
                "q": "What is the retail price of a Starbucks Caffe Latte (Tall size, 354ml) in an Indian Metro outlet?",
                "options": ["₹185", "₹285", "₹395", "₹480"],
                "ans": 1,
                "ansText": "₹285",
                "expl": "Starbucks India charges ₹285 (plus taxes) for a classic Tall Caffe Latte."
            },
            {
                "q": "What was the official launch price of the Apple iPhone 16 (Base 128GB model) in India?",
                "options": ["₹69,900", "₹79,900", "₹89,900", "₹99,900"],
                "ans": 1,
                "ansText": "₹79,900",
                "expl": "Apple officially launched the base iPhone 16 128GB at ₹79,900 in India."
            },
            {
                "q": "What is the official annual cost for a 1-Year Amazon Prime subscription in India?",
                "options": ["₹1,499", "₹999", "₹1,999", "₹2,499"],
                "ans": 0,
                "ansText": "₹1,499",
                "expl": "Amazon Prime annual membership in India is standard at ₹1,499/year."
            },
            {
                "q": "What is the typical price of a Large Salted Tub Popcorn at a PVR Cinemas weekend multiplex?",
                "options": ["₹190", "₹250", "₹380", "₹490"],
                "ans": 3,
                "ansText": "₹490",
                "expl": "Multiplex large popcorn tubs range between ₹450 and ₹490 at weekend PVR counters."
            },
            {
                "q": "What is the monthly subscription price of the Netflix Standard HD Plan (2 screens) in India?",
                "options": ["₹199", "₹349", "₹499", "₹799"],
                "ans": 2,
                "ansText": "₹499",
                "expl": "Netflix Standard 1080p two-screen plan costs ₹499 per month in India."
            },
            {
                "q": "What is the counter price of a single McDonald's McAloo Tikki Burger in India?",
                "options": ["₹35", "₹59", "₹89", "₹110"],
                "ans": 1,
                "ansText": "₹59",
                "expl": "The standalone McAloo Tikki burger is priced at ₹59 (plus taxes) across Indian outlets."
            },
            {
                "q": "What is the official retail price of the iconic Nike Air Force 1 '07 Classic White sneakers in India?",
                "options": ["₹4,495", "₹7,495", "₹9,695", "₹12,995"],
                "ans": 2,
                "ansText": "₹9,695",
                "expl": "Nike India retails the classic Air Force 1 '07 Triple White at ₹9,695."
            },
            {
                "q": "What is the price of 1 Tub (450ml) of Baskin Robbins Belgian Chocolate Ice Cream?",
                "options": ["₹220", "₹340", "₹425", "₹599"],
                "ans": 2,
                "ansText": "₹425",
                "expl": "A 450ml pre-packed Baskin Robbins gourmet tub costs ₹425."
            },
            {
                "q": "What was the launch price of Apple AirPods Pro (2nd Generation with USB-C) in India?",
                "options": ["₹18,900", "₹24,900", "₹29,900", "₹34,900"],
                "ans": 1,
                "ansText": "₹24,900",
                "expl": "AirPods Pro (2nd Gen) with MagSafe Case USB-C officially retailed at ₹24,900."
            },
            {
                "q": "What is the menu price of a Domino's Regular Farmhouse Pizza (Single pizza)?",
                "options": ["₹149", "₹389", "₹499", "₹259"],
                "ans": 3,
                "ansText": "₹259",
                "expl": "A regular size Domino's Farmhouse pizza is priced at ₹259."
            },
            {
                "q": "What is the annual individual membership cost for YouTube Premium in India?",
                "options": ["₹1,490", "₹890", "₹1,290", "₹1,890"],
                "ans": 0,
                "ansText": "₹1,490",
                "expl": "YouTube Premium individual annual prepaid plan in India is ₹1,490."
            },
            {
                "q": "What is the retail price of an Amul Butter 500g slab at Indian supermarkets?",
                "options": ["₹195", "₹235", "₹285", "₹320"],
                "ans": 2,
                "ansText": "₹285",
                "expl": "A 500g slab of Amul Pasteurised Butter currently retails at ₹285 MRP."
            },
            {
                "q": "What is the official Indian price for a Dyson Supersonic Hair Dryer?",
                "options": ["₹19,900", "₹28,900", "₹37,900", "₹45,900"],
                "ans": 2,
                "ansText": "₹37,900",
                "expl": "Dyson India retails the Supersonic Hair Dryer at ₹37,900."
            },
            {
                "q": "What is the standard price of a Zara Men’s Classic Oxford Cotton Shirt in India?",
                "options": ["₹1,290", "₹1,990", "₹4,590", "₹2,990"],
                "ans": 3,
                "ansText": "₹2,990",
                "expl": "Classic Oxford cotton shirts at Zara India retail at ₹2,990."
            },
            {
                "q": "What is the counter price of a KFC 8-Piece Hot & Crispy Chicken Bucket in India?",
                "options": ["₹449", "₹599", "₹749", "₹899"],
                "ans": 2,
                "ansText": "₹749",
                "expl": "The KFC 8-piece signature Hot & Crispy chicken bucket is priced around ₹749."
            },
            {
                "q": "What is the official retail price of a classic pair of Crocs Classic Clogs in India?",
                "options": ["₹1,495", "₹2,495", "₹5,495", "₹3,995"],
                "ans": 3,
                "ansText": "₹3,995",
                "expl": "The adult Crocs Classic Clog retails officially at ₹3,995 in India."
            },
            {
                "q": "What is the MRP of a Ferrero Rocher 16-Pieces Chocolate gift box in India?",
                "options": ["₹350", "₹549", "₹695", "₹850"],
                "ans": 1,
                "ansText": "₹549",
                "expl": "A 16-piece (200g) Ferrero Rocher box carries an MRP of ₹549."
            },
            {
                "q": "What is the price of Ray-Ban Classic Aviator Sunglasses (Gold frame, G-15 green lens)?",
                "options": ["₹8,990", "₹4,290", "₹6,590", "₹11,990"],
                "ans": 0,
                "ansText": "₹8,990",
                "expl": "Original Ray-Ban Aviator RB3025 sunglasses retail at ₹8,990 in India."
            },
            {
                "q": "What is the standard price of a Fastrack Casual Analog Watch for Men/Women in India?",
                "options": ["₹895", "₹1,695", "₹2,995", "₹4,495"],
                "ans": 1,
                "ansText": "₹1,695",
                "expl": "Popular entry-level Fastrack analog watches retail around ₹1,695."
            },
            {
                "q": "What is the MRP of 1 Can of Red Bull Energy Drink (250ml) in India?",
                "options": ["₹65", "₹90", "₹125", "₹160"],
                "ans": 2,
                "ansText": "₹125",
                "expl": "A 250ml can of Red Bull retails at ₹125 MRP across India."
            },
            {
                "q": "What is the standard price of a Cult.fit 12-Month Elite All-Access Gym Pass?",
                "options": ["₹8,990", "₹14,990", "₹19,990", "₹24,990"],
                "ans": 1,
                "ansText": "₹14,990",
                "expl": "The standard promotional rate for Cultpass Elite 12-Month pass is ₹14,990."
            },
            {
                "q": "What is the price of an Amazon Kindle Paperwhite (16GB, 6.8-inch display) in India?",
                "options": ["₹9,999", "₹14,999", "₹18,999", "₹22,999"],
                "ans": 1,
                "ansText": "₹14,999",
                "expl": "The 16GB Kindle Paperwhite with adjustable warm light is ₹14,999."
            },
            {
                "q": "What is the price of a 1 Litre bottle of imported Evian Natural Spring Mineral Water in India?",
                "options": ["₹75", "₹140", "₹240", "₹450"],
                "ans": 2,
                "ansText": "₹240",
                "expl": "Imported French Evian 1L bottled water retails at ₹240 in India."
            },
            {
                "q": "What is the retail price of a single pack of Maggi 2-Minute Noodles (70g pack)?",
                "options": ["₹10", "₹14", "₹18", "₹22"],
                "ans": 1,
                "ansText": "₹14",
                "expl": "A single standard 70g pack of Maggi Masala noodles is ₹14."
            },
            {
                "q": "What is the regular price for a Swiggy One 3-Month Membership in India?",
                "options": ["₹149", "₹299", "₹499", "₹899"],
                "ans": 1,
                "ansText": "₹299",
                "expl": "Swiggy One 3-month subscription plan has a standard price of ₹299."
            }
        ]
    },
    {
        "id": 2,
        "name": "Round 2: Spot the Global MNC Imposter",
        "type": "imposter",
        "description": "Find the Corporate / Product DNA Outlier • 4 Global Brands • 25 Questions",
        "questions": [
            {
                "items": ["KitKat", "Maggi", "Nescafe", "Oreo"],
                "ans": 3,
                "ansText": "Oreo",
                "expl": "Oreo is owned by Mondelez; KitKat, Maggi, and Nescafe are all owned by Nestlé!"
            },
            {
                "items": ["Sprite", "Fanta", "Thums Up", "7UP"],
                "ans": 3,
                "ansText": "7UP",
                "expl": "7UP is manufactured by PepsiCo; Sprite, Fanta, and Thums Up belong to Coca-Cola!"
            },
            {
                "items": ["Rolls-Royce", "Mini Cooper", "BMW", "Bentley"],
                "ans": 3,
                "ansText": "Bentley",
                "expl": "Bentley belongs to Volkswagen Group; Rolls-Royce and Mini Cooper belong to BMW Group!"
            },
            {
                "items": ["Mountain Dew", "Mirinda", "Doritos", "Limca"],
                "ans": 3,
                "ansText": "Limca",
                "expl": "Limca belongs to Coca-Cola; Mountain Dew, Mirinda, and Doritos are PepsiCo brands!"
            },
            {
                "items": ["Instagram", "WhatsApp", "Oculus VR", "Snapchat"],
                "ans": 3,
                "ansText": "Snapchat",
                "expl": "Snapchat is owned by Snap Inc.; the other three are subsidiaries of Meta Platforms!"
            },
            {
                "items": ["Gucci", "Saint Laurent", "Balenciaga", "Louis Vuitton"],
                "ans": 3,
                "ansText": "Louis Vuitton",
                "expl": "Louis Vuitton belongs to LVMH; Gucci, Saint Laurent, and Balenciaga belong to Kering!"
            },
            {
                "items": ["Zara", "Massimo Dutti", "Bershka", "H&M"],
                "ans": 3,
                "ansText": "H&M",
                "expl": "H&M is an independent Swedish group; Zara, Massimo Dutti, and Bershka belong to Inditex!"
            },
            {
                "items": ["YouTube", "Waze GPS", "Fitbit", "Spotify"],
                "ans": 3,
                "ansText": "Spotify",
                "expl": "Spotify is an independent Swedish company; YouTube, Waze, and Fitbit are owned by Google!"
            },
            {
                "items": ["Dove", "Lifebuoy", "Pears", "Head & Shoulders"],
                "ans": 3,
                "ansText": "Head & Shoulders",
                "expl": "Head & Shoulders belongs to P&G; Dove, Lifebuoy, and Pears belong to Unilever!"
            },
            {
                "items": ["Pantene", "Gillette", "Oral-B", "Nivea"],
                "ans": 3,
                "ansText": "Nivea",
                "expl": "Nivea is owned by Beiersdorf; Pantene, Gillette, and Oral-B belong to P&G!"
            },
            {
                "items": ["Tinder", "Hinge", "OkCupid", "Bumble"],
                "ans": 3,
                "ansText": "Bumble",
                "expl": "Bumble is independent; Tinder, Hinge, and OkCupid are all owned by Match Group!"
            },
            {
                "items": ["Lamborghini", "Porsche", "Bugatti", "Ferrari"],
                "ans": 3,
                "ansText": "Ferrari",
                "expl": "Ferrari is an independent public company; the others share Volkswagen Group ownership!"
            },
            {
                "items": ["Lay's", "Cheetos", "Quaker Oats", "Pringles"],
                "ans": 3,
                "ansText": "Pringles",
                "expl": "Pringles is owned by Kellanova; Lay's, Cheetos, and Quaker Oats are PepsiCo brands!"
            },
            {
                "items": ["Ray-Ban", "Oakley", "Persol", "Titan"],
                "ans": 3,
                "ansText": "Titan",
                "expl": "Titan is Indian/Tata; Ray-Ban, Oakley, and Persol are luxury brands of EssilorLuxottica!"
            },
            {
                "items": ["Pizza Hut", "KFC", "Taco Bell", "Subway"],
                "ans": 3,
                "ansText": "Subway",
                "expl": "Subway is owned by Roark Capital; Pizza Hut, KFC, and Taco Bell are Yum! Brands!"
            },
            {
                "items": ["PlayStation", "Columbia Pictures", "Sony Music", "Xbox"],
                "ans": 3,
                "ansText": "Xbox",
                "expl": "Xbox is owned by Microsoft; the other three are divisions of Sony Group!"
            },
            {
                "items": ["Toblerone", "Milka", "Cadbury", "Snickers"],
                "ans": 3,
                "ansText": "Snickers",
                "expl": "Snickers is made by Mars Inc.; Toblerone, Milka, and Cadbury belong to Mondelez!"
            },
            {
                "items": ["Marvel Studios", "Pixar", "Lucasfilm", "Warner Bros"],
                "ans": 3,
                "ansText": "Warner Bros",
                "expl": "Warner Bros is Warner Bros. Discovery; Marvel, Pixar, and Lucasfilm belong to Disney!"
            },
            {
                "items": ["LinkedIn", "GitHub", "Skype", "Slack"],
                "ans": 3,
                "ansText": "Slack",
                "expl": "Slack was acquired by Salesforce; LinkedIn, GitHub, and Skype belong to Microsoft!"
            },
            {
                "items": ["Sephora", "Dior", "Fendi", "L'Oreal"],
                "ans": 3,
                "ansText": "L'Oreal",
                "expl": "L'Oreal is an independent French group; Sephora, Dior, and Fendi belong to LVMH!"
            },
            {
                "items": ["Uber", "Uber Eats", "Careem", "Swiggy"],
                "ans": 3,
                "ansText": "Swiggy",
                "expl": "Swiggy is an Indian independent company; the others are Uber Technologies brands!"
            },
            {
                "items": ["Colgate", "Palmolive", "Speed Stick", "Dettol"],
                "ans": 3,
                "ansText": "Dettol",
                "expl": "Dettol is made by Reckitt; Colgate, Palmolive, and Speed Stick belong to Colgate-Palmolive!"
            },
            {
                "items": ["Jaguar", "Land Rover", "Tetley Tea", "Royal Enfield"],
                "ans": 3,
                "ansText": "Royal Enfield",
                "expl": "Royal Enfield belongs to Eicher Motors; Jaguar, Land Rover, and Tetley belong to Tata Group!"
            },
            {
                "items": ["Ariel", "Tide", "Downy", "Surf Excel"],
                "ans": 3,
                "ansText": "Surf Excel",
                "expl": "Surf Excel belongs to Unilever; Ariel, Tide, and Downy are P&G laundry brands!"
            },
            {
                "items": ["Cartier", "Montblanc", "Van Cleef & Arpels", "Rolex"],
                "ans": 3,
                "ansText": "Rolex",
                "expl": "Rolex is an independent charitable trust; Cartier, Montblanc, and Van Cleef belong to Richemont!"
            }
        ]
    },
    {
        "id": 3,
        "name": "Round 3: Global MNC Tagline Master",
        "type": "mcq",
        "description": "Complete the World-Famous Brand Slogans • 4 Options • 25 Questions",
        "questions": [
            {
                "q": "Apple (1997 Historic Renaissance Campaign) — \"Think...\"",
                "options": ["Big", "Ahead", "Different", "Simple"],
                "ans": 2,
                "ansText": "Different",
                "expl": "Apple's 'Think Different' campaign marked Steve Jobs' return and company rebirth."
            },
            {
                "q": "Nike — \"Just...\"",
                "options": ["Run", "Fly", "Win", "Do It"],
                "ans": 3,
                "ansText": "Do It",
                "expl": "'Just Do It' was created in 1988 by Wieden+Kennedy and is Nike's worldwide motto."
            },
            {
                "q": "McDonald's — \"I'm...\"",
                "options": ["Loving It", "Craving It", "Happy Now", "Hungry"],
                "ans": 0,
                "ansText": "Loving It",
                "expl": "'I'm Lovin' It' launched in 2003 with Justin Timberlake and is their longest-running slogan."
            },
            {
                "q": "L'Oreal Paris — \"Because You're...\"",
                "options": ["Beautiful", "Worth It", "Special", "The Queen"],
                "ans": 1,
                "ansText": "Worth It",
                "expl": "'Because You're Worth It' was coined in 1971 celebrating female self-worth."
            },
            {
                "q": "Gillette (P&G Men's Grooming) — \"The Best a Man Can...\"",
                "options": ["Shave", "Choose", "Wear", "Get"],
                "ans": 3,
                "ansText": "Get",
                "expl": "'The Best a Man Can Get' debuted during Super Bowl XXIII in 1989."
            },
            {
                "q": "BMW (German Luxury Motors) — \"The Ultimate Driving...\"",
                "options": ["Experience", "Machine", "Performance", "Passion"],
                "ans": 1,
                "ansText": "Machine",
                "expl": "'The Ultimate Driving Machine' has defined BMW engineering for over 45 years."
            },
            {
                "q": "Red Bull — \"Red Bull gives you...\"",
                "options": ["Energy", "Wings", "Power", "Speed"],
                "ans": 1,
                "ansText": "Wings",
                "expl": "'Red Bull gives you wiiings' is the world-famous energy drink tagline."
            },
            {
                "q": "KitKat (Nestlé Confectionery) — \"Have a break, have a...\"",
                "options": ["KitKat", "Snickers", "Coffee", "Smile"],
                "ans": 0,
                "ansText": "KitKat",
                "expl": "'Have a break, have a KitKat' was coined in 1957 by Donald Gilles."
            },
            {
                "q": "De Beers (The 1947 Diamond Slogan) — \"A Diamond is...\"",
                "options": ["Forever", "Precious", "Eternal", "Unbreakable"],
                "ans": 0,
                "ansText": "Forever",
                "expl": "'A Diamond is Forever' by Frances Gerety was named Slogan of the 20th Century."
            },
            {
                "q": "Coca-Cola — \"Open...\"",
                "options": ["Refreshment", "Happiness", "Cold Joy", "The Bottle"],
                "ans": 1,
                "ansText": "Happiness",
                "expl": "'Open Happiness' was Coca-Cola's global feel-good campaign launched in 2009."
            },
            {
                "q": "Adidas (Global Athletic Campaign) — \"Impossible is...\"",
                "options": ["Temporary", "Overcome", "Nothing", "Defeated"],
                "ans": 2,
                "ansText": "Nothing",
                "expl": "'Impossible is Nothing' was inspired by a quote from boxing legend Muhammad Ali."
            },
            {
                "q": "KFC (Yum! Brands Poultry Mascot) — \"It's Finger Lickin'...\"",
                "options": ["Tasty", "Good", "Fresh", "Hot"],
                "ans": 1,
                "ansText": "Good",
                "expl": "'Finger Lickin' Good' has been KFC's trademark slogan since the 1950s."
            },
            {
                "q": "Subway — \"Eat...\"",
                "options": ["Healthy", "Fresh", "Clean", "Good"],
                "ans": 1,
                "ansText": "Fresh",
                "expl": "'Eat Fresh' highlights Subway's custom sandwiches made in front of customers."
            },
            {
                "q": "Disneyland / Walt Disney Parks — \"The Happiest Place on...\"",
                "options": ["Earth", "The Globe", "Vacation", "The Map"],
                "ans": 0,
                "ansText": "Earth",
                "expl": "Walt Disney personally dedicated Disneyland as 'The Happiest Place on Earth' in 1955."
            },
            {
                "q": "Mercedes-Benz — \"The Best or...\"",
                "options": ["Nothing", "Luxury", "Perfection", "Standard"],
                "ans": 0,
                "ansText": "Nothing",
                "expl": "'Das Beste oder nichts' translates globally to 'The Best or Nothing'."
            },
            {
                "q": "Burger King — \"Have It Your...\"",
                "options": ["Style", "Taste", "Way", "Choice"],
                "ans": 2,
                "ansText": "Way",
                "expl": "'Have It Your Way' emphasized custom burger toppings compared to McDonald's."
            },
            {
                "q": "Mastercard — \"There are some things money can't buy. For everything else, there's...\"",
                "options": ["Cash", "Credit", "Mastercard", "Freedom"],
                "ans": 2,
                "ansText": "Mastercard",
                "expl": "The 'Priceless' campaign launched in 1997 is one of the most successful in finance."
            },
            {
                "q": "Airbnb — \"Belong...\"",
                "options": ["Everywhere", "Anywhere", "Together", "At Home"],
                "ans": 1,
                "ansText": "Anywhere",
                "expl": "'Belong Anywhere' reflects Airbnb's vision of community-powered global travel."
            },
            {
                "q": "Calvin Klein — \"Between love and madness lies...\"",
                "options": ["Passion", "Obsession", "Desire", "Eternity"],
                "ans": 1,
                "ansText": "Obsession",
                "expl": "Calvin Klein's iconic fragrance campaign declared: 'Between love and madness lies Obsession'."
            },
            {
                "q": "Skittles (Mars Candy) — \"Taste the...\"",
                "options": ["Colors", "Sweetness", "Rainbow", "Fruit"],
                "ans": 2,
                "ansText": "Rainbow",
                "expl": "'Taste the Rainbow' has been Skittles' colorful slogan since 1994."
            },
            {
                "q": "Nokia — \"Connecting...\"",
                "options": ["People", "The World", "Hearts", "Minds"],
                "ans": 0,
                "ansText": "People",
                "expl": "'Connecting People' debuted in 1992 alongside the famous Nokia ringtone."
            },
            {
                "q": "Thums Up — \"Taste the...\"",
                "options": ["Power", "Lightning", "Energy", "Thunder"],
                "ans": 3,
                "ansText": "Thunder",
                "expl": "'Taste the Thunder' is the bold, fizzy trademark slogan of Thums Up."
            },
            {
                "q": "Lay's Potato Chips — \"No one can eat just...\"",
                "options": ["Once", "A Few", "One", "A Packet"],
                "ans": 2,
                "ansText": "One",
                "expl": "'Betcha can't eat just one' / 'No one can eat just one' is Lay's crispy promise."
            },
            {
                "q": "Boost — \"Boost is the secret of our...\"",
                "options": ["Energy", "Power", "Victory", "Strength"],
                "ans": 0,
                "ansText": "Energy",
                "expl": "'Boost is the secret of my energy' was voiced by Kapil Dev and Sachin Tendulkar."
            },
            {
                "q": "Mentos — \"Dimag ki...\"",
                "options": ["Ghanti Bajao", "Bati Jala De", "Shakti Badhao", "Light On"],
                "ans": 1,
                "ansText": "Bati Jala De",
                "expl": "'Mentos: Dimag ki bati jala de' is the classic clever-thinking candy campaign."
            }
        ]
    },
    {
        "id": 4,
        "name": "Round 4: The Origin Story (Birthplace of Global Brands)",
        "type": "mcq",
        "description": "Which Country or City was this Famous Brand Born in? • 25 Questions",
        "questions": [
            {
                "q": "In which country did the flat-pack furniture and home superstore IKEA originate?",
                "options": ["Sweden", "Germany", "Denmark", "Switzerland"],
                "ans": 0,
                "ansText": "Sweden",
                "expl": "IKEA was founded by Ingvar Kamprad in Almhult, Sweden in 1943."
            },
            {
                "q": "In which country was the athletic sportswear giant Adidas founded?",
                "options": ["USA", "Germany", "UK", "Italy"],
                "ans": 1,
                "ansText": "Germany",
                "expl": "Adidas was founded in Herzogenaurach, Germany by Adolf Dassler in 1949."
            },
            {
                "q": "In which city did coffeehouse chain Starbucks open its very first store in 1971?",
                "options": ["Seattle", "New York", "Los Angeles", "Chicago"],
                "ans": 0,
                "ansText": "Seattle",
                "expl": "Starbucks opened its historic first cafe at Pike Place Market, Seattle in 1971."
            },
            {
                "q": "In which country did the fast-fashion clothing giant Zara originate?",
                "options": ["France", "Italy", "Spain", "Portugal"],
                "ans": 2,
                "ansText": "Spain",
                "expl": "Amancio Ortega opened the first Zara store in A Coruna, Galicia, Spain in 1975."
            },
            {
                "q": "Which Indian city is the birthplace and headquarters of food delivery platform Swiggy?",
                "options": ["Bengaluru", "Mumbai", "Hyderabad", "Delhi"],
                "ans": 0,
                "ansText": "Bengaluru",
                "expl": "Swiggy was founded in Koramangala, Bengaluru in 2014."
            },
            {
                "q": "In which country did the electronics and smartphone giant Samsung originate?",
                "options": ["Japan", "South Korea", "Taiwan", "Singapore"],
                "ans": 1,
                "ansText": "South Korea",
                "expl": "Lee Byung-chul founded Samsung in Daegu, South Korea in 1938 as a trading firm."
            },
            {
                "q": "In which European country was luxury supercar manufacturer Ferrari founded?",
                "options": ["Germany", "France", "Italy", "Austria"],
                "ans": 2,
                "ansText": "Italy",
                "expl": "Enzo Ferrari founded Scuderia Ferrari in Maranello / Modena, Italy in 1939."
            },
            {
                "q": "Which Indian state is dairy giant Amul (Anand Milk Union Limited) headquartered in?",
                "options": ["Gujarat", "Maharashtra", "Punjab", "Rajasthan"],
                "ans": 0,
                "ansText": "Gujarat",
                "expl": "Amul was founded in Anand, Gujarat in 1946 sparking India's White Revolution."
            },
            {
                "q": "In which country was the multinational food company Nestlé born in 1866?",
                "options": ["Switzerland", "Belgium", "UK", "Netherlands"],
                "ans": 0,
                "ansText": "Switzerland",
                "expl": "Henri Nestle founded the company in Vevey, Switzerland."
            },
            {
                "q": "In which country was global fashion retailer H&M (Hennes & Mauritz) founded?",
                "options": ["Sweden", "Norway", "Finland", "France"],
                "ans": 0,
                "ansText": "Sweden",
                "expl": "Erling Persson founded Hennes in Vasteras, Sweden in 1947."
            },
            {
                "q": "In which Indian city was Zomato founded in 2008 (originally launched as Foodiebay)?",
                "options": ["Gurugram / Delhi NCR", "Bengaluru", "Pune", "Chennai"],
                "ans": 0,
                "ansText": "Gurugram / Delhi NCR",
                "expl": "Deepinder Goyal and Pankaj Chaddah founded Zomato in Gurugram, Haryana."
            },
            {
                "q": "In which country did the iconic building-brick toy company Lego originate?",
                "options": ["Denmark", "Sweden", "Germany", "Netherlands"],
                "ans": 0,
                "ansText": "Denmark",
                "expl": "Ole Kirk Christiansen founded Lego in Billund, Denmark in 1932."
            },
            {
                "q": "In which country did the luxury chocolate brand Ferrero Rocher originate?",
                "options": ["Italy", "Belgium", "Switzerland", "France"],
                "ans": 0,
                "ansText": "Italy",
                "expl": "Michele Ferrero introduced Ferrero Rocher in Alba, Piedmont, Italy in 1982."
            },
            {
                "q": "In which country was the popular energy drink Red Bull co-created and formulated?",
                "options": ["Austria (inspired by Thailand)", "USA", "UK", "Germany"],
                "ans": 0,
                "ansText": "Austria (inspired by Thailand)",
                "expl": "Dietrich Mateschitz adapted Thai drink Krating Daeng into Austria's Red Bull in 1987."
            },
            {
                "q": "In which city did ride-hailing company Uber launch its very first cab service?",
                "options": ["San Francisco", "New York", "Boston", "London"],
                "ans": 0,
                "ansText": "San Francisco",
                "expl": "UberCab launched in San Francisco, California in May 2010."
            },
            {
                "q": "In which country did the luxury sports car maker Porsche originate?",
                "options": ["Germany", "Italy", "Switzerland", "Sweden"],
                "ans": 0,
                "ansText": "Germany",
                "expl": "Ferdinand Porsche founded the automotive design firm in Stuttgart, Germany in 1931."
            },
            {
                "q": "In which Indian city was beauty retail platform Nykaa founded by Falguni Nayar?",
                "options": ["Mumbai", "Bengaluru", "Delhi", "Kolkata"],
                "ans": 0,
                "ansText": "Mumbai",
                "expl": "Former investment banker Falguni Nayar launched Nykaa in Mumbai in 2012."
            },
            {
                "q": "In which European country was music streaming giant Spotify created in 2006?",
                "options": ["Sweden", "UK", "Germany", "Ireland"],
                "ans": 0,
                "ansText": "Sweden",
                "expl": "Daniel Ek and Martin Lorentzon founded Spotify in Stockholm, Sweden."
            },
            {
                "q": "In which country was luxury wristwatch brand Rolex founded and headquartered today?",
                "options": ["Switzerland", "Germany", "Italy", "Japan"],
                "ans": 0,
                "ansText": "Switzerland",
                "expl": "Rolex was registered in Geneva, Switzerland and maintains its global headquarters there."
            },
            {
                "q": "In which country did sportswear giant Puma originate?",
                "options": ["Germany", "USA", "UK", "France"],
                "ans": 0,
                "ansText": "Germany",
                "expl": "Rudolf Dassler founded Puma in Herzogenaurach, Germany in 1948."
            },
            {
                "q": "In which country was consumer electronics giant Sony founded in 1946?",
                "options": ["Japan", "South Korea", "China", "Singapore"],
                "ans": 0,
                "ansText": "Japan",
                "expl": "Masaru Ibuka and Akio Morita founded Tokyo Tsushin Kogyo (Sony) in Tokyo, Japan."
            },
            {
                "q": "In which country was multinational supermarket pioneer Carrefour founded?",
                "options": ["France", "Germany", "Spain", "Belgium"],
                "ans": 0,
                "ansText": "France",
                "expl": "Carrefour opened its first hypermarket in Annecy, France in 1958."
            },
            {
                "q": "In which country did eyewear giant Ray-Ban originally begin before moving to Italy?",
                "options": ["USA (Bausch & Lomb)", "UK", "France", "Germany"],
                "ans": 0,
                "ansText": "USA (Bausch & Lomb)",
                "expl": "Ray-Ban was created by Bausch & Lomb in Rochester, New York in 1937."
            },
            {
                "q": "In which European country was beverage giant Heineken founded in 1864?",
                "options": ["Netherlands", "Germany", "Belgium", "Denmark"],
                "ans": 0,
                "ansText": "Netherlands",
                "expl": "Gerard Adriaan Heineken founded the historic brewery in Amsterdam, Netherlands."
            },
            {
                "q": "In which city was e-commerce behemoth Amazon founded by Jeff Bezos in 1994?",
                "options": ["Bellevue / Seattle (Washington)", "San Francisco", "New York", "Austin"],
                "ans": 0,
                "ansText": "Bellevue / Seattle (Washington)",
                "expl": "Jeff Bezos founded Amazon in the garage of his rented house in Bellevue, Washington."
            }
        ]
    },
    {
        "id": 5,
        "name": "Round 5: Guess the Brand Logo (Visuals & Insignias)",
        "type": "mcq",
        "description": "Identify Global Logos, Hidden Symbols & Insignias • 25 Questions",
        "questions": [
            {
                "q": "In the FedEx logo, what hidden symbol is formed in the negative white space between letters 'E' and 'x'?",
                "options": ["A Package", "A Forward Arrow", "An Airplane", "A Star"],
                "ans": 1,
                "ansText": "A Forward Arrow",
                "expl": "The white space between 'E' and 'x' forms an arrow symbolizing forward motion and speed."
            },
            {
                "q": "In the Amazon logo, what does the curved yellow arrow specifically point between?",
                "options": ["Letter 'A' to letter 'Z'", "Letter 'a' to letter 'm'", "First and last letter", "Arrow has no meaning"],
                "ans": 0,
                "ansText": "Letter 'A' to letter 'Z'",
                "expl": "The yellow arrow represents customer happiness and shows they sell everything from A to Z."
            },
            {
                "q": "The logo of Baskin Robbins uses pink highlights inside 'B' and 'R' to reveal what famous number?",
                "options": ["24", "31", "50", "99"],
                "ans": 1,
                "ansText": "31",
                "expl": "The pink parts spell '31' representing a different ice cream flavor for every day of the month."
            },
            {
                "q": "Which luxury car company features a Prancing Stallion (Cavallino Rampante) black horse on a yellow crest?",
                "options": ["Porsche", "Ferrari", "Mustang", "Lamborghini"],
                "ans": 1,
                "ansText": "Ferrari",
                "expl": "Enzo Ferrari adopted the prancing black horse from Italian WWI flying ace Francesco Baracca."
            },
            {
                "q": "Which Italian supercar manufacturer’s logo features a golden raging fighting bull?",
                "options": ["Maserati", "Ferrari", "Lamborghini", "Alfa Romeo"],
                "ans": 2,
                "ansText": "Lamborghini",
                "expl": "Ferruccio Lamborghini chose the raging bull based on his zodiac sign (Taurus)."
            },
            {
                "q": "The circular blue and white propeller quadrants in the BMW logo represent the flag colors of which German state?",
                "options": ["Bavaria", "Saxony", "Berlin", "Hamburg"],
                "ans": 0,
                "ansText": "Bavaria",
                "expl": "BMW (Bavarian Motor Works) uses the white and blue checkered colors of the Bavarian state flag."
            },
            {
                "q": "In the logo of chocolate brand Toblerone, what hidden animal is silhouetted inside the Matterhorn mountain drawing?",
                "options": ["An Eagle", "A Wolf", "A Mountain Bear", "An Ibex Goat"],
                "ans": 2,
                "ansText": "A Mountain Bear",
                "expl": "A silhouette of a bear is hidden inside the mountain representing Bern, the City of Bears."
            },
            {
                "q": "What legendary creature is featured as the green crowned icon in the Starbucks round logo?",
                "options": ["Twin-tailed Siren (Mermaid)", "Greek Goddess Athena", "Medusa", "Sea Nymph"],
                "ans": 0,
                "ansText": "Twin-tailed Siren (Mermaid)",
                "expl": "The icon is a Norse 16th-century twin-tailed siren reflecting maritime coffee roots."
            },
            {
                "q": "The three parallel diagonal stripes in the Adidas logo are angled together to form what symbolic shape?",
                "options": ["A Mountain to overcome", "A Shoe sole", "An Arrow", "A Running track"],
                "ans": 0,
                "ansText": "A Mountain to overcome",
                "expl": "The three slanted stripes symbolize a mountain representing athletic challenges to conquer."
            },
            {
                "q": "Which luxury fashion house uses two interlocking, mirrored capital letters \"G\" as its primary monogram?",
                "options": ["Givenchy", "Gucci", "Goyard", "Giorgio Armani"],
                "ans": 1,
                "ansText": "Gucci",
                "expl": "The double-G logo honors the Italian fashion brand's founder, Guccio Gucci."
            },
            {
                "q": "Which French luxury luggage brand is universally known for the gold interlocking monogram \"LV\"?",
                "options": ["Louis Vuitton", "Lacoste", "Longchamp", "Lanvin"],
                "ans": 0,
                "ansText": "Louis Vuitton",
                "expl": "Georges Vuitton designed the iconic 'LV' monogram canvas in 1896 to honor his late father."
            },
            {
                "q": "Which sportswear brand features an iconic green crocodile stitched onto its polo t-shirts?",
                "options": ["Lacoste", "Crocodile", "Ralph Lauren", "Tommy Hilfiger"],
                "ans": 0,
                "ansText": "Lacoste",
                "expl": "French tennis champion Rene Lacoste was nicknamed 'The Crocodile' for his tenacity."
            },
            {
                "q": "What is the famous single-stroke Nike curved checkmark logo officially called in corporate design history?",
                "options": ["The Tick", "The Stripe", "The Swoosh", "The Glide"],
                "ans": 2,
                "ansText": "The Swoosh",
                "expl": "Designed by Carolyn Davidson in 1971, it represents the sound and motion of speed."
            },
            {
                "q": "In the Unilever corporate logo, the large letter 'U' is formed by weaving together 25 tiny icons representing what?",
                "options": ["Alphabet letters", "Sustainable living and daily vitality icons", "Chemical molecules", "Historical dates"],
                "ans": 1,
                "ansText": "Sustainable living and daily vitality icons",
                "expl": "The 25 distinct miniature icons include a sun, bird, tea leaf, and drop representing their diverse brands."
            },
            {
                "q": "What animal is depicted on the luxury logo of British sports car manufacturer Jaguar?",
                "options": ["Leaping Panther", "Leaping Jaguar", "Roaring Lion", "Sprinting Cheetah"],
                "ans": 1,
                "ansText": "Leaping Jaguar",
                "expl": "The leaping silver feline embodies agility, speed, and sleek luxury."
            },
            {
                "q": "What do the four horizontally interlocking chrome rings in the Audi logo historically represent?",
                "options": ["The four wheels of a car", "Merger of 4 independent motor companies (Auto Union)", "4 Olympic medals", "4 German founders"],
                "ans": 1,
                "ansText": "Merger of 4 independent motor companies (Auto Union)",
                "expl": "The rings symbolize the 1932 merger of Audi, DKW, Horch, and Wanderer."
            },
            {
                "q": "The three points of the star in the Mercedes-Benz hood ornament symbolize Gottlieb Daimler's ambition for motorization where?",
                "options": ["Land, Sea, and Air", "Europe, Asia, and America", "Past, Present, and Future", "Speed, Luxury, and Safety"],
                "ans": 0,
                "ansText": "Land, Sea, and Air",
                "expl": "The tri-star represents universal motorization across land, water, and skies."
            },
            {
                "q": "Which cycling event’s logo incorporates a hidden bicycle inside the letters 'T', 'o', and 'u' of its name?",
                "options": ["Tour de France", "Giro d'Italia", "Vuelta a Espana", "Paris-Roubaix"],
                "ans": 0,
                "ansText": "Tour de France",
                "expl": "The yellow circle and letters 'o-u-r' cleverly form a cyclist leaning over bicycle wheels."
            },
            {
                "q": "The peacock logo of American TV network NBC originally used 6 colorful feathers to represent what breakthrough?",
                "options": ["6 Founding members", "Transition to Color Television programming", "6 continents", "6 radio stations"],
                "ans": 1,
                "ansText": "Transition to Color Television programming",
                "expl": "Introduced in 1956 to encourage viewers to purchase color TV sets."
            },
            {
                "q": "Which famous luxury Swiss watchmaker uses a golden five-pointed royal coronet crown as its brand emblem?",
                "options": ["Omega", "Tag Heuer", "Rolex", "Patek Philippe"],
                "ans": 2,
                "ansText": "Rolex",
                "expl": "Rolex's coronet crown matches their slogan: 'A crown for every achievement'."
            },
            {
                "q": "What fruit silhouette with a single bite taken out of its right side defines the tech giant Apple?",
                "options": ["Apple", "Peach", "Cherry", "Pear"],
                "ans": 0,
                "ansText": "Apple",
                "expl": "Designer Rob Janoff added the bite so people wouldn't confuse the apple with a cherry."
            },
            {
                "q": "Which retail giant’s logo consists of a bright red circle containing a clean white bullseye target?",
                "options": ["Walmart", "Target", "Costco", "Kmart"],
                "ans": 1,
                "ansText": "Target",
                "expl": "Target debuted the iconic bullseye in 1962 to represent hitting the mark in retail value."
            },
            {
                "q": "What fast-food chain features twin interlocking golden arches forming a giant letter 'M'?",
                "options": ["Burger King", "Subway", "McDonald's", "Wendy's"],
                "ans": 2,
                "ansText": "McDonald's",
                "expl": "The Golden Arches were originally architectural features of the first franchised restaurants."
            },
            {
                "q": "Which food brand’s logo depicts a caricature of a southern gentleman with white hair and black string tie?",
                "options": ["KFC (Colonel Sanders)", "Wendy's", "Popeyes", "Chic-fil-A"],
                "ans": 0,
                "ansText": "KFC (Colonel Sanders)",
                "expl": "Colonel Harland Sanders' face has been the global mascot of Kentucky Fried Chicken since 1952."
            },
            {
                "q": "Which beverage logo features a circular red, white, and blue globe with a horizontal wavy center stripe?",
                "options": ["Pepsi", "Coca-Cola", "Red Bull", "Thums Up"],
                "ans": 0,
                "ansText": "Pepsi",
                "expl": "The Pepsi Globe adopted the red, white, and blue colors during WWII to show patriotism."
            }
        ]
    },
    {
        "id": 6,
        "name": "Round 6: Who Owns Who? (Mega Conglomerates & Brand Parents)",
        "type": "mcq",
        "description": "Which Parent Company Owns These Famous Household Brands? • 25 Questions",
        "questions": [
            {
                "q": "Which global food giant owns both Maggi instant noodles and KitKat chocolate?",
                "options": ["Unilever", "Nestle", "Mondelez", "Danone"],
                "ans": 1,
                "ansText": "Nestle",
                "expl": "Nestle owns hundreds of brands worldwide including Maggi, KitKat, and Nescafe."
            },
            {
                "q": "Which Indian conglomerate owns British luxury car makers Jaguar and Land Rover (JLR)?",
                "options": ["Mahindra Group", "Tata Motors", "Reliance Industries", "Ashok Leyland"],
                "ans": 1,
                "ansText": "Tata Motors",
                "expl": "Tata Motors acquired Jaguar Land Rover from Ford in 2008 for $2.3 Billion."
            },
            {
                "q": "Who is the parent company that owns Instagram, WhatsApp, and Facebook?",
                "options": ["Alphabet", "Microsoft", "Meta Platforms", "Apple"],
                "ans": 2,
                "ansText": "Meta Platforms",
                "expl": "Mark Zuckerberg rebranded the parent company to Meta Platforms in 2021."
            },
            {
                "q": "Which soft drink giant owns Thums Up, Limca, Sprite, and Maaza in India?",
                "options": ["PepsiCo", "The Coca-Cola Company", "Parle Agro", "Red Bull GmbH"],
                "ans": 1,
                "ansText": "The Coca-Cola Company",
                "expl": "Coca-Cola acquired Indian brands Thums Up, Limca, and Gold Spot from Parle in 1993."
            },
            {
                "q": "Which multinational acquired quick-commerce delivery platform Blinkit in an all-stock deal?",
                "options": ["Swiggy", "Zomato", "Flipkart", "Amazon India"],
                "ans": 1,
                "ansText": "Zomato",
                "expl": "Zomato acquired quick-commerce platform Blinkit (formerly Grofers) in 2022."
            },
            {
                "q": "Which parent company owns luxury vehicle brands Audi, Porsche, Lamborghini, and Bentley?",
                "options": ["BMW Group", "Mercedes-Benz Group", "Volkswagen Group", "Stellantis"],
                "ans": 2,
                "ansText": "Volkswagen Group",
                "expl": "German giant Volkswagen Group owns Audi, Porsche, Lamborghini, Bentley, and Ducati."
            },
            {
                "q": "Who is the corporate parent holding company that owns search giant Google, YouTube, and Android?",
                "options": ["Alphabet Inc.", "Meta", "Oracle", "SoftBank"],
                "ans": 0,
                "ansText": "Alphabet Inc.",
                "expl": "Larry Page and Sergey Brin reorganized Google under the parent holding company Alphabet in 2015."
            },
            {
                "q": "Which Indian corporate titan owns Jio Platforms, Hamleys toy stores, and Trends retail?",
                "options": ["Adani Group", "Reliance Industries", "Tata Group", "Aditya Birla Group"],
                "ans": 1,
                "ansText": "Reliance Industries",
                "expl": "Mukesh Ambani's Reliance Industries holds diverse stakes in telecom, retail, and energy."
            },
            {
                "q": "Which American conglomerate owns consumer brands Gillette, Oral-B, Pampers, and Ariel?",
                "options": ["Procter & Gamble (P&G)", "Johnson & Johnson", "Unilever", "Colgate-Palmolive"],
                "ans": 0,
                "ansText": "Procter & Gamble (P&G)",
                "expl": "P&G operates household staples across personal grooming, hygiene, and baby care."
            },
            {
                "q": "Which confectionery multinational owns Oreo, Toblerone, and Cadbury Dairy Milk?",
                "options": ["Nestle", "Mondelez International", "Mars Inc.", "Hershey's"],
                "ans": 1,
                "ansText": "Mondelez International",
                "expl": "Mondelez was created from the spinoff of Kraft Foods and owns Cadbury and Oreo."
            },
            {
                "q": "Which retail empire acquired Indian e-commerce pioneer Flipkart in 2018 for $16 Billion?",
                "options": ["Amazon", "Walmart", "Alibaba", "SoftBank"],
                "ans": 1,
                "ansText": "Walmart",
                "expl": "Walmart bought a majority 77% stake in Flipkart in the world's largest e-commerce deal."
            },
            {
                "q": "Which quick-service restaurant conglomerate operates KFC, Pizza Hut, and Taco Bell globally?",
                "options": ["Restaurant Brands International", "Yum! Brands", "McDonald's Corp", "Darden Restaurants"],
                "ans": 1,
                "ansText": "Yum! Brands",
                "expl": "Yum! Brands operates over 55,000 restaurants across KFC, Pizza Hut, and Taco Bell."
            },
            {
                "q": "Which parent company acquired code-sharing platform GitHub and owns LinkedIn?",
                "options": ["Apple", "Microsoft", "Google", "IBM"],
                "ans": 1,
                "ansText": "Microsoft",
                "expl": "Microsoft acquired LinkedIn for $26.2B in 2016 and GitHub for $7.5B in 2018."
            },
            {
                "q": "Which Indian consumer group manufactures Bingo! chips, Aashirvaad Atta, and Sunfeast biscuits?",
                "options": ["Britannia", "ITC Limited", "Parle", "Marico"],
                "ans": 1,
                "ansText": "ITC Limited",
                "expl": "Kolkata-headquartered ITC is one of India's largest FMCG and packaging conglomerates."
            },
            {
                "q": "Which German luxury conglomerate owns both Rolls-Royce Motor Cars and MINI Cooper?",
                "options": ["Volkswagen Group", "BMW Group", "Mercedes-Benz Group", "Porsche SE"],
                "ans": 1,
                "ansText": "BMW Group",
                "expl": "BMW Group owns BMW, MINI, Rolls-Royce Motor Cars, and BMW Motorrad."
            },
            {
                "q": "Which French luxury titan headed by Bernard Arnault owns Louis Vuitton, Dior, Sephora, and Tiffany & Co.?",
                "options": ["Kering", "LVMH (Moët Hennessy Louis Vuitton)", "Hermes", "Richemont"],
                "ans": 1,
                "ansText": "LVMH",
                "expl": "LVMH is the world's largest luxury goods empire comprising 75 prestigious houses."
            },
            {
                "q": "Which snack & beverage giant owns Lay's, Doritos, Kurkure, and Gatorade?",
                "options": ["PepsiCo", "Coca-Cola", "Kraft Heinz", "Kellogg's"],
                "ans": 0,
                "ansText": "PepsiCo",
                "expl": "PepsiCo owns major snack brands via Frito-Lay alongside its global beverage empire."
            },
            {
                "q": "Which consumer company owns health food drinks Horlicks and Boost in India?",
                "options": ["GlaxoSmithKline", "Hindustan Unilever (HUL)", "Nestle", "Dabur"],
                "ans": 1,
                "ansText": "Hindustan Unilever (HUL)",
                "expl": "HUL merged GSK Consumer Healthcare to acquire Horlicks and Boost for ₹31,700 Crore."
            },
            {
                "q": "Which Indian conglomerate owns Titan, Tanishq, Fastrack, and Air India?",
                "options": ["Tata Group", "Birla Group", "Godrej", "Mahindra"],
                "ans": 0,
                "ansText": "Tata Group",
                "expl": "The Tata Group operates in steel, automotive, tech, jewelry, and aviation."
            },
            {
                "q": "Which candy company manufactures M&M's, Snickers, Twix, and Pedigree pet food?",
                "options": ["Mars, Incorporated", "Hershey's", "Mondelez", "Ferrero"],
                "ans": 0,
                "ansText": "Mars, Incorporated",
                "expl": "Family-owned Mars Inc. operates global confectionery and pet care giants."
            },
            {
                "q": "Which cloud CRM giant acquired workplace chat platform Slack for $27.7 Billion?",
                "options": ["Salesforce", "Microsoft", "Oracle", "Adobe"],
                "ans": 0,
                "ansText": "Salesforce",
                "expl": "Marc Benioff's Salesforce completed the blockbuster acquisition of Slack in 2021."
            },
            {
                "q": "Which Italian eyewear monopoly owns Ray-Ban, Oakley, and Sunglass Hut?",
                "options": ["Safilo", "EssilorLuxottica", "Marcolin", "De Rigo"],
                "ans": 1,
                "ansText": "EssilorLuxottica",
                "expl": "EssilorLuxottica produces over 80% of the world's major designer eyewear frames."
            },
            {
                "q": "Which entertainment powerhouse acquired Marvel Studios, Pixar, and Lucasfilm (Star Wars)?",
                "options": ["Warner Bros.", "The Walt Disney Company", "Sony Pictures", "Paramount"],
                "ans": 1,
                "ansText": "The Walt Disney Company",
                "expl": "Under Bob Iger, Disney acquired Pixar in 2006, Marvel in 2009, and Lucasfilm in 2012."
            },
            {
                "q": "Which company acquired audio hardware brand Beats by Dre for $3 Billion in 2014?",
                "options": ["Sony", "Apple", "Bose", "Samsung"],
                "ans": 1,
                "ansText": "Apple",
                "expl": "Apple bought Beats Electronics from Dr. Dre and Jimmy Iovine to build Apple Music."
            },
            {
                "q": "Which gaming giant acquired Activision Blizzard (Call of Duty, Candy Crush) for $68.7 Billion?",
                "options": ["Sony", "Microsoft", "Electronic Arts", "Nintendo"],
                "ans": 1,
                "ansText": "Microsoft",
                "expl": "Microsoft finalized the record-breaking $68.7B buyout of Activision Blizzard in 2023."
            }
        ]
    }
]

with open('public/questions.json', 'w', encoding='utf-8') as f:
    json.dump(rounds, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(rounds)} rounds with {sum(len(r['questions']) for r in rounds)} total questions.")
