"""
Intelligent Conversational Reasoning Engine for Sarkar Mitra.
Provides human-like, context-aware reasoning for user-specific questions
(e.g., age limits, minor status, income boundaries, document alternatives, validity, fees)
so the bot thinks and answers directly instead of dumping static brochures.
"""

import re
from typing import Optional, Tuple, Dict, Any

def extract_number(pattern: str, text: str) -> Optional[float]:
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        try:
            return float(match.group(1))
        except Exception:
            return None
    return None

def detect_scheme_from_context(query: str, history: list, schemes_data: list) -> Optional[dict]:
    """Infers the active scheme from current query or prior conversation history."""
    q_lower = query.lower()
    
    # 1. Direct keywords in query
    for s in schemes_data:
        for kw in s.get("keywords", []):
            if re.search(r'\b' + re.escape(kw.lower()) + r'\b', q_lower):
                return s
        if any(w in s["title"].lower() for w in q_lower.split() if len(w) > 3):
            return s
        if any(w in s["title_mr"] for w in q_lower.split() if len(w) > 3):
            return s

    # 2. Pronouns or generic phrases ("this certificate", "this scheme", "it", "या योजनेसाठी", "हा दाखला")
    is_referring_to_context = any(p in q_lower for p in [
        "this certificate", "this scheme", "this", "it", "for this", "apply for this",
        "या दाखल्यासाठी", "या योजनेसाठी", "हा दाखला", "ही योजना", "याच्यासाठी"
    ]) or "certificate" in q_lower or "दाखला" in q_lower or "योजना" in q_lower

    if is_referring_to_context and history:
        for msg in reversed(history):
            content = msg.get("content", "").lower()
            for s in schemes_data:
                if s["id"] in content or s["title"].lower() in content or s["title_mr"] in content:
                    return s
            if "उत्पन्न" in content or "income" in content:
                for s in schemes_data:
                    if s["id"] == "income_certificate":
                        return s
            if "लाडकी बहीण" in content or "ladki bahin" in content:
                for s in schemes_data:
                    if s["id"] == "ladki_bahin":
                        return s
            if "pm kisan" in content or "किसान" in content:
                for s in schemes_data:
                    if s["id"] == "pm_kisan":
                        return s
            if "7/12" in content or "सातबारा" in content:
                for s in schemes_data:
                    if s["id"] == "digital_712":
                        return s

    return None


