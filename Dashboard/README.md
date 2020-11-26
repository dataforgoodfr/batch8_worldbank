
# Table of Contents

1.  [<code>[2/2]</code> Dataset](#orgcd1b1c7)
    1.  [Variables](#orgc7b7407)
    2.  [<code>[11/11]</code> Data sources](#orgb06bf4b)
        1.  [`Decade`](#org6b5da49)
        2.  [`UN_Geosheme_Subregion`](#org20a195c)
        3.  [`Disaster_Type`](#org5af653e)
        4.  [`RCP`](#org0a73012)
        5.  [`DO`](#orgb8b2eca)
        6.  [`Human_Impact`](#orgaa3d641)
        7.  [`Financial_Impact`](#orgce0564b)
        8.  [`°C`](#orgc10c7d6)
        9.  [`Geo`](#orgee8af80)
2.  [<code>[1/2]</code> Prototyping](#org85bd0e3)
    1.  [Features](#org6efea2a)
    2.  [<code>[1/3]</code> Wireframe](#orgdfaed27)
        1.  [World map](#org7fa7bf6)
        2.  [Sub region pop-up](#org7a9f9ce)
        3.  [World figures](#org9fea22c)
3.  [<code>[3/4]</code> Development](#org40c3541)
    1.  [Why did we pick Dash?](#org4018451)
    2.  [Architecture](#org18e1a3d)
        1.  [`app.py`](#org1af5fd3)
        2.  [`assets/style.css`](#org17635be)
        3.  [`assets/WB_logo.jpg`](#orgd92fe20)
    3.  [Visual identity guidelines](#orgbe315c9)
        1.  [Colors](#org096083f)
            -   [Primary colors](#org48534a8)
            -   [Secondary colors](#orgde17f20)
        2.  [Fonts](#orgeb4a771)
            -   [Primary fonts](#org9f0918a)
            -   [Secondary fonts](#org3441f82)
        3.  [Logo](#orgd9cdaa4)
            -   [Symbol](#org95701d8)
            -   [Logotype](#org1681633)
    4.  [How to contribute](#orgb275652)
        1.  [Setting up a new Git repository](#org532abfc)
        2.  [Adding or modifying owned files (`push`)](#org3a4eb5c)
        3.  [Submit proposed changes to review](#org3411d49)
        4.  [Adding reviewed files (`merge`)](#org0cca4df)
4.  [Tools that we used](#org17f34b5)

Todo : upload a screenshot of the delivered dashboard


<a id="orgcd1b1c7"></a>

# DONE <code>[2/2]</code> Dataset


<a id="orgc7b7407"></a>

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
<td class="org-left">`DO`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of disasters<sup><a id="fnr.1" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`Human_Impact`</td>
<td class="org-left">int64</td>
<td class="org-left">Provides the number of impacted people<sup><a id="fnr.1.100" class="footref" href="#fn.1">1</a></sup>.</td>
</tr>


<tr>
<td class="org-left">`Financial_Impact`</td>
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


<a id="orgb06bf4b"></a>

## DONE <code>[11/11]</code> Data sources


<a id="org6b5da49"></a>

### DONE `Decade`

-   Source: in-house
-   Values: 
    
        Decade = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090]
-   Notes: each value represents a decade. For example, `2020` starts with the year 2020 and ends with the year 2029.


<a id="org20a195c"></a>

### DONE `UN_Geosheme_Subregion`

-   Source: [UN Geographic Intermediary Regions](https://unstats.un.org/unsd/methodology/m49/) used by the UN Statistics Division in its publications and databases.
-   Values:
    
        UN_Geosheme_Subregion = ['Australia and New Zealand','Caribbean','Central America','Central Asia','Eastern Africa','Eastern Asia','Eastern Europe','Melanesia','Micronesia','Middle Africa','Northern Africa','Northern America','Northern Europe','Polynesia','South America','South-Eastern Asia','Southern Africa','Southern Asia','Southern Europe','Western Africa','Western Asia','Western Europe']
-   Notes: This classification is also referred as [United Nations geoscheme](https://en.wikipedia.org/wiki/United_Nations_geoscheme) and [UN M49](https://en.wikipedia.org/wiki/UN_M49).


<a id="org5af653e"></a>

### DONE `Disaster_Type`

-   Source: in-house
-   Values:

    Disaster_Type = ['Droughts', 'Floods', 'Storms']

-   Notes: These disasters will be respectively described in the following pages : [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes)


<a id="org0a73012"></a>

### DONE `RCP`

-   Source: [IPCC](https://www.iiasa.ac.at/web-apps/tnt/RcpDb/dsd?Action=htmlpage&page=welcome)
-   Values:

    RCP = [2.6, 4.5, 6.0, 8.5]

-   Notes: Representative Concentration Pathways (RCP) are greenhouse gas concentration (not emissions) trajectories adopted by the IPCC. Four pathways were used for climate modeling and research for the IPCC fifth Assessment Report (AR5) in 2014. The pathways describe different climate futures, all of which are considered possible depending on the volume of greenhouse gases (GHG) emitted in the years to come. The RCPs are labelled after a possible range of radiative forcing values in the year 2100.
    
    <img src="./Pics/rcp.png" width="300px">


<a id="orgb8b2eca"></a>

### DONE `DO`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) **Disaster Occurrences** (DO) see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="orgaa3d641"></a>

### DONE `Human_Impact`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) Human Impact see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="orgce0564b"></a>

### DONE `Financial_Impact`

-   Source: In-house (for prediction)
-   Values: Natural number (non-negative integers)
-   Notes: For explanation on past and future (based on in house statistical models) Financial Impact see: [droughts](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_secheresse), [floods](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_innondations), and [storms](https://github.com/dataforgoodfr/batch8_worldbank/tree/master/model_tempetes) pages.


<a id="orgc10c7d6"></a>

### DONE `°C`

-   Source: [World Bank](https://climateknowledgeportal.worldbank.org/download-data)
-   Values: Temperatures


<a id="orgee8af80"></a>

### DONE `Geo`

-   Source: In-house (generated by [this script](https://github.com/dataforgoodfr/batch8_worldbank/blob/master/Dashboard/scripts/ContourGeneration.ipynb))


<a id="org85bd0e3"></a>

# BACKLOG <code>[1/2]</code> Prototyping


<a id="org6efea2a"></a>

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


<a id="orgdfaed27"></a>

## BACKLOG <code>[1/3]</code> Wireframe


<a id="org7fa7bf6"></a>

### DONE World map

![img](./Pics/worldmapwireframe.png "World map wireframe")


<a id="org7a9f9ce"></a>

### BACKLOG Sub region pop-up


<a id="org9fea22c"></a>

### BACKLOG World figures


<a id="org40c3541"></a>

# STARTED <code>[3/4]</code> Development


<a id="org4018451"></a>

## DONE Why did we pick [Dash](https://plotly.com/dash/)?

As we wanted to use Python to build the Dashboard we had to pick among [Python dashboard libraries](https://pyviz.org/tools.html) :

![img](./Pics/dashboardlibraries.png "Python dashboarding libraries")

According to following benchmarck the team decided to develop the PoC with ****Dash****

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


<a id="org18e1a3d"></a>

## BACKLOG Architecture

Todo : describe files


<a id="org1af5fd3"></a>

### `app.py`


<a id="org17635be"></a>

### `assets/style.css`


<a id="orgd92fe20"></a>

### `assets/WB_logo.jpg`


<a id="orgbe315c9"></a>

## DONE Visual identity guidelines

We will follow World Bank's visual identity guidelines for colors and fonts.


<a id="org096083f"></a>

### Colors


<a id="org48534a8"></a>

#### Primary colors

<img src="./Pics/primarycolors.png" width="700px">

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Name</th>
<th scope="col" class="org-left">Hex code</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Sapphire blue</td>
<td class="org-left">#002244</td>
</tr>


<tr>
<td class="org-left">Sky blue</td>
<td class="org-left">#009FDA</td>
</tr>


<tr>
<td class="org-left">Black</td>
<td class="org-left">#000000</td>
</tr>


<tr>
<td class="org-left">White</td>
<td class="org-left">#FFFFFF</td>
</tr>
</tbody>
</table>


<a id="orgde17f20"></a>

#### Secondary colors

<img src="./Pics/secondarycolors.png" width="700px">

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Family</th>
<th scope="col" class="org-left">Hex code</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">F05023</td>
</tr>


<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">FDB714</td>
</tr>


<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">2EB1C2D</td>
</tr>


<tr>
<td class="org-left">Brighter Warm</td>
<td class="org-left">F78D28</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">009CA7</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">00AB51</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">872B90</td>
</tr>


<tr>
<td class="org-left">Brighter Cool</td>
<td class="org-left">00A996</td>
</tr>


<tr>
<td class="org-left">Muted Warm</td>
<td class="org-left">98252B</td>
</tr>


<tr>
<td class="org-left">Muted Warm</td>
<td class="org-left">E16A2D</td>
</tr>


<tr>
<td class="org-left">Muted Warm</td>
<td class="org-left">B88C1D</td>
</tr>


<tr>
<td class="org-left">Muted Cool</td>
<td class="org-left">614776</td>
</tr>


<tr>
<td class="org-left">Muted Cool</td>
<td class="org-left">006068</td>
</tr>


<tr>
<td class="org-left">Muted Cool</td>
<td class="org-left">006450</td>
</tr>
</tbody>
</table>


<a id="orgeb4a771"></a>

### Fonts


<a id="org9f0918a"></a>

#### Primary fonts

<img src="./Pics/primaryfonts.png" width="400px">


<a id="org3441f82"></a>

#### Secondary fonts

<img src="./Pics/secondaryfonts.png" width="400px">


<a id="orgd9cdaa4"></a>

### Logo


<a id="org95701d8"></a>

#### Symbol

<img src="./Pics/symbol.png" width="300px">


<a id="org1681633"></a>

#### Logotype

<img src="./Pics/logotype.png" width="300px">


<a id="orgb275652"></a>

## DONE How to contribute


<a id="org532abfc"></a>

### Setting up a new Git repository

-   Clone project locally
    
        $ git init
        $ git clone https://github.com/dataforgoodfr/batch8_worldbank/tree/master/plateforme
-   Ask to join our GitHub


<a id="org3a4eb5c"></a>

### Adding or modifying owned files (`push`)

When adding a new file or modifying a file that you own, do:

    $ git add filename
    $ git commit
    $ git push

Where `filename` is the name of the file


<a id="org3411d49"></a>

### Submit proposed changes to review

When modifying an existing file, if you're not its owner, you have to submit the modifications to its owner (i.e. reviewer). Ownership is distributed as follow :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Owner GitHub name</th>
<th scope="col" class="org-left">File</th>
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

To submit changes reviewees have to do: 

    $ git add filename
    $ git commit
    $ hub pull-request -h revieweename:master -b dataforgoodfr:master -m -r reviewername -f

Where `revieweename` and `reviewername` are the GitHub names of the reviewee and the reviewer/owner.


<a id="org0cca4df"></a>

### Adding reviewed files (`merge`)

-Reviewers have to do 

    $ hub merge PRurl 

Where `PRurl` is the url of the pull request.


<a id="org17f34b5"></a>

# DONE Tools that we used

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Function</th>
<th scope="col" class="org-left">Tools</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Wireframing</td>
<td class="org-left">Krita, Figma</td>
</tr>


<tr>
<td class="org-left">Documentation</td>
<td class="org-left">Org-mode, Github, Notion</td>
</tr>


<tr>
<td class="org-left">Code storage/versioning</td>
<td class="org-left">Git, GitHub</td>
</tr>


<tr>
<td class="org-left">Chat</td>
<td class="org-left">Slack</td>
</tr>


<tr>
<td class="org-left">Meetings</td>
<td class="org-left">Zoom</td>
</tr>


<tr>
<td class="org-left">Code editing</td>
<td class="org-left">Pycharm, Jupyter</td>
</tr>


<tr>
<td class="org-left">Coding languages</td>
<td class="org-left">Python, CSS</td>
</tr>


<tr>
<td class="org-left">Python librairies</td>
<td class="org-left">dash, dash-daq pandas, gunicorn</td>
</tr>
</tbody>
</table>


# Footnotes

<sup><a id="fn.1" href="#fnr.1">1</a></sup> Given a disaster, a decade, a region, and a climate scenario

<sup><a id="fn.2" href="#fnr.2">2</a></sup> Given a decade, a region, and a climate scenario.
