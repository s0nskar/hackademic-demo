Feature: Authentication

	Scenario: Accessing "/" url without login
		Given I access the url "/"
		Then I see the text "Hi Anonymous!"

	Scenario: Creating Account with user: "abc" and pwd:"abc"
		Given I access the url "/register/"
		Given I fill username "abc"
		Given I fill pwd "abcd1234"
		Given I fill email "abc@abc.abc"
		Given I fill type "Student"
		Then I press "Submit"
		Then I see the text "Login"

	Scenario: Again creating new account with same username: "abc" and pwd: "abcd1234"
		Given I access the url "/register/"
		Given I fill username "abc"
		Given I fill pwd "abcd1234"
		Given I fill email "abc@abc.abc"
		Given I fill type "Student"
		Then I press "Submit"
		Then I see the text "Register"

	Scenario: Login with false credential
		Given I access the url "/login/"
		Given I fill username "abc"
		Given I fill pwd "123456789"
		Then I press "Login"
		Then I see the text "Login"

	Scenario: Login with non-existing username
		Given I access the url "/login/"
		Given I fill username "abcd"
		Given I fill pwd "123456789"
		Then I press "Login"
		Then I see the text "Login"

	Scenario: Login with correct credential i.e username: "abc" and pwd: "abcd1234"
		Given I access the url "/login/"
		Given I fill username "abc"
		Given I fill pwd "abcd1234"
		Then I press "Login"
		Then I see the text "Welcome abc!"

	Scenario: Accessing "/" with login
		Given I access the url "/"
		Then I don't see the text "Hi Anonymous!"