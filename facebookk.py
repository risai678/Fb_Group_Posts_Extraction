import pandas as pd
from selenium import webdriver
from time import sleep

def main(link):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(link)

    sleep(10)
    names_list = []
    status_list = []
    full_data = []

    namess = driver.find_elements_by_xpath('//*[@class="gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl aahdfvyu hzawbc8m"]')
    statusss = driver.find_elements_by_xpath('//div[@class="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"]')
    persons = driver.find_elements_by_xpath('//div[@class="cwj9ozl2 tvmbv18p"]')

    all_comments = []
    caption = persons[0].find_elements_by_xpath('//div[@class="ecm0bbzt e5nlhep0 a8c37x1j"]')
    for dataa in caption:
        all_comments.append(dataa.text)

    for status in statusss:
        comments = []
        commwnter_name = []
        indd = statusss.index(status)
        status_list.append(status.text)

        names_list.append(namess[indd + 1].text)

        dd = persons[indd].find_elements_by_class_name('nc684nl6')

        for d in dd:
            current = dd.index(d)
            if d.text != '':
                try:
                    if d.text == dd[current + 1].text:
                        commwnter_name.append(d.text)
                except:
                    pass

        for comee in range(0, len(commwnter_name)):
            comments.append(all_comments[0])
            all_comments.pop(0)

        full_data.append([namess[indd + 1].text, status.text, commwnter_name, comments])
    dff=pd.DataFrame(full_data)

    dff.to_csv('data.csv',index=False,header=['Username','Status','Commenters_name','Comments'])


group=input('Enter group url: ')
main(group)