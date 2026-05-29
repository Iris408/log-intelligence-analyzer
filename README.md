# Log Intelligence Analyzer 
## ログインテリジェンスアナライザー

Python-based log analysis and monitoring tool designed to parse, analyse, and report operational server logs through a modular backend architecture.
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

---

## Tech Stack / 技術スタック

- Python
- Colorama
- Docker
- Git & GitHub
- Linux/macOS terminal
- Modular Backend Architecture

---

## Docker Usage

Build container:

```bash
docker build -t log-analyzer .
```

Run container:
```bash
docker run -it log-analyzer
```

---

## Example Output & Docker Container

<table>
<tr>
<td width="50%" align="center">

### Example Output

<img src="./terminal_output.png" width="100%"/>

</td>

<td width="50%" align="center">

### Docker Container

<img src="./docker_container.png" width="100%"/>

</td>
</tr>
</table>

---

## Project Structure / プロジェクト構成

```text
log-intelligence-analyzer/

├── analyzer.py
├── parser.py
├── analytics.py
├── reporter.py
├── sample_logs/
│   └── server.log
└── analysis_report.txt
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

- FastAPI dashboard
- PostgreSQL log storage
- Live log monitoring
- Slack/email alert integration
