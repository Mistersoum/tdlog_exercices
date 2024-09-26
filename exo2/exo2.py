"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""


def solution(string, ending):
    # Utilise la méthode endswith pour vérifier si 'string' se termine par 'ending'.
    # Retourne True si c'est le cas, sinon False.
    return string.endswith(ending)


import unittest

# Création d'une classe de tests unitaires qui hérite de unittest.TestCase
class TestSolution(unittest.TestCase):
    
    # Test pour les cas où la fonction doit retourner True
    def test_fixed_tests_true(self):
        # Ensemble de cas de test où la fonction doit retourner True
        fixed_tests_True = (
            ("samurai", "ai"),   # "samurai" se termine par "ai"
            ("ninja", "ja"),     # "ninja" se termine par "ja"
            ("sensei", "i"),     # "sensei" se termine par "i"
            ("abc", "abc"),      # "abc" se termine par "abc"
            ("abcabc", "bc"),    # "abcabc" se termine par "bc"
            ("fails", "ails"),   # "fails" se termine par "ails"
        )
        
        # Boucle sur chaque cas de test
        for s, e in fixed_tests_True:
            # subTest crée un sous-test pour chaque itération, cela permet de continuer les autres tests
            # même si un test échoue
            with self.subTest(s=s, e=e):
                # Vérifie que solution(s, e) retourne True
                self.assertTrue(solution(s, e))
    
    # Test pour les cas où la fonction doit retourner False
    def test_fixed_tests_false(self):
        # Ensemble de cas de test où la fonction doit retourner False
        fixed_tests_False = (
            ("sumo", "omo"),     # "sumo" ne se termine pas par "omo"
            ("samurai", "ra"),   # "samurai" ne se termine pas par "ra"
            ("abc", "abcd"),     # "abc" ne se termine pas par "abcd"
            ("ails", "fails"),   # "ails" ne se termine pas par "fails"
            ("this", "fails"),   # "this" ne se termine pas par "fails"
            ("spam", "eggs"),    # "spam" ne se termine pas par "eggs"
        )
        
        # Boucle sur chaque cas de test
        for s, e in fixed_tests_False:
            # Utilise subTest pour créer un sous-test pour chaque itération
            with self.subTest(s=s, e=e):
                # Vérifie que solution(s, e) retourne False
                self.assertFalse(solution(s, e))

# Point d'entrée pour exécuter les tests unitaires
if __name__ == "__main__":
    unittest.main()  # Exécute tous les tests définis dans la classe
