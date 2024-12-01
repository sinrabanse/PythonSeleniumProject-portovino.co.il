# Software Testing Automation Project

This project is part of the course "Software Testing: Automation and Programming (Python, Selenium)" on the [Stepik platform](https://stepik.org/).

### Objective
The goal of this project is to perform a sanity test on the website [https://www.portovino.co.il/](https://www.portovino.co.il/) to ensure the functionality of the checkout process. The test includes:

1. Navigating through the main page
2. Visiting the whisky category page
3. Adding a product to the cart
4. Adding a gift box to the cart
5. Checking the checkout page

### Test Overview
The automation test goes through the following steps:

1. **Main Page**: Test starts by visiting the main page and clicking necessary elements.
2. **Whisky Page**: Navigate to the whisky category and select a product.
3. **Cart Page**: Verify the product is added to the cart along with a gift box.
4. **Checkout Page**: Proceed to the checkout page to simulate the final step of the purchase process.

### Technologies Used
- Python
- Selenium WebDriver
- Pytest for test execution
- WebDriverWait

### How to Run the Tests
1. Clone the repository:
    ```bash
    git clone https://github.com/sinrabanse/PythonSeleniumProject-portovino.co.il.git
    cd PythonSeleniumProject-portovino.co.il
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tests:
    ```bash
    pytest ./tests/test_buy_product.py
    ```

### Notes
- Make sure you have ChromeDriver installed and accessible in your system's PATH.
- The test simulates an automated user journey, including product selection and checkout, ensuring the website’s functionality from product selection to checkout.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
