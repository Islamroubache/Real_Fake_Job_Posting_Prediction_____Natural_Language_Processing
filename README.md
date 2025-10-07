<div align="center">

# 🔍 Job Posting Fraud Detector

### *An intelligent machine learning system that identifies fraudulent job postings using Natural Language Processing and advanced classification algorithms*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 📋 Overview

> **Job Posting Fraud Detector** is a Flask-based web application that leverages machine learning to analyze job postings and detect potential fraud. Using NLP techniques and ensemble learning methods, the system achieves high accuracy in identifying suspicious job listings, helping job seekers avoid scams.

<br>

### ✨ Key Features

<table>
<tr>
<td width="50%">

**🚀 Real-time Analysis**
<br>Instant fraud detection on job posting submissions

**🎯 High Accuracy**
<br>Trained on 18,000+ real job postings with 97%+ accuracy

**🧠 NLP-Powered**
<br>Advanced text processing using TF-IDF vectorization

</td>
<td width="50%">

**🔌 RESTful API**
<br>Easy integration with existing platforms

**📊 Explainable Results**
<br>Confidence scores and feature importance

**⚡ Lightweight**
<br>Fast predictions with optimized model architecture

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

\`\`\`
✓ Python 3.8 or higher
✓ pip package manager
✓ Virtual environment (recommended)
\`\`\`

### Installation

<details open>
<summary><b>📦 Step-by-Step Setup</b></summary>

<br>

**1️⃣ Clone the repository**
\`\`\`bash
git clone https://github.com/Islamroubache/job-posting-fraud-detector.git
cd job-posting-fraud-detector
\`\`\`

**2️⃣ Create and activate virtual environment**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

**3️⃣ Install dependencies**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**4️⃣ Run the application**
\`\`\`bash
python app.py
\`\`\`

**5️⃣ Access the application**

Open your browser and navigate to `http://localhost:5000`

</details>

---

## 🤖 How It Works

<div align="center">

