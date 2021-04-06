Feature: Assure good enough predictions

    As an AI system,
    I want to provide good predictions of the pricing the users should rent their property.

  Background:
    Given I already have a model trained

  Scenario: Predictions has a global good enough accuracy 
    When I test the model 
    Then I have an accuracy over 60%

  Scenario: Predictions for Luxury properties has a high accuracy
    When I test the model 
    Then I have an accuracy for Luxury properties over 75%

  Scenario: Predictions for the most Economy properties has a good enough accuracy
    When I test the model 
    Then I have an accuracy for Economy properties over 55%

