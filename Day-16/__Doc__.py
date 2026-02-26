"""
Day 16
• FastAPI	testing
• Async	tests
• API	test	strategies
• TestClient
"""

"""
FastAPI testing
     - use TestClient to test FastAPI applications
     - TestClient is a wrapper around the requests library that allows you to make HTTP requests to your FastAPI application
     - you can use TestClient to test your API endpoints, validate responses, and ensure that your application behaves as expected

"""
"""
async tests
     - FastAPI supports asynchronous programming, and you can write async tests to test your async endpoints
     - use the pytest-asyncio library to write async tests with pytest
     - async tests allow you to test the behavior of your application when handling concurrent requests and ensure that your async code is working correctly
     use the @pytest.mark.asyncio decorator to mark your test functions as async and use the await keyword to call your async endpoints in your tests
"""
"""
Api Testing Strategies
     - Unit Testing: Test individual functions or components of your API in isolation. This helps ensure that each part of your code works correctly on its own.
     - Integration Testing: Test how different parts of your API work together. This can include testing the interaction between your API and a database, or between different endpoints.
     - End-to-End Testing: Test the entire flow of your application from start to finish. This simulates real user interactions and ensures that all components of your application work together as expected.
     - Mocking: Use mocking to simulate external dependencies, such as databases or third-party services, to test how your API handles different scenarios without relying on actual external resources.
     - Parameterized Testing: Use parameterized tests to run the same test with different input values, which can help you cover a wider range of scenarios and edge cases.
     - performance Testing: Test the performance of your API under load to ensure it can handle a high number of requests and maintain acceptable response times.

Strategies for testng:
     - Use pytest and testclient
     - Dependency overrides
     - Mocking and patching
     - Isolated Test environments
     - Asynchronous testing
     - fixture management
     - test edge cases and error handling
     - code covergae
     - Continuous Integration (CI) integration
"""

"""

"""
