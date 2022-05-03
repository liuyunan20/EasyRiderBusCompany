class TestPetOwner(unittest.TestCase):

    def setUp(self):
        self.pet_owner = PetOwner('Polly', 'parrot', 'Joshy')

    def test_add(self):
        self.assertEqual(self.pet_owner.owner_with_pet(), 'Polly has a parrot named Joshy')
        self.pet_owner.spec = 'dog'
        self.assertEqual(self.pet_owner.owner_with_pet(), 'Polly has a dog named Joshy')


if __name__ == '__main__':
    unittest.main()
