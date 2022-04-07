import unittest

from src.task_decider import *
from src.task import Task

class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Wash Dishes", 20)
        self.task2 = Task("Cook Dinner", 60)
        self.task3 = Task("Clean Windows", 90)
        self.task4 = Task("Wash Clothes", 40)
        self.task5 = Task("Do Ironing", 30)

    def test_input_wash_dishes_dinner(self):
        self.input_wash_dishes = get_preferred_option(self.task1, self.task2)
        self.assertTrue("Wash Dishes", self.input_wash_dishes)
    
    def test_input_wash_dishes_dinner2(self):
        self.input_wash_dishes = get_preferred_option(self.task2, self.task1)
        self.assertTrue("Wash Dishes", self.input_wash_dishes)

    def test_input_cook_dinner_windows(self):
        self.input_cook_dinner = get_preferred_option(self.task2, self.task3)
        self.assertTrue("Cook Dinner", self.input_cook_dinner)

    def test_input_cook_dinner_windows2(self):
        self.input_cook_dinner = get_preferred_option(self.task3, self.task2)
        self.assertTrue("Cook Dinner", self.input_cook_dinner)
    
    def test_input_cook_dinner_ironing(self):
        self.input_cook_dinner = get_preferred_option(self.task2, self.task5)
        self.assertTrue("Cook Dinner", self.input_cook_dinner)
    
    def test_input_cook_dinner_ironing2(self):
        self.input_cook_dinner = get_preferred_option(self.task5, self.task2)
        self.assertTrue("Cook Dinner", self.input_cook_dinner)
    
    def test_input_clean_windows_dishes(self):  
        self.input_cook_dinner = get_preferred_option(self.task3, self.task1)
        self.assertTrue("Clean Windows", self.input_cook_dinner)

    def test_input_clean_windows_dishes2(self):  
        self.input_cook_dinner = get_preferred_option(self.task1, self.task3)
        self.assertTrue("Clean Windows", self.input_cook_dinner)
    

