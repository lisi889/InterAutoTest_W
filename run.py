from config import Conf
import os
import pytest
if __name__ == '__main__':

    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "test_excel_case.py", "--alluredir", report_path])