from bs4 import BeautifulSoup
with open('G:/Python_Code/Crowler4Week/week1/1_1codeInVideo/the_blah.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    print(Soup)