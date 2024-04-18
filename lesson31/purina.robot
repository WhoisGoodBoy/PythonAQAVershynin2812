*** Settings ***
Library    SeleniumLibrary
Library    AppiumLibrary

*** Variables ***
${start_url}    https://petslike.ua/
${browser}    Chrome

*** Test Cases ***
Search
    Open Browser On Main Page
    Type Into Search Field    purina
    Press Enter
    Time To Sleep
    Header Should Be    Пошук товарів

*** Keywords ***
Open Browser On Main Page
    Open Browser    ${start_url}    ${browser}

Type Into Search Field
    [Arguments]    ${input text}
    SeleniumLibrary.Input Text    xpath://input[@type="text"]    ${input text}

Press Enter
    Press Key    xpath://input[@type="text"]    \\13
    
Time To Sleep
    Sleep    3

Header Should Be
    [Arguments]    ${header text}
    SeleniumLibrary.Element Text Should Be    xpath://h1[@class="catalog__title h2"]    ${header text}


