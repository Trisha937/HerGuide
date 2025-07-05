# 🛡️ Safety Support & Scam Detection Assistant

A smart, voice-ready tool to help users — especially women in India — stay safe from scam messages, predatory loan offers, and fraud.  
It also connects users to verified NGOs and women’s helplines for support.

Built with ❤️ using **Python + Streamlit + Google Translate API**.

---

## 🔍 Features

- 📩 **Scam & Loan Message Analyzer**  
  Detects scammy or fraudulent content in SMS, WhatsApp texts, or online ads using smart keyword matching.

- 🧠 **Hindi/Multilingual Support**  
  Automatically translates messages to English before analyzing (works for Hindi and other local languages).

- 📞 **Trusted NGO & Women Helpline Directory**  
  Provides verified links to Indian women safety NGOs like Sakhi, Snehalaya, NCW, and more.

- 📈 **Scam Analytics Dashboard**  
  Tracks how many messages were checked, how many scams detected, and breakdown by type (scam, phishing, loan, etc.).

---

## 🧪 Tech Stack

- Python
- Streamlit
- `googletrans` (for translation)
- `langdetect` (for language detection)
- Regex for smart keyword detection

---

## 🚀 Try It Live

> [Click to use the app](https://yourusername-safety-support-app.streamlit.app)  
> _(Replace with your actual link after deployment)_

---

## 💻 Local Setup (Optional)

```bash
git clone https://github.com/yourusername/safety-support-app.git
cd safety-support-app
pip install -r requirements.txt
streamlit run app.py
