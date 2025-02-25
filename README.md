# 🔢 AI-Powered Math Solver & Graph Plotter

🚀 **Solve mathematical expressions & equations with AI-powered explanations and dynamic graph plotting!**

## 📌 Features
✅ Solve complex **mathematical expressions** with step-by-step AI-generated explanations.  
✅ **Solve one or two equations** and get accurate solutions.  
✅ **Graph plotting** 📈 for visualizing equations dynamically.  
✅ **AI-powered graph explanation** for deeper insights.  
✅ **Session storage** to retain results after submission.  
✅ User-friendly **web interface** 🌐 built using Flask.

---

## 🛠️ Installation & Setup
Follow these simple steps to set up and run the project.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-math-solver.git
cd ai-math-solver
```

### **2️⃣ Install Dependencies**
Ensure you have Python installed (preferably 3.8+), then run:
```bash
pip install -r requirements.txt
```

### **3️⃣ Install & Run Ollama**
Since this project uses **LangChain Ollama**, you need to install and serve it:
```bash
ollama serve
```
> 📌 **Note:** Make sure **Ollama is running** on `http://localhost:11434` before starting the Flask app.

### **4️⃣ Run the Flask App**
```bash
python app.py
```

### **5️⃣ Open in Browser** 🌐
Once the server starts, open:
```
http://127.0.0.1:5000/
```
Now you can **solve math problems & plot graphs visually!** 🎯

---

## 🔹 How to Use
### **🔢 Solve Expressions**
1️⃣ Enter a **mathematical expression** (e.g., `2*x + 5*x - 3`).  
2️⃣ Click **"Solve Expression"** button.  
3️⃣ AI will generate **step-by-step explanation** with the **final solution**.

### **📝 Solve Equations**
1️⃣ Enter **one or two equations** (e.g., `x + y = 5, x - y = 1`).  
2️⃣ Click **"Solve Equation"** button.  
3️⃣ Solution appears **along with a graph** 📈 and **AI-generated explanation**.

### **📊 View Graphs**
- If you enter a **single equation**, the system **plots its graph**.  
- If you enter **two equations**, it **plots both lines and their intersection**.

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Flask** 🌐 (Web Framework)
- **CrewAI** 🤖 (AI Agent for solving)
- **LangChain Ollama** 🧠 (LLM-based explanations)
- **SymPy** 🔢 (Mathematical Computation)
- **Matplotlib** 📈 (Graph Plotting)
- **HTML/CSS** 🎨 (Frontend UI)

---

## 🚀 Future Enhancements
🔹 Add **voice input** 🎤 to solve problems hands-free.  
🔹 Support **3D graph plotting** for complex equations.  
🔹 Improve **UI/UX design** for a better experience.  

---

## 📞 Contact & Contributions
💡 Found a bug? Want to contribute? PRs are welcome! 😊  
📧 Contact: **saniav2711@gmail.com**  
🌟 Don't forget to **⭐ Star** this repo if you like it!

