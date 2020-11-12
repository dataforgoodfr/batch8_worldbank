- [Prototype/Wireframe](#orge1f2c48)
  - [Features](#org3fd6c42)
    - [Worldmap](#org9fe2680)
    - [Pop-up](#orge64bfc5)
    - [World figure](#org6bde853)
- [Dataset](#orgd57c898)
  - [Variables](#org2b48010)
  - [Data sources](#org48fd0c5)
    - [Decade](#orgc6de6e4)
    - [UN<sub>Geosheme</sub><sub>Subregion</sub>](#orge106ea9)
    - [Disaster<sub>Type</sub>](#orgd9c4c91)
    - [RCP](#org614b4b2)
    - [#LoDO](#org7acc7f0)
    - [#MeDO](#org8cbfe82)
    - [#HiDO](#orgfaab396)
    - [Human<sub>Impact</sub>](#org9e91394)
    - [Financial<sub>mpact</sub>](#orgcb1e511)
    - [°C](#org5c2cdf7)
    - [Geo](#org544918f)
- [The Dashboard](#org0b5863e)
  - [Why did we pick [Dash](https://plotly.com/dash/)?](#orgbf49077)
  - [Design](#org27ee618)
  - [Required files to run it](#org808365b)
    - [app.py](#org6ecd7dc)
    - [assets/style.css](#org2ffdbf5)
    - [assets/WB<sub>logo.jpg</sub>](#orgb7403af)
- [Project Management](#org3f51fa4)
  - [Methodology](#orgcfdd220)
  - [tools](#org9e56f75)
  - [How to contribute](#org695fb22)

Todo : upload a screenshot of the delivered dashboard


<a id="orge1f2c48"></a>

# Prototype/Wireframe


<a id="org3fd6c42"></a>

## Features


<a id="org9fe2680"></a>

### Worldmap


<a id="orge64bfc5"></a>

### Pop-up


<a id="org6bde853"></a>

### World figure


<a id="orgd57c898"></a>

# Dataset


<a id="org2b48010"></a>

## DONE Variables

| Variable name                             | Data type | Description/Example                                                                                                 |
| Decade                                    | int64     | 1900, 1910, &#x2026;, 2080, 2090                                                                                    |
| UN<sub>Geosheme</sub><sub>Subregion</sub> | str       | 'Australia and New Zealand', 'Caribbean', etc., see [M49 sub regions](https://unstats.un.org/unsd/methodology/m49/) |
| Disaster<sub>Type</sub>                   | str       | Either 'Floods', 'Droughts' or 'Storms'                                                                             |
| RCP                                       | float64   | NaN for the past, either 2.6, 4.5, 6.0 or 8.5 for the future                                                        |
| #LoDO                                     | int64     | Provides the number of low impact disasters<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.             |
| #MeDO                                     | int64     | Provides the number of medium impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.      |
| #HiDO                                     | int64     | Provides the number of high impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.        |
| Human<sub>Impact</sub>                    | int64     | Provides the number of impacted people<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.              |
| Financial<sub>mpact</sub>                 | int64     | Provides the financial impact<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.                       |
| °C                                        | int64     | Provides the temperature in Celsius degrees<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup>              |
| Geo                                       | GeoPandas | Geospatial data delimitating geoscheme sub regions on the map                                                       |


<a id="org48fd0c5"></a>

## BACKLOG Data sources


<a id="orgc6de6e4"></a>

### Decade

Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090] For example `2020` starts in 2020 and ends in 2029


<a id="orge106ea9"></a>

### UN<sub>Geosheme</sub><sub>Subregion</sub>

UN<sub>Geosheme</sub><sub>Subregion</sub>=['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe'] Todo : take from

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide link


<a id="orgd9c4c91"></a>

### Disaster<sub>Type</sub>

Disaster<sub>Type</sub> = ['Droughts', 'Floods', 'Storms'] Todo : link to github respective workstream pages


<a id="org614b4b2"></a>

### RCP

RCP = [2.6,4.5,6.0,8.5] TODO : take from <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link


<a id="org7acc7f0"></a>

### #LoDO

Todo : link to github respective workstream pages


<a id="org8cbfe82"></a>

### #MeDO

Todo : link to github respective workstream pages


<a id="orgfaab396"></a>

### #HiDO

Todo : link to github respective workstream pages


<a id="org9e91394"></a>

### Human<sub>Impact</sub>

Todo : link to github respective workstream pages


<a id="orgcb1e511"></a>

### Financial<sub>mpact</sub>

Todo : link to github respective workstream pages


<a id="org5c2cdf7"></a>

### °C

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="org544918f"></a>

### Geo

Todo : explain


<a id="org0b5863e"></a>

# The Dashboard


<a id="orgbf49077"></a>

## Why did we pick [Dash](https://plotly.com/dash/)?

[List of Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck team decided to develop the PoC with ****Dash****

|           | Maturity | Popularity | Simplicity | Adaptability |
| Streamlit | C        | A          | A          | C            |
| Dash      | B        | A          | B          | B            |
| Voila     | C        | C          | A          | C            |

****Maturity****: Based on the age of the project and how stable it is.

****Popularity****: Based on adoption and GitHub stars.

****Simplicity****: Based on how easy it is to get started using the library.

****Adaptability****: Based on how flexible and opinionated the library is.


<a id="org27ee618"></a>

## Design

Todo mention World Bank Visual Identity Guidelines


<a id="org808365b"></a>

## Required files to run it

Todo : describe files


<a id="org6ecd7dc"></a>

### app.py


<a id="org2ffdbf5"></a>

### assets/style.css


<a id="orgb7403af"></a>

### assets/WB<sub>logo.jpg</sub>


<a id="org3f51fa4"></a>

# Project Management


<a id="orgcfdd220"></a>

## Methodology


<a id="org9e56f75"></a>

## tools

-   Notion
-   Slack
-   Zoom


<a id="org695fb22"></a>

## How to contribute

-   Get our project locally
    
    ```sh
    $ git init
    $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme   
    ```
-   Ask to join our GitHub
-   When adding a new file do
    
    ```sh
    $ git add newfilename
    $ git commit
    $ git push origin master
    ```

-   When modifying an existing file do
    
    ```sh
    ???
    ```

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.