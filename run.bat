set Browser=edge

behave -f allure_behave.formatter:AllureFormatter -o Report\allure_result -D browser=%Browser%
python Utility/generate_allure_report.py
python Utility/send_mail.py %Browser%