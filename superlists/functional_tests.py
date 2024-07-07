from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online para
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get("http://localhost:8000")

        # Ela percebe que o título da página e o cabeçalho mencionam listas de
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # Ela é convidada a inserir um item de tarefa imediatamente

        # Ela digita "Arrumar minha cama" em uma caixa de texto

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # "1: Arrumar a cama" como um item em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto, convidando-a a acrescentar outro
        # item. Ela insere "Fazer café da manhã"

        # A página é atualizada novamente e agora mostra dois item em sua lista

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela -- há um pequeno
        # texto explicativo para isso

        # Ela acessa essa URL - sua lista de tarefas continua lá

        # satisfeita, ela volta a dormir

if __name__ == '__main__':
    unittest.main(warnings='ignore')