# 🌾 Croptrix– AI-Powered WhatsApp Assistant for Farmers

Croptrix is a lightweight, AI-powered WhatsApp chatbot designed to support farmers with real-time agricultural advice, crop care tips, and localized insights. Built using Python, Flask and Google AI, this bot empowers rural communities with accessible, intelligent support, right from their phones.

---

## 🏆Team Members
- Payal Morar
- Caleb Padotan
- Tyler Abraham
- Kivara Juta

## 🚀 Features

- 📱 WhatsApp integration via Meta Cloud API  
- 🧠 AI-powered responses using Google Gemini Flash
- 🌍 Localized support for farming queries  
- 🗣️ Natural language understanding for easy interaction  
- ⚡ Fast, lightweight, and demo-ready  

---

## 🛠️ Tech Stack

- Python 3.12  
- Flask  
- Google AI (Gemini Flash)  
- Meta WhatsApp Cloud API  
- Ngrok (for local webhook tunneling)  

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Payal429/CroptrixBot.git
   cd CroptrixBot

2.  **Install dependencies**
    
    ```bash
    pip install -r requirements.txt
    
    
3.  **Set up environment variables**  
    Create a `.env` file based on `example.env` and add:
    
    ```
    GOOGLE_API_KEY=your_google_ai_key
    WHATSAPP_TOKEN=your_meta_access_token
    VERIFY_TOKEN=your_webhook_verify_token
    
    ```
    
4.  **Run the Flask app**
    
    ```bash
    python run.py
    
    ```
    
5.  **Expose your local server**
    
    ```bash
    ngrok http 8000
    
    ```
    
6.  **Configure your webhook**  
    Use the Ngrok URL in your Meta App Dashboard to set up the webhook endpoint.
    

----------

## 💬 Example Usage

Send a WhatsApp message like:

> "How do I treat leaf blight in maize?"

AgriBot responds with:

> "Leaf blight in maize can be treated using copper-based fungicides. Ensure proper crop rotation and avoid overhead irrigation."

----------

## 🧠 How It Works

Croptrix receives incoming messages via WhatsApp, processes them through a Flask webhook, and sends the query to Google Gemini Flash. The AI generates a clear, localized response which is sent back to the user in real time.

----------

## 🤝 Contributing

Pull requests are welcome! If you’d like to expand Croptrix with new features (like voice input, local language support, or crop image analysis), feel free to fork and build.

----------

## 📜 License

This project is licensed under the MIT License.

----------

## 🙌 Acknowledgments

-   Google AI for powering the intelligence
-   Meta for WhatsApp Cloud API
-   Dave Ebbelaar’s WhatsApp bot tutorial for foundational structure
-   Hackathon 2025 team for collaboration and inspiration

