from selenium.webdriver.common.by import By

class RecipePageLocators:
    create_recipe_tab = By.XPATH, "//a[text()='Создать рецепт']"  # Вкладка для создания рецепта

    recipe_input_fields = By.XPATH, "//input[@class[contains(.,'styles_inputField__3eqTj')]]"  # Поля для заполнения рецепта
    recipe_description = By.XPATH, "//textarea[@class='styles_textareaField__1wfhC']"  # Описание рецепта
    ingredients_container = By.XPATH, "//div[@class='styles_container__3ukwm']"  # Контейнер списка ингредиентов
    add_ingredient_button = By.XPATH, "//div[@class='styles_ingredientAdd__3fc32']"  # Кнопка добавления ингредиента
    ingredient_div = By.XPATH, "//div"  # Общий див для ингредиента (при необходимости уточнить)

    recipe_image_form = By.XPATH, "//div[@class='styles_button__xzu5F']"  # Форма выбора файла с изображением
    recipe_image_input = By.XPATH, "//input[@class='styles_fileInput__3HjP3']"  # Поле загрузки файла с изображением

    create_recipe_button = By.XPATH, "//button[text()='Создать рецепт']"  # Кнопка подтверждения создания рецепта

    recipe_title_card = By.XPATH, "//h1[@class='styles_single-card__title__2QMPq']"  # Название рецепта на карточке
    edit_recipe_link = By.XPATH, "//a[@class[contains(.,'style_link__1kPh8 styles_single-card__edit__Mb_wc')]]"  # Ссылка для редактирования рецепта

    first_ingredient_div = By.CSS_SELECTOR, "div:first-child"  # Первый элемент списка ингредиентов