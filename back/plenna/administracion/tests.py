from django.test import Client, TestCase

class Prueba(TestCase):
    def test_login(self):

        c = Client()

        response = c.post('/login/', {'usu':'doctor 2', 'pass':'basura'})
        

        self.assertTemplateUsed('administacion:vista_doc.html')