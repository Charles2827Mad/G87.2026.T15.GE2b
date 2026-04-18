"""Module """
import json
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

        return input_data