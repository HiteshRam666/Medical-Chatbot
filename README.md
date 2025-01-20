# 🏥 **RAG (Retrieval-Augmented Generation)-Based Medical Chatbot**

Welcome to the **RAG-Based Medical Chatbot**! This AI-powered medical assistant is trained on **The Gale Encyclopedia of Medicine** to provide reliable and context-aware answers to medical queries. By leveraging **Retrieval-Augmented Generation (RAG)**, the chatbot can retrieve medical information and generate precise responses with the help of **Pinecone** for document retrieval and **OpenAI** for natural language processing. 🤖💉💬

**Demo link 👉 [Click Here](https://medical-chatbot-72el.onrender.com/)** 

---

### 📚 **What is RAG?**

**Retrieval-Augmented Generation (RAG)** is a cutting-edge AI technique that combines the best of both worlds: document retrieval and text generation. The chatbot first retrieves relevant medical documents from a knowledge base and then uses a language model (like OpenAI's GPT) to generate a contextually aware response based on the retrieved documents.

---

### 💡 **Project Overview**

This **Medical Chatbot**:
- Uses **RAG** to provide answers from an extensive database of medical knowledge, specifically **The Gale Encyclopedia of Medicine** 📖.
- Integrates **Pinecone** for fast and accurate document retrieval 🔍.
- Uses **OpenAI GPT** for generating detailed and accurate medical answers 💡.
- Built on **Flask**, a lightweight web framework for creating web-based applications 🌐.

---

### **Workflow of project⚙**
![Add a heading (1)](https://github.com/user-attachments/assets/df238c59-683f-42ef-a42a-e21197ad984f)

---

### **Demo of App**


https://github.com/user-attachments/assets/cbffaf40-26e7-48cf-9def-dbf9c63b76fd


---

### 🛠️ **Technologies Used**

- **Flask**: Web framework for building the chatbot interface 🖥️
- **LangChain**: A framework for developing AI-powered applications 🧠
- **Pinecone**: Vector database for document search and retrieval ⚡
- **OpenAI**: Powerful language models used for text generation 🌍
- **dotenv**: Manages environment variables for securely handling API keys 🔑
- **HTML/CSS/JavaScript**: For building the interactive user interface 🖋️

---

### 🌟 **Features**

- **Medical Knowledge Retrieval**: Retrieve information from The Gale Encyclopedia of Medicine 📚.
- **Context-Aware Responses**: Generate responses based on the retrieved medical documents 🧠.
- **User-Friendly Interface**: Simple web interface to interact with the chatbot 🗣️.
- **Fast and Efficient**: Real-time responses with the power of Pinecone and OpenAI ⚡.
- **Comprehensive Medical Topics**: Ask about diseases, treatments, symptoms, medical terminology, and more 🌐.

---

### 🚀 **Installation & Setup**

#### 1. **Clone the Repository**
First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/rag-medical-chatbot.git
cd rag-medical-chatbot
```

#### 2. **Install Dependencies**
Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

#### 3. **Environment Variables**
Create a `.env` file in the root of your project and add the following environment variables with your API keys:

```plaintext
PINECONE_API_KEY=your-pinecone-api-key
OPENAI_API_KEY=your-openai-api-key
```

You can get your API keys by:
- **Pinecone**: Sign up at [Pinecone](https://www.pinecone.io/) and obtain your API key 🔑.
- **OpenAI**: Sign up at [OpenAI](https://beta.openai.com/signup/) and generate your API key 💥.

#### 4. **Run the Application**
Start the Flask app with the following command:

```bash
python app.py
```

Your app will be running on `http://127.0.0.1:8000`. Open it in your browser, and you're all set to start chatting! 🌐

---

### 💬 **How It Works**

1. **User Input**: The user types a medical question on the web interface.
2. **Document Retrieval**: The input is used to search for relevant documents in the **Pinecone** vector database, which stores embeddings of The Gale Encyclopedia of Medicine.
3. **Answer Generation**: OpenAI's GPT model processes the retrieved documents to generate a medically accurate response.
4. **Response Display**: The chatbot displays the response to the user in real-time.

---

### 📁 **Project Structure**

Here’s the structure of the project:

```
/rag-medical-chatbot
    /src
        /prompt.py        # Contains the system prompt used by the chatbot
    /templates
        /chat.html        # Frontend for user interaction (HTML)
    app.py                # Main Flask app file
    requirements.txt      # Required Python dependencies
    .env                  # Environment variables (API keys)
    README.md             # Project documentation
```

---

### 🌐 **Frontend (chat.html)**

The **`chat.html`** file provides the user interface, where users can ask questions and get medical answers. It’s built using basic **HTML**, **CSS**, and **JavaScript** for dynamic interactions.

---

### 🔧 **Customization**

Feel free to customize the chatbot:
- **Change Pinecone Index**: Update the `index_name` variable in `app.py` to a different Pinecone index.
- **Adjust OpenAI Parameters**: You can fine-tune the `OpenAI` model's parameters like `temperature`, `max_tokens`, and more to control the response style.
- **Update System Prompt**: Modify the `src/prompt.py` to adjust how the chatbot responds based on the retrieved documents.

---

### ⚡ **Potential Improvements**

- **Multilingual Support**: Extend the bot to support multiple languages 🌍.
- **Medical Specialization**: Implement different models for specific medical fields (e.g., oncology, cardiology) 💡.
- **User History Tracking**: Add features to track user queries for personalized answers 🔐.

---

### 🌍 **Deploying to the Web**

You can deploy the chatbot on platforms like **Heroku**, **Render**, or **AWS**. Ensure that the environment variables are properly set in the production environment for API keys.

---

### 📝 **Contribute**

We welcome contributions! Fork the repo, make improvements, and submit a pull request. If you have any issues, feel free to open an issue on GitHub! 🙌

---

### 📬 **Contact**

If you have any questions or feedback, feel free to reach out:

- GitHub: [HiteshRam666]([https://github.com/your-username](https://github.com/HiteshRam666))
- Email: hiteshram321@gmail.com 📧

---

### 🎉 **Enjoy Your Medical Assistant!**

Your AI-powered medical assistant is now ready to help with any medical queries. Dive in, explore medical knowledge, and get instant, reliable answers! 🏥💬🚀

---

### ⭐ **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

---
