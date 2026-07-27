import os
import unittest
from retos_cli.repository.challenge_repository import find_challenge
from retos_cli.repository.file_repository import find_challenge_file
from retos_cli.core.create import create_challenge_file
from retos_cli.core.review import review_challenge


class TestRetosCLI(unittest.TestCase):

    def test_find_challenge_exists(self):
        challenge = find_challenge(1)
        self.assertIn("name", challenge)
        self.assertEqual(challenge["number"], 1)

    def test_find_challenge_not_found(self):
        challenge = find_challenge(999999)
        self.assertEqual(challenge, {})

    def test_find_challenge_file(self):
        path = find_challenge_file(1)
        self.assertIsNotNone(path)
        self.assertTrue(path.startswith("Ejercicios_Logica/"))

    def test_create_challenge_file(self):
        result = create_challenge_file(1)
        if isinstance(result, tuple):
            self.assertEqual(result[0], "success")
            file_path = result[2]
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
        else:
            self.assertEqual(result, "already exist file")

    def test_review_challenge_debug(self):
        os.environ["DEBUG"] = "true"
        try:
            report = review_challenge(28)
            self.assertIn("Review Report", report)
        finally:
            os.environ.pop("DEBUG", None)


if __name__ == "__main__":
    unittest.main()