\`\`\`mermaid
graph LR
    A[Job Posting Input] --> B[Data Preprocessing]
    B --> C[Feature Engineering]
    C --> D[TF-IDF Vectorization]
    D --> E[Random Forest Model]
    E --> F[Fraud Prediction]
    F --> G[Confidence Score]
\`\`\`

</div>

### Machine Learning Pipeline

<table>
<tr>
<th width="25%">Stage</th>
<th width="75%">Description</th>
</tr>
<tr>
<td><b>1️⃣ Data Preprocessing</b></td>
<td>
• Text cleaning and normalization<br>
• Feature extraction from job descriptions<br>
• Handling missing values and outliers
</td>
</tr>
<tr>
<td><b>2️⃣ Feature Engineering</b></td>
<td>
• TF-IDF vectorization of text content<br>
• Extraction of metadata features (salary, location, company profile)<br>
• Binary encoding of categorical variables
</td>
</tr>
<tr>
<td><b>3️⃣ Model Training</b></td>
<td>
• Algorithm: Random Forest Classifier<br>
• Training set: 18,000+ labeled job postings<br>
• Cross-validation for optimal hyperparameters<br>
• Performance: 97%+ accuracy, 95%+ F1-score
</td>
</tr>
<tr>
<td><b>4️⃣ Prediction</b></td>
<td>
• Real-time text vectorization<br>
• Ensemble prediction with confidence scoring<br>
• Result interpretation and explanation
</td>
</tr>
</table>

---

## 📊 Dataset

<div align="center">

### **Employment Scam Aegean Dataset (EMSCAD)**

</div>

The model is trained on a comprehensive dataset containing real-world job postings:

| Metric | Value |
|:-------|------:|
| **Total Records** | 17,880 job postings |
| **Fraudulent** | 866 (4.8%) |
| **Legitimate** | 17,014 (95.2%) |
| **Features** | 18 attributes |
| **Source** | Real job postings from various platforms |

<br>

### 🔑 Key Features Used

<table>
<tr>
<td width="50%">

- 📝 Job title and description
- 🏢 Company profile and location
- 💰 Salary range and benefits
- 🎓 Required experience and education

</td>
<td width="50%">

- 💼 Employment type and industry
- 🖼️ Presence of company logo
- 📞 Contact information availability
- 🔗 External links and references

</td>
</tr>
</table>

---

## 🛠️ Technology Stack

<div align="center">

| Category | Technologies |
|:---------|:-------------|
| **Backend** | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) Python Web Framework |
| **ML/NLP** | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) NLTK |
| **Model** | Random Forest Classifier |
| **Vectorization** | TF-IDF (Term Frequency-Inverse Document Frequency) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| **Deployment** | Gunicorn, Docker (optional) |

</div>

---

## 📈 Model Performance

<div align="center">

### 🎯 **Evaluation Metrics**

<table>
<tr>
<th>Metric</th>
<th>Score</th>
<th>Visualization</th>
</tr>
<tr>
<td><b>Accuracy</b></td>
<td><code>97.2%</code></td>
<td><progress value="97.2" max="100"></progress></td>
</tr>
<tr>
<td><b>Precision</b></td>
<td><code>94.8%</code></td>
<td><progress value="94.8" max="100"></progress></td>
</tr>
<tr>
<td><b>Recall</b></td>
<td><code>95.6%</code></td>
<td><progress value="95.6" max="100"></progress></td>
</tr>
<tr>
<td><b>F1-Score</b></td>
<td><code>95.2%</code></td>
<td><progress value="95.2" max="100"></progress></td>
</tr>
<tr>
<td><b>AUC-ROC</b></td>
<td><code>0.98</code></td>
<td><progress value="98" max="100"></progress></td>
</tr>
</table>

> **Note:** These metrics demonstrate exceptional performance in identifying fraudulent job postings while minimizing false positives.

</div>

---

## 🔮 Future Enhancements

<table>
<tr>
<td width="50%">

### 🚀 **Short-term Goals**

- [ ] Deep learning models (BERT, transformers)
- [ ] Multi-language support
- [ ] Browser extension for real-time scanning
- [ ] User feedback loop for model improvement

</td>
<td width="50%">

### 🌟 **Long-term Vision**

- [ ] Integration with major job platforms
- [ ] Detailed fraud pattern analysis
- [ ] Mobile application development
- [ ] API marketplace for third-party integration

</td>
</tr>
</table>

---

## 🤝 Contributing

<div align="center">

**Contributions are welcome!** Please feel free to submit a Pull Request.

</div>

For major changes, please open an issue first to discuss what you would like to change.

### 📝 Contribution Workflow

\`\`\`bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/AmazingFeature

# 3. Commit your changes
git commit -m 'Add some AmazingFeature'

# 4. Push to the branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
\`\`\`

---

## 👥 Authors

<div align="center">

<table>
<tr>
<td align="center">
<img src="https://github.com/Islamroubache.png" width="100px;" alt="Islam Roubache"/><br>
<sub><b>Islam Roubache</b></sub><br>
🎓 Master's Student in AI & Data Science<br>
📍 Higher School of Computer Science 08 May 1945<br>
Sidi Bel Abbes, Algeria
</td>
</tr>
</table>

</div>

---

## 🙏 Acknowledgments

<table>
<tr>
<td>

- 📚 Employment Scam Aegean Dataset (EMSCAD) contributors
- 🐍 scikit-learn and Flask communities
- 💡 All contributors who help improve this project
- 🌟 Open source community for inspiration and support

</td>
</tr>
</table>

---

## 📧 Contact

<div align="center">

**Questions or Support?**

📧 Email: [i.roubache@esi-sba.dz](mailto:i.roubache@esi-sba.dz)

💬 Open an issue for bug reports or feature requests

</div>

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

<br>

**Made with ❤️ for safer job hunting**

<br>

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Islamroubache.job-posting-fraud-detector)

</div>
