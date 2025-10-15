import allure
from pages.form_field import FormField

@allure.feature("Заполнение форм")
@allure.title("Позитивный тест на заполнение всех форм, получение алерта после отправки")

def test_positive(driver):
    url = "https://practice-automation.com/form-fields/"
    page = FormField(driver, url)
    name = "Test Name"
    password = "Test password"
    email = "test@example.com"

    with allure.step("Открытие страницы"):
        page.open()

    with allure.step("Заполнить поле Name"):
        page.fill_name(name)

    with allure.step("Заполнить поле Password"):
        page.fill_password(password)

    with allure.step("Выбрать Milk"):
        page.choose_milk()

    with allure.step("Выбрать Coffee"):
        page.choose_coffee()

    with allure.step("Выбрать Yellow"):
        page.choose_yellow()

    with allure.step("Выбираем Yes"):
        page.automation_yes()

    with allure.step("Заполнить Email"):
        page.fill_email(email)

    with allure.step("Заполнить Message"):
        page.fill_message()

    with allure.step("Нажать Submit"):
        page.submit()

    with allure.step("Проверить алерт"):
        page.submit_result()


@allure.title("Негативный тест на заполнение всех форм кроме Name, и на отсутствие алерта")
def test_negative(driver):
    url = "https://practice-automation.com/form-fields/"

    page = FormField(driver, url)

    name = ""
    password = "password"
    email = "mail@mail.com"

    with allure.step("Открытие страницы"):
        page.open()

    with allure.step("Заполнить поле Name"):
        page.fill_name(name)

    with allure.step("Заполнить поле Password"):
        page.fill_password(password)

    with allure.step("Выбрать Milk"):
        page.choose_milk()

    with allure.step("Выбрать Coffee"):
        page.choose_coffee()

    with allure.step("Выбрать Yellow"):
        page.choose_yellow()

    with allure.step("Выбираем Yes"):
        page.automation_yes()

    with allure.step("Заполнить Email"):
        page.fill_email(email)

    with allure.step("Заполнить Message"):
        page.fill_message()

    with allure.step("Нажать Submit"):
        page.submit()

    with allure.step("Проверить что алерт отсутствует"):
        page.no_submit_alert()