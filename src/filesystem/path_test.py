import unittest

import filesystem.path


class Test(unittest.TestCase):
    def test_get_extension(self) -> None:
        ext = filesystem.path.get_file_extension("/path/to/file.txt")
        self.assertEqual(ext, "txt")
        with self.assertRaises(filesystem.path.AmbiguousExtensionError):
            filesystem.path.get_file_extension("/path/to/file.test.txt")


if __name__ == "__main__":
    unittest.main()
