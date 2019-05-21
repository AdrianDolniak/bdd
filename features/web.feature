@web
Feature: Testing e-mail account

  Scenario: Check if there is a word "Odebrane" on the e-mail account home page
     Given the user is on the home page of the portal wp.pl
      When the user login to the e-mail account
      Then the user will see a word "Odebrane on the page"

  Scenario: Check if the wrong password allert is shown
     Given the logging page to the e-mail account is displayed
      When the user enter valid username and wrong password
      Then the warning is shown "Wrong username or password"
