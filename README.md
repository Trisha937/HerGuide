## HerGuide - Women Empowerment Portal
Financial and skill-development assistant for Indian women

## Key Features:-

-Hindi voice/text input for financial queries.
-Government scheme recommendations (based on income/age/state).
-SkillHER Directory: Connect with women entrepreneurs.
-Scam message detection (OTP/fraud alerts).
 
## Installation  

1.Install Requirements  
--->pip install -r requirements.txt

2.Run the App
--->streamlit run app.py

## Make sure all requirements are installed.

## Technical Stack
Component	         Technology Used

Frontend	            Streamlit
NLP	                    HuggingFace Transformers (Hindi QnA)
Voice Processing	    PyAudio + SpeechRecognition
Database	            SQLite3

## Usage Guide
1. वित्तीय प्रश्न पूछें (Ask Financial Questions)

-Click "वित्तीय प्रश्न पूछें" (QnA Module)
-Tap 🎤 बोलें for voice input or type your query (e.g., "महिला किसान लोन")
-View instant answers with scheme links

2. योजनाएं प्राप्त करें (Recommendation Module)

-Select "योजनाएं प्राप्त करें"

-Fill:
आयु (Age)
वार्षिक आय (Annual Income)
राज्य (State)

-Get top 3 योजनाएं with contacts

3. व्यवसाय प्रोफ़ाइल (SkillHER Module)

-Click "व्यवसाय प्रोफ़ाइल जोड़ें"

-Enter: नाम, स्थान, व्यवसाय प्रकार (e.g., मेहंदी, सिलाई)

-Browse पहले से मौजूद प्रोफाइल (Existing Profiles)

Watch YouTube tutorials from business_yt_links.json

4. घोटाला पहचानें (Safety Module)
-Select "घोटाला पहचानें"

-🎤 बोलें or paste suspicious message (e.g., "जल्दी OTP भेजें")

-Get 🛑 लाल चेतावनी (Red Alert) if scam detected


## Troubleshooting

-Microphone not working:
1.Check system permissions.
2.Run pip install pyaudio separately.

-Hindi text recognition issues:
1.Ensure transformers library is updated.
2.Use clear pronunciation for voice queries.

## Future Roadmap
-WhatsApp integration for scam alerts.
-Multilingual support (Tamil, Bengali).
-Government scheme API integration.