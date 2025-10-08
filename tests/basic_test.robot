*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL}    https://astroscale.com/
${GOOGLE}    https://google.com

*** Test Cases ***
Open Browser and Check Title
    [Tags]    REQ001
    Open Browser    ${URL}    chrome
    Title Should Be    Astroscale, Securing Space Sustainability
    Close Browser

Open and Close Google
    [Tags]    REQ001
    Open Browser    ${GOOGLE}    chrome
    Close Browser

Equality Should Pass
    [Tags]    REQ002
    ${a}=    Set Variable    2
    ${b}=    Set Variable    2
    Should Be Equal    ${a}    ${b}

Equality Should Fail
    [Tags]    REQ003
    ${a}=    Set Variable    2
    ${b}=    Set Variable    3
    Should Be Equal    ${a}    ${b}

String Match Pass
    [Tags]    REQ004
    ${x}=    Set Variable    hello
    ${y}=    Set Variable    hello
    Should Be Equal    ${x}    ${y}

String Match Fail
    [Tags]    REQ005
    ${x}=    Set Variable    hello
    ${y}=    Set Variable    world
    Should Be Equal    ${x}    ${y}

String Match Cases
    [Tags]    REQ005
    ${x}=    Set Variable    hello
    ${y}=    Set Variable    HeLlo
    Should Be Equal    ${x}    ${y}

Greater Than Pass
    [Tags]    REQ006
    ${a}=    Set Variable    10
    ${b}=    Set Variable    5
    Should Be True    condition=${a} > ${b}

Greater Than Fail
    [Tags]    REQ007
    ${a}=    Set Variable    5
    ${b}=    Set Variable    10
    Should Be True    condition=${a} > ${b}

Skipped Test
    [Tags]    REQ008
    Skip    This test is intentionally skipped

File Should Exist Pass
    [Tags]    REQ009
    ${Count}=    OperatingSystem.Count Items In Directory    path=${CURDIR}
    Log To Console    ${Count}

File Should Exist Fail
    [Tags]    REQ010
    File Should Exist    non_existent_file.txt

