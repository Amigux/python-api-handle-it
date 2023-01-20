import unittest
import HtmlTestRunner

from application import Application
from machine import Machine

class TestApplication(unittest.TestCase):
    # Initialisation de données pour mes tests
    def setUp(self):
        self.demo_donnes=('ma_super_liste',1)
        self.data="data"
    
    # Nettoyage après les tests
    def tearDown(self) -> None:
        print('Je nettoie les données')
        return super().tearDown()
    

    # Exemple de test avec un echec (failure)
    # def test_liste_application_ko(self):
    #     contenu_liste = Application.liste()
    #     self.assertEquals(contenu_liste,'Une phrase')

    def test_liste_application_ok(self):
        contenu_liste = Application.liste()
        self.assertEqual(contenu_liste,'Liste des applications')
        
    def test_add_func_application(self):
    	message_returned = Application.add(self.data)
    	self.assertEqual(message_returned, 'Application ajoutée')


#class TestMachines(unittest.TestCase):
#    def test_ajout_machine(self):
#        ajout_machine = Machine.add((),('mes donnees à écrire',"fichier=machines.json"))
#        with open('machines.json', 'r') as f:
#            try:
#                contenu_fichier = json.load(f)
#            except Exception as e:
#                print("Exception raised | %s " % str(e))
#                exit()
#        self.assertIn(contenu_fichier,'mes donnees à écrire')
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
    
