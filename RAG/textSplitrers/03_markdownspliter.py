

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """<h1 align="center">Hi there 👋, I'm Tarun Munjani</h1>

<p align="center">
<img 
  src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=24&pause=1000&center=true&vCenter=true&width=700&lines=Machine+Learning+Engineer+in+Progress;AI+%7C+NLP+%7C+Transformers+%7C+Django;Backend+and+Data+Science+Developer;Always+Learning+and+Building" 
  alt="Typing animation showing developer skills" 
/>
</p>

---

### 👨‍💻 About Me

- 🤖 Aspiring **Machine Learning / NLP Engineer** focused on real model building, not just tutorials.
- 🧠 Strong in **Python, Machine Learning, NLP, Transformers (BERT, LLMs)**.
- 🔥 Backend development with **Django, Flask, REST APIs**, model deployment.
- 🗄️ Databases: **SQL, MySQL**.
- 📍 India | Building projects that are actually production-grade, not toy demos.

---

### 🧰 Tech Stack

**AI / ML / NLP:**  
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat)
![Scikit-Learn](https://img.shields.io/badge/-ScikitLearn-F7931E?logo=scikitlearn&logoColor=white&style=flat)
![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?logo=pytorch&logoColor=white&style=flat)
![Transformers](https://img.shields.io/badge/-HuggingFace%20Transformers-FFD21E?logo=huggingface&logoColor=black&style=flat)
![NLP](https://img.shields.io/badge/-NLP-8A2BE2?style=flat)
![LLMs](https://img.shields.io/badge/-LLMs-0A0A0A?style=flat)

**Backend & Web:**  
![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white&style=flat)
![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&style=flat)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&logoColor=white&style=flat)

**Database & Dev Tools:**  
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?logo=mysql&logoColor=white&style=flat)
![SQL](https://img.shields.io/badge/-SQL-336791?style=flat)
![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white&style=flat)

---

### 🚀 Projects

- 🔍 **Vader-based Sentiment Analyzer** – Fine-tuned Vader model, REST API with Flask, deployed locally.
- 🌿 **Carbon Footprint Tracker** – Django + SQL, analytics dashboard.
- 💊 **Pharmacy Management System** – Java + MySQL.

---

### 📈 GitHub Stats

<p><img align="left" src="https://github-readme-stats-lyart-kappa-72.vercel.app/api/top-langs?username=deepseek23&show_icons=true&theme=dark&locale=en&layout=compact" alt="deepseek23" /></p>

<p>&nbsp;<img align="center" src="https://github-readme-stats-lyart-kappa-72.vercel.app/api?username=deepseek23&show_icons=true&theme=dark&locale=en" alt="deepseek23" /></p>

<p><img align="center" src="https://github-readme-streak-stats.demolab.com/?user=deepseek23&theme=dark" alt="deepseek23" /></p>

---

### 📫 Connect With Me

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tarun-munjani-72a4b3341/)
[![Gmail](https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:t.s.clashers@gmail.com)

---

> *"Don’t just use AI. Understand it. Build it. Deploy it."*"""

spliter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=700,
    chunk_overlap=0,
)


result = spliter.split_text(text)

print(len(result))
print(result[0])