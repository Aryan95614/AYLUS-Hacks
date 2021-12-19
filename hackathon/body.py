from collections import deque
import PySimpleGUI as sg
from selenium import webdriver
import sys

class country:
    def __init__(self, info):
        self.info: str = info
        DRIVER_PATH = "C:/Users/aryan/PycharmProjects/sample/hackathon/chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)



    def findInfo(self):


        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(., '" + self.info + "')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")

        total_cases = data[2]
        total_pop = data[-1]
        active_cases = data[-7]
        total_tests = data[-3]
        total_per = data[-2]
        stack = Stack()


        stack.push(self.info)
        stack.push(total_cases)
        stack.push(total_pop)
        stack.push(active_cases)
        stack.push(total_tests)
        stack.push(total_per)
        return stack
    def close_Window(self):
        self.driver.close()

class Stack(deque):
    def __init__(self):
        super(deque, self).__init__()

    def push(self, element):
        self.append(element)

    def returnList(self):
        return list(self)

    def __repr__(self):
        return self

    def __eq__(self, other) -> bool:
        if isinstance(other) == isinstance(self):
            return True
        return False


class window():
    def __init__(self, title, layout):
        self.title = title
        self.layout = layout
        self.wind = sg.Window(self.title, self.layout)

        self.gameover = False
        self.endProtocol = sg.WIN_CLOSED
        self.events = None
        self.values = None
        self.OKBUTTON = "Ok"

    def runLoop(self, allcountries):
        while not self.gameover:
            self.events, self.values = self.wind.read()
            if self.events == self.endProtocol:
                print('clicked')
                self.gameover = True
            if self.values['-COMBO-'] in allcountries and self.events == self.OKBUTTON:self.wind.close();return self.values
        self.wind.close()

    def runloop(self):
        while not self.gameover:
            self.events, self.values = self.wind.read()
            if self.events == self.endProtocol or self.events == self.OKBUTTON:
                self.gameover = True
                self.wind.close()
        self.wind.close()