def reason_on_user_question(query: str, history: list, schemes_data: list, language: str = "auto") -> Tuple[Optional[str], Optional[dict]]:
    """
    Evaluates the user's specific context (age, income, land, document issues)
    and produces a thinking, direct, conversational answer like ChatGPT or Claude.
    Returns (reply_text, matched_scheme) or (None, None) if generic.
    """
    q_lower = query.lower().strip()
    is_marathi = language == "mr" or any(0x0900 <= ord(c) <= 0x097F for c in query)
    
    # Infer active scheme
    scheme = detect_scheme_from_context(query, history, schemes_data)
    scheme_id = scheme.get("id") if scheme else None

    # Extract Age signals
    age_match = re.search(r'\b(?:i am|age|am|my age is|i\'m)\s*(\d{1,2})\b', q_lower) or \
                re.search(r'\b(\d{1,2})\s*(?:years old|year old|yr old|वर्षांचा|वर्षांची|वय)\b', q_lower)
    age = int(age_match.group(1)) if age_match else None
    
    is_asking_eligibility = any(w in q_lower for w in [
        "can i apply", "am i eligible", "eligible", "apply", "can i get",
        "मी अर्ज करू शकतो का", "पात्र आहे का", "मिळेल का", "अर्ज करता येईल का"
    ])

    # ─── CASE 1: AGE & MINOR ELIGIBILITY ─────────────────────────────────────
    if (age is not None or "minor" in q_lower or "लहान" in q_lower) and is_asking_eligibility:
        
        # 1A. Minor asking about Income Certificate
        if scheme_id == "income_certificate" or (scheme_id is None and ("certificate" in q_lower or "दाखला" in q_lower or "income" in q_lower)):
            if age is not None and age < 18 or "minor" in q_lower:
                age_str = f"{age} years old" if age else "a minor"
                age_mr_str = f"वय {age} वर्षे" if age else "अल्पवयीन (१८ वर्षांखालील)"
                
                reply_en = f"""### 👤 Can you apply for an Income Certificate at {age_str}?

**Direct Answer:** **YES, you can obtain an Income Certificate for educational and scholarship purposes, BUT as a minor (under 18), you cannot submit the application independently in your own name.**

---

#### 🔍 Why and How it Works:
1. **Legal Minor Status:**
   - Anyone under 18 does not have an independent taxable or legal earning status.
   - In Maharashtra, the Tahsildar Income Certificate is **always issued based on the family's annual income** (parents' income).
2. **Who Must Apply:**
   - Your **father, mother, or legal guardian** must submit the application on the **Aaple Sarkar portal** as the primary applicant (Head of Family).
   - In the application form under *"Reason for Certificate"*, they select **"Child's Education / School Admission / Scholarship"** and your name will be clearly endorsed on the certificate as the beneficiary student.

---

#### 📑 Documents You & Your Parents Need:
1. **Parent's Documents:**
   - Father's/Mother's Aadhaar Card
   - Proof of Income: Salary Slip, Form 16, IT Return, or **Talathi Income Report / Self-Declaration (स्वयंघोषणापत्र)**
   - Ration Card (showing your name as a family member)
2. **Student's Documents:**
   - Your School Bonafide Certificate / School ID / Birth Certificate
   - Your Aadhaar Card

---

#### 🌐 How to Apply:
- Online: [aaplesarkar.mahaonline.gov.in](https://aaplesarkar.mahaonline.gov.in) (under Revenue Department $\to$ Income Certificate)
- Offline: Visit any local **Aaple Sarkar Seva Kendra (CSC)** with your parent
- **Govt Fee:** ₹33.60 | **Validity:** 1 Year or 3 Years (choose 3 years for continuous scholarship benefits)."""

                reply_mr = f"""### 👤 {age_mr_str} असताना उत्पन्न दाखल्यासाठी अर्ज करता येतो का?

**थेट उत्तर:** **होय, शिक्षणासाठी आणि शिष्यवृत्तीसाठी तुम्हाला उत्पन्न दाखला मिळू शकतो; परंतु तुम्ही १८ वर्षांखालील (अल्पवयीन) असल्याने स्वतःच्या नावावर थेट अर्ज करू शकत नाही.**

---

#### 🔍 नियम आणि कार्यपद्धत:
1. **अल्पवयीन व्यक्तीचे नियम:**
   - १८ वर्षांखालील व्यक्तीचे स्वतंत्र उत्पन्न ग्राह्य धरले जात नाही. उत्पन्न दाखला नेहमी **कौटुंबिक उत्पन्नावर (पालकांच्या उत्पन्नावर)** दिला जातो.
2. **अर्ज कोणी करावा?**
   - तुमच्या **वडिलांनी, आईने किंवा कायदेशीर पालकांनी** 'आपले सरकार' पोर्टलवर कुटुंबप्रमुख म्हणून अर्ज करणे आवश्यक आहे.
   - अर्जामध्ये दाखल्याचे कारण *"मुलाच्या/मुलीच्या शिक्षणासाठी किंवा शिष्यवृत्तीसाठी"* असे निवडून लाभार्थी म्हणून तुमचे नाव नमूद केले जाते.

---

#### 📑 आवश्यक कागदपत्रे:
1. **पालकांची कागदपत्रे:** आधार कार्ड, रेशन कार्ड (ज्यात तुमचे नाव आहे), पगाराची पावती किंवा तलाठी उत्पन्न अहवाल / स्वयंघोषणापत्र.
2. **विद्यार्थ्याची कागदपत्रे:** शाळेचे बोनाफाईड प्रमाणपत्र / ओळखपत्र आणि आधार कार्ड.

---

#### 🌐 अर्ज कुठे करावा?
- अधिकृत पोर्टल: [aaplesarkar.mahaonline.gov.in](https://aaplesarkar.mahaonline.gov.in)
- किंवा जवळच्या **आपले सरकार सेवा केंद्रावर** पालकांसोबत जाऊन अर्ज सादर करा.
- **शासकीय शुल्क:** ₹३३.६० | **कालावधी:** १ किंवा ३ वर्षांसाठी वैध."""

                if is_marathi:
                    return f"{reply_mr}\n\n---\n\n🌐 **English Translation & Summary:**\n\n{reply_en}", scheme
                else:
                    return f"{reply_en}\n\n---\n\n🌐 **मराठी सारांश (Marathi Summary):**\n\n{reply_mr}", scheme

        # 1B. Minor / under-age asking about Ladki Bahin Yojana
        elif scheme_id == "ladki_bahin":
            if age is not None and (age < 21 or age > 65):
                status_text = "below the minimum age of 21" if age < 21 else "above the maximum age limit of 65"
                reply_en = f"""### 👩 Age Eligibility for Mukhyamantri Majhi Ladki Bahin Yojana

**Direct Answer:** **NO, at {age} years of age, you are unfortunately NOT eligible for Mukhyamantri Majhi Ladki Bahin Yojana because you are {status_text}.**

---

#### 📋 Strict Age Criteria under Government Resolution (GR):
- **Minimum Age:** 21 Years (completed on the cut-off date).
- **Maximum Age:** 65 Years.

---

#### 💡 Alternative Schemes for Students / Girls under 21:
If you are under 21 years old in Maharashtra, you can benefit from:
1. **Lek Ladki Yojana (लेक लाडकी योजना):** Financial assistance of up to ₹1,01,000 provided at stages (birth, school admission, 18 years of age) for yellow/orange ration card families.
2. **MahaDBT Post-Matric Scholarships:** 100% tuition and exam fee reimbursement for higher education.
3. **Free Higher Education for Girls:** 100% tuition fee waiver for girls in government and aided colleges pursuing professional degrees."""

                reply_mr = f"""### 👩 माझी लाडकी बहीण योजनेसाठी वयाची पात्रता

**थेट उत्तर:** **नाही, तुमचे वय {age} वर्षे असल्याने तुम्ही 'मुख्यमंत्री माझी लाडकी बहीण योजने'साठी पात्र नाही.**

---

#### 📋 शासन निर्णयानुसार (GR) वयाचे निकष:
- **किमान वय:** २१ वर्षे पूर्ण असावे.
- **कमाल वय:** ६५ वर्षांपर्यंत.

---

#### 💡 २१ वर्षांखालील मुलींसाठी इतर महत्त्वाच्या योजना:
1. **लेक लाडकी योजना:** पिवळे/केशरी रेशन कार्डधारक कुटुंबातील मुलींना टप्प्याटप्प्याने एकूण ₹१,०१,००० ची आर्थिक मदत.
2. **महाडीबीटी शिष्यवृत्ती:** १० वी व १२ वी नंतरच्या उच्च शिक्षणासाठी मोफत शिक्षण व परीक्षा फी माफी.
3. **मुलींसाठी मोफत उच्च शिक्षण योजना:** व्यावसायिक पदवी शिक्षणासाठी १००% फी माफी."""

                if is_marathi:
                    return f"{reply_mr}\n\n---\n\n🌐 **English Translation:**\n\n{reply_en}", scheme
                else:
                    return f"{reply_en}\n\n---\n\n🌐 **मराठी सारांश:**\n\n{reply_mr}", scheme

        # 1C. Minor asking about PM Kisan / Namo Shetkari
        elif scheme_id == "pm_kisan":
            if age is not None and age < 18:
                reply_en = f"""### 🌾 Can a {age}-Year-Old Minor Apply for PM Kisan / Namo Shetkari?

**Direct Answer:** **Generally NO. PM Kisan and Namo Shetkari require the applicant to be an adult farmer with cultivable land registered in their own name in the state land records (7/12 & 8-A extract).**

- **Exception:** If a minor has inherited agricultural land as a legal heir due to the demise of parents, the land is recorded in the 7/12 extract through a legal guardian (*पालक*). In such rare cases, the legal guardian can apply on behalf of the minor beneficiary family."""
                reply_mr = f"""### 🌾 वय {age} वर्षे असताना पीएम किसान योजनेचा लाभ मिळतो का?

**थेट उत्तर:** **सामान्यतः नाही. पीएम किसान योजनेसाठी अर्जदाराचे स्वतःच्या नावावर शेतजमीन (७/१२ उतारा) असणे आणि वय १८ वर्षे पूर्ण असणे आवश्यक आहे.**

- **अपवाद:** पालकांच्या पश्चात अल्पवयीन मुलांच्या नावावर वारसा हक्काने शेतजमीन असल्यास, कायदेशीर पालकांच्या देखरेखीखाली लाभ मिळू शकतो."""
                if is_marathi:
                    return f"{reply_mr}\n\n---\n\n🌐 **English Translation:**\n\n{reply_en}", scheme
                else:
                    return f"{reply_en}\n\n---\n\n🌐 **मराठी सारांश:**\n\n{reply_mr}", scheme

    # ─── CASE 2: INCOME LIMIT QUERIES ────────────────────────────────────────
    income_val = extract_number(r'(?:income|उत्पन्न|earning)\s*(?:is|of|around)?\s*(\d+(?:\.\d+)?)\s*(?:lakh|lac|लाख)', q_lower)
    if income_val is not None:
        if scheme_id == "ladki_bahin":
            if income_val > 2.5:
                reply_en = f"""### 💰 Income Limit Check: Mukhyamantri Majhi Ladki Bahin Yojana

**Question:** *Family income is ₹{income_val} Lakh/year. Are you eligible?*

**Direct Answer:** **If your family annual income is ₹{income_val} Lakh, you EXCEED the official ₹2.50 Lakh income cap.**

- **CRITICAL EXCEPTION:** If your family holds a **Yellow (पिवळे)** or **Orange (केशरी)** Ration Card, you are **EXEMPT** from providing an income certificate, and you **ARE ELIGIBLE** regardless!
- Only families with a **White (पांढरे) Ration Card** or taxpayers earning above ₹2.5 Lakh are strictly excluded."""

                reply_mr = f"""### 💰 उत्पन्न मर्यादा तपासणी: माझी लाडकी बहीण योजना

**प्रश्न:** *कौटुंबिक उत्पन्न ₹{income_val} लाख आहे, मी पात्र आहे का?*

**थेट उत्तर:** **नियमानुसार कौटुंबिक वार्षिक उत्पन्न ₹२.५ लाखांपेक्षा जास्त असल्यास थेट पात्र ठरत नाही.**

- **महत्त्वाचा अपवाद:** जर तुमच्या कुटुंबाकडे **पिवळे किंवा केशरी रेशन कार्ड** असेल, तर उत्पन्नाचा दाखला देण्याची आवश्यकता नाही; तुम्ही थेट **पात्र आहात**!
- केवळ पांढरे रेशन कार्डधारक आणि आयकर (Income Tax) भरणाऱ्या कुटुंबांना या योजनेचा लाभ मिळत नाही."""

                if is_marathi:
                    return f"{reply_mr}\n\n---\n\n🌐 **English Translation:**\n\n{reply_en}", scheme
                else:
                    return f"{reply_en}\n\n---\n\n🌐 **मराठी सारांश:**\n\n{reply_mr}", scheme

    # ─── CASE 3: MISSING DOCUMENTS OR RECOVERY ──────────────────────────────
    if any(w in q_lower for w in ["lost", "don't have", "do not have", "nahi aahe", "नाही", "गहाळ", "हरवले", "नसल्यास"]):
        if "domicile" in q_lower or "अधिवास" in q_lower:
            reply_en = f"""### 📄 What if you don't have a Domicile Certificate (अधिवास प्रमाणपत्र)?

**Direct Answer:** For most Maharashtra schemes (including Ladki Bahin and college admissions), the government allows **valid alternatives** in place of a Domicile Certificate:

1. **Ration Card issued at least 15 years ago** in Maharashtra.
2. **School Leaving Certificate (TC / LC)** showing birthplace in Maharashtra.
3. **Birth Certificate** issued by a Maharashtra Gram Panchayat or Municipal Corporation.
4. **Voter ID Card** showing Maharashtra address for 15+ years."""

            reply_mr = f"""### 📄 डोमिसिल (अधिवास) प्रमाणपत्र नसल्यास काय करावे?

**थेट उत्तर:** जर तुमच्याकडे अधिवास प्रमाणपत्र नसेल, तर शासन निर्णयानुसार खालीलपैकी कोणताही एक पुरावा ग्राह्य धरला जातो:

१. **१५ वर्षे जुने रेशन कार्ड**
२. **शाळा सोडल्याचा दाखला (LC / TC)** - ज्यावर महाराष्ट्रातील जन्मस्थळाची नोंद आहे.
३. **ग्रामपंचायत किंवा महानगरपालिकेचा जन्म दाखला**
४. **१५ वर्षे जुने मतदार ओळखपत्र (Election Card)**"""

            if is_marathi:
                return f"{reply_mr}\n\n---\n\n🌐 **English Translation:**\n\n{reply_en}", scheme
            else:
                return f"{reply_en}\n\n---\n\n🌐 **मराठी सारांश:**\n\n{reply_mr}", scheme

    # ─── CASE 4: FEES, VALIDITY & DURATION ──────────────────────────────────
    if any(w in q_lower for w in ["fee", "fees", "cost", "validity", "how long", "valid", "कालावधी", "शुल्क", "फी", "मुदत"]):
        if scheme_id == "income_certificate":
            reply_en = """### ⏱️ Income Certificate: Validity, Fees & Processing Time

1. **Government Fee:** ₹33.60 on the official Aaple Sarkar portal (Maha e-Seva Kendras may charge up to ₹50).
2. **Validity Period:**
   - **1-Year Certificate:** Valid for the current Financial Year (1st April to 31st March).
   - **3-Year Certificate:** Valid for 3 consecutive Financial Years (recommended for students applying for multi-year scholarships).
3. **Processing Time:** Legally mandated delivery within **15 business days** under the *Maharashtra Right to Public Services Act (RTS)*."""
            reply_mr = """### ⏱️ उत्पन्न दाखला: शासकीय शुल्क, मुदत आणि वेळ

१. **शासकीय शुल्क:** 'आपले सरकार' पोर्टलवर फक्त **₹३३.६०** (आपले सरकार सेवा केंद्रावर साधारण ₹५० पर्यंत).
२. **वैधता मुदत:**
   - **१ वर्षाचा दाखला:** चालू आर्थिक वर्षासाठी (१ एप्रिल ते ३१ मार्च) वैध.
   - **३ वर्षांचा दाखला:** सलग ३ आर्थिक वर्षांसाठी वैध (विद्यार्थ्यांनी शिष्यवृत्तीसाठी ३ वर्षांचा दाखला काढणे फायदेशीर).
३. **मिळण्याचा कालावधी:** महाराष्ट्र लोकसेवा हमी कायद्यानुसार **१५ कामकाजाच्या दिवसांत** दाखला मिळणे बंधनकारक आहे."""

            if is_marathi:
                return f"{reply_mr}\n\n---\n\n🌐 **English Translation:**\n\n{reply_en}", scheme
            else:
                return f"{reply_en}\n\n---\n\n🌐 **मराठी सारांश:**\n\n{reply_mr}", scheme

    return None, None
