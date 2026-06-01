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

---

## Tech Stack / 技術スタック

- Python
- FastAPI
- Uvicorn
- Docker
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

## API Endpoints

```markdown
| Method | Endpoint | Description |
| --- | --- | --- |
| GET | / | API health/status route |
| GET | /logs/summary | Returns log severity summary |
| GET | /logs/errors | Returns error log entries |
| GET | /logs/report | Returns generated analysis report |

---

## Project Structure / プロジェクト構成

```text
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

- PostgreSQL log storage
- Live log monitoring
- Slack/email alert integration
- CI/CD pipeline
