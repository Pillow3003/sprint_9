from selenium.webdriver.common.by import By

class MainPageLocators:
    main_page_header_text = By.XPATH, "//h1[text()='Войти на сайт']"  # Заголовок "Войти на сайт" на главной странице
    login_button = By.XPATH, "//button[text()='Войти']"  # Кнопка входа
    logout_link = By.XPATH, "//a[text()='Выход']"  # Ссылка выхода
    recipes_page_header = By.XPATH, "//h1[text()='Рецепты']"  # Заголовок "Рецепты" на странице рецептов

    create_account_link = By.XPATH, "//a[text()='Создать аккаунт']"  # Ссылка для перехода к созданию аккаунта
    create_account_button = By.XPATH, "//button[text()='Создать аккаунт']"  # Кнопка для регистрации нового аккаунта
    registration_input_fields = By.XPATH, "//input[@class='styles_inputField__3eqTj']"  # Поля ввода при регистрации
    registration_email_input = By.XPATH, "//input[@name='email']"  # Поле ввода email для регистрации
    registration_password_input = By.XPATH, "//input[@name='password']"  # Поле ввода пароля для регистрации