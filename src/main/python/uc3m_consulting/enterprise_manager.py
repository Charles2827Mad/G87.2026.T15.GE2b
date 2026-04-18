"""Module """
import json
import re
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True

    @staticmethod
    def register_document(input_file: str):
        try:
            with open(input_file, "r", encoding="utf-8") as file:
                try:
                    input_data = json.load(file)
                except json.JSONDecodeError as exc:
                    raise EnterpriseManagementException(
                        "The file is not JSON formatted"
                    ) from exc
        except FileNotFoundError as exc:
            raise EnterpriseManagementException("Input file not found") from exc

        if not isinstance(input_data, dict):
            raise EnterpriseManagementException(
                "JSON does not have the expected structure"
            )

        if "PROJECT_ID" not in input_data or "FILENAME" not in input_data:
            raise EnterpriseManagementException(
                "JSON does not have the expected structure"
            )

        project_id = input_data["PROJECT_ID"]
        file_name = input_data["FILENAME"]

        if not isinstance(project_id, str) or not isinstance(file_name, str):
            raise EnterpriseManagementException(
                "JSON data has no valid values"
            )

        if not re.fullmatch(r"[0-9a-fA-F]{32}", project_id):
            raise EnterpriseManagementException(
                "JSON data has no valid values"
            )

        if not re.fullmatch(r"[A-Za-z0-9]{8}(\.pdf|\.docx|\.xlsx)", file_name):
            raise EnterpriseManagementException(
                "JSON data has no valid values"
            )

        return input_data