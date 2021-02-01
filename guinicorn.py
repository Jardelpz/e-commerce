bind = "http://127.0.0.1:8000"
workers = 1
workers_connections = 2
max_requests = 500
max_requests_jitter = 2
keepalive = 10
timeout = 120
worker_class = 'uvicorn.workers.UvicornWorker'