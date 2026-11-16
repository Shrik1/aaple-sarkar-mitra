"""
General Knowledge & Custom Questions Engine for Sarkar Mitra.
Provides instant, high-quality, formatted answers for custom academic, technical,
scientific, historical, and general questions (like ChatGPT / Claude),
functioning both offline and as an intelligent fallback when external LLM keys are absent.
"""

import re
from typing import Optional, Tuple

GENERAL_KNOWLEDGE_TOPICS = [
    # ─── 1. COMPUTER SCIENCE, AI & CODING ─────────────────────────────────────
    {
        "keywords": ["quantum computing", "quantum computer", "qubit", "quantum"],
        "title": "Quantum Computing (क्वांटम कॉम्प्युटिंग)",
        "content_en": """### ⚛️ What is Quantum Computing?

**Quantum Computing** is an advanced paradigm of computation that harnesses the principles of quantum mechanics—such as **superposition** and **entanglement**—to process complex information exponentially faster than classical computers.

---

#### 🔑 Key Concepts:
1. **Qubits (Quantum Bits):**
   - Classical computers use **bits** that represent either `0` or `1`.
   - Quantum computers use **qubits**, which can exist as `0`, `1`, or **both simultaneously** due to superposition.
2. **Superposition:**
   - A qubit can be in multiple states at once, allowing a quantum processor to evaluate millions of possibilities in parallel.
3. **Quantum Entanglement:**
   - Two or more qubits can be linked so that the state of one instantly dictates the state of another, no matter how far apart they are.
4. **Quantum Decoherence:**
   - The fragile quantum state is susceptible to environmental noise (heat, electromagnetic fields), which is why quantum processors must be cooled to near absolute zero (-273°C).

---

#### 🚀 Real-World Applications:
- **Cryptography:** Breaking and creating unbreakable encryption algorithms (post-quantum cryptography).
- **Drug Discovery & Healthcare:** Simulating molecular structures at the atomic level to discover new medicines.
- **Financial Modeling:** Optimizing complex global portfolios and risk simulations.
- **Climate & Materials Science:** Designing superconductors, efficient solar panels, and better batteries.

> 💡 *Leading quantum frameworks: IBM Qiskit (Python), Google Cirq, and Microsoft Q#.*""",
        "content_mr": """### ⚛️ क्वांटम कॉम्प्युटिंग म्हणजे काय? (Quantum Computing)

**क्वांटम कॉम्प्युटिंग** हे संगणक शास्त्रातील प्रगत तंत्रज्ञान आहे जे **क्वांटम मेकॅनिक्स** (भौतिकशास्त्राचे नियम) वापरून सामान्य संगणकांपेक्षा लाखो पटीने जलद गतीने कठीण समस्या सोडवू शकते.

---

#### 🔑 मुख्य संकल्पना:
1. **क्युबिट्स (Qubits):**
   - सामान्य संगणक **Bits** (`0` किंवा `1`) वापरतात.
   - क्वांटम संगणक **Qubits** वापरतात, जे एकाच वेळी `0` आणि `1` दोन्ही असू शकतात (**Superposition**).
2. **सुपरपोझिशन (Superposition):**
   - एकाच वेळी अनेक शक्यतांची गणना करण्याची क्षमता.
3. **क्वांटम एन्टँग्लमेंट (Entanglement):**
   - दोन क्युबिट्स एकमेकांशी अशा प्रकारे जोडलेले असतात की एकाची स्थिती बदलल्यास दुसऱ्याची स्थिती त्वरित बदलते.

---

#### 🚀 प्रत्यक्ष उपयोग:
- **वैद्यकीय संशोधन:** नवीन औषधांचे रेणू (Molecules) शोधणे.
- **सुरक्षा व सायबर सुरक्षा:** प्रगत एन्क्रिप्शन सिस्टीम तयार करणे.
- **हवामान अंदाज:** अचूक हवामान बदल आणि आपत्ती व्यवस्थापन."""
    },

    {
        "keywords": ["machine learning", "ml", "artificial intelligence", "ai vs ml", "deep learning"],
        "title": "Artificial Intelligence & Machine Learning (AI व ML)",
        "content_en": """### 🤖 Artificial Intelligence vs Machine Learning vs Deep Learning

Understanding the relationship between modern AI technologies:

```text
┌────────────────────────────────────────────────────────┐
│  ARTIFICIAL INTELLIGENCE (Broad Vision)                │
│  Systems capable of performing tasks requiring human   │
│  intelligence (vision, speech, reasoning).             │
│  ┌──────────────────────────────────────────────────┐  │
│  │  MACHINE LEARNING (Technique)                    │  │
│  │  Algorithms that learn patterns directly from    │  │
│  │  data without being explicitly programmed.       │  │
│  │  ┌────────────────────────────────────────────┐  │  │
│  │  │  DEEP LEARNING (Multi-layer Networks)      │  │  │
│  │  │  Deep neural networks modeled loosely      │  │  │
│  │  │  after the human brain (LLMs, Vision, etc) │  │  │
│  │  └────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

---

#### 📊 The 3 Types of Machine Learning:
1. **Supervised Learning (पर्यवेक्षित शिक्षण):**
   - Trained on labeled data (`Input → Correct Output`).
   - *Examples:* Spam email detection, house price prediction, medical diagnosis.
   - *Algorithms:* Linear Regression, Decision Trees, Random Forests, SVM.
2. **Unsupervised Learning (अनिर्देशित शिक्षण):**
   - Discovers hidden patterns in unlabeled data.
   - *Examples:* Customer segmentation, anomaly detection, recommendation engines.
   - *Algorithms:* K-Means Clustering, PCA, Autoencoders.
3. **Reinforcement Learning (बक्षीस आधारित शिक्षण):**
   - Agents learn by trial-and-error to maximize a reward signal.
   - *Examples:* AlphaGo, self-driving cars, robotics control.

---

#### 💻 Essential Tech Stack for AI/ML:
- **Languages:** Python (dominant), C++, Julia, R.
- **Key Libraries:** PyTorch, TensorFlow, Scikit-Learn, Pandas, NumPy.
- **Modern GenAI:** Transformers, LangChain, Gemini API, HuggingFace.""",
        "content_mr": """### 🤖 कृत्रिम बुद्धिमत्ता (AI) आणि मशीन लर्निंग (ML)

**AI (Artificial Intelligence):** मानवाप्रमाणे विचार, विश्लेषण आणि निर्णय घेण्याची क्षमता संगणकात निर्माण करणारे विज्ञान.

**ML (Machine Learning):** AI चा एक भाग, ज्यामध्ये संगणकाला कोड न लिहिता डेटावरून शिकवले जाते.

---

#### 📊 मशीन लर्निंगचे ३ मुख्य प्रकार:
1. **Supervised Learning:** लेबल केलेल्या डेटावरून शिकणे (उदा. ईमेल स्पॅम ओळखणे).
2. **Unsupervised Learning:** न सांगता डेटामधील छुपे पॅटर्न शोधणे (उदा. ग्राहक वर्गवारी).
3. **Reinforcement Learning:** चुका आणि बक्षीस (Reward) पद्धतीतून शिकणे (उदा. बुद्धिबळ किंवा रोबोटिक्स)."""
    },

    {
        "keywords": ["python", "python programming", "learn python", "python code", "reverse string"],
        "title": "Python Programming Language (पायथॉन प्रोग्रामिंग)",
        "content_en": """### 🐍 Python Programming Essentials

**Python** is a high-level, interpreted, general-purpose programming language known for its clear syntax and exceptional versatility across Web Development, Data Science, AI, Automation, and Scripting.

---

#### 💻 Code Examples:

##### 1. String Manipulation & Reversal:
```python
# Reversing a string in Python
text = "Sarkar Mitra"
reversed_text = text[::-1]
print(reversed_text)  # Output: artiM rakraS

# Check palindrome
def is_palindrome(s: str) -> bool:
    clean = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

print(is_palindrome("Madam, in Eden, I'm Adam"))  # Output: True
```

##### 2. List Comprehensions & Dictionaries:
```python
# Square only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Dictionary sorting by value
scores = {"Amit": 88, "Pooja": 95, "Rahul": 79}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)  # {'Pooja': 95, 'Amit': 88, 'Rahul': 79}
```

##### 3. Object-Oriented Programming (OOP):
```python
class Citizen:
    def __init__(self, name: str, district: str):
        self.name = name
        self.district = district

    def greet(self):
        return f"Namaskar {self.name} from {self.district}!"

c = Citizen("Sachin", "Pune")
print(c.greet())
```

---

#### 🌟 Why Python is #1 in 2026:
- **Clean Readability:** Reads almost like plain English.
- **Massive Ecosystem:** FastAPI, Django, NumPy, Pandas, PyTorch, Google GenAI.
- **Cross-Platform:** Runs seamlessly on Windows, Linux, macOS, and Cloud.""",
        "content_mr": """### 🐍 पायथॉन प्रोग्रामिंग (Python Programming)

**पायथॉन** ही जगातील सर्वात लोकप्रिय आणि शिकायला अत्यंत सोपी प्रोग्रामिंग भाषा आहे.

#### 💡 मुख्य वैशिष्ट्ये:
- इंग्रजीसारखी सोपी वाक्यरचना (Clean Syntax).
- AI, डेटा सायन्स, वेब डेव्हलपमेंट (FastAPI/Django) मध्ये सर्वाधिक वापर.
- मोफत आणि ओपन सोर्स.

#### 📝 सोपे उदाहरण (String उलट करणे):
```python
name = "महाराष्ट्र"
reversed_name = name[::-1]
print(reversed_name)
```"""
    },

    {
        "keywords": ["sql", "database", "rdbms", "relational database", "nosql", "query"],
        "title": "SQL & Relational Databases (एसक्यूएल व डेटाबेस)",
        "content_en": """### 🗄️ SQL & Modern Database Systems

**SQL (Structured Query Language)** is the standard language for storing, manipulating, and retrieving data stored in relational database management systems (RDBMS).

---

#### 📋 Core SQL Commands Cheat Sheet:

##### 1. Data Definition (DDL):
```sql
-- Create a Citizen Table
CREATE TABLE citizens (
    citizen_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    aadhaar_last4 CHAR(4),
    district VARCHAR(50) DEFAULT 'Maharashtra',
    annual_income DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

##### 2. Data Manipulation (CRUD):
```sql
-- Insert
INSERT INTO citizens (name, aadhaar_last4, district, annual_income)
VALUES ('Pooja Patil', '4589', 'Kolhapur', 180000.00);

-- Query with Filtering and Sorting
SELECT name, district, annual_income 
FROM citizens 
WHERE annual_income <= 250000 
ORDER BY annual_income ASC;

-- Aggregation with GROUP BY
SELECT district, COUNT(*) AS total_beneficiaries, AVG(annual_income) AS avg_income
FROM citizens
GROUP BY district
HAVING COUNT(*) > 5;
```

---

#### ⚖️ SQL (Relational) vs NoSQL:
| Feature | SQL (PostgreSQL, MySQL) | NoSQL (MongoDB, Redis) |
| :--- | :--- | :--- |
| **Data Structure** | Structured Tables, Rows, Columns | JSON Documents, Key-Value, Graphs |
| **Schema** | Rigid, predefined schema | Dynamic, flexible schema |
| **Scaling** | Vertical (scale up compute/RAM) | Horizontal (scale out across clusters) |
| **ACID Compliance** | Strong consistency guaranteed | Often eventual consistency (BASE) |""",
        "content_mr": """### 🗄️ SQL व डेटाबेस व्यवस्थापन

**SQL (Structured Query Language)** डेटाबेसमध्ये माहिती साठवण्यासाठी आणि शोधण्यासाठी वापरली जाते.

#### 📋 मूलभूत ऑपरेशन्स (CRUD):
- **Create (INSERT):** नवीन डेटा जोडणे
- **Read (SELECT):** डेटा शोधणे व पाहणे
- **Update (UPDATE):** माहितीमध्ये बदल करणे
- **Delete (DELETE):** नको असलेला डेटा हटवणे"""
    },

    {
        "keywords": ["data structures", "algorithms", "dsa", "binary search", "linked list", "array"],
        "title": "Data Structures & Algorithms (DSA)",
        "content_en": r"""### ⚡ Data Structures & Algorithms (DSA) Foundation

Mastering DSA is essential for technical interviews, efficient software design, and optimal computation.

---

#### 📚 Essential Data Structures:
1. **Array / List:** Contiguous memory, $O(1)$ random access, $O(n)$ search/insert.
2. **Linked List:** Nodes linked via pointers, $O(1)$ insertion at head, $O(n)$ traversal.
3. **Stack (LIFO):** Last In, First Out (undo operations, call stack, parenthesis matching).
4. **Queue (FIFO):** First In, First Out (print jobs, BFS graph traversal).
5. **Hash Map / Dictionary:** Key-value pairs with average $O(1)$ lookup, insertion, and deletion.
6. **Binary Search Tree (BST):** Left child < parent < right child. Average $O(\log n)$ search.

---

#### 🔍 Binary Search Algorithm ($O(\log n)$):
```python
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Array must be SORTED
arr = [10, 25, 33, 47, 59, 72, 88, 95]
print("Index:", binary_search(arr, 59))  # Output: 4
```

---

#### ⏱️ Big-O Complexity Hierarchy:
$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$$
*(Constant $\to$ Logarithmic $\to$ Linear $\to$ Linearithmic $\to$ Quadratic $\to$ Exponential)*""",
        "content_mr": """### ⚡ डेटा स्ट्रक्चर्स आणि अल्गोरिदम (DSA)

सॉफ्टवेअर प्रोग्रामिंग कार्यक्षम होण्यासाठी डेटा स्ट्रक्चर्स अत्यंत महत्त्वाचे आहेत.

#### 📌 मुख्य डेटा प्रकार:
- **Array:** क्रमाक्रमाने साठवलेला डेटा.
- **Stack (LIFO):** शेवटचा आलेला डेटा प्रथम बाहेर पडतो.
- **Queue (FIFO):** रांगेप्रमाणे पहिला आलेला डेटा प्रथम बाहेर पडतो.
- **Hash Table / Dictionary:** की-व्हॅल्यू (Key-Value) जोडीने जलद शोध घेणे."""
    },

    # ─── 2. SCIENCE, PHYSICS & BIOLOGY ───────────────────────────────────────
    {
        "keywords": ["photosynthesis", "प्रकाशसंश्लेषण", "plants food", "calvin cycle"],
        "title": "Photosynthesis (प्रकाशसंश्लेषण प्रक्रिया)",
        "content_en": r"""### 🌿 How Photosynthesis Works

**Photosynthesis** is the biological process by which green plants, algae, and certain bacteria convert sunlight energy into chemical energy (glucose) using water and carbon dioxide, releasing oxygen as a vital byproduct.

---

#### 🧪 Chemical Equation:
$$6\text{CO}_2 + 6\text{H}_2\text{O} + \text{Light Energy} \xrightarrow{\text{Chlorophyll}} \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2$$
*(Carbon Dioxide + Water + Sunlight $\to$ Glucose + Oxygen)*

---

#### 🔬 The Two Main Stages:
1. **Light-Dependent Reactions (Thylakoid Membrane):**
   - Chlorophyll pigments absorb sunlight photons.
   - Water molecules ($\text{H}_2\text{O}$) are split into hydrogen ions and oxygen ($\text{O}_2$).
   - Generates energy-carrier molecules: **ATP** and **NADPH**.
2. **Light-Independent Reactions / Calvin Cycle (Stroma):**
   - Carbon dioxide ($\text{CO}_2$) is fixed using enzyme **RuBisCO**.
   - Chemical energy from ATP and NADPH converts carbon into **glucose ($\text{C}_6\text{H}_{12}\text{O}_6$)**.

---

#### 🌍 Ecological Significance:
- Produces almost all the atmospheric oxygen on Earth.
- Forms the foundational base of all planetary food chains (primary producers).
- Absorbs millions of metric tons of carbon dioxide, moderating Earth's climate.""",
        "content_mr": """### 🌿 प्रकाशसंश्लेषण प्रक्रिया (Photosynthesis)

**प्रकाशसंश्लेषण** म्हणजे वनस्पती सूर्यप्रकाश, पाणी आणि कार्बन डायऑक्साईडचा वापर करून स्वतःचे अन्न (ग्लुकोज) तयार करतात आणि ऑक्सिजन वायू बाहेर टाकतात.

---

#### 🧪 रासायनिक समीकरण:
$$६\text{CO}_2 + ६\text{H}_2\text{O} + \text{सूर्यप्रकाश} \to \text{C}_6\text{H}_{12}\text{O}_6 (\text{अन्न}) + ६\text{O}_2 (\text{ऑक्सिजन})$$

#### 🔑 महत्त्व:
- पृथ्वीवरील सजीवांना जगण्यासाठी आवश्यक असणारा ऑक्सिजन मिळतो.
- सर्व अन्नसाखळीचा मूळ पाया ही प्रक्रिया आहे."""
    },

    {
        "keywords": ["newton's laws", "newtons law", "laws of motion", "newton law", "गतिविषयक नियम"],
        "title": "Newton's Laws of Motion (न्यूटनचे गतिविषयक नियम)",
        "content_en": r"""### 🍎 Newton's Three Laws of Motion

Formulated by Sir Isaac Newton in 1687, these three laws form the foundation of classical mechanics:

---

#### 1️⃣ First Law: The Law of Inertia (जडत्वाचा नियम)
> *"An object at rest stays at rest, and an object in motion stays in motion at a constant velocity, unless acted upon by a net external force."*
- **Real-World Example:** When a bus suddenly brakes, passengers jerk forward because their bodies resist the change in motion.

---

#### 2️⃣ Second Law: Force and Acceleration (बल आणि प्रवेग)
> *"The rate of change of momentum of a body is directly proportional to the applied force and takes place in the direction of the force."*
$$\mathbf{F} = m \cdot \mathbf{a}$$
- **Formula:** $\text{Force (Newtons)} = \text{Mass (kg)} \times \text{Acceleration (m/s}^2\text{)}$
- **Real-World Example:** Pushing an empty cart requires less force than pushing a heavy loaded cart to reach the same speed.

---

#### 3️⃣ Third Law: Action and Reaction (क्रिया आणि प्रतिक्रिया)
> *"For every action, there is an equal and opposite reaction."*
$$\mathbf{F}_{A \to B} = -\mathbf{F}_{B \to A}$$
- **Real-World Example:** When a rocket fires exhaust gases downward, the equal and opposite reaction propels the rocket upward into space.""",
        "content_mr": """### 🍎 न्यूटनचे तीन गतिविषयक नियम (Newton's Laws of Motion)

#### १. पहिला नियम (जडत्वाचा नियम - Law of Inertia):
कोणत्याही वस्तूवर बाह्य असंतुलित बल कार्य करत नसेल, तर ती वस्तू स्थिर असल्यास स्थिर राहते आणि गतिमान असल्यास सरळ रेषेत गतिमान राहते.
- *उदाहरण:* धावती बस अचानक थांबल्यास प्रवासी पुढे झुकतात.

#### २. दुसरा नियम (बल व प्रवेग - F = m × a):
संवेग परिवर्तनाचा दर प्रयुक्त बलाशी समप्रमाणात असतो आणि संवेगाचे परिवर्तन बलाच्या दिशेने होते.
- *सूत्र:* **बल (Force) = वस्तुमान (Mass) × प्रवेग (Acceleration)**

#### ३. तिसरा नियम (क्रिया व प्रतिक्रिया बल):
प्रत्येक क्रिया बलासाठी तितकेच आणि विरुद्ध दिशेने कार्य करणारे प्रतिक्रिया बल अस्तित्वात असते.
- *उदाहरण:* बंदुकीतून गोळी सुटल्यावर बंदूक पाठीमागे धक्का देते."""
    },

    # ─── 3. MAHARASHTRA HISTORY & CIVICS ─────────────────────────────────────
    {
        "keywords": ["shivaji maharaj", "chhatrapati shivaji", "shivaji", "शिवाजी महाराज", "स्वराज्य"],
        "title": "Chhatrapati Shivaji Maharaj (छत्रपती शिवाजी महाराज)",
        "content_en": """### 🚩 Chhatrapati Shivaji Maharaj (1630 – 1680)

**Chhatrapati Shivaji Maharaj** was the illustrious founder of the **Maratha Empire (Hindavi Swarajya)**, celebrated as one of history's greatest military strategists, administrators, and visionary monarchs.

---

#### ⚔️ Key Milestones & Legacy:
1. **Birth & Oath of Swarajya (1630 / 1645):**
   - Born at Fort Shivneri to Jijabai and Shahaji Raje Bhosale.
   - Took the historic oath of *Hindavi Swarajya* at Raireshwar Temple in 1645 at the young age of 15.
2. **Fortress Architecture & Mastery:**
   - Captured and fortified over 300 forts across Maharashtra (Torna, Raigad, Rajgad, Pratapgad, Sinhagad, Panhala).
   - Pioneered sea forts like **Sindhudurg** and **Vijaydurg**, laying the foundation of the **Indian Navy (Father of the Indian Navy)**.
3. **Guerrilla Warfare (Ganimi Kava):**
   - Perfected asymmetrical warfare utilizing the rugged terrain of the Sahyadri mountains against numerically superior Mughal and Adil Shahi armies.
   - Masterful military triumphs: Battle of Pratapgad (Afzal Khan encounter), Shaista Khan raid at Lal Mahal, and the daring escape from Agra (1666).
4. **Coronation & Progressive Administration (1674):**
   - Crowned as *Chhatrapati* at Raigad on 6th June 1674.
   - Instituted the **Ashta Pradhan Mandal** (council of 8 ministers).
   - Strict protection of farmers, women's honor, zero caste discrimination, and official promotion of Marathi and Sanskrit through the *Rajyavyavahara Kosha*.""",
        "content_mr": """### 🚩 छत्रपती शिवाजी महाराज (१६३० – १६८०)

**छत्रपती शिवाजी महाराज** हे **हिंदवी स्वराज्याचे संस्थापक**, रयतेचे राजे आणि भारतीय नौदलाचे जनक (Father of Indian Navy) आहेत.

---

#### ⚔️ ऐतिहासिक महत्त्वाचे टप्पे:
1. **जन्म व स्वराज्याची शपथ:**
   - जन्म १९ फेब्रुवारी १६३० रोजी किल्ले शिवनेरीवर झाला.
   - वयाच्या अवघ्या १५ व्या वर्षी रायरेश्वराच्या मंदिरात हिंदवी स्वराज्याची शपथ घेतली.
2. **गनिमी कावा (Guerrilla Warfare):**
   - सह्याद्रीच्या डोंगररांगांचा वापर करून बलाढ्य मुघल आणि आदिलशाही सैन्याला धूळ चारली.
   - अफजलखानाचा वध (प्रतापगड), शाहिस्तेखानाची बोटे छाटणे आणि आग्य्राहून सुटका (१६६६).
3. **दुर्ग निर्मिती व जलदुर्ग:**
   - ३०० पेक्षा अधिक किल्ल्यांचे संवर्धन व सिंधुदुर्ग, विजयदुर्ग यांसारख्या अभेद्य जलदुर्गांची निर्मिती.
4. **शिवराज्याभिषेक (६ जून १६७४):**
   - किल्ले रायगडावर शिवराज्याभिषेक झाला.
   - अष्टप्रधान मंडळाची स्थापना, शेतकऱ्यांना कर्जमाफी, महिलांचा सन्मान आणि धार्मिक सहिष्णुतेचे राज्य निर्माण केले."""
    },

    {
        "keywords": ["dr ambedkar", "b r ambedkar", "babasaheb", "आंबेडकर", "संविधान", "constitution"],
        "title": "Dr. B. R. Ambedkar & Constitution (डॉ. बाबासाहेब आंबेडकर)",
        "content_en": """### ⚖️ Dr. B. R. Ambedkar (1891 – 1956)

**Dr. Bhimrao Ramji Ambedkar (Babasaheb)** was a jurist, economist, social reformer, and the **Chief Architect of the Constitution of India**.

---

#### 🌟 Key Contributions:
1. **Father of the Indian Constitution:**
   - Chairman of the Drafting Committee of the Constituent Assembly.
   - Embedded Fundamental Rights, universal adult franchise, abolition of untouchability (Article 17), and gender equality into the legal backbone of India.
2. **Economic Architect:**
   - His doctoral thesis *"The Problem of the Rupee: Its Origin and Its Solution"* provided the conceptual blueprint for the establishment of the **Reserve Bank of India (RBI)** in 1935.
   - Pioneered major river-valley projects (Damodar Valley, Hirakud) and national electricity policy.
3. **Social Liberation & Human Rights:**
   - Mahad Satyagraha (1927) for equal drinking water rights.
   - Champion of the **Hindu Code Bill**, establishing legal property, divorce, and inheritance rights for women.
   - Slogan: *"Educate, Agitate, Organize" (शिका, संघटित व्हा, संघर्ष करा).*""",
        "content_mr": """### ⚖️ भारतरत्न डॉ. बाबासाहेब आंबेडकर (१८९१ – १९५६)

**डॉ. बाबासाहेब आंबेडकर** हे महान अर्थतज्ज्ञ, कायदेपंडित, समाजसुधारक आणि **भारतीय संविधानाचे शिल्पकार** आहेत.

---

#### 🌟 प्रमुख कार्य:
1. **भारतीय संविधान:** संविधानाच्या मसुदा समितीचे अध्यक्ष. स्वातंत्र्य, समता आणि बंधुतेवर आधारित जगातील सर्वात मोठी लोकशाही घडवली.
2. **रिझर्व्ह बँक ऑफ इंडिया (RBI):** बाबासाहेबांच्या 'द प्रॉब्लेम ऑफ द रुपी' या ग्रंथातील सिद्धांतांवरून १९३५ मध्ये RBI ची स्थापना झाली.
3. **स्त्री मुक्ती व हक्क:** हिंदू कोड बिलाद्वारे महिलांना वारसा हक्क, घटस्फोट आणि मालमत्तेत समान हक्क मिळवून दिले.
4. **अमर संदेश:** *"शिका, संघटित व्हा आणि संघर्ष करा."*"""
    },

    # ─── 4. STUDENT, CAREER & PRACTICAL SKILLS ───────────────────────────────
    {
        "keywords": ["resume", "cv", "how to write resume", "job interview", "बायोडाटा", "interview tips"],
        "title": "Resume Writing & Interview Preparation (रेझ्युमे व मुलाखत तयारी)",
        "content_en": """### 📄 How to Build a Standout Resume & Ace Interviews

A high-converting, ATS-friendly resume structure for students and professionals:

---

#### 📝 Ideal 1-Page Resume Layout:
1. **Header:** Full Name | Professional Title | Email | Phone | LinkedIn | GitHub / Portfolio.
2. **Professional Summary:** 2-3 lines summarizing core skills, technical stack, and impactful achievements.
3. **Technical Skills:**
   - *Languages:* Python, JavaScript, SQL, C++.
   - *Frameworks:* FastAPI, React, Node.js.
   - *Tools/Cloud:* Git, Docker, Linux, Cloudflare, Postman.
4. **Projects (The Most Important Section for Freshers):**
   - **Project Name** | *Technologies Used* | [Live Demo / GitHub Link]
   - *Bullet 1:* What problem did it solve? (e.g., "Engineered Sarkar Mitra, a voice-enabled AI assistant for 10M+ citizens...")
   - *Bullet 2:* What tech and performance was achieved? (e.g., "Achieved sub-200ms latency using FastAPI and local RAG caching.")
5. **Education:** Degree, College Name, University, CGPA/Percentage, Graduation Year.
6. **Certifications & Achievements:** Hackathons, academic honors, verified course credentials.

---

#### 🎯 Top 4 Interview Tips (STAR Method):
- When answering behavioral questions, use the **STAR** framework:
  - **S (Situation):** Context of the problem.
  - **T (Task):** What was required of you.
  - **A (Action):** What specific steps you took.
  - **R (Result):** Quantifiable outcome (e.g., "improved speed by 40%").""",
        "content_mr": """### 📄 प्रभावी रेझ्युमे (Resume) व मुलाखत तयारी

#### 📌 रेझ्युमे तयार करण्याचे महत्त्वाचे टप्पे:
1. **संपर्क माहिती:** पूर्ण नाव, मोबाईल, ईमेल, लिंक्डइन (LinkedIn), GitHub प्रोफाइल.
2. **प्रोजेक्ट्स (Projects):** तुम्ही स्वतः तयार केलेले प्रोजेक्ट्स सविस्तर लिहा.
   - उदा. "सरकार मित्र AI बॉट - FastAPI व Python द्वारे शासकीय योजनांचा व्हॉईस बॉट."
3. **तांत्रिक कौशल्ये (Skills):** Python, SQL, Git, वेब डेव्हलपमेंट.
4. **शिक्षण (Education):** पदवी, कॉलेजचे नाव, गुण (CGPA).

#### 🎯 मुलाखतीचे नियम:
- आत्मविश्वासाने आणि स्पष्ट बोला.
- प्रश्नांची उत्तरे थेट आणि उदाहरणांसह द्या."""
    },

    {
        "keywords": ["leave letter", "sick leave", "application letter", "email format", "रजेचा अर्ज"],
        "title": "Formal Leave Application & Email Templates (रजेचा अर्ज / ईमेल)",
        "content_en": """### ✉️ Ready-to-Use Leave Application Templates

#### 1. Professional Email to Manager / Employer (Sick Leave):
```text
Subject: Sick Leave Application — [Your Full Name] — [Date]

Dear [Manager's Name],

I am writing to inform you that I am unwell today due to [fever/illness] and will be unable to attend work on [Date or Date Range].

I have updated my pending tasks and [Colleague's Name] has kindly agreed to cover any urgent client queries during my absence. I will monitor my email periodically for critical matters.

Thank you for your understanding.

Sincerely,
[Your Name]
[Your Designation] | [Contact Number]
```

---

#### 2. Leave Application to College Principal / HOD (Student):
```text
To,
The Head of Department,
Department of Computer Engineering,
[College Name], [City]

Subject: Application for 2 days leave of absence

Respected Sir/Madam,

I am [Your Name], a student of [Class/Year, e.g., BE Computer, Roll No. 42]. I am writing to respectfully request leave from [Start Date] to [End Date] due to [medical reasons / personal emergency].

I will ensure I catch up on all lecture notes and laboratory assignments immediately upon my return.

Kindly grant me leave for the specified days.

Yours obediently,
[Your Name]
Roll No: [Number] | [Contact Number]
Date: [Today's Date]
```""",
        "content_mr": """### ✉️ रजेचा अधिकृत अर्ज नमुना (Leave Application)

#### महाविद्यालयाच्या प्राचार्यांना / शिक्षकांना रजेचा अर्ज:
```text
प्रति,
मा. प्राचार्य / विभागप्रमुख,
[कॉलेजचे नाव],
[शहराचे नाव]

विषय: आजारपणामुळे २ दिवसांची रजा मिळण्याबाबत अर्ज.

आदरणीय सर/मॅडम,
मी [तुमचे नाव], आपल्या महाविद्यालयात [वर्ग, उदा. तृतीय वर्ष संगणक, रोल नंबर: २५] चा विद्यार्थी आहे.

मला अचानक ताप आल्यामुळे डॉक्टरने दोन दिवस विश्रांती घेण्याचा सल्ला दिला आहे. तरी मला दिनांक [तारीख] ते [तारीख] या कालावधीत रजा मंजूर करावी ही नम्र विनंती.

आपला नम्र विद्यार्थी,
[तुमचे नाव]
रोल नंबर: [तुमचा नंबर]
मोबाईल: [मोबाईल नंबर]
दिनांक: [आजची तारीख]
```"""
    },

    {
        "keywords": ["who are you", "what can you do", "about you", "तू कोण आहेस", "काय करू शकतोस", "intro"],
        "title": "About Sarkar Mitra (सरकार मित्र परिचय)",
        "content_en": """### 🏛️ About Sarkar Mitra (सरकार मित्र)

Hello! I am **Sarkar Mitra** — an advanced, dual-purpose conversational AI assistant.

---

#### 🌟 What I Can Do For You:

1. **🏛️ Maharashtra Government Schemes Expert:**
   - Deep, verified information on flagship schemes: **Majhi Ladki Bahin Yojana (₹1,500/mo)**, **PM Kisan & Namo Shetkari (₹12,000/yr)**, **Digital 7/12 & 8-A Satbara**, **Crop Loan Waiver (₹2 Lakh)**, **Ration Cards**, **Income/Caste/Domicile Certificates**, and **Farm Machinery Subsidies**.
   - Eligibility checklists, document lists, official portal links, and toll-free helplines (`1800-120-8040`).

2. **🤖 General Knowledge & Conversational AI (Like ChatGPT & Claude):**
   - Answer academic and coding questions in Python, JavaScript, DSA, SQL.
   - Explain scientific concepts (quantum physics, biology, mathematics).
   - Write essays, resume bullets, professional emails, and leave applications.
   - Discuss history, culture, geography, and current world facts.

3. **🗣️ Voice & Multilingual First:**
   - Speak your queries in **Marathi**, **Hindi**, or **English**.
   - Listen to answers with built-in voice readout (Text-to-Speech).
   - Instant bilingual translations (Marathi + English) on every reply!""",
        "content_mr": """### 🏛️ सरकार मित्र (Sarkar Mitra) परिचय

नमस्कार! मी **सरकार मित्र** — तुमचा हुशार, बहुभाषिक AI सहाय्यक आहे!

---

#### 🌟 मी तुम्हाला कशी मदत करू शकतो?

1. **🏛️ शासकीय योजना मार्गदर्शन:**
   - **लाडकी बहीण योजना (दरमहा ₹१,५००)**, **पीएम किसान व नमो शेतकरी (वार्षिक ₹१२,०००)**, **डिजिटल ७/१२ उतारा**, **पीक कर्जमाफी**, **रेशन कार्ड**, आणि **तहसीलदार दाखले**.
   - अचूक पात्रता, लागणारी कागदपत्रे, अधिकृत लिंक आणि हेल्पलाइन `१८००-१२०-८०४०`.

2. **🤖 सामान्य ज्ञान आणि AI संवाद (ChatGPT सारखे):**
   - कोडिंग (Python, SQL), विज्ञान, गणित आणि सामान्य ज्ञानाचे प्रश्न सोडवणे.
   - कॉलेजचे अभ्यासक्रम, रेझ्युमे लेखन, रजेचे अर्ज तयार करणे.
   - कोणताही प्रश्न मराठी, इंग्रजी किंवा हिंदीत विचारल्यास सविस्तर उत्तर देणे!"""
    }
]


