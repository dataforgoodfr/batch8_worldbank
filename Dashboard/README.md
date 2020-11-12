First a screenshot of the dashboard

Prototype/Wireframe
===================

Features
--------

### Worldmap

### Pop-up

### World figure

Dataset
=======

[DONE]{.done .DONE} Variables {#variables}
-----------------------------

  Variable name           Data type   Description/Example
  ----------------------- ----------- -------------------------------------------------------------------------------------------------------------------------
  Decade                  int64       1900, 1910, ..., 2080, 2090
  UN~GeoshemeSubregion~   str         \'Australia and New Zealand\', \'Caribbean\', etc., see [M49 sub regions](https://unstats.un.org/unsd/methodology/m49/)
  Disaster~Type~          str         Either \'Floods\', \'Droughts\' or \'Storms\'
  RCP                     float64     NaN for the past, either 2.6, 4.5, 6.0 or 8.5 for the future
  \#LoDO                  int64       Provides the number of low impact disasters[^1].
  \#MeDO                  int64       Provides the number of medium impact disasters[^2].
  \#HiDO                  int64       Provides the number of high impact disasters[^3].
  Human~Impact~           int64       Provides the number of impacted people[^4].
  Financial~mpact~        int64       Provides the financial impact[^5].
  °C                      int64       Provides the temperature in Celsius degrees[^6]
  Geo                     GeoPandas   Geospatial data delimitating geoscheme sub regions on the map

BACKLOG Data sources
--------------------

### Decade

Decade = \[1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990,
2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090\] For example `2020`
starts in 2020 and ends in 2029

### UN~GeoshemeSubregion~

UN~GeoshemeSubregion~=\[\'Australia and New
Zealand\',\'Caribbean\',\'Central America\',\'Central Asia\',\'Eastern
Africa\',\'Eastern Asia\',\'Eastern
Europe\',\'Melanesia\',\'Micronesia\',\'Middle Africa\',\'Northern
Africa\',\'Northern America\',\'Northern Europe\',\'Polynesia\',\'South
America\',\'South-Eastern Asia\',\'Southern Africa\',\'Southern
Asia\',\'Southern Europe\',\'Western Africa\',\'Western Asia\',\'Western
Europe\'\] Todo : take from

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide link

### Disaster~Type~

Disaster~Type~ = \[\'Droughts\', \'Floods\', \'Storms\'\] Todo : link to
github respective workstream pages

### RCP

RCP = \[2.6,4.5,6.0,8.5\] TODO : take from
<https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and
provide link

### \#LoDO

Todo : link to github respective workstream pages

### \#MeDO

Todo : link to github respective workstream pages

### \#HiDO

Todo : link to github respective workstream pages

### Human~Impact~

Todo : link to github respective workstream pages

### Financial~mpact~

Todo : link to github respective workstream pages

### °C

Todo : provide link and explain :
<https://climateknowledgeportal.worldbank.org/download-data>

### Geo

Todo : explain

The Dashboard
=============

Why did we pick [Dash](https://plotly.com/dash/)?
-------------------------------------------------

[List of Python dashboard libraries](https://pyviz.org/tools.html) :

![Python dashboarding
libraries](./Pics/dashboardlibraries.png "Fig 1"){width="1200px"}

According to following benchmarck team decided to develop the PoC with
****Dash****

              Maturity   Popularity   Simplicity   Adaptability
  ----------- ---------- ------------ ------------ --------------
  Streamlit   C          A            A            C
  Dash        B          A            B            B
  Voila       C          C            A            C

****Maturity****: Based on the age of the project and how stable it is.

****Popularity****: Based on adoption and GitHub stars.

****Simplicity****: Based on how easy it is to get started using the
library.

****Adaptability****: Based on how flexible and opinionated the library
is.

Design
------

Todo mention World Bank Visual Identity Guidelines

Required files to run it
------------------------

Todo : describe files

### app.py

### assets/style.css

### assets/WB~logo~.jpg

Project Management
==================

Methodology
-----------

tools
-----

-   Notion
-   Slack
-   Zoom

How to contribute
-----------------

-   Get our project locally

    ``` {.bash org-language="sh"}
    $ git init
    $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme   
    ```

-   Ask to join our GitHub
-   When adding a new file do

    ``` {.bash org-language="sh"}
    $ git add newfilename
    $ git commit
    $ git push origin master
    ```

<!-- -->

-   When modifying an existing file do

    ``` {.bash org-language="sh"}
    ???
    ```

Footnotes
=========

[^1]: Given a disaster, a decade, a region, and a climate scenario

[^2]: Given a disaster, a decade, a region, and a climate scenario

[^3]: Given a disaster, a decade, a region, and a climate scenario

[^4]: Given a disaster, a decade, a region, and a climate scenario

[^5]: Given a disaster, a decade, a region, and a climate scenario

[^6]: Given a decade, a region, and a climate scenario.
