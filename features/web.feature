Feature: Testing E-mail account

  Scenario: Check if there is a word "Odebrane" on e-mail account home page
     Given the user is logged on the e-mail account
      When the user looks for a word "Odebrane" on the page
      Then the user sees a word "Odebrane on the page


  Scenario: Check if wrong password allert is shown
     Given the logging page is displayed
      When the user enter valid username and wrong password
      Then the warning is shown "Wrong username or password"
