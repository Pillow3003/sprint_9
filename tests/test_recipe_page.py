import allure

import data
from pages.recipe_page import RecipePage


class TestRecipePage():

    @allure.title('Создание нового рецепта и отображение карточки')
    @allure.description('Проверить, что после создания рецепта отображается его карточка.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_recipe_card_recipe(self, driver, createaccount, loginaccount):
        testcreaterecipe = RecipePage(driver)

        recipe_params = testcreaterecipe.create_recipe()

        assert recipe_params[1] == data.RECIPE_FORM_EDIT

    @allure.title('Проверка названия созданного рецепта')
    @allure.description('Убеждаемся, что отображается название, которое вводили при создании.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_recipe_name_recipe(self, driver, createaccount, loginaccount):
        testcreaterecipe = RecipePage(driver)

        recipe_params = testcreaterecipe.create_recipe()

        assert recipe_params[0] == data.RECIPE_NAME