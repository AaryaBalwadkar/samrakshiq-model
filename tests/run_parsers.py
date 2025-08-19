import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from parsers.xml.parser import parse_xml
from parsers.csv.parser import parse_csv
from parsers.json.parser import parse_json
from utils.metrics.track import track_latency
from schema.message import Message

@track_latency
def test_parser(file_path: str, parser):
    messages = [Message(**msg) for msg in parser(file_path)]
    return len(messages)

if __name__ == "__main__":
    print("XML:", test_parser("samples/test.xml", parse_xml))
    print("CSV:", test_parser("samples/test.csv", parse_csv))
    print("JSON:", test_parser("samples/test.json", parse_json))