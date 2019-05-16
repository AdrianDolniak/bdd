Feature: Testing remote hosts with Ssh library

  Scenario: Check if we are connected with remote host
     Given the connection is set with remote host
      When we check if there is a connection
      Then the response contain phrase "adi-vmware"


  Scenario: Check if the host machine has processor with 4 cores
     Given the connection is set with remote host
      When we check if remote machine has 4 cores
      Then the response is "4"


  Scenario: Check if we are connected to Internet on host
     Given the connection is set with remote host
      When we execute command "ping -c1 8.8.8.8"
      Then the response contain phrase "1 received"
