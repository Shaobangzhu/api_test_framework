# Pytest + Request + Allure
1. Utilized Python 3, Pytest, Requests, and Allure to build from scratch the department's interface automation testing.
2. Added and improved the proportion of automated interface test cases, accounting for over 30% of all department interfaces.
3. Detailed design of automated test cases, using Pytest parameterization to enhance case scenarios, covering every interface's conditional branch process, aiming for high test coverage.
4. Learned development knowledge, capable of writing CRUD interfaces independently, and through business encapsulation, achieved the objective of a data factory with product name, product title, product status, product quantity, and product images. Now, by using the interfaces I developed, it only takes two parameters. If a business interface requires many parameters, we can set unnecessary ones to default values, only passing those we frequently need to modify, which greatly improves the efficiency of data creation.

## Allure:
1. Run the test with output an allure report to the report folder: pytest -s testcases/test_get_wallet_info.py --alluredir=report
2. Generate Allure Test Report: allure generate report -o report/api_report
3. Run Allure server locally: allure serve report
4. allure.step
5. allure.description
6. epic, feature, story, tag
7. allure.attach
