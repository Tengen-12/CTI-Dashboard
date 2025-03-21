# 🛡️ Cyber Threat Intelligence Dashboard

A real-time web-based dashboard for visualizing cybersecurity threats using Flask, Power BI, and Tableau.

---

## 🚀 Features
✅ **Real-Time Threat Data**: Displays simulated cybersecurity threats (can be replaced with real API feeds).  
✅ **Data Visualization**: Uses Chart.js to visualize threat severity levels.  
✅ **Filtering Options**: Users can filter threats by date.  
✅ **Power BI & Tableau Integration**: Embeds interactive reports from Power BI and Tableau.  
✅ **Live Updates**: Fetches new threat data every 5 seconds.  

---

## 🛠️ Technologies Used
- **Python (Flask)** - Backend framework.
- **JavaScript (jQuery, Chart.js)** - Frontend interactions and visualizations.
- **HTML/CSS** - User interface.
- **Power BI & Tableau** - Embedded dashboards.

---

## 📂 Project Structure
```plaintext
CTI Dashboard/
├── templates/
│   └── dashboard.html      # Main frontend UI
├── app.py              # Main Flask application
└── README.md           # Project documentation
```

---

## 🔧 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/CTI-Dashboard.git
cd CTI-Dashboard
```

### 2️⃣ Install Dependencies
Ensure Python is installed, then install Flask:
```bash
pip install -r <library names>
```

### 3️⃣ Run the Application
```bash
python app.py
```
The app will be available at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**.

---

## ⚙️ Configuration

### 🔹 Power BI & Tableau Integration
To embed Power BI and Tableau dashboards:
- Replace the `src` in `<iframe>` tags inside `index.html` with your actual report links.
- Example:
  ```html
  <iframe src="https://app.powerbi.com/view?r=YOUR_EMBED_ID" width="800" height="600"></iframe>
  ```
  ```html
  <iframe src="https://public.tableau.com/views/YOUR_DASHBOARD" width="800" height="600"></iframe>
  ```

---

## 📌 Future Improvements
🔹 Replace dummy data with real-time cybersecurity threat feeds.  
🔹 Add authentication and user roles.  
🔹 Improve frontend with Bootstrap or Material UI.  
🔹 Deploy to a cloud platform like AWS, GCP, or Azure.  

---

## 📜 License
This project is open-source. You are free to modify and distribute it under the **MIT License**.

🎯 *Happy Coding & Stay Secure!* 🚀

