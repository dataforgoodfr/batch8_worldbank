
# Table of Contents

1.  [<code>[1/2]</code> Prototyping](#orgf0d851e)
    1.  [Features](#org86d9665)
    2.  [<code>[1/3]</code> Wireframe](#orgeab84e3)
        1.  [World map](#org900c054)
        2.  [Sub region pop-up](#org700951a)
        3.  [World figures](#org3faf70d)
2.  [<code>[1/2]</code> Dataset](#org122fb86)
    1.  [Variables](#org2552cb4)
    2.  [<code>[1/11]</code> Data sources](#orgce351f6)
        1.  [`Decade`](#orgfaaefa9)
        2.  [`UN_Geosheme_Subregion`](#org4cbe894)
        3.  [`Disaster_Type`](#orgb7c54ea)
        4.  [`RCP`](#org6b3cc35)
        5.  [`#LoDO`](#org9fd10af)
        6.  [`#MeDO`](#org0c5cefa)
        7.  [`#HiDO`](#org0e393f5)
        8.  [`Human_Impact`](#org37fcecf)
        9.  [`Financial_Impact`](#org264622e)
        10. [`°C`](#org709672e)
        11. [`Geo`](#orgd1aeb56)
3.  [<code>[0/3]</code> Development](#org415fe88)
    1.  [Why did we pick Dash?](#orgbc57d33)
    2.  [Visual identity](#orgd6d4d82)
    3.  [Architecture](#org499275b)
        1.  [`app.py`](#org2ee9eaa)
        2.  [`assets/style.css`](#org04be787)
        3.  [`assets/WB_logo.jpg`](#org4706fbe)
4.  [<code>[0/3]</code> Project Management](#org3e8b393)
    1.  [Methodology](#orgfa3e4b1)
    2.  [tools](#org32e3d42)
    3.  [How to contribute](#orgfad9cca)

Todo : upload a screenshot of the delivered dashboard


<a id="orgf0d851e"></a>

# BACKLOG <code>[1/2]</code> Prototyping


<a id="org86d9665"></a>

## DONE Features

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Feature name</th>
<th scope="col" class="org-left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Main layout</td>
<td class="org-left">Organise features and widgets on the main page</td>
</tr>


<tr>
<td class="org-left">World map</td>
<td class="org-left">Displays the world map, with UN sub regions</td>
</tr>


<tr>
<td class="org-left">World map dataviz</td>
<td class="org-left">Displays data on the worldmap, with a legend</td>
</tr>


<tr>
<td class="org-left">RCP thermometer</td>
<td class="org-left">To choose among the 4 RCP</td>
</tr>


<tr>
<td class="org-left">Disaster toggle</td>
<td class="org-left">To choose among 1 over 3 disaster type</td>
</tr>


<tr>
<td class="org-left">Impact toggle</td>
<td class="org-left">To choose between human or financial impact</td>
</tr>


<tr>
<td class="org-left">Selectable timeframe</td>
<td class="org-left">To choose from 1 to 20 decades</td>
</tr>


<tr>
<td class="org-left">Sub region mouseover</td>
<td class="org-left">Mouseover on a sub region triggers a popup</td>
</tr>


<tr>
<td class="org-left">Sub region popup</td>
<td class="org-left">Shows region's figures</td>
</tr>


<tr>
<td class="org-left">World figures</td>
<td class="org-left">Shows world figures</td>
</tr>


<tr>
<td class="org-left">World figures expand</td>
<td class="org-left">Button that triggers world figures popup</td>
</tr>


<tr>
<td class="org-left">World figures popup</td>
<td class="org-left">Expends world figures additional figures</td>
</tr>


<tr>
<td class="org-left">Play/Pause toggle</td>
<td class="org-left">launch a per decade animation on the world map</td>
</tr>
</tbody>
</table>


<a id="orgeab84e3"></a>

## BACKLOG <code>[1/3]</code> Wireframe


<a id="org900c054"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="org700951a"></a>

### BACKLOG Sub region pop-up


<a id="org3faf70d"></a>

### BACKLOG World figures


<a id="org122fb86"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="org2552cb4"></a>

## DONE Variables

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Variable name</th>
<th scope="col" class="org-left">Data type</th>
<th scope="col" class="org-left">Description/Example</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">`Decade`</td>
<td class="org-left">int64</td>
<td class="org-left">1900, 1910, &#x2026;, 2080, 2090</td>
</tr>


<tr>
<td class="org-left">`UN_Geosheme_Subregion`</td>
<td class="org-left">str</td>
<td class="org-left">'Australia and New Zealand', 'Caribbean', etc.</td>
</tr>


<tr>
<td class="org-left">`Disaster_Type`</td>
<td class="org-left">str</td>
<td class="org-left">Either 'Floods', 'Droughts' or 'Storms'</td>
</tr>


<tr>
<td class="org-left">`RCP`</td>
<td class="org-left">float64</td>
<td class="org-left">NaN for the past, either 2.6, 4.5, 6.0 or 8.5 for the future</td>
</tr>


<tr>
<td class="org-left">`#LoDO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of low impact disasters<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`#MeDO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of medium impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`#HiDO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of high impact disasters<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`Human_Impact`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of impacted people<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`Financial_mpact`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the financial impact<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`°C`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the temperature in Celsius degrees<sup><a id="fnr.2" class="footref" href="#fn.2">2</a></sup></td>
</tr>


<tr>
<td class="org-left">`Geo`</td>
<td class="org-left">GeoPandas</td>
<td class="org-left">Geospatial data delimitating geoscheme sub regions on the map</td>
</tr>
</tbody>
</table>


<a id="orgce351f6"></a>

## STARTED <code>[1/11]</code> Data sources


<a id="orgfaaefa9"></a>

### DONE `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org4cbe894"></a>

### STARTED `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="orgb7c54ea"></a>

### STARTED `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org6b3cc35"></a>

### STARTED `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="org9fd10af"></a>

### BACKLOG `#LoDO`

Todo : link to github respective workstream pages


<a id="org0c5cefa"></a>

### BACKLOG `#MeDO`

Todo : link to github respective workstream pages


<a id="org0e393f5"></a>

### BACKLOG `#HiDO`

Todo : link to github respective workstream pages


<a id="org37fcecf"></a>

### BACKLOG `Human_Impact`

Todo : link to github respective workstream pages


<a id="org264622e"></a>

### BACKLOG `Financial_Impact`

Todo : link to github respective workstream pages


<a id="org709672e"></a>

### BACKLOG `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="orgd1aeb56"></a>

### BACKLOG `Geo`

Todo : explain


<a id="org415fe88"></a>

# STARTED <code>[0/3]</code> Development


<a id="orgbc57d33"></a>

## STARTED Why did we pick [Dash](https://plotly.com/dash/)?

[List of Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck team decided to develop the PoC with ****Dash****

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Maturity</th>
<th scope="col" class="org-left">Popularity</th>
<th scope="col" class="org-left">Simplicity</th>
<th scope="col" class="org-left">Adaptability</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Streamlit</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>


<tr>
<td class="org-left">Dash</td>
<td class="org-left">B</td>
<td class="org-left">A</td>
<td class="org-left">B</td>
<td class="org-left">B</td>
</tr>


<tr>
<td class="org-left">Voila</td>
<td class="org-left">C</td>
<td class="org-left">C</td>
<td class="org-left">A</td>
<td class="org-left">C</td>
</tr>
</tbody>
</table>

****Maturity****: Based on the age of the project and how stable it is.

****Popularity****: Based on adoption and GitHub stars.

****Simplicity****: Based on how easy it is to get started using the library.

****Adaptability****: Based on how flexible and opinionated the library is.


<a id="orgd6d4d82"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="org499275b"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org2ee9eaa"></a>

### `app.py`


<a id="org04be787"></a>

### `assets/style.css`


<a id="org4706fbe"></a>

### `assets/WB_logo.jpg`


<a id="org3e8b393"></a>

# STARTED <code>[0/3]</code> Project Management


<a id="orgfa3e4b1"></a>

## BACKLOG Methodology


<a id="org32e3d42"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="orgfad9cca"></a>

## STARTED How to contribute

-   Clone our project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub
-   When adding a new file do
    
        $ git add newfilename
        $ git commit
        $ git push
-   When modifying an existing file, you have to submit modifications to its reviewer (i.e. owner). Ownership is distributed as follow :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">owner</th>
<th scope="col" class="org-left">file</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">mahdiqb</td>
<td class="org-left">`./app.py`</td>
</tr>


<tr>
<td class="org-left">morgandavidson</td>
<td class="org-left">`./README.md`</td>
</tr>


<tr>
<td class="org-left">alencon</td>
<td class="org-left">`./asset/style.css`</td>
</tr>
</tbody>
</table>

-   reviewees have to do
    
        $ hub pull-request -h revieweename:master -b dataforgoodfr:master -m "pull request attempt" -r reviewername -f
    
    Where revieweename and reviewername are the names of the reviewee and the reviewer on GitHub
-   Reviewers have to do 
    
        ???


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
