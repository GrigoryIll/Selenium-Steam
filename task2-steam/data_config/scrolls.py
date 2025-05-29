class Scrolls:

    def __init__(self, driver):
        self.driver = driver

    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, element):
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)
