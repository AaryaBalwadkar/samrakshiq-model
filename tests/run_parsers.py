from src.parsers.xml.parser import parse_xml
from src.parsers.csv.parser import parse_csv
from src.parsers.json.parser import parse_json
from src.utils.metrics.track import track_latency
from src.schema.message import Message

@track_latency
def test_parser(file_path: str, parser):
    messages = [Message(**msg) for msg in parser(file_path)]
    return len(messages)

if __name__ == "__main__":
    print("XML:", test_parser("samples/test.xml", parse_xml))
    print("CSV:", test_parser("samples/test.csv", parse_csv))
    print("JSON:", test_parser("samples/test.json", parse_json))