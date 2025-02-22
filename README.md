
# **🧠 Mental Health Chatbot**  

This is an **AI-powered mental health chatbot** built using **OpenAI's GPT API** and **LangChain**. The chatbot provides self-care tips and mental health support based on user input.  

---

## **📌 Features**  
✅ Uses **GPT-3.5/4** for natural language understanding.  
✅ Provides **self-care advice** and mental health guidance.  
✅ Integrated with **LangChain** for structured responses.  
✅ Supports **customizable prompts and API calls**.  

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
```

### **2️⃣ Create a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**  
Create a `.env` file and add your **OpenAI API key**:  
```sh
OPENAI_API_KEY=your_actual_openai_api_key
```

Or set it manually in the script:  
```python
import os
os.environ["OPENAI_API_KEY"] = "your_actual_openai_api_key"
```

---

## **🛠 Usage**  

### **Run the Chatbot**
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the chatbot
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
    temperature=0.4,
    max_tokens=50,
)

# Example query
response = llm.invoke("What are some self-care practices for mental health?")
print(response)
```

---

## **🛑 Troubleshooting**  

### **1️⃣ Invalid API Key Error**  
If you see:  
```
openai.error.AuthenticationError: Incorrect API key provided
```
- Ensure your **API key is correct** in `.env`.  
- You can verify it in **OpenAI's API dashboard**: [https://platform.openai.com/](https://platform.openai.com/).  

### **2️⃣ Rate Limit Error (429)**  
- Your API quota might be **exceeded**. Upgrade your OpenAI plan if needed.  
- Implement **request throttling** if making frequent API calls.  

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---

## **🙌 Contributing**  
Feel free to **open issues** or submit **pull requests** to improve the project! 💡  

---

Let me know if you need **modifications** or **additional sections**! 🚀
