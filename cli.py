import sys
from modules.report_generator import ReportGenerator

if len(sys.argv) > 1:
    if sys.argv[1] == "report":
        print(ReportGenerator().generate_report())
    else:
        print("Unknown command")
else:
    print("Usage: python cli.py report")
