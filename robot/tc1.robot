*** Settings ***
Library    SeleniumLibrary    timeout=30

*** Variables ***
${SEARCH_ENGINE}    https://www.google.com
${BROWSER}          firefox
${SEARCH_TERM}      nokia wikipedia
${GOOGLE_INPUT}    APjFqb
${COOKIES_BUTTON}    W0wltc
${WIKIPEDIA_LINK}    wikipedia.org
${FOUNDING_YEAR}    1865

*** Test Cases ***
Get Nokia founding year from Wikipedia
    # open the browser
    Open Browser    ${SEARCH_ENGINE}    ${BROWSER} 
    Press Keys    name=q    RETURN
    Click Element    id=${COOKIES_BUTTON}
    # search for nokia wikipedia in google.com
    Input Text    id=${GOOGLE_INPUT}    ${SEARCH_TERM}
    Press Keys    name=q    RETURN
    Wait Until Element Is Visible    xpath=//a[contains(@href, 'wikipedia.org')]    timeout=10s
    # check if page contains wikipedia link
    Page Should Contain Element    xpath=//a[contains(@href, 'wikipedia.org')]
    ${link_found}=    Run Keyword And Return Status    Page Should Contain Element    xpath=//a[contains(@href, 'wikipedia.org')]

    Run Keyword If    '${link_found}' == 'True'    Click Element    xpath=//a[contains(@href, 'wikipedia.org')]
    Run Keyword If    '${link_found}' == 'False'    Fail    Wikipedia link not found on the search results page.
    # get founding year
    ${founding_date}=    Get Text    xpath=//table[contains(@class, 'infobox')]//tr[th[contains(text(), 'Data założenia')] or th[contains(text(), 'Founded')]]/td
    ${founding_year}=    Convert To Integer    ${founding_date}[-4:]
    Log To Console   Data założenia firmy: ${founding_date}
    Log To Console   Rok założenia firmy: ${founding_year}
    Should Be Equal As Numbers    ${founding_year}    ${FOUNDING_YEAR}
    Run Keyword If    '${founding_year}' != '${FOUNDING_YEAR}'    Fail    Founding year does not match expected year. Expected: ${FOUNDING_YEAR}, Found: ${founding_year}
    
    [Teardown]    Close Browser