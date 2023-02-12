import glob
import shutil
from google.oauth2 import service_account
from google.cloud import storage
import os
from datetime import datetime

google_credentials = service_account.Credentials.from_service_account_file("E:\\DOWNLOADS\\ast_google_cred.json")
storage_client = storage.Client(credentials=google_credentials)

bucket_name = "ast_automation_bucket"
allure_report_path = os.path.join(os.path.abspath(__file__+"/../../"), "Report\\allure_report")
allure_report_cloud_path = f"behave_tutorial_allure_reports/allure_{datetime.now().strftime('%d_%m_%Y_%I_%M_%p')}"


def upload_report_to_cloud():
    """This method upload the allure report to the google cloud storage and return the cloud link"""
    report_cloud_url = ''
    bucket = storage_client.bucket(bucket_name)
    allure_files_path = glob.glob(allure_report_path + '/**', recursive=True)
    try:
        for item in allure_files_path:
            if os.path.isfile(item):
                sub_directory = item.split("allure_report")[-1].replace("\\", "/")
                blob = bucket.blob(allure_report_cloud_path+sub_directory)
                blob.upload_from_filename(item)
        report_cloud_url = f"https://storage.googleapis.com/{bucket_name}/{allure_report_cloud_path}/index.html"
    except Exception as e:
        print(f"Exception occurred while uploading allure to cloud: {e}")
    return report_cloud_url


def delete_allure_result_and_failed_screenshots():
    """This method deletes the allure result folder and failed screenshots"""
    allure_result_path = os.path.join(os.path.abspath(__file__+"/../../"), "Report\\allure_result")
    shutil.rmtree(allure_result_path, ignore_errors=True)
    screenshot_folder = os.path.join(os.path.abspath(__file__+"/../../"), "Failed_Screenshots")
    for file in os.listdir(screenshot_folder):
        os.remove(f"{screenshot_folder}\\{file}")


delete_allure_result_and_failed_screenshots()