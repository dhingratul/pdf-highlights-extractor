import unittest
from pdfhextract.core import PdfHighlightExtractor


class TestPdfHighlightExtractor(unittest.TestCase):
    def test_read_one_file(self):
        hex = PdfHighlightExtractor()
        highlights = hex.read_one_file("pdfhextract/tests/test_data/pose/OpenPose.pdf")
        self.assertEqual(len(highlights), 2)
        self.assertEqual(highlights[0], "Part Afﬁnity Fields (PAFs),")

    def test_read_directory(self):
        hex = PdfHighlightExtractor()
        highlights = hex.read_directory("pdfhextract/tests/test_data/pose")
        self.assertEqual(len(highlights), 2)
        self.assertEqual(highlights[0], "Part Afﬁnity Fields (PAFs),")


if __name__ == "__main__":
    unittest.main()
