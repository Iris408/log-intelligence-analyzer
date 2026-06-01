# Log Intelligence Analyzer 

Python-based log analysis and monitoring tool designed to parse, analyse, and report operational server logs through a modular backend architecture.
## ログインテリジェンスアナライザー
Pythonベースのログ解析・監視ツール。サーバーログの分析、エラー追跡、レポート生成を行うバックエンドプロジェクト。

---

## Features / 機能

- Log severity categorisation (INFO / WARNING / ERROR)
- Repeated error tracking
- Error frequency analysis
- Timestamp/hour-based error analysis
- Exportable analysis reports
- Color-coded CLI output
- Modular backend structure
- Operational monitoring workflow
- Docker containerization
- FastAPI dashboard/ API layer
- Swagger API documentation
- PostgreSQL log storage
- Docker Compose API + PostgreSQL setup
- Live log preview route

---

## Tech Stack / 技術スタック

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- Docker | Docker Compose
- Colorama
- Git & GitHub
- Linux/macOS terminal
- Modular Backend Architecture

---

## Docker Usage

Build container:

```bash
docker build -t log-intelligence-api .
```

Run container:
```bash
docker run -p 8000:8000 log-intelligence-api
```

Open FastAPI docs:
```text
http://127.0.0.1:8000/docs
```
---

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | / | API health/status route |
| GET | /logs/summary | Returns log severity summary |
| GET | /logs/errors | Returns error log entries |
| GET | /logs/report | Returns generated analysis report |
| POST | /logs/import | Imports log entries into PostgreSQL |
| GET | /logs/stored | Returns stored log entries from PostgreSQL |
| GET | /logs/live | Returns the latest log entries from the log file |
| DELETE | /logs/stored | Clears stored log entries from PostgreSQL |

---

## Project Structure / プロジェクト構成
```markdown
log-intelligence-analyzer/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── log_routes.py
│   └── services/
│       └── log_service.py
├── analyzer.py
├── parser.py
├── analytics.py
├── reporter.py
├── sample_logs/
│   └── server.log
├── analysis_report.txt
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Learning Outcomes / 学習成果

- Modular backend architecture
- Separation of concerns
- CLI application development
- Log parsing and analytics
- Report generation workflows
- Debugging and error handling

---

## Future Improvements / 今後の改善点

- Background live log monitioring
- Slack/email alert integration
- CI/CD pipeline
