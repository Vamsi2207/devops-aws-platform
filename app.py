import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self.send_json(200, {"status": "healthy"})
            return

        self.send_json(
            200,
            {
                "message": "DevOps AWS Platform API",
                "environment": os.getenv("ENVIRONMENT", "local"),
                "version": os.getenv("APP_VERSION", "1.0.0"),
            },
        )


port = int(os.getenv("PORT", "8080"))
print(f"Server listening on port {port}")
HTTPServer(("0.0.0.0", port), AppHandler).serve_forever()