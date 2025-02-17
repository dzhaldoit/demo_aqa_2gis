import allure
from selene import browser, be
from demo_aqa_2gis_tests.test_data.data import Urls


class RoutePage:
    @allure.step('Открытие главной страницы')
    def browser_open(self):
        browser.open(Urls.main_url())
        return self

    @allure.step('Поиск маршрута')
    def searching_for_route(self):
        browser.element('//input[@placeholder="Поиск в 2ГИС"]').should(be.visible).click().type(
            'Московский Кремль').press_enter()
        browser.element('(//span[text()="Московский Кремль"])[1]').should(be.visible).click()
        return self

    @allure.step('Клик по маршруту')
    def finding_route(self):
        browser.element('//span[text()="Проехать"]').click()
        return self

    @allure.step('Выбор маршрута откуда')
    def checking_route(self):
        browser.element('//input[@placeholder="Откуда"]').send_keys("Санкт-Петербург")
        browser.element('//div[text()="Санкт-Петербург"]').click()
        return self

    @allure.step('Проверка что есть построенный маршрут')
    def checking_distance(self):
        browser.element('//div[@class="_sgs1pz"]').should(be.visible)
        return self


route_page = RoutePage()
