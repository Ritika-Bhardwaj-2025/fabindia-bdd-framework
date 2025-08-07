# run_behave.py
from utilities.report import BehaveXReporter

if __name__ == "__main__":
    reporter = BehaveXReporter()
    report_path = reporter.generate_report()
    reporter.send_report_via_sendgrid(report_path)