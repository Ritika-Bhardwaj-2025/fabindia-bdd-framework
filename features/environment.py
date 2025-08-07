# from selenium import webdriver
# from utilities.logger import setup_logzero_logger
#
# def before_feature(context, feature):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     service = webdriver.ChromeService()
#     context.driver = webdriver.Chrome(service=service, options=options)
#     context.logger = setup_logzero_logger()
#
# def after_feature(context, feature):
#     context.driver.quit()

import os
import datetime
from selenium import webdriver
from utilities.report import BehaveXReporter
from utilities.logger import setup_logzero_logger

# Setup log directory
base_dir = r'C:\Users\10835846\PycharmProjects\ProjectGladiator_BDD'
log_dir = os.path.join(base_dir, 'report_steps')
os.makedirs(log_dir, exist_ok=True)

scenario_log_file = os.path.join(log_dir, 'scenario_log.txt')
step_log_file = os.path.join(log_dir, 'step_log.txt')

logger = setup_logzero_logger()
def before_feature(context,feature):
    options = webdriver.ChromeOptions()
    print("Instance created")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.logger = logger

def after_step(context, step):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "PASSED" if step.status == "passed" else "FAILED"
    log_entry = f"[{timestamp}] Step: {step.name} - {status}\n"

    with open(step_log_file, "a") as log:
        log.write(log_entry)

def after_scenario(context, scenario):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "PASSED" if scenario.status == "passed" else "FAILED"
    log_entry = f"[{timestamp}] Scenario: {scenario.name} - {status}\n"

    with open(scenario_log_file, "a") as log:
        log.write(log_entry)

def after_feature(context,feature):
    print("Instance destroyed")
    context.driver.quit()

    if __name__ == "__main__":
        reporter = BehaveXReporter()
        report_path = reporter.generate_report()
        reporter.send_report_via_sendgrid(report_path)


