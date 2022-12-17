Feature: Facebook login functionality

  @logincase
  Scenario Outline: Test login with incorrect login credentials
    When user input wrong email id "<login_id>" and password "<password>"
         """
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
         """
    Then Error message will come
         | name      | department  |
         | Barry     | Beer Cans   |
         | Pudey     | Silly Walks |
         | Two-Lumps | Silly Walks |
    Examples: Credentials
      | login_id         | password |
      | anshul123.io | anshul       |
      | anshul12345.io | rahul      |
