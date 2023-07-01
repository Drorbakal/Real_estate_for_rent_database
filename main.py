import csv
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.ad.co.il")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10000)
    link_element = driver.find_elements(By.CSS_SELECTOR, "a.home-card-link.home-lobby")[1]
    link_element.click()
    time.sleep(7)
    Type = []
    Area = []
    Balcony = []
    Floor = []
    Build_Size = []
    Pay_For_A_Year = []
    City = []
    Rooms = []
    Address = []
    Price = []
    count = 0
    number_of_pages = driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[1]/div/div/h6')
    print(number_of_pages.text)
    if "מתוך" in number_of_pages.text:
        text = number_of_pages.text
        key, value = text.split("מתוך ")
        print("key" , key)
        print("value" , value)
    if ")" in value:
        text = value
        key, value = text.split(")")
        print("key" , key)
        print("value" , value)

    end_of_pages = int(key)
    for j in range(1 , end_of_pages):
        driver.get(f'https://www.ad.co.il/nadlanrent?pageindex={j}')
        try:
            elements = driver.find_elements(By.CLASS_NAME, 'card-block')
        except:
            continue
        end = len(elements) - 3
        time.sleep(7)
        for i in range(end):
            count += 1
            print('page ' , j , 'item ' ,i)
            try:
                elements[i].click()
                time.sleep(7)
                try:
                    inside_elements = driver.find_element(By.CLASS_NAME, 'col-xxl-4.col-lg-4.col-md-5')
                    try:
                        address = inside_elements.find_element(By.CLASS_NAME, 'card-title')
                        Address.append(address.text)
                    except:
                        Address.append('0')
                    try:
                        price = inside_elements.find_elements(By.CSS_SELECTOR, 'h2.card-title')[1]
                        Price.append(price.text)
                    except:
                        Price.append('0')

                    try:
                        area_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[2]
                        if "אזור" in area_check.text:
                            area_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[3]
                            Area.append(area_to_data.text)
                    except:
                        Area.append('0')
                    try:
                        city_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[4]
                        if "עיר" in city_check.text:
                            city_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[5]
                            City.append(city_to_data.text)
                    except:
                        City.append('0')
                    try:
                        rooms_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[8]
                        if "חדרים" in rooms_check.text:
                            rooms_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[9]
                            Rooms.append(rooms_to_data.text)
                        else:
                            try:
                                rooms_check_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[10]
                                if "חדרים" in rooms_check_2.text:
                                    rooms_to_data_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[11]
                                    Rooms.append(rooms_to_data_2)
                            except:
                                Rooms.append('0')
                    except:
                        Rooms.append('0')
                    try:
                        types_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[0]
                        if "פרטי הנכס" in types_check.text:
                            types_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[1]
                            Type.append(types_to_data.text)
                    except:
                        Type.append('0')
                    try:
                        balcony_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[10]
                        if "מרפסות" in balcony_check.text:
                            balcony_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[11]
                            Balcony.append(balcony_to_data.text)
                        else:
                            try:
                                balcony_check_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[12]
                                if "מרפסות" in balcony_check_2.text:
                                    balcony_to_data_2 = inside_elements.find_elements(By.CSS_SELECTOR, td)[13]
                                    Balcony.append(balcony_to_data_2.text)
                            except:
                                Balcony.append('0')
                    except:
                        Balcony.append('0')
                    try:
                        floor_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[12]
                        if "קומה" in floor_check.text:
                            floor_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[13]
                            Floor.append(floor_to_data.text)
                        else:
                            try:
                                floor_check_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[14]
                                if "קומה" in floor_check_2.text:
                                    floor_to_data_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[15]
                                    Floor.append(floor_to_data_2.text)
                            except:
                                Floor.append('0')
                    except:
                        Floor.append('0')
                    try:
                        build_size_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[14]
                        if "שטח בנוי" in build_size_check.text:
                            build_size_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[15]
                            Build_Size.append(build_size_to_data.text)
                        else:
                            try:
                                build_size_check_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[16]
                                if "שטח בנוי" in build_size_check_2.text:
                                    build_size_to_data_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[17]
                                    Build_Size.append(build_size_to_data_2.text)
                            except:
                                Build_Size.append('0')
                    except:
                        Build_Size.append('0')
                    try:
                        pay_for_year_check = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[16]
                        if "תשלומים בשנה" in pay_for_year_check.text:
                            pay_for_year_to_data = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[17]
                            Pay_For_A_Year.append(pay_for_year_to_data.text)
                        else:
                            try:
                                pay_for_year_check_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[18]
                                if "תשלומים בשנה" in pay_for_year_check_2.text:
                                    pay_for_year_to_data_2 = inside_elements.find_elements(By.CSS_SELECTOR, 'td')[19]
                                    Pay_For_A_Year.append(pay_for_year_to_data_2.text)
                            except:
                                Pay_For_A_Year.append('0')
                    except:
                        Pay_For_A_Year.append('0')
                    try:
                        wait.until(EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="pop-modal"]/div/div/div[1]/div/button'))).click()
                    except:
                        break
                except:
                    break
            except :
                break

    print(count)

    data = [['Address ', 'Price ', 'Pay For A Year ', 'Meters ', 'Rooms ',
             'City ', 'Build Size ', 'Floor ', 'Balcony ', 'Area ', 'Type ']]
    file_path = 'C:/Users/Asus/pythonProject4/First_Data_Base.csv'
    data_2 = [Address, Price, Pay_For_A_Year,Rooms, City, Build_Size, Floor, Balcony, Area, Type]
    try:
        with open(file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)
            for k in range(0, count):
                try:
                    data_2 = [Address[k], Price[k], Pay_For_A_Year[k], Rooms[k], City[k], Build_Size[k],
                              Floor[k], Balcony[k], Area[k], Type[k]]
                    csv_writer.writerow(data_2)
                except:
                    continue
    except IOError:
        print("Error creating file or taking permissions")
    else:
        print("Data written successfully")

    csv_file.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
