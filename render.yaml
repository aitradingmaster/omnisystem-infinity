services:
  - type: web
    name: omnisystem-dashboard
    env: docker
    plan: free
    startCommand: "streamlit run dashboard/main.py"
  - type: worker
    name: omnisystem-autotrader
    env: docker
    plan: free
    startCommand: "python autotrade/scheduler.py"
  - type: worker
    name: omnisystem-trainer
    env: docker
    plan: free
    startCommand: "python training/automl_manager.py"