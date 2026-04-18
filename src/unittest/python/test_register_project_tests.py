"""class for testing the register_document method"""
import unittest
import os
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRegisterProject(unittest.TestCase):
    """class for testing the register_document method"""
    @staticmethod
    def _write_test_file(self, file_path: str, content: str):
        """Creates the test file with the provided content."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def _delete_test_file(self, file_path: str):
        """Deletes the test file if it exists."""
        if os.path.exists(file_path):
            os.remove(file_path)

    def _assert_invalid_case(self, file_path: str, content: str):
        """Creates a file, calls the method, and checks it raises the exception."""
        manager = EnterpriseManager()
        self._write_test_file(file_path, content)
        try:
            with self.assertRaises(EnterpriseManagementException):
                manager.register_document(file_path)
        finally:
            self._delete_test_file(file_path)

    def _assert_file_not_found(self, file_path: str):
        """Checks the method raises the exception when the file does not exist."""
        manager = EnterpriseManager()
        if os.path.exists(file_path):
            os.remove(file_path)
        with self.assertRaises(EnterpriseManagementException):
            manager.register_document(file_path)

    def test_TC1(self):
        pass

    def test_TC2(self):
        pass

    def test_TC3(self):
        pass

    def test_TC4(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc4-invalid_pdf.json",
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC5(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc5-invalid_pdf.json",
            '{\n'
            ', "FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC6( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc6-invalid_pdf.json",
            '{\n'
            'PROJECT_ID"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC7( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc7-invalid_pdf.json",
            '{\n'
            '"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC8( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc8-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID: "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC9( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc9-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID" "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC10( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc10-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC11( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc11-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC12(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc12-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90,\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC13(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc13-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90"\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC14(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc14-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '}'
        )

    def test_TC15(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc15-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            'FILENAME"": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC16(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc16-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC17(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc17-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME: "TstFile4.pdf"\n'
            '}'
        )

    def test_TC18(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc18-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME" "TstFile4.pdf"\n'
            '}'
        )

    def test_TC19(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc19-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": TstFile4.pdf"\n'
            '}'
        )

    def test_TC20(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc20-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": ".pdf"\n'
            '}'
        )

    def test_TC21(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc21-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4"\n'
            '}'
        )

    def test_TC22(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc22-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf\n'
            '}'
        )

    def test_TC23(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc23-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
        )

    def test_TC24(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc24-invalid_pdf.json",
            '{\n'
            '}\n'
        )

    def test_TC25(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc25-invalid_pdf.json",
            ''
        )

    def test_TC26(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc26-invalid_pdf.json',
            '{{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC27(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc27-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90", "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC28(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc28-invalid_pdf.json',
            '{\n  ""PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC29(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc29-invalid_pdf.json',
            '{\n  "PROJECT_IDPROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC30(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc30-invalid_pdf.json',
            '{\n  "PROJECT_ID"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC31(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc31-invalid_pdf.json',
            '{\n  "PROJECT_ID":: "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC32(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc32-invalid_pdf.json',
            '{\n  "PROJECT_ID": ""a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC33(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc33-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC34(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc34-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90"",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC35(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc35-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",,\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC36(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc36-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf", "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC37(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc37-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  ""FILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC38(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc38-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAMEFILENAME": "TstFile4.pdf"\n}'
        )

    def test_TC39(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc39-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME"": "TstFile4.pdf"\n}'
        )

    def test_TC40(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc40-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME":: "TstFile4.pdf"\n}'
        )



if __name__ == '__main__':
    unittest.main()
