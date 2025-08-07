import os
import time
import datetime
import ssl
import base64
import subprocess
import sendgrid
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

class BehaveXReporter:
    BASE_DIRECTORY = 'C:/Users/10835846/PycharmProjects/ProjectGladiator_BDD/reports'
    REPORT_DIRECTORY = os.path.join(BASE_DIRECTORY, "BehaveXReports")

    def __init__(self):
        os.makedirs(self.REPORT_DIRECTORY, exist_ok=True)

    def generate_report(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        timestamped_folder = os.path.join(self.REPORT_DIRECTORY, f"BeautifulReports_{timestamp}")
        os.makedirs(timestamped_folder, exist_ok=True)
        behave_command = (
            f"behave -f behave_html_formatter:HTMLFormatter -o {timestamped_folder}/report.html"
        )

        os.system(behave_command)

        report_path = os.path.join(timestamped_folder, "report.html")
        if os.path.exists(report_path):
            os.startfile(report_path)

        return report_path

    def send_report_via_sendgrid(self, report_path):
        SENDGRID_API_KEY = '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'
        SENDER_EMAIL = 'aw9016226@gmail.com'
        RECIPIENT_EMAIL = 'valorantmorgan5@gmail.com'

        ssl._create_default_https_context = ssl._create_unverified_context

        sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
        with open(report_path, 'rb') as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()

        attachment = Attachment(
            FileContent(encoded),
            FileName(os.path.basename(report_path)),
            FileType("text/html"),
            Disposition("attachment")
        )

        mail = Mail(
            from_email=SENDER_EMAIL,
            to_emails=RECIPIENT_EMAIL,
            subject="BDD Automation Test Report",
            plain_text_content="Please find the attached BDD automation test report.",
        )
        mail.attachment = attachment

        try:
            response = sg.send(mail)
            print(f"Status Code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send email: {e}")
