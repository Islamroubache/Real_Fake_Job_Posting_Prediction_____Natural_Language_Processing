# 🔍 Job Posting Fraud Detector

> An intelligent machine learning system that identifies fraudulent job postings using Natural Language Processing and advanced classification algorithms.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

Job Posting Fraud Detector is a Flask-based web application that leverages machine learning to analyze job postings and detect potential fraud. Using NLP techniques and ensemble learning methods, the system achieves high accuracy in identifying suspicious job listings, helping job seekers avoid scams.

### ✨ Key Features

- **Real-time Analysis** - Instant fraud detection on job posting submissions
- **High Accuracy** - Trained on 18,000+ real job postings with 97%+ accuracy
- **NLP-Powered** - Advanced text processing using TF-IDF vectorization
- **RESTful API** - Easy integration with existing platforms
- **Explainable Results** - Confidence scores and feature importance
- **Lightweight** - Fast predictions with optimized model architecture

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/Islamroubache/job-posting-fraud-detector.git
   cd job-posting-fraud-detector
   \`\`\`

2. **Create and activate virtual environment**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run the application**
   \`\`\`bash
   python app.py
   \`\`\`

5. **Access the application**
   
   Open your browser and navigate to `http://localhost:5000`


---

## 🤖 How It Works

### Machine Learning Pipeline

1. **Data Preprocessing**
   - Text cleaning and normalization
   - Feature extraction from job descriptions
   - Handling missing values and outliers

2. **Feature Engineering**
   - TF-IDF vectorization of text content
   - Extraction of metadata features (salary, location, company profile)
   - Binary encoding of categorical variables

3. **Model Training**
   - Algorithm: Random Forest Classifier
   - Training set: 18,000+ labeled job postings
   - Cross-validation for optimal hyperparameters
   - Performance: 97%+ accuracy, 95%+ F1-score

4. **Prediction**
   - Real-time text vectorization
   - Ensemble prediction with confidence scoring
   - Result interpretation and explanation

---

## 🔌 API Usage

### Predict Endpoint

**POST** `/api/predict`

**Request Body:**
\`\`\`json
{
  "title": "Senior Software Engineer",
  "location": "San Francisco, CA",
  "department": "Engineering",
  "salary_range": "$120k-$180k",
  "company_profile": "Tech startup building AI solutions",
  "description": "We are looking for an experienced software engineer...",
  "requirements": "5+ years Python, ML experience, Bachelor's degree",
  "benefits": "Health insurance, 401k, stock options",
  "employment_type": "Full-time",
  "required_experience": "Mid-Senior level",
  "required_education": "Bachelor's Degree",
  "industry": "Technology",
  "function": "Engineering"
}
\`\`\`

**Response:**
\`\`\`json
{
  "prediction": "legitimate",
  "confidence": 0.94,
  "risk_score": 0.06,
  "analysis": {
    "suspicious_indicators": [],
    "positive_indicators": ["verified_company", "detailed_description", "realistic_salary"]
  }
}
\`\`\`

---

## 📊 Dataset

The model is trained on the **Employment Scam Aegean Dataset (EMSCAD)**, which contains:

- **Total Records:** 17,880 job postings
- **Fraudulent:** 866 (4.8%)
- **Legitimate:** 17,014 (95.2%)
- **Features:** 18 attributes including text and metadata
- **Source:** Real job postings collected from various platforms

### Key Features Used

- Job title and description
- Company profile and location
- Salary range and benefits
- Required experience and education
- Employment type and industry
- Presence of company logo and contact information

---

## 🛠️ Technology Stack

- **Backend:** Flask (Python web framework)
- **ML/NLP:** scikit-learn, NLTK, pandas, numpy
- **Model:** Random Forest Classifier
- **Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Gunicorn, Docker (optional)

---

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 97.2% |
| Precision | 94.8% |
| Recall | 95.6% |
| F1-Score | 95.2% |
| AUC-ROC | 0.98 |

---

## 🔮 Future Enhancements

- [ ] Deep learning models (BERT, transformers) for improved accuracy
- [ ] Multi-language support for international job postings
- [ ] Browser extension for real-time job board scanning
- [ ] User feedback loop for continuous model improvement
- [ ] Integration with major job platforms (LinkedIn, Indeed, etc.)
- [ ] Detailed fraud pattern analysis and reporting
- [ ] Mobile application for on-the-go verification

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---


---

## 👥 Authors

- Islam Roubache - 🎓 Master’s Student in Artificial Intelligence & Data Science - 📍 Higher School of Computer Science 08 May 1945 – Sidi Bel Abbes, Algeria

---

## 🙏 Acknowledgments

- Employment Scam Aegean Dataset (EMSCAD) contributors
- scikit-learn and Flask communities
- All contributors who help improve this project

---

## 📧 Contact

For questions or support, please open an issue or contact [i.roubache@esi-sba.dz](mailto:i.roubache@esi-sba.dz)

---

<p align="center">Made with ❤️ for safer job hunting</p>
