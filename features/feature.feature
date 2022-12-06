# Created by Daniil at 06.12.2022
Feature: Test
  # Enter feature description here

  Scenario: Test counting
    Given  I have 3 numbers: 0, 1, 1
    When I count diskriminant and korni
    Then I expect to get result = [-1.0, 1.0]