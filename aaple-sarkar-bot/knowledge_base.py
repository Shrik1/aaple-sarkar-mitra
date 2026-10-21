"""
Knowledge base for Aaple Sarkar government schemes.
Contains verified information about Maharashtra government schemes and services.
"""

SCHEMES_DATA = [
    {
        "id": "pm_kisan",
        "title": "PM Kisan Samman Nidhi",
        "title_mr": "पीएम किसान सन्मान निधी",
        "category": "Agriculture / शेती",
        "description": "PM Kisan provides income support of Rs. 6,000 per year in three equal instalments to all land holding farmer families.",
        "description_mr": "पीएम किसान योजनेत सर्व जमीनधारक शेतकरी कुटुंबांना वर्षाला ₹6,000 तीन समान हप्त्यांमध्ये दिले जातात.",
        "eligibility": [
            "Must be a small/marginal farmer",
            "Must own cultivable land",
            "Family annual income must be below Rs. 2 lakh",
            "Must not be a government employee",
            "Must not be an income tax payer"
        ],
        "eligibility_mr": [
            "लघु/अल्पभूधारक शेतकरी असणे आवश्यक",
            "लागवडीयोग्य जमीन असणे आवश्यक",
            "कौटुंबिक वार्षिक उत्पन्न ₹2 लाखांपेक्षा कमी असावे",
            "सरकारी कर्मचारी नसावे",
            "आयकर भरत नसावे"
        ],
        "benefits": "Rs. 6,000 per year (₹2,000 every 4 months)",
        "benefits_mr": "दरवर्षी ₹6,000 (दर 4 महिन्यांनी ₹2,000)",
        "documents": ["Aadhaar Card", "Land Records (7/12 Utara)", "Bank Account Details", "Mobile Number"],
        "documents_mr": ["आधार कार्ड", "जमीन नोंद (७/१२ उतारा)", "बँक खाते तपशील", "मोबाईल नंबर"],
        "apply_link": "https://pmkisan.gov.in",
        "helpline": "155261",
        "keywords": ["pm kisan", "किसान", "farmer", "शेतकरी", "6000", "subsidy", "अनुदान", "pm kisan eligibility"]
    },
    {
        "id": "mahatma_phule_krishi",
        "title": "Mahatma Phule Krishi Karj Mafi Yojana",
        "title_mr": "महात्मा फुले कृषी कर्जमाफी योजना",
        "category": "Agriculture / शेती",
        "description": "Loan waiver scheme for farmers in Maharashtra who have outstanding agricultural loans.",
        "description_mr": "महाराष्ट्रातील शेतकऱ्यांसाठी थकीत कृषी कर्ज माफ करण्याची योजना.",
        "eligibility": [
            "Maharashtra resident farmer",
            "Has outstanding agricultural loan from cooperative/nationalized bank",
            "Loan taken before a cutoff date specified by state govt"
        ],
        "eligibility_mr": [
            "महाराष्ट्राचे रहिवासी शेतकरी",
            "सहकारी/राष्ट्रीयकृत बँकेचे थकीत कृषी कर्ज असणे",
            "राज्य सरकारने ठरवलेल्या कट-ऑफ तारखेपूर्वी घेतलेले कर्ज"
        ],
        "benefits": "Loan waiver up to Rs. 2 lakh",
        "benefits_mr": "₹2 लाखांपर्यंत कर्जमाफी",
        "documents": ["Aadhaar Card", "7/12 Land Record", "Loan Documents", "Bank Passbook"],
        "documents_mr": ["आधार कार्ड", "७/१२ उतारा", "कर्ज दस्तावेज", "बँक पासबुक"],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1800-120-8040",
        "keywords": ["karj mafi", "कर्जमाफी", "loan waiver", "कर्ज", "farmer loan", "sheti karj"]
    },
    {
        "id": "ladki_bahin",
        "title": "Mukhyamantri Ladki Bahin Yojana",
        "title_mr": "मुख्यमंत्री लाडकी बहीण योजना",
        "category": "Women Welfare / महिला कल्याण",
        "description": "Monthly financial assistance scheme for women in Maharashtra to improve their economic and social status.",
        "description_mr": "महाराष्ट्रातील महिलांच्या आर्थिक व सामाजिक स्थितीत सुधारणा करण्यासाठी मासिक आर्थिक सहाय्य योजना.",
        "eligibility": [
            "Age between 21 to 65 years",
            "Maharashtra domicile",
            "Annual family income below Rs. 2.5 lakh",
            "Must not be a government employee",
            "Must not be an income tax payer"
        ],
        "eligibility_mr": [
            "वय २१ ते ६५ वर्षांदरम्यान",
            "महाराष्ट्राचे अधिवास प्रमाणपत्र",
            "वार्षिक कौटुंबिक उत्पन्न ₹२.५ लाखांपेक्षा कमी",
            "सरकारी कर्मचारी नसाव्या",
            "आयकर भरत नसाव्या"
        ],
        "benefits": "Rs. 1,500 per month directly to bank account",
        "benefits_mr": "दरमहा ₹1,500 थेट बँक खात्यात",
        "documents": ["Aadhaar Card", "Domicile Certificate", "Income Certificate", "Bank Account", "Mobile Number"],
        "documents_mr": ["आधार कार्ड", "अधिवास प्रमाणपत्र", "उत्पन्न प्रमाणपत्र", "बँक खाते", "मोबाईल नंबर"],
        "apply_link": "https://ladakibahin.maharashtra.gov.in",
        "helpline": "1800-212-4526",
        "keywords": ["ladki bahin", "लाडकी बहीण", "women scheme", "महिला योजना", "1500", "monthly", "मासिक"]
    },
    {
        "id": "mahaswayam",
        "title": "Mahaswayam Employment Portal",
        "title_mr": "महास्वयम रोजगार पोर्टल",
        "category": "Employment / रोजगार",
        "description": "One-stop employment portal by Maharashtra government connecting job seekers with employers and skill development programs.",
        "description_mr": "नोकरी शोधणाऱ्यांना नियोक्त्यांशी आणि कौशल्य विकास कार्यक्रमांशी जोडणारे महाराष्ट्र सरकारचे एकात्मिक रोजगार पोर्टल.",
        "eligibility": [
            "Maharashtra resident",
            "Age 18 years and above",
            "Job seekers, employers, or skill training seekers"
        ],
        "eligibility_mr": [
            "महाराष्ट्राचे रहिवासी",
            "वय १८ वर्षे व त्यावरील",
            "नोकरी शोधणारे, नियोक्ते, किंवा कौशल्य प्रशिक्षण इच्छुक"
        ],
        "benefits": "Access to jobs, skill training, and career guidance",
        "benefits_mr": "नोकऱ्या, कौशल्य प्रशिक्षण, आणि करिअर मार्गदर्शन",
        "documents": ["Aadhaar Card", "Educational Certificates", "Resume"],
        "documents_mr": ["आधार कार्ड", "शैक्षणिक प्रमाणपत्रे", "रेझ्युमे"],
        "apply_link": "https://mahaswayam.in",
        "helpline": "1800-233-3666",
        "keywords": ["job", "नोकरी", "employment", "रोजगार", "skill", "कौशल्य", "mahaswayam"]
    },
    {
        "id": "ration_card",
        "title": "Ration Card / Public Distribution System",
        "title_mr": "रेशन कार्ड / सार्वजनिक वितरण प्रणाली",
        "category": "Food Security / अन्न सुरक्षा",
        "description": "Ration card provides subsidized food grains (rice, wheat, sugar) to eligible families through fair price shops.",
        "description_mr": "रेशन कार्डद्वारे पात्र कुटुंबांना स्वस्त दराने अन्नधान्य (तांदूळ, गहू, साखर) स्वस्त धान्य दुकानांतून मिळते.",
        "eligibility": [
            "Maharashtra domicile",
            "Annual income below Rs. 1 lakh (APL/BPL criteria)",
            "Not already having a ration card in any state"
        ],
        "eligibility_mr": [
            "महाराष्ट्राचे अधिवास",
            "वार्षिक उत्पन्न ₹1 लाखांपेक्षा कमी",
            "कोणत्याही राज्यात आधीच रेशन कार्ड नसावे"
        ],
        "benefits": "Subsidized food grains at Rs. 2-3 per kg",
        "benefits_mr": "₹2-3 प्रति किलो दराने स्वस्त धान्य",
        "documents": ["Aadhaar Card", "Proof of Residence", "Income Certificate", "Family Photo", "Mobile Number"],
        "documents_mr": ["आधार कार्ड", "निवास पुरावा", "उत्पन्न प्रमाणपत्र", "कुटुंब फोटो", "मोबाईल नंबर"],
        "apply_link": "https://rcms.mahafood.gov.in",
        "helpline": "1967",
        "keywords": ["ration", "रेशन", "food", "अन्न", "ration card", "BPL", "APL", "wheat", "rice", "गहू", "तांदूळ"]
    },
    {
        "id": "seven_twelve_utara",
        "title": "7/12 Satbara Utara (Land Record)",
        "title_mr": "सातबारा उतारा (जमीन नोंद)",
        "category": "Land Records / जमीन नोंदी",
        "description": "7/12 Utara is an official land record document issued by Maharashtra Revenue Department showing ownership and land details.",
        "description_mr": "७/१२ उतारा हे महाराष्ट्र महसूल विभागाने जारी केलेले अधिकृत जमीन नोंद दस्तावेज आहे जे मालकी व जमीन तपशील दर्शवते.",
        "eligibility": [
            "Any person who owns land in Maharashtra",
            "Any person with legitimate interest in land records"
        ],
        "eligibility_mr": [
            "महाराष्ट्रात जमीन मालकी असलेली कोणतीही व्यक्ती",
            "जमीन नोंदींमध्ये वैध रस असलेली कोणतीही व्यक्ती"
        ],
        "benefits": "Official proof of land ownership",
        "benefits_mr": "जमीन मालकीचा अधिकृत पुरावा",
        "documents": ["Survey Number", "Village Name", "District Name"],
        "documents_mr": ["सर्वे नंबर", "गावाचे नाव", "जिल्ह्याचे नाव"],
        "apply_link": "https://digitalsatbara.mahabhumi.gov.in",
        "helpline": "1800-200-5552",
        "keywords": ["7/12", "satbara", "सातबारा", "land record", "जमीन नोंद", "mahabhumi", "utara", "उतारा"]
    },
    {
        "id": "birth_certificate",
        "title": "Birth Certificate",
        "title_mr": "जन्म प्रमाणपत्र",
        "category": "Certificates / प्रमाणपत्रे",
        "description": "Official document certifying the birth of a person, required for school admissions, passports, and other services.",
        "description_mr": "व्यक्तीच्या जन्माचे प्रमाणित करणारे अधिकृत दस्तावेज, शाळा प्रवेश, पासपोर्ट आणि इतर सेवांसाठी आवश्यक.",
        "eligibility": [
            "All citizens born in Maharashtra",
            "Application within 21 days of birth is free",
            "Late registration possible with additional documentation"
        ],
        "eligibility_mr": [
            "महाराष्ट्रात जन्मलेले सर्व नागरिक",
            "जन्माच्या २१ दिवसांत अर्ज केल्यास मोफत",
            "उशीरा नोंदणी अतिरिक्त कागदपत्रांसह शक्य"
        ],
        "benefits": "Official birth certificate document",
        "benefits_mr": "अधिकृत जन्म प्रमाणपत्र",
        "documents": ["Hospital Discharge Summary", "Parent's Aadhaar", "Parent's Marriage Certificate"],
        "documents_mr": ["रुग्णालय डिस्चार्ज सारांश", "पालकांचे आधार", "पालकांचे विवाह प्रमाणपत्र"],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1077",
        "keywords": ["birth certificate", "जन्म प्रमाणपत्र", "janm", "certificate", "जन्म दाखला"]
    },
    {
        "id": "income_certificate",
        "title": "Income Certificate",
        "title_mr": "उत्पन्न प्रमाणपत्र",
        "category": "Certificates / प्रमाणपत्रे",
        "description": "Official certificate issued by Tahsildar showing family annual income, required for various scheme applications.",
        "description_mr": "तहसीलदाराने जारी केलेले कौटुंबिक वार्षिक उत्पन्न दर्शवणारे अधिकृत प्रमाणपत्र, विविध योजनांसाठी आवश्यक.",
        "eligibility": [
            "Any resident of Maharashtra",
            "Needed for scholarship, loan, welfare scheme applications"
        ],
        "eligibility_mr": [
            "महाराष्ट्राचे कोणतेही रहिवासी",
            "शिष्यवृत्ती, कर्ज, कल्याण योजना अर्जांसाठी आवश्यक"
        ],
        "benefits": "Proof of annual family income",
        "benefits_mr": "वार्षिक कौटुंबिक उत्पन्नाचा पुरावा",
        "documents": ["Aadhaar Card", "Ration Card", "Self-Declaration of income", "Salary Slips (if employed)"],
        "documents_mr": ["आधार कार्ड", "रेशन कार्ड", "उत्पन्न स्व-घोषणापत्र", "पगार स्लिप (नोकरी असल्यास)"],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1077",
        "keywords": ["income certificate", "उत्पन्न प्रमाणपत्र", "utpanna", "income proof", "उत्पन्न दाखला"]
    },
    {
        "id": "aaple_sarkar_general",
        "title": "Aaple Sarkar Portal",
        "title_mr": "आपले सरकार पोर्टल",
        "category": "General / सामान्य",
        "description": "Aaple Sarkar is Maharashtra's single-window digital platform for 400+ government services including certificates, schemes, land records, and more.",
        "description_mr": "आपले सरकार हे महाराष्ट्राचे ४०० पेक्षा जास्त सरकारी सेवांसाठी एकल खिडकी डिजिटल व्यासपीठ आहे.",
        "eligibility": ["All citizens of Maharashtra"],
        "eligibility_mr": ["महाराष्ट्राचे सर्व नागरिक"],
        "benefits": "Access to 400+ government services online",
        "benefits_mr": "४०० पेक्षा जास्त सरकारी सेवा ऑनलाइन",
        "documents": ["Aadhaar Card", "Mobile Number for OTP"],
        "documents_mr": ["आधार कार्ड", "OTP साठी मोबाईल नंबर"],
        "apply_link": "https://aaplesarkar.mahaonline.gov.in",
        "helpline": "1800-120-8040",
        "keywords": ["aaple sarkar", "आपले सरकार", "portal", "government", "सरकार", "online service", "ऑनलाइन सेवा"]
    }
]


def search_knowledge_base(query: str) -> list:
    """Search the knowledge base for relevant scheme information."""
    query_lower = query.lower()
    results = []
    
    for scheme in SCHEMES_DATA:
        score = 0
        for keyword in scheme["keywords"]:
            if keyword.lower() in query_lower:
                score += 2
        
        # Also check title and description
        if any(word in scheme["title"].lower() for word in query_lower.split()):
            score += 1
        if any(word in scheme["description"].lower() for word in query_lower.split()):
            score += 1
            
        if score > 0:
            results.append((score, scheme))
    
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:3]]
