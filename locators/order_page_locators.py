from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_NEXT_BUTTON = By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM'
    TOP_ORDER_BUTTON = By.CSS_SELECTOR, ".Header_Nav__AGCXC > button:nth-child(1)"
    BOTTOM_ORDER_BUTTON = By.CSS_SELECTOR, ".Header_Nav__AGCXC > button:nth-child(1)"
    ORDER_INPUT_NAME = By.CSS_SELECTOR, '.Input_Input__1iN_Z[placeholder="* Имя"]'
    ORDER_INPUT_LAST_NAME = By.CSS_SELECTOR, '.Input_Input__1iN_Z[placeholder="* Фамилия"]'
    ORDER_INPUT_ADDRESS = By.CSS_SELECTOR, '.Input_Input__1iN_Z[placeholder="* Адрес: куда привезти заказ"]'
    ORDER_INPUT_STATION_ALL = By.CSS_SELECTOR, 'input.select-search__input[placeholder="* Станция метро"]'
    ORDER_INPUT_STATION = By.CSS_SELECTOR, 'button.Order_SelectOption__82bhS.select-search__option[value="9"]'
    ORDER_INPUT_MOBILE = By.CSS_SELECTOR, '.Input_Input__1iN_Z[placeholder="* Телефон: на него позвонит курьер"]'
    ORDER_BACK_BUTTON = By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM'
    ORDER_INPUT_WHEN_1 = By.CSS_SELECTOR, '.Input_Input__1iN_Z[placeholder="* Когда привезти самокат"]'
    ORDER_INPUT_WHEN_2 = By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day--014'
    ORDER_INPUT_RENTAL_PERIOD_1 = By.CSS_SELECTOR, "div.Dropdown-control"
    ORDER_INPUT_RENTAL_PERIOD_2 = By.CSS_SELECTOR, "div.Dropdown-option:nth-child(3)"
    ORDER_INPUT_COLOR = By.CSS_SELECTOR, 'input#black'
    ORDER_INPUT_COMMENT = By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']"
    ORDER_INPUT_WANNA_ORDER_YES_BUTTON = By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']"
    ORDER_INPUT_WANNA_ORDER = By.CSS_SELECTOR, 'div.Order_Buttons__1xGrp button:nth-of-type(2)'
    ORDER_SUCCESSFULLY_PLACED = By.CSS_SELECTOR, '.Order_Text__2broi'
    LOGO_SCOOTER = By.CSS_SELECTOR, 'a.Header_LogoScooter__3lsAR'
    SCOOTER_MAIN_PAGE_TEXT = By.CSS_SELECTOR, 'div.Home_Header__iJKdX'
    YANDEX_LOGO = By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI[href='//yandex.ru']"









