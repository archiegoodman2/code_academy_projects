import surfshop 
import unittest
import datetime

class TestCase(unittest.TestCase):

  #get the shopping cart class from our file
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  #test adding a single surfboard
  def test_add_surfboard(self):
    #first, store the result of calling the add_surfboards function
        message = self.cart.add_surfboards(quantity=1)
        #should return this string if successful:
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  #if you care about performance, should just do individual test cases for normal numbers + edge cases because Python For Loops are absolutely awful     
  def test_add_surfboards(self):
      for i in range(2, 5):
        #the with keyword allows us to replace try-catch blocks, allowing the code to be more readable
           with self.subTest(i=i):
              message = self.cart.add_surfboards(i)
              #assert equal checks that the output of a funct is as expected
              self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
              self.cart = surfshop.ShoppingCart()
  
  @unittest.skip #this wrapper means it expects a failure
  def test_too_many_boards(self):
    #assertRaises checks if it's raising the right error
    self.assertRaises(surfshop.TooManyBoardsError, surfshop.ShoppingCart.add_surfboards, 5)

#test locals discount functionality
  def test_apply_locals_discount(self):
    #call method
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

#testing checkout date error:
def test_add_invalid_checkout_date(self):
      #get current date
      date = datetime.datetime.now()
      self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)


unittest.main() ##all tests should pass

    
  