def match_general_knowledge(query: str) -> Optional[dict]:
    """Matches a user query against the general knowledge engine."""
    q_lower = query.lower().strip()
    words = set(re.findall(r'\b\w+\b', q_lower))

    best_match = None
    best_score = 0

    for topic in GENERAL_KNOWLEDGE_TOPICS:
        score = 0
        for kw in topic["keywords"]:
            kw_l = kw.lower()
            if kw_l in q_lower:
                score += 5
            elif kw_l in words:
                score += 3
            else:
                kw_words = set(kw_l.split())
                overlap = kw_words.intersection(words)
                if len(overlap) == len(kw_words) and len(kw_words) > 1:
                    score += 4

        if score > best_score:
            best_score = score
            best_match = topic

    if best_score >= 3:
        return best_match
    return None


def generate_general_answer(query: str, language: str = "auto") -> Tuple[str, bool]:
    """
    Produces a complete, formatted answer for general/custom questions.
    Returns (reply_text, was_matched).
    """
    is_marathi = language == "mr" or any(0x0900 <= ord(c) <= 0x097F for c in query)
    topic = match_general_knowledge(query)

    if topic:
        if is_marathi:
            reply = topic["content_mr"] + "\n\n---\n\n🌐 **English Version:**\n\n" + topic["content_en"]
        else:
            reply = topic["content_en"] + "\n\n---\n\n🌐 **मराठी आवृत्ती (Marathi Version):**\n\n" + topic["content_mr"]
        return reply, True

    # Generic intelligent assistant response for any other open-ended question
    if is_marathi:
        reply = (
            f"💡 **तुमचा प्रश्न:** *\"{query}\"*\n\n"
            "मी **सरकार मित्र** — तुमचा AI सहाय्यक आहे. मी शासकीय योजनांबरोबरच सामान्य ज्ञान, कोडिंग, विज्ञान आणि विविध विषयांची उत्तरे देऊ शकतो.\n\n"
            "🔑 **अमर्याद खुल्या प्रश्नांसाठी (Open-Ended AI like ChatGPT):**\n"
            "वर उजव्या कोपऱ्यातील **⚙️ Settings** वर क्लिक करा आणि तुमची मोफत **Google Gemini API Key** टाका.\n"
            "👉 [aistudio.google.com/apikey](https://aistudio.google.com/apikey) वरून ३० सेकंदात मोफत की मिळवा.\n\n"
            "**तुम्ही मला खालीलपैकी कोणतेही प्रश्न विचारू शकता:**\n"
            "• `What is quantum computing?` (क्वांटम कॉम्प्युटिंग)\n"
            "• `Explain machine learning vs AI` (मशीन लर्निंग)\n"
            "• `Write a Python code to reverse string` (पायथॉन कोडिंग)\n"
            "• `छत्रपती शिवाजी महाराज इतिहास` किंवा `डॉ. बाबासाहेब आंबेडकर`\n"
            "• `How to write a resume?` किंवा `Leave application format`\n"
            "• तसेच कोणतीही महाराष्ट्र शासकीय योजना (लाडकी बहीण, पीएम किसान, ७/१२)."
        )
    else:
        reply = (
            f"💡 **Question:** *\"{query}\"*\n\n"
            "I am **Sarkar Mitra**, your conversational AI assistant. I can answer academic, coding, science, and general questions just like ChatGPT or Claude, while also providing expert guidance on Maharashtra government schemes.\n\n"
            "🔑 **To unlock full open-ended generative AI for any question:**\n"
            "Click **⚙️ Settings** in the menu and add your free **Google Gemini API Key**.\n"
            "👉 Get a free instant key at: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)\n\n"
            "**Try asking me any of these topics right now:**\n"
            "• ⚛️ `\"What is quantum computing?\"`\n"
            "• 🤖 `\"Explain machine learning and deep learning\"`\n"
            "• 🐍 `\"Write a Python function to check palindrome\"`\n"
            "• 🍎 `\"Explain Newton's three laws of motion\"`\n"
            "• 🌿 `\"How does photosynthesis work?\"`\n"
            "• 📄 `\"How to write a job-winning resume?\"`\n"
            "• ✉️ `\"Format for sick leave email\"`\n"
            "• 🚩 `\"History of Chhatrapati Shivaji Maharaj\"`\n"
            "• 🏛️ Any Maharashtra welfare scheme (Ladki Bahin, PM Kisan, Digital 7/12, etc.)"
        )

    return reply, False
