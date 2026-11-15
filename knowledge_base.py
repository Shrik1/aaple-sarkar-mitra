"""
Knowledge base for Aaple Sarkar government schemes.
Contains verified information about Maharashtra government schemes and citizen services.
Includes intelligent local RAG matching and rule-based generation fallback.
"""

SCHEMES_DATA = [
    {
        "id": "pm_kisan",
        "title": "PM Kisan Samman Nidhi",
        "title_mr": "पीएम किसान सन्मान निधी",
        "category": "Agriculture / शेती",
        "description": "Income support scheme providing Rs. 6,000 per year in three equal instalments of Rs. 2,000 to all eligible landholding farmer families across Maharashtra.",
        "description_mr": "सर्व पात्र जमीनधारक शेतकरी कुटुंबांना वर्षाला ₹6,000 (दर 4 महिन्यांनी ₹2,000 चा हप्ता) थेट बँक खात्यात देणारी केंद्र व राज्य पुरस्कृत योजना.",
        "eligibility": [
            "Must be a small or marginal landholding farmer family",
            "Cultivable land ownership registered in state land records (7/12)",
            "Aadhaar-seeded bank account with active e-KYC",
            "Not an institutional landholder",
            "Family members must not be serving or retired government employees",
            "Family members must not be income tax payers"
        ],
        "eligibility_mr": [
            "लघु किंवा अल्पभूधारक शेतकरी कुटुंब असणे आवश्यक",
            "स्वतःच्या नावावर शेतजमीन (७/१२ व ८-अ नोंद) असणे आवश्यक",
            "आधार कार्ड बँक खात्याशी संलग्न आणि e-KYC पूर्ण असणे बंधनकारक",
            "संस्थात्मक शेतजमीनधारक अपात्र",
            "कुटुंबातील कोणीही सरकारी नोकरदार किंवा पेन्शनधारक नसावा",
            "कुटुंबातील व्यक्ती आयकरदाता (Income Tax Payer) नसावी"
        ],
        "benefits": "Rs. 6,000 annually credited in 3 tranches of Rs. 2,000 each + additional Namo Shetkari Mahasanman Nidhi Rs. 6,000 from Maharashtra Govt (Total ₹12,000/year).",
        "benefits_mr": "दरवर्षी ₹6,000 (₹2,000 चे 3 हप्ते) + महाराष्ट्र शासनाची नमो शेतकरी महासन्मान निधी योजना ₹6,000 (एकूण वार्षिक ₹12,000 थेट खात्यात).",
        "documents": [
            "Aadhaar Card of applicant",
            "Digital 7/12 & 8-A Land Extract (सातबारा व ८-अ)",
            "Active Bank Passbook with IFSC code",
            "Aadhaar linked mobile number for OTP"
        ],
        "documents_mr": [
            "अर्जदाराचे आधार कार्ड",
            "डिजिटल सातबारा (७/१२) व ८-अ उतारा",
            "आधार संलग्न बँक खाते पासबुक",
            "OTP साठी आधार लिंक मोबाईल नंबर"
        ],
        "apply_link": "https://pmkisan.gov.in",
        "helpline": "155261 / 1800-115-526",
        "keywords": ["pm kisan", "किसान", "farmer", "शेतकरी", "6000", "12000", "namo shetkari", "नमो शेतकरी", "subsidy", "अनुदान", "sheti", "krishi", "कृषी"]
    },
    {
        "id": "ladki_bahin",
        "title": "Mukhyamantri Majhi Ladki Bahin Yojana",
        "title_mr": "मुख्यमंत्री माझी लाडकी बहीण योजना",
        "category": "Women Welfare / महिला व बालविकास",
        "description": "Flagship direct benefit transfer scheme in Maharashtra providing monthly financial aid of Rs. 1,500 to underprivileged women aged 21 to 65 years.",
        "description_mr": "महाराष्ट्रातील २१ ते ६५ वयोगटातील पात्र महिलांना दरमहा ₹१,५०० थेट बँक खात्यात आर्थिक सहाय्य देणारी योजना.",
        "eligibility": [
            "Woman resident and domicile of Maharashtra",
            "Age between 21 and 65 years",
            "Annual family income must not exceed Rs. 2.5 Lakhs (or hold Yellow/Orange Ration Card)",
            "Bank account must be Aadhaar-linked and enabled for DBT",
            "No family member should be a regular government employee or income tax payer",
            "Family should not own a four-wheeler vehicle (excluding tractors)"
        ],
        "eligibility_mr": [
            "महाराष्ट्र राज्याची कायमस्वरूपी रहिवासी महिला",
            "वय २१ ते ६५ वर्षांच्या दरम्यान असावे",
            "कौटुंबिक वार्षिक उत्पन्न ₹२.५ लाखांपेक्षा कमी असावे (किंवा पिवळे/केशरी रेशन कार्डधारक)",
            "बँक खाते आधार लिंक (DBT Enabled) असणे अनिवार्य",
            "कुटुंबातील कोणीही नियमित सरकारी कर्मचारी किंवा आयकरदाता नसावा",
            "कुटुंबाकडे चारचाकी वाहन (ट्रॅक्टर वगळून) नसावे"
        ],
        "benefits": "Rs. 1,500 deposited every month directly to the beneficiary's bank account (Rs. 18,000 per year).",
        "benefits_mr": "दरमहा ₹१,५०० थेट लाभार्थीच्या बँक खात्यात (वार्षिक ₹१८,००० ची आर्थिक मदत).",
        "documents": [
            "Aadhaar Card",
            "Maharashtra Domicile Certificate or Ration Card issued before 15 years / Voter ID",
            "Income Certificate (not required if Yellow/Orange Ration card available)",
            "Bank Passbook copy (Aadhaar linked)",
            "Hamipatra (Self-Declaration Form)"
        ],
        "documents_mr": [
            "आधार कार्ड",
            "अधिवास प्रमाणपत्र (Domicile) किंवा १५ वर्षे जुने रेशन कार्ड / मतदार ओळखपत्र",
            "वार्षिक उत्पन्न प्रमाणपत्र (पिवळे/केशरी रेशन कार्ड असल्यास आवश्यक नाही)",
            "बँक पासबुक झेरॉक्स (आधार संलग्न खात्याचे)",
            "हमीपत्र (स्वयंघोषणापत्र)"
        ],
        "apply_link": "https://ladakibahin.maharashtra.gov.in",
        "helpline": "181 / 1800-120-8040",
        "keywords": ["ladki bahin", "लाडकी बहीण", "majhi ladki bahin", "women", "महिला", "1500", "dbt", "bahin", "माझी लाडकी"]
    },
    {
        "id": "seven_twelve_utara",
        "title": "Digital Satbara 7/12 & 8-A Extract",
        "title_mr": "डिजिटल स्वाक्षरीत ७/१२ व ८-अ उतारा",
        "category": "Land Records / महसूल व जमीन",
        "description": "Legally valid digitally signed 7/12 land ownership record and 8-A holding extract issued by Maharashtra Revenue Department under the Mahabhumi portal.",
        "description_mr": "महाराष्ट्र शासनाच्या महसूल विभागामार्फत डिजिटल स्वाक्षरीसह उपलब्ध होणारा कायदेशीर अधिकृत ७/१२ व ८-अ जमीन मालकी उतारा.",
        "eligibility": [
            "Any land owner, farmer, legal heir, or citizen needing verified land records in Maharashtra",
            "Available 24/7 online for any registered Survey / Gat Number"
        ],
        "eligibility_mr": [
            "महाराष्ट्रातील कोणताही शेतकरी, खातेदार, वारसदार किंवा नागरिक",
            "कोणत्याही गावातील सर्व्हे नंबर किंवा गट नंबर टाकून २४x७ उपलब्ध"
        ],
        "benefits": "Digitally signed with QR code verification; valid in all banks, courts, tehsildar offices without needing Talathi stamp.",
        "benefits_mr": "QR कोडसह डिजिटल स्वाक्षरी असलेला उतारा; तलाठी किंवा तहसीलदार यांच्या प्रत्यक्ष स्वाक्षरीची गरज नाही; बँका व न्यायालयांत कायदेशीर ग्राह्य.",
        "documents": [
            "District, Taluka, and Village name",
            "Survey Number / Gat Number / Khata Number"
        ],
        "documents_mr": [
            "जिल्हा, तालुका आणि गावाचे नाव",
            "सर्व्हे नंबर किंवा गट नंबर किंवा खाते नंबर"
        ],
        "apply_link": "https://digitalsatbara.mahabhumi.gov.in",
        "helpline": "1800-200-5552 / 020-25709000",
        "keywords": ["7/12", "satbara", "सातबारा", "utara", "उतारा", "8a", "८-अ", "land record", "जमीन", "gat number", "गट नंबर", "mahabhumi"]
    },
    {
        "id": "mahatma_phule_krishi",
        "title": "Mahatma Jyotirao Phule Karj Mafi Yojana",
        "title_mr": "महात्मा जोतीराव फुले शेतकरी कर्जमुक्ती योजना",
        "category": "Agriculture / शेती",
        "description": "Farm loan waiver scheme by Maharashtra Government providing relief up to Rs. 2 Lakh on crop loans, plus incentive subsidies for regular payers.",
        "description_mr": "महाराष्ट्रातील थकबाकीदार शेतकऱ्यांना ₹२ लाखांपर्यंत कर्जमुक्ती आणि नियमित कर्जफेड करणाऱ्या शेतकऱ्यांना ₹५०,००० प्रोत्साहन अनुदान देणारी योजना.",
        "eligibility": [
            "Maharashtra resident farmers who took short-term crop loans from cooperative or nationalized banks",
            "Overdue crop loan balance up to Rs. 2,00,000",
            "Farmers paying loan regularly are eligible for up to ₹50,000 incentive bonus",
            "State/Central govt employees and politicians are excluded"
        ],
        "eligibility_mr": [
            "सहकारी किंवा राष्ट्रीयकृत बँकांकडून पीककर्ज घेतलेले महाराष्ट्रातील शेतकरी",
            "₹२,००,००० पर्यंत थकबाकी असलेले पीक कर्ज खाते",
            "नियमित कर्ज परतफेड करणाऱ्या शेतकऱ्यांना ₹५०,००० पर्यंत प्रोत्साहनपर लाभ",
            "सरकारी कर्मचारी, आमदार, खासदार, आयकरदाते अपात्र"
        ],
        "benefits": "Complete waiver on outstanding agricultural loan up to Rs. 2,00,000 directly cleared at bank branch.",
        "benefits_mr": "₹२ लाखांपर्यंतची थकीत पीककर्ज रक्कम थेट बँकेत जमा होऊन खाते नील (ऋणमुक्त) होते.",
        "documents": [
            "Aadhaar Card & Loan Account Number",
            "Bank Passbook showing agricultural loan entry",
            "Biometric Aadhaar authentication at nearest CSC or Bank"
        ],
        "documents_mr": [
            "आधार कार्ड व बँक कर्ज खाते क्रमांक",
            "पीक कर्जाची नोंद असलेले बँक पासबुक",
            "आपले सरकार केंद्र (CSC) किंवा बँकेत बायोमेट्रिक आधार प्रमाणीकरण"
        ],
        "apply_link": "https://mjpsky.maharashtra.gov.in",
        "helpline": "1800-120-8040 / 8655823100",
        "keywords": ["karj mafi", "कर्जमाफी", "loan waiver", "कर्ज", "karj mukti", "कर्जमुक्ती", "sheti karj", "पीक कर्ज"]
    },
    {
        "id": "ration_card",
        "title": "Ration Card (APL, BPL, Antyodaya)",
        "title_mr": "रेशन कार्ड / अन्न सुरक्षा योजना",
        "category": "Food Security / अन्न व नागरी पुरवठा",
        "description": "Public Distribution System providing heavily subsidized or free foodgrains (wheat, rice) under National Food Security Act (NFSA) and Maharashtra PDS.",
        "description_mr": "राष्ट्रीय अन्न सुरक्षा योजना (NFSA) अंतर्गत पात्र कुटुंबांना स्वस्त धान्य (गहू, तांदूळ) आणि नवीन रेशन कार्ड/नावे जोडण्याची शासकीय सेवा.",
        "eligibility": [
            "Resident family of Maharashtra without an existing card in another state",
            "Antyodaya Anna Yojana (AAY): Poorest families, destitute seniors, disabled heads",
            "BPL / Priority Household (PHH): Annual family income below specified state limit",
            "APL (Orange/White): Middle and higher income families"
        ],
        "eligibility_mr": [
            "महाराष्ट्रातील रहिवासी कुटुंब (इतर कोणत्याही राज्यात सक्रिय रेशन कार्ड नसावे)",
            "अंत्योदय योजना: अत्यंत गरीब, निराधार वृद्ध, विधवा किंवा दिव्यांग कुटुंबप्रमुख",
            "प्राधान्य कुटुंब (BPL/PHH): उत्पन्न मर्यादेच्या आतील गरजू कुटुंबे",
            "केशरी/पांढरे रेशन कार्ड: मध्यम व उच्च उत्पन्न गट"
        ],
        "benefits": "Free or heavily subsidized food grains (5kg per person or 35kg per Antyodaya family) every month from Fair Price Shop (रास्त भाव दुकान).",
        "benefits_mr": "दरमहा प्रति व्यक्ती ५ किलो किंवा अंत्योदय कुटुंबाला ३५ किलो मोफत/सवलतीच्या दरात अन्नधान्य.",
        "documents": [
            "Aadhaar cards of all family members",
            "Electricity bill or Gas connection proof or Rent agreement",
            "Tehsildar Income Certificate",
            "Passport size photo of female head of family"
        ],
        "documents_mr": [
            "कुटुंबातील सर्व सदस्यांचे आधार कार्ड",
            "लाईट बिल किंवा गॅस पासबुक किंवा घरपट्टी पावती",
            "तहसीलदार/तलाठी उत्पन्न दाखला",
            "कुटुंबप्रमुख महिलेचे २ पासपोर्ट फोटो"
        ],
        "apply_link": "https://rcms.mahafood.gov.in",
        "helpline": "1967 / 1800-22-4950",
        "keywords": ["ration", "रेशन", "ration card", "रेशन कार्ड", "bpl", "apl", "antyodaya", "अंत्योदय", "wheat", "rice", "धान्य", "गहू", "तांदूळ"]
    },
    {
        "id": "sanjay_gandhi_niradhar",
        "title": "Sanjay Gandhi Niradhar Anudan Yojana",
        "title_mr": "संजय गांधी निराधार अनुदान योजना",
        "category": "Social Welfare / सामाजिक न्याय",
        "description": "Monthly pension for destitute persons, elderly, widows, divorced women, abandoned wives, and persons with severe disabilities.",
        "description_mr": "निराधार वृद्ध, विधवा महिला, घटस्फोटित स्त्रिया, तृतीयपंथी आणि दिव्यांग व्यक्तींना सन्मानजनक जगण्यासाठी दरमहा आर्थिक पेन्शन.",
        "eligibility": [
            "Destitute persons aged 65 years or above, or widows, or person with 40%+ disability",
            "Maharashtra resident for at least 15 years",
            "Annual family income must be below Rs. 21,000 to Rs. 50,000 as per category"
        ],
        "eligibility_mr": [
            "६५ वर्षे किंवा त्यावरील निराधार वृद्ध, विधवा किंवा ४०% पेक्षा जास्त दिव्यांग",
            "महाराष्ट्रात किमान १५ वर्षे वास्तव्य असणे आवश्यक",
            "कौटुंबिक वार्षिक उत्पन्न ₹२१,००० ते ₹५०,००० च्या आत असणे आवश्यक"
        ],
        "benefits": "Rs. 1,500 per month for single beneficiary (Rs. 1,500 per month directly in bank account).",
        "benefits_mr": "दरमहा ₹१,५०० थेट लाभार्थीच्या बँक खात्यात पेन्शन.",
        "documents": [
            "Age Proof (School Leaving Certificate or Birth Certificate)",
            "Domicile / 15 years residence proof",
            "Income certificate by Tehsildar",
            "Disability certificate from Civil Surgeon (if applicable)",
            "Death Certificate of husband (for widows)"
        ],
        "documents_mr": [
            "वयाचा पुरावा (शाळा सोडल्याचा दाखला किंवा जन्म प्रमाणपत्र)",
            "महाराष्ट्रात १५ वर्षे राहिल्याचा दाखला (अधिवास)",
            "तहसीलदारांचा उत्पन्नाचा दाखला",
            "दिव्यांग असल्यास जिल्हा शल्यचिकित्सकांचे (Civil Hospital) प्रमाणपत्र",
            "पतीचे मृत्यू प्रमाणपत्र (विधवा असल्यास)"
        ],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1800-120-8040",
        "keywords": ["niradhar", "निराधार", "sanjay gandhi", "संजय गांधी", "pension", "पेन्शन", "widow", "विधवा", "disabled", "दिव्यांग", "vruddha", "वृद्ध"]
    },
    {
        "id": "income_certificate",
        "title": "Income Certificate (उत्पन्न प्रमाणपत्र)",
        "title_mr": "तहसीलदार उत्पन्न दाखला (१ व ३ वर्ष)",
        "category": "Certificates / प्रमाणपत्रे",
        "description": "Official Revenue Department certificate certifying annual family income; mandatory for college admissions, scholarships, subsidies, and schemes.",
        "description_mr": "शासकीय योजना, शिष्यवृत्ती आणि शैक्षणिक सवलतींसाठी आवश्यक असणारे अधिकृत महसूल विभागाचे वार्षिक उत्पन्न प्रमाणपत्र.",
        "eligibility": [
            "Any resident citizen of Maharashtra needing income validation for education, scholarship, or welfare schemes."
        ],
        "eligibility_mr": [
            "महाराष्ट्रातील कोणताही नागरिक ज्याला शिष्यवृत्ती किंवा सरकारी योजनांसाठी कौटुंबिक उत्पन्नाचा दाखला हवा आहे."
        ],
        "benefits": "Digitally verified certificate valid for 1 or 3 financial years across Maharashtra government institutions and portals.",
        "benefits_mr": "१ किंवा ३ आर्थिक वर्षांसाठी वैध, बारकोड व डिजिटल स्वाक्षरीयुक्त अधिकृत दाखला.",
        "documents": [
            "Applicant Aadhaar Card",
            "Ration Card copy",
            "Salary Slip / Form 16 (for salaried) OR Talathi Income Report / Affidavit (for agriculture/unorganized)",
            "Electricity Bill or Tax receipt"
        ],
        "documents_mr": [
            "अर्जदाराचे आधार कार्ड",
            "रेशन कार्डची प्रत",
            "पगार स्लिप किंवा तलाठी अहवाल / स्वयंघोषणापत्र",
            "निवास पुरावा (लाईट बिल / कर पावती)"
        ],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1800-120-8040",
        "keywords": ["income", "उत्पन्न", "certificate", "दाखला", "utpanna", "scholarship", "शिष्यवृत्ती", "tahsildar"]
    },
    {
        "id": "caste_domicile_certificate",
        "title": "Caste & Domicile Certificate (जात व अधिवास)",
        "title_mr": "जात प्रमाणपत्र व रहिवासी/अधिवास दाखला",
        "category": "Certificates / प्रमाणपत्रे",
        "description": "Essential citizen certificates issued by Sub-Divisional Officer (SDO) proving residence of 15+ years in Maharashtra and caste category reservation.",
        "description_mr": "महाराष्ट्रात १५ वर्षांपेक्षा जास्त वास्तव्याचा पुरावा (Domicile) आणि शासकीय आरक्षण व सवलतींसाठी लागणारे जात प्रमाणपत्र.",
        "eligibility": [
            "Continuous residence of minimum 15 years in Maharashtra (for Domicile)",
            "Belonging to SC, ST, VJNT, OBC, or SBC community with historical pre-cutoff proof (for Caste)"
        ],
        "eligibility_mr": [
            "महाराष्ट्रात किमान १५ वर्षे सतत वास्तव्य (अधिवास प्रमाणपत्रासाठी)",
            "विहित वर्षापूर्वीचे महसुली किंवा शैक्षणिक जात पुरावे (जात प्रमाणपत्रासाठी)"
        ],
        "benefits": "Permanent proof of domicile and eligibility for college seats, government job recruitment, and welfare subsidies.",
        "benefits_mr": "कायमस्वरूपी अधिवास पुरावा; नोकऱ्या, स्पर्धा परीक्षा आणि कॉलेज प्रवेशासाठी आवश्यक.",
        "documents": [
            "Aadhaar Card and School Leaving Certificate (LC)",
            "Father's School Leaving Certificate / Primary school register entry",
            "Ration Card or continuous 15 years residence proof (Electricity bill, tax receipt)",
            "Affidavit on Stamp Paper"
        ],
        "documents_mr": [
            "अर्जदाराचे आधार कार्ड व शाळा सोडल्याचा दाखला (LC)",
            "वडिलांचा किंवा आजोबांचा शाळा सोडल्याचा दाखला / महसूल नोंद",
            "१५ वर्षांचा वास्तव्याचा पुरावा (रेशन कार्ड, जुनी वीज बिले)",
            "प्रतिज्ञापत्र (Affidavit)"
        ],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1800-120-8040",
        "keywords": ["caste", "जात", "domicile", "अधिवास", "certificate", "दाखला", "obc", "sc", "st", "vjnt", "rahiwasi", "रहिवासी"]
    },
    {
        "id": "krishi_yantrikikaran",
        "title": "MahaDBT Krishi Yantrikikaran (Farm Machinery)",
        "title_mr": "महाडीबीटी कृषी यांत्रिकीकरण योजना",
        "category": "Agriculture / शेती",
        "description": "Subsidies ranging from 40% to 50% for purchasing tractors, power tillers, rotavators, sprayers, and harvesting machinery under MahaDBT Farmer portal.",
        "description_mr": "शेतकऱ्यांना ट्रॅक्टर, रोटाव्हेटर, पॉवर टिलर, पेरणी यंत्र आणि शेती अवजारे खरेदीसाठी ४०% ते ५०% शासकीय अनुदान.",
        "eligibility": [
            "Farmer with cultivable land holding in Maharashtra",
            "Registered on MahaDBT Farmer Portal",
            "One farmer family can avail tractor subsidy once in 10 years",
            "SC/ST/Women/Small farmers get up to 50% subsidy; Others get up to 40%"
        ],
        "eligibility_mr": [
            "महाराष्ट्रातील शेतजमीनधारक शेतकरी",
            "महाडीबीटी शेतकरी पोर्टलवर नोंदणीकृत असणे आवश्यक",
            "एका कुटुंबाला १० वर्षांत एकदाच ट्रॅक्टर अनुदानाचा लाभ",
            "महिला, अल्पभूधारक व अनु. जाती/जमाती शेतकऱ्यांना ५०% पर्यंत, इतरांना ४०% अनुदान"
        ],
        "benefits": "Direct subsidy transferred to bank account after purchasing and uploading machinery invoice and physical inspection.",
        "benefits_mr": "अवजारे खरेदीनंतर प्रत्यक्ष तपासणी करून अनुदानाची रक्कम थेट बँक खात्यात जमा.",
        "documents": [
            "7/12 & 8-A Extract with Aadhaar linkage",
            "Aadhaar Card",
            "Caste Certificate (for SC/ST farmers for higher subsidy)",
            "Bank Passbook copy"
        ],
        "documents_mr": [
            "७/१२ व ८-अ उतारा",
            "आधार कार्ड",
            "जात प्रमाणपत्र (अनु. जाती/जमाती प्रवर्गातील असल्यास)",
            "बँक खाते पासबुक झेरॉक्स"
        ],
        "apply_link": "https://mahadbt.maharashtra.gov.in/farmer",
        "helpline": "022-49150800",
        "keywords": ["tractor", "ट्रॅक्टर", "machinery", "अवजारे", "krishi yantra", "rotavator", "mahadbt", "महाडीबीटी", "yantrikikaran"]
    },
    {
        "id": "aaple_sarkar_general",
        "title": "Aaple Sarkar Citizen Services Portal",
        "title_mr": "आपले सरकार पोर्टल (४००+ सेवा)",
        "category": "General / सर्वसमावेशक",
        "description": "Single-window portal by Govt of Maharashtra delivering 400+ public services (Revenue, Rural Development, Police, Urban, Labour) with guaranteed statutory timelines.",
        "description_mr": "महाराष्ट्र शासनाचे अधिकृत एकल-खिडकी पोर्टल, ज्यावर महसूल, ग्रामविकास, नगरविकास अशा विविध विभागांच्या ४०० पेक्षा जास्त सेवा घरबसल्या उपलब्ध आहेत.",
        "eligibility": ["All citizens, residents, farmers, and students in Maharashtra."],
        "eligibility_mr": ["महाराष्ट्रातील सर्व नागरिक, शेतकरी, महिला व विद्यार्थी."],
        "benefits": "Right to Services (RTS) compliance; tracking application status via token; downloadable digitally signed certificates without physical office visits.",
        "benefits_mr": "महाराष्ट्र लोकसेवा हक्क कायद्यानुसार विहित मुदतीत सेवा; अर्जाची ऑनलाइन स्थिती; डिजिटल दाखले डाऊनलोड.",
        "documents": [
            "Aadhaar Card",
            "Active Mobile Number for OTP",
            "Passport Size Photograph"
        ],
        "documents_mr": [
            "आधार कार्ड",
            "OTP साठी सक्रिय मोबाईल नंबर",
            "पासपोर्ट आकाराचा फोटो"
        ],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1800-120-8040 (24x7 Toll-Free)",
        "keywords": ["aaple sarkar", "आपले सरकार", "portal", "पोर्टल", "mahaonline", "revenue", "महसूल", "online", "दाखले", "certificate"]
    }
]


