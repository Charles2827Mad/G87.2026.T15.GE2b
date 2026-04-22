"""main.py, used to test and generate sample hashes
to compare against valid test cases"""
from uc3m_consulting.project_document import ProjectDocument
from freezegun import freeze_time

@freeze_time("2024-01-28")
def show_sha256():
    """Function used to generate SHA-256 sample hashes for test cases."""
    obj = ProjectDocument(
        "b1b8c3d4e3f60148293a4b0c6d5e1f91",
        "TstFil34.pdf"
    )
    print(obj.document_signature)

if __name__ == '__main__':
    show_sha256()
