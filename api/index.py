import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load the marks data from the JSON file
        with open('marks.json', 'r') as f:
            marks_data = json.load(f)
        
        # Convert marks data into a dictionary for easier lookup
        marks_dict = {student["name"]: student["marks"] for student in marks_data}

        # Parse the query parameters
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        names = query_params.get("name", [])

        # Extract the marks for the requested names
        marks = [marks_dict.get(name, None) for name in names if name in marks_dict]

        # Prepare the response
        response = {"marks": marks}

        # Send the HTTP response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Write the JSON response body
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return