def search_knowledge_base(query: str) -> list:
    """Smart search across all schemes with keyword scoring."""
    query_lower = query.lower().strip()
    words = [w for w in query_lower.split() if len(w) > 1]
    results = []

    for scheme in SCHEMES_DATA:
        score = 0
        # Exact keyword matches
        for kw in scheme["keywords"]:
            kw_l = kw.lower()
            if kw_l in query_lower:
                score += 3
            elif any(w == kw_l for w in words):
                score += 2

        # Title matches
        if any(w in scheme["title"].lower() for w in words):
            score += 2
        if any(w in scheme["title_mr"] for w in words):
            score += 3

        # Description matches
        if any(w in scheme["description"].lower() for w in words):
            score += 1
        if any(w in scheme["description_mr"] for w in words):
            score += 1

        if score > 0:
            results.append((score, scheme))

    results.sort(key=lambda x: x[0], reverse=True)
    if results:
        return [r[1] for r in results[:3]]
    return []


def generate_smart_fallback(query: str, language: str = "auto") -> tuple[str, list]:
    """
    Generates a high-quality, formatted, factual response from the verified knowledge base
    even when Gemini API is unavailable, rate-limited, or offline.
    """
    schemes = search_knowledge_base(query)
    q_lower = query.lower()
    
    # Detect language preference
    is_marathi = language == "mr" or any(ord(char) >= 0x0900 and ord(char) <= 0x097F for char in query)

    if not schemes:
        if is_marathi:
            reply = (
                "🙏 **नमस्कार! मी सरकार मित्र (Aaple Sarkar AI सहाय्यक).**\n\n"
                "तुमच्या विचारलेल्या प्रश्नानुसार थेट योजना शोधता आली नाही. तुम्ही खालीलपैकी कोणत्याही विषयावर माहिती विचारू शकता:\n\n"
                "• **शेतकरी योजना**: पीएम किसान (₹६००० + नमो शेतकरी ₹६०००), पीक कर्जमाफी, शेती अवजारे अनुदान\n"
                "• **महिला योजना**: मुख्यमंत्री माझी लाडकी बहीण योजना (दरमहा ₹१,५००)\n"
                "• **जमीन महसूल**: डिजिटल स्वाक्षरीत ७/१२ व ८-अ उतारा कसा काढायचा\n"
                "• **अन्न सुरक्षा**: नवीन रेशन कार्ड, मोफत धान्य नियम, BPL/अंत्योदय यादी\n"
                "• **प्रमाणपत्रे**: उत्पन्न दाखला, जात प्रमाणपत्र, अधिवास (Domicile) दाखला\n\n"
                "📞 **अधिक मदतीसाठी २४x७ मोफत हेल्पलाइन:** `1800-120-8040`"
            )
        else:
            reply = (
                "🙏 **Welcome to Sarkar Mitra (Aaple Sarkar AI Assistant).**\n\n"
                "I couldn't match a specific scheme for your exact words, but I can guide you through all major Maharashtra services:\n\n"
                "• **Farmer Schemes**: PM Kisan (₹6,000 + Namo Shetkari ₹6,000), Crop Loan Waiver, Farm Machinery Subsidies\n"
                "• **Women Welfare**: Mukhyamantri Majhi Ladki Bahin Yojana (₹1,500/month)\n"
                "• **Land Records**: Digitally signed 7/12 & 8-A Satbara extracts\n"
                "• **Food Security**: Ration Cards (AAY, BPL, PHH) and free foodgrains\n"
                "• **Certificates**: Income, Caste, and Domicile certificates on Aaple Sarkar\n\n"
                "📞 **24x7 Official Toll-Free Helpline:** `1800-120-8040`"
            )
        return reply, []

    # Format the top scheme response
    top = schemes[0]
    mr_elig_list = "\n".join([f"  ✅ {e}" for e in top["eligibility_mr"]])
    mr_doc_list = "\n".join([f"  📋 {d}" for d in top["documents_mr"]])
    en_elig_list = "\n".join([f"  ✅ {e}" for e in top["eligibility"]])
    en_doc_list = "\n".join([f"  📋 {d}" for d in top["documents"]])

    if is_marathi:
        reply = (
            f"🏛️ **{top['title_mr']} ({top['title']})**\n\n"
            f"📌 **योजनेचा तपशील:**\n{top['description_mr']}\n\n"
            f"💰 **मिळणारा लाभ:**\n{top['benefits_mr']}\n\n"
            f"👥 **पात्रता निकष:**\n{mr_elig_list}\n\n"
            f"📑 **आवश्यक कागदपत्रे:**\n{mr_doc_list}\n\n"
            f"🌐 **अधिकृत अर्ज लिंक:** [{top['apply_link']}]({top['apply_link']})\n"
            f"📞 **हेल्पलाइन नंबर:** `{top['helpline']}`\n\n"
            f"💡 *टीप: अर्ज करण्यासाठी जवळच्या 'आपले सरकार सेवा केंद्र' किंवा अधिकृत पोर्टलला भेट द्या.*\n\n"
            f"---\n\n"
            f"🌐 **English Translation & Summary:**\n\n"
            f"🏛️ **{top['title']}**\n"
            f"📌 **Overview:** {top['description']}\n\n"
            f"💰 **Key Benefits:** {top['benefits']}\n\n"
            f"👥 **Eligibility Criteria:**\n{en_elig_list}\n\n"
            f"📑 **Required Documents:**\n{en_doc_list}\n\n"
            f"🔗 **Official Apply Link:** [{top['apply_link']}]({top['apply_link']})\n"
            f"📞 **Toll-Free Helpline:** `{top['helpline']}`"
        )
    else:
        reply = (
            f"🏛️ **{top['title']} ({top['title_mr']})**\n\n"
            f"📌 **Overview:**\n{top['description']}\n\n"
            f"💰 **Key Benefits:**\n{top['benefits']}\n\n"
            f"👥 **Eligibility Criteria:**\n{en_elig_list}\n\n"
            f"📑 **Required Documents:**\n{en_doc_list}\n\n"
            f"🌐 **Official Portal:** [{top['apply_link']}]({top['apply_link']})\n"
            f"📞 **Toll-Free Helpline:** `{top['helpline']}`\n\n"
            f"💡 *Tip: You can apply online or visit any local Maha e-Seva Kendra (CSC).*\n\n"
            f"---\n\n"
            f"🌐 **मराठी सारांश (Marathi Summary):**\n\n"
            f"🏛️ **{top['title_mr']}**\n"
            f"📌 **तपशील:** {top['description_mr']}\n\n"
            f"💰 **लाभ:** {top['benefits_mr']}\n\n"
            f"👥 **पात्रता:**\n{mr_elig_list}\n\n"
            f"📑 **कागदपत्रे:**\n{mr_doc_list}\n\n"
            f"🔗 **अधिकृत लिंक:** [{top['apply_link']}]({top['apply_link']}) | 📞 **हेल्पलाइन:** `{top['helpline']}`"
        )

    return reply, schemes
