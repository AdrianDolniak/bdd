@ssh
Feature: Testing remote hosts with Ssh library

  Scenario: Connection with remote host
     Given the ssh connection is set
      When we check the connection with remote host
      Then the response should contain a phrase "adi-vmware"


  Scenario: Remote machine with 4 cores processor
     Given the ssh connection is set
      When we check if the remote machine has 4 cores processor
      Then the response should be "4"


  Scenario: Connection to Internet on remote host
     Given the ssh connection is set
      When we check if the remote machine has internet connection
      Then the response should contain phrase "1 received"
