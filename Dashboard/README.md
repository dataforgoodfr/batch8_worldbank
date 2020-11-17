
# Table of Contents

1.  [<code>[1/2]</code> Prototyping](#org2020a7d)
    1.  [Features](#org64f3683)
    2.  [<code>[1/3]</code> Wireframe](#orgbbc646a)
        1.  [World map](#org536a0e3)
        2.  [Sub region pop-up](#orgaf31d87)
        3.  [World figures](#org0506c27)
2.  [<code>[1/2]</code> Dataset](#org3d2db46)
    1.  [Variables](#org1e0a479)
    2.  [<code>[1/11]</code> Data sources](#org615a78c)
        1.  [`Decade`](#org106892d)
        2.  [`UN_Geosheme_Subregion`](#org3a95cec)
        3.  [`Disaster_Type`](#orgbc6a982)
        4.  [`RCP`](#org9ad2c8e)
        5.  [`#LoDO`](#orgb5d5cdc)
        6.  [`#MeDO`](#org16bf690)
        7.  [`#HiDO`](#org08dbba5)
        8.  [`Human_Impact`](#org3d4fb29)
        9.  [`Financial_Impact`](#org4b3a6ee)
        10. [`°C`](#org6ad2d8f)
        11. [`Geo`](#orgda52597)
3.  [<code>[0/3]</code> Development](#org46e5558)
    1.  [Why did we pick Dash?](#orgcf30294)
    2.  [Visual identity](#org31ae74e)
    3.  [Architecture](#orgbc60f2f)
        1.  [`app.py`](#org21eb98f)
        2.  [`assets/style.css`](#org11a6926)
        3.  [`assets/WB_logo.jpg`](#org7fbf4b1)
4.  [<code>[0/3]</code> Project Management](#orgf81dc70)
    1.  [Methodology](#org74a6b55)
    2.  [tools](#orgca716f2)
    3.  [How to contribute](#orgf8411a7)

Todo : upload a screenshot of the delivered dashboard


<a id="org2020a7d"></a>

# BACKLOG <code>[1/2]</code> Prototyping


<a id="org64f3683"></a>

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


<a id="orgbbc646a"></a>

## BACKLOG <code>[1/3]</code> Wireframe


<a id="org536a0e3"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="orgaf31d87"></a>

### BACKLOG Sub region pop-up


<a id="org0506c27"></a>

### BACKLOG World figures


<a id="org3d2db46"></a>

# STARTED <code>[1/2]</code> Dataset


<a id="org1e0a479"></a>

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


<a id="org615a78c"></a>

## STARTED <code>[1/11]</code> Data sources


<a id="org106892d"></a>

### DONE `Decade`

    Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010,2020,2030,2040,2050,2060,2070,2080,2090]

For example `2020` starts in 2020 and ends in 2029


<a id="org3a95cec"></a>

### STARTED `UN_Geosheme_Subregion`

    UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']

Todo : sum up

-   <https://en.wikipedia.org/wiki/United_Nations_geoscheme>
-   <https://en.wikipedia.org/wiki/UN_M49>
-   <https://unstats.un.org/unsd/methodology/m49/>

and provide links as sources  


<a id="orgbc6a982"></a>

### STARTED `Disaster_Type`

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

Todo : link to github respective workstream pages


<a id="org9ad2c8e"></a>

### STARTED `RCP`

    RCP = [2.6,4.5,6.0,8.5]

TODO : sum up <https://en.wikipedia.org/wiki/Representative_Concentration_Pathway> and provide link as source


<a id="orgb5d5cdc"></a>

### BACKLOG `#LoDO`

Todo : link to github respective workstream pages


<a id="org16bf690"></a>

### BACKLOG `#MeDO`

Todo : link to github respective workstream pages


<a id="org08dbba5"></a>

### BACKLOG `#HiDO`

Todo : link to github respective workstream pages


<a id="org3d4fb29"></a>

### BACKLOG `Human_Impact`

Todo : link to github respective workstream pages


<a id="org4b3a6ee"></a>

### BACKLOG `Financial_Impact`

Todo : link to github respective workstream pages


<a id="org6ad2d8f"></a>

### BACKLOG `°C`

Todo : provide link and explain : <https://climateknowledgeportal.worldbank.org/download-data>


<a id="orgda52597"></a>

### BACKLOG `Geo`

Todo : explain


<a id="org46e5558"></a>

# STARTED <code>[0/3]</code> Development


<a id="orgcf30294"></a>

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


<a id="org31ae74e"></a>

## BACKLOG Visual identity

Todo mention World Bank Visual Identity Guidelines


<a id="orgbc60f2f"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org21eb98f"></a>

### `app.py`


<a id="org11a6926"></a>

### `assets/style.css`


<a id="org7fbf4b1"></a>

### `assets/WB_logo.jpg`


<a id="orgf81dc70"></a>

# STARTED <code>[0/3]</code> Project Management


<a id="org74a6b55"></a>

## BACKLOG Methodology


<a id="orgca716f2"></a>

## BACKLOG tools

-   Notion
-   Slack
-   Zoom


<a id="orgf8411a7"></a>

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

    - by Github interface to submit a review:
        1. On the pull request, click Files changed.
        2. Above the changed code, click Review changes.
        3. Type a comment summarizing your feedback on the proposed changes.
        4. Select the type of review you'd like to leave: ...
        5. Click Submit review.

-   Reviewers have to do 
    
        add git command


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
