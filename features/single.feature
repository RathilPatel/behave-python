Feature: BrowserStack's Login Functionality    
    Scenario: can find search results
        When visit url "http://browserstack.com"
        When button clicked with path "//*[@id="primary-menu"]/li[6]/a"
        When field with id "user_email_login" is given "rathilvasani@gmail.com"
        When field with id "user_password" is given "lihtar787898"
        When button clicked with id "user_submit"
        When button clicked with id "skip-local-installation"
        When button clicked with path "//*[@id="rf-os-list-wrapper"]/nav/ul/ul[1]/ul/li[1]"
        When button clicked with path "//*[@id="rf-browsers"]/div/div[2]/div[4]/ul/li[4]/a"
        When mouse move to
        When wait 
        Then title becomes "Dashboard"
