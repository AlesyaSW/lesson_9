from selene import by, be
from selene import browser


def test_github():

    browser.open_url("https://github.com")
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("AlesyaSW/lesson_9")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("AlesyaSW/lesson_9")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("homework_9")).should(be.visible)