"""Module """
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
                return file.read()
        except FileNotFoundError as exc:
            raise EnterpriseManagementException("Input file not found") from exc