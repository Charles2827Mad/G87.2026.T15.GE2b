"""class for testing the register_document method"""
import unittest
import os
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRegisterProject(unittest.TestCase):
    """class for testing the register_document method"""
    @staticmethod
    def _write_test_file(file_path: str, content: str):
        """Creates the test file with the provided content."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def _delete_test_file(file_path: str):
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

    def test_tc_1(self):
        manager = EnterpriseManager()
        result = manager.register_document(
            "desktop/register_document/valid/tc1-valid_pdf.json"
        )
        self.assertEqual(
            "3c296a4a2ebe42d02236ac7fa24f7156676ba60cc5ccc9309d3f2bd4f0b112ad",
            result
        )

    def test_tc_2(self):
        manager = EnterpriseManager()
        result = manager.register_document(
            "desktop/register_document/valid/tc2-valid_pdf.json"
        )
        self.assertEqual(
            "14a957d0b6dd2235f404a6165cbd51329b54e55c40c0c71fd7d064e8b32142f9",
            result
        )

    def test_tc_3(self):
        manager = EnterpriseManager()
        result = manager.register_document(
            "desktop/register_document/valid/tc3-valid_pdf.json"
        )
        self.assertEqual(
            "31d49ce57e610e2769b369f5b37428810a4d763d1238ca096f66eab5b0e0d7b8",
            result
        )

    def test_tc_4(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc4-invalid_pdf.json",
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_5(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc5-invalid_pdf.json",
            '{\n'
            ', "FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_6( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc6-invalid_pdf.json",
            '{\n'
            'PROJECT_ID"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_7( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc7-invalid_pdf.json",
            '{\n'
            '"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_8( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc8-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID: "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_9( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc9-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID" "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_10( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc10-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_11( self ):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc11-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_12(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc12-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90,\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_13(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc13-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90"\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_14(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc14-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '}'
        )

    def test_tc_15(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc15-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            'FILENAME"": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_16(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc16-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"": "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_17(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc17-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME: "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_18(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc18-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME" "TstFile4.pdf"\n'
            '}'
        )

    def test_tc_19(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc19-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": TstFile4.pdf"\n'
            '}'
        )

    def test_tc_20(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc20-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": ".pdf"\n'
            '}'
        )

    def test_tc_21(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc21-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4"\n'
            '}'
        )

    def test_tc_22(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc22-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf\n'
            '}'
        )

    def test_tc_23(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc23-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
        )

    def test_tc_24(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc24-invalid_pdf.json",
            '{\n'
            '}\n'
        )

    def test_tc_25(self):
        self._assert_invalid_case(
            "desktop/register_document/deletion/tc25-invalid_pdf.json",
            ''
        )

    def test_tc_26(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc26-invalid_pdf.json',
            '{{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_27(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc27-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90", "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_28(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc28-invalid_pdf.json',
            '{\n  ""PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_29(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc29-invalid_pdf.json',
            '{\n  "PROJECT_IDPROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_30(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc30-invalid_pdf.json',
            '{\n  "PROJECT_ID"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_31(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc31-invalid_pdf.json',
            '{\n  "PROJECT_ID":: "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_32(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc32-invalid_pdf.json',
            '{\n  "PROJECT_ID": ""a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_33(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc33-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_34(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc34-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90"",\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_35(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc35-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",,\n  "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_36(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc36-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf", "FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_37(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc37-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  ""FILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_38(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc38-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAMEFILENAME": "TstFile4.pdf"\n}'
        )

    def test_tc_39(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc39-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME"": "TstFile4.pdf"\n}'
        )

    def test_tc_40(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc40-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME":: "TstFile4.pdf"\n}'
        )

    def test_tc_41(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc41-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": ""TstFile4.pdf"\n}'
        )

    def test_tc_42(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc42-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4TstFile4.pdf"\n}'
        )

    def test_tc_43(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc43-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf.pdf"\n}'
        )

    def test_tc_44(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc44-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.docx.docx"\n}'
        )

    def test_tc_45(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc45-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.xlsx.xlsx"\n}'
        )

    def test_tc_46(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc46-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf""\n}'
        )

    def test_tc_47(self):
        self._assert_invalid_case(
            'desktop/register_document/duplication/tc47-invalid_pdf.json',
            '{\n  "PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n  "FILENAME": "TstFile4.pdf"\n}}'
        )

    def test_TC48(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc48-invalid_pdf.json",
            '/\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC49(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc49-invalid_pdf.json",
            '{\n'
            '"PROJ": "a1b8c3d4e3f60148293a4b0c6d5e1f9011",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC50(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc50-invalid_pdf.json",
            '{\n'
            '*PROJECT_ID"": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC51(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc51-invalid_pdf.json",
            '{\n'
            '"P": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC52(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc52-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID^: "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC53(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc53-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID"- "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC54(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc54-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": *a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC55(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc55-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC56(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc56-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90^,\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC57(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc57-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90".\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC58(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc58-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENME": "TstFile4.a"\n'
            '}'
        )

    def test_TC59(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc59-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '\\FILENAME"": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC60(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc60-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"File": "TstFile4.pdf"\n'
            '}'
        )

    def test_TC61(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc61-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME*: "TstFile4.pdf"\n'
            '}'
        )

    def test_TC62(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc62-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME"< "TstFile4.pdf"\n'
            '}'
        )

    def test_TC63(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc63-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": ^TstFile4.pdf"\n'
            '}'
        )

    def test_TC64(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc64-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile433.pdf"\n'
            '}'
        )

    def test_TC65(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc65-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdd"\n'
            '}'
        )

    def test_TC66(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc66-invalid_docx.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.docy"\n'
            '}'
        )

    def test_TC67(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc67-invalid_xlsx.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.xlzx"\n'
            '}'
        )

    def test_TC68(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc68-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf*\n'
            '}'
        )

    def test_TC69(self):
        self._assert_invalid_case(
            "desktop/register_document/modification/tc69-invalid_pdf.json",
            '{\n'
            '"PROJECT_ID": "a1b8c3d4e3f60148293a4b0c6d5e1f90",\n'
            '"FILENAME": "TstFile4.pdf"\n'
            '|'
        )


if __name__ == '__main__':
    unittest.main()
