# Student Attendance App

| File | Task |
|------|------|
| `app.py` | Flask app: login page + `calculate_attendance()` |
| `.github/workflows/ci.yml` | (b) GitHub Actions CI |
| `Dockerfile` | (c) Docker image |
| `test_attendance.py` | (d) pytest cases |
| `login_selenium.py` | (f) Selenium login test |

Login: `student` / `1234`

## a. Git
```
git init -b main
git add .
git commit -m "Initial commit: student attendance app"
git checkout -b feature_attendance_report
# edit app.py
git add .
git commit -m "Add attendance_report function"
git checkout main
git merge feature_attendance_report
git log --oneline --graph --all
```

## b. GitHub Actions
Push the repo to GitHub, then push to the feature branch:
```
git remote add origin https://github.com/<your-username>/student-attendance-app.git
git push -u origin main
git checkout feature_attendance_report
git push -u origin feature_attendance_report
```
Open the **Actions** tab on GitHub to see the run status (green tick = passed, red cross = failed).

## c. Docker
```
docker build -t attendance-app .
docker run -d -p 8080:5000 --name attendance attendance-app
docker ps
```
Open http://localhost:8080 (host port 8080 -> container port 5000).

## d. pytest
```
pip install -r requirements.txt
pytest -v
```

## f. Selenium
Container must be running first (step c), then:
```
pip install selenium
python login_selenium.py
```
