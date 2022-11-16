Feature: Facebook login functionality

  @logincase
  Scenario: Test login with incorrect login credentials
      When user input wrong credentials
      Then Error message will come
