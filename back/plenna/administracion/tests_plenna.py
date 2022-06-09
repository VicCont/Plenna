

from django.test import Client, TestCase

class Prueba(TestCase):


    def test_login(self):

        c = Client()
 
        response = c.post('/login/', {'usu':'doctor 2', 'pass':'basura'})
        

        self.assertTemplateUsed('administacion:vista_doc.html')

        c = Client()

        response = c.post('/login/', {'usu':'doctor a', 'pass':'basura'})

        self.assertTemplateUsed('administacion:login.html')

    def test_loginA(self):

        c = Client()
 
        response = c.post('/loginA/', {'usu':'doctor 2', 'pass':'basura'})
        

        self.assertTemplateUsed('administacion:vista_dra_gral.html')

        c = Client()

        response = c.post('/loginA/', {'usu':'doctor a', 'pass':'basura'})

        self.assertTemplateUsed('administacion:login.html')

    def 



        
