# Staff Leave Management System (SLMS)

A modern, highly responsive, and full-featured Staff Leave Management System built with Django. SLMS allows staff members to seamlessly apply for leaves and allows administrators to review, approve, or reject these applications from a unified dashboard.

## 🚀 Live Demo
**View the deployed application here:** [https://staff-leave-management-system-eight.vercel.app/](https://staff-leave-management-system-eight.vercel.app/)

*(Note: The live demo is running on Vercel's ephemeral filesystem using SQLite. Accounts and leave requests created there may be periodically reset.)*

---

## ✨ Key Features

### For Staff
- **Personal Dashboard**: View your overall leave statistics (Total Applied, Pending, Approved) with animated counters.
- **Apply for Leave**: Submit detailed leave requests including leave type, duration, and reason.
- **Track Applications**: Monitor the status of your applications through a dedicated "My Leaves" page featuring intuitive status badges and filter tabs.

### For Administrators
- **Global Dashboard**: Access a bird's-eye view of all leave applications across the organization.
- **Data Visualization**: Visualize leave distribution (Pending/Approved/Rejected) with interactive Chart.js doughnut charts and animated approval rate progress bars.
- **Manage Staff**: Add, edit, or remove staff members securely. Includes a custom, polished JavaScript confirmation modal for deletions to prevent accidental removals.
- **Leave Actions**: Approve or reject leaves directly from the dashboard with immediate UI feedback.

---

## 🎨 UI & UX Highlights
The entire application was built focusing on a premium, corporate user experience:
- **Intelligent Dark Mode**: System-level toggle between a crisp white/green light theme and a rich deep navy/slate dark theme. Preferences are saved automatically via `localStorage`.
- **Mobile-First Design**: A fully responsive sidebar that collapses into a sleek off-canvas drawer on mobile devices, complete with a backdrop dimming effect and hamburger menu.
- **Micro-Animations**: Scroll reveal animations cascade through the cards and stats as you scroll down the page, providing a highly modern feel.
- **Dynamic Notifications**: Action-driven Toast notifications and animated pending request badges ensure users are always informed of system states.

---

## 🛠️ Technology Stack
- **Backend:** Python, Django 5+
- **Frontend:** HTML5, Vanilla CSS (Custom Design System using CSS Variables), Vanilla JavaScript
- **Data Visualization:** Chart.js
- **Database:** SQLite (default for development)
- **Deployment & Production:** Gunicorn, WhiteNoise (for static file serving)

---

## 💻 Local Setup & Installation

If you'd like to run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MallikGowdaM/Staff-Leave-Management-System.git
   cd Staff-Leave-Management-System
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   # Windows:
   env\Scripts\activate
   # macOS/Linux:
   source env/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Admin account):**
   ```bash
   python manage.py createsuperuser
   # (Follow the prompts to set username and password)
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## ☁️ Deployment Guides

This repository includes configuration files for simple deployment to either **Vercel** or **Render**.

### Vercel (`vercel.json`)
1. Import the repository into your Vercel dashboard.
2. Vercel will automatically detect the `vercel.json` and Python runtime.
3. Deploy!

### Render (`build.sh`)
1. Create a new Web Service in the Render dashboard and link this repository.
2. Set the **Build Command** to `./build.sh`
3. Set the **Start Command** to `gunicorn slms.wsgi:application`
4. Deploy!
