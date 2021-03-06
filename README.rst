Introduction
============

A plone.app.theming theme based on HTML5 Boilerplate and Less Css, designed to
be the starting point for rapid theme development.


Create a new theme with ZopeSkel
================================
To create a new theme with this ZopeSkel template, run:

    ./bin/zopeskel less_theme my.theme

Where my.theme is the name of your package. Answer a few questions, or just hit
enter to get the default values. Move the new package to the src folder and edit
your buildout to include the newly created package. In the buildout section add:

    develop =
        src/my.theme

And in the instance section add:

    eggs =
        my.theme

Don't forget to run the buildout after these changes.


Package content
================

  * browser
  * docs
  * locales
  * profiles
  * tests
  * theme_resources
    * css - holds the generated css that is actually used by plone
    * images - holds all the images used by the theme
    * javascript - holds all the javascripts used by the theme
    * less - holds all the less files that will produce the css
        * theme - theme specific less files
        * desktop - styles that are only applied to desktops
        * mobile - styles that are only applied to mobiles
        * tablet - styles that are only applied to tablets
        * style.less - HTML5Boilerplate css file that includes all the other
          less files in the appropriate places.
        * responsive.less - styles that are for responsive design
    * index.html - main template used by plone.app.theming
    * rules.xml - rules file used by plone.app.theming


HTML 5 Boilerplate
==================

The main template that we are using is based on the index.html file from
HTML 5 Boilerplate.

The same goes for our finally generated css file.


Less Css
========

We are using lesscss.org for producing the final css that is used by Plone.
This means that less is only used in the development process, and the less files
are compiled before they are used by Plone. We are using CodeKit for the
compiling and it needs to be set up so the output of style.less is to our css
folder.

Setting up CodeKit
------------------

Add the less folder from theme_resources to CodeKit. Select less/style.less and
less/response.less and set it's CSS Output Path to point to theme_resources/css.
Usually the output folder is set like this, so you just need to make sure this
is the case.

After each update to the files, CodeKit will recompile style.less and
responsive.less automatically, so just reload your page, if the server is in
debug mode.

Important: If less files are changed in the themeskel itself, compile them, so
in css/style.css and css/responsive.css we always have the newest code.


Structure of less folder
------------------------

The less folder holds all the css needed by Plone, so there is no need for
additional css. We have disabled all the css that we don't need in
profiles/default/cssregistry.xml

The theme is built with responsive design principle in mind, so the less folder
is structured in this fashion.

We have three major devices that we are theming for: mobile, tablet and desktop.
All of them have a separate folder that holds all the styles that are applied
only for the specific device. The styles that are in common to all are located
in the theme folder.

The basic idea is to take the Plone's default css files and "lessify" them.
The result of this can be found in theme/main.less.
For fast development, we need a quick way to change the default colors and
stylings to reflect the design we are implementing, so we have modified the
files so they use variables that are set in one location. This is something that
we have seen before in form of base_properties.props, but this time we are doing
it right with less variables.

All the common styles for desktop, tablet and mobile go into theme folder. This
folder includes the base.less and mixins.less that holds all the variables and
mixins that are used in the other styles. Modify these values to meet your
theme's needs.

The theme specific styling that cannot be set in base.less, should go to
theme/custom.less. If you would like to have multiple files for your theme, just
create a new .less file and include it to init.less. All the less files are
imported to the init.less files in their folders, which then get imported to
style.less and/or responsive.less.

For styles that should be applied to mobile version only, we add them to
mobile/main-moible.less. The same goes for desktop/main-desktop.less and
tablet/main-tablet.less.

The media queries have been moved out from style.less to responsive.less to have
clear separation of the styles. Also this was done because of a bug that was
present in Internet Explorer 9. When the rich text editor is initialized, it
picks up all the css from portal css and puts it in the iframe that contains
the editor. This way the media queries were picked up too, and their presence in
multiple places on one page caused IE9 to flicker between mobile-tablet-desktop
mode. To prevent this, the css that holds the media queries have been moved
outside of portal css and it's included directly in index.html.

Note: Lessification of theme/main.less is not finished yet, so there still
might be some styles that are not converted to variables and included in
base.less.


Javascript
==========

HTML5Boilerplate suggests to have all Javascript plugins in plugins.js and all
user scripts in script.js. We have decided to go against it, and we are using
Plone's default javascript registry. The final result is the same, as Plone does
merge and minimize all the registered javascripts.

Javascript/script.js holds helper functions that are taken from Mobile HTML5
Boilerplate project and also some functions for the mobile version of the theme.
(temporarily removed)
Every additional javascript should go into this file. If you need multiple files
for javascript, just create them in the javascript folder and include them in
Plone's JS registry (profiles/default/jsregistry.xml).

Javascript that is common to all themes is located in the hexagonit.primacontrol
package, and to include it in the theme it needs to be set in the JS registry
of the theme (profiles/default/jsregistry.xml):

    <javascript
        cacheable="True"
        compression="safe"
        conditionalcomment=""
        cookable="True"
        enabled="True"
        expression=""
        inline="False"
        id="++resource++hexagonit.primacontrol.js/form_accordion.js"
    />

Available JS libraries:
  * content_type.js
  * descriptiontooltip.js
  * form_accordion.js
  * jquery.richmenu.js
  * portletoverlay.js


Javascript position within the page
-----------------------------------
The default behavior for 'script' tags are to be moved to the bottom of the
page. Some external widgets however require to have the 'script' tag in
specific location within the page. For this purpose we have created special
diazo rules that will take care of the positioning.
To leave the tag in place, set the data-js-move attribute to 'js-dont-move':

    <script src="foo.js" data-js-move="js-dont-move"></script>

To move the tag to the head, set the data-js-move attribute to
'js-move-to-head':

    <script src="foo.js" data-js-move="js-move-to-head"></script>

To move the tag to the beginning of the body, set the data-js-move attribute
to 'js-move-to-beginning-of-body':

    <script src="foo.js" data-js-move="js-move-to-beginning-of-body"></script>


Plone.app.theming
=================

index.html is the main template that we use, so to have a custom layout, you'll
need to modify this file. The header tag holds the header of the site, the div
with id="visual-portal-wrapper" should hold the body region, and the footer tag
should hold the footer.

Some selectors in Plone rely on having the visual-portal-wrapper id present, so
we have just included an additional wrapper div within the main div.

The mobile version of the theme has a slightly different layout for the menu and
search, so we have included additional elements in our main layout and updated
the rules. The final generated html has the same structure, so there will be no
problems with the selectors used by Plone.

rules.xml is the rules file, and we have set up the copying of the css and
javascripts to proper location within the index.html, and it also includes rules
that copy everything from Plone and put it into proper place. Feel free to
modify this to suite your needs. Boilerplate encourages us to have the styles
and javascript inclusions in specific place, so please don't modify the rules
that make this happen.

Within the less files, there are relative paths to some images, and Diazo will
append a previously set prefix on them, even though we actually don't want that.
One of the solutions would be to split the CSS files into two groups, the one
that need prefix applied, and ones that don't. Html 5 Boilerplate suggests to
have all the styles in one file, so we decided not to modify the structure, but
to include the missing images in our theme. This way we don't rely on other
products and we can easily update the images to suite our needs.


Exceptions
----------

Modernizer.js and Respond.js should be the only JS in the header, so it’s hard
to have a rule that will put it there, so we have put only these two js in the
index.html and it is not served from Plone’s js registry. In case if the site is
loaded without the Diazo theme, the modernizer.js and respond.js will be
provided by Plone.
Update: respond.js has been removed, as we decided to drop responsive design
support to browsers that do not support media queries.


Layout
======

The layout is constructed with responsive design in mind, and it can have from 1
to 3 columns.
Setting the width of the portal columns using the Deco grid will produce a fluid
width of the left and right columns. In some cases we need fixed with sidebars,
so v2 has been modified to support this feature. In base.less the width can be
set either to fixed number of pixels, or percentages:

    @sidebar-right-width: 300px; // or 25%
    @sidebar-left-width: 200px; // or 25%
    @sidebar-right-margin-left: 12px; // or 1.125%
    @sidebar-left-margin-left: 12px; // or 1.125%


Sidebar position
----------------
Some layouts require both of the sidebars to be on the right hand side.
In manifest.cfg there is a theme parameter set that is used to determine if the
sidebars should be on the right, without the need to actually modify the
templates and setting it on the fly:

    sidebarsright = python: False

True value is for moving the sidebars to the right, False for having one on the
left and one on the right.

This value can be updated in the control panel -> Diazo theme -> Advanced
settings.


Sidebar behavior for tablet
---------------------------
As there is not enough room for both of the sidebars on a tablet, we need to
move one of them below the content. In manifest.cfg there is a theme parameter
set that is used to determine which column should be moved below the content.
To move the left column down set:

    tabletleftcolumndown = python: True

To move the right column down set:

    tabletleftcolumndown = python: False

This value can be updated in the control panel -> Diazo theme -> Advanced
settings.


Deco Grid System
================

We are using the Deco Grid System that comes with Plone for the content column.
The size of the columns and gutters are set in percentages:
column width - 4%
margin left/right - 1.125%

Here are some recommended sizes (page width / column width / left/right margin):
Desktop: 1088px / 44px / 12px - (http://gridcalculator.dk/#/1088/16/24/12)
Tablet:   800px / 32px /  9px - (http://gridcalculator.dk/#/800/16/18/9)
Mobile:   480px / 20px /  5px - (http://gridcalculator.dk/#/480/16/10/5)



Best practices (Do's and Don'ts)
================================

Don't mix grid css classes with others
--------------------------------------
In order not to overwrite grid properties by accident, we encourage you to have
the theme specific CSS classes in a separate element. For example instead of
this:

  <div class="cell width-full position-0 myclass">

You should have this:

  <div class="cell width-full position-0">
    <div class="myclass">


Setting grid widths and positions in the stylesheets
----------------------------------------------------
The responsive design often forces us to have different widths and positions
for the same element on different screen sizes, and as we can't edit the markup,
we'll need to apply these changes in our stylesheets. Instead of giving it a
fixed width value, we can use the .grid-column-width() and .grid-position()
mixins. To set an element to be 6 columns wide and on position 3, just add this
to the appropriate css selector:

    .grid-column-width(6)
    .grid-position(3)

This mixin will calculate the appropriate width and margin for our element.


Centering a fixed width body
----------------------------
To be more precise, the title should be "Centering a fixed width container". The
main idea is to set a fixed width to the container that holds all the elements,
and center it. This way we can have a different background for the body and for
the container.

Responsive design suggests to have a fixed width layout only when the browser
window is wide enough, so we have included the desktop-body-max-width variable
in base.less where you can set the desired width of the page.


Using custom logo
-----------------
If the logo is not coming from Plone, here is the way to put it into the theme:
1. Insert this code in index.html, and make sure the src is pointing to correct
file and the height and width are the actual size of the logo:

    <a href="#" accesskey="1" title="Site" id="portal-logo">
        <img width="305" height="32" title="Site" alt="Site" src="images/logo.png" />
    </a>

2. In rules.xml copy the href, title and alt attributes from Plone logo:

    <copy attributes="href title" css:content="#portal-logo" css:theme="#portal-logo" />
    <copy attributes="title alt" css:content="#portal-logo > img" css:theme="#portal-logo > img" />

Some additional modification might be required for the rules, to everything
fall into right place.


Show portal-personaltools only when the user is logged in
---------------------------------------------------------
In rules.xml add:

    <before css:content="#portal-personaltools-wrapper"
            css:theme="#portal-logo"
            css:if-content="#portal-header .actionMenuHeader" />


Remove advanced search options from search box in the header
------------------------------------------------------------
In rules.xml add:

    <drop css:content=".searchSection" />
    <drop css:content="#portal-advanced-search" />


Add quicklinks before search in header
--------------------------------------
In index.html add:

    <div id="quicklinks">
        Medialle | Opettajille | Paikkakunnallasi
    </div>

Also apply styling in custom.less:

    #quicklinks {
        clear: right;
        float: right;
        margin-top: 10px;
    }


Move breadcrumbs outside of the content column
----------------------------------------------
If you need to move a subelement of an element that is copied by another rule,
then you just can't drop it and append it to another place, but you have to drop
it and use method="raw" to include it in the other location:

    <drop css:content="#portal-breadcrumbs"/>
    <replace css:content="#portal-breadcrumbs" css:theme="#portal-breadcrumbs" method="raw" />


Fix for IE7 hasLayout bug
-------------------------
Internet Explorer has a nice habit of not applying layout to some elements and
that manifests in an overall messed up look of the site. Usually adding some
css properties that are default values in browsers resolve this bug, so first
try setting them in global level, and if that messes up the look in other
browsers, only then apply it with the .ie7 parent class.
Read more about this bug and possible fixes on:
http://haslayout.net/haslayout


IE TinyMCE body background color bug
------------------------------------
If you are using the background-gradient mixin for the body tag, then IE will
apply the same gradient to the body tags within the iframes. To work around this
bug, set a new background gradient only for TinyMCE body that will go from white
to white:

    .mceContentBody {
        .background-gradient(#fff, #fff, #fff);
    }


How to hide elements
--------------------
Hide from both screenreaders and browsers: apply "hidden" css class.
Hide only visually, but have it available for screenreaders: .visuallyhidden
Hide visually and from screenreaders, but maintain layout: .invisible


Contain floats
--------------
Instead of having an additional element after the floats and applying clear:both
in your css, just apply the clearfix css class to your html element that
contains the floated elements.
Note: clearfix class is defined in style.less.

If the content that needs to be cleared is copied with a diazo rule and we don't
have access to its html, then apply the .clearfix() mixin to it in the
appropriate less file.


Using custom fonts
------------------
@Font-Face is used for applying custom fonts. The preferred way is to have the
font files on your server and use that, and the other way would be to use
Google Font API or FontSquirrel. Both are free and have big font collection that
are licensed for web.
With google, only a stylesheet is added to the page, which points to their
server and they will provide all the font files that are needed.
With FontSquirrel you download everything and serve it from your server.
In case if you do not find the proper font, and have a web license for that
font, FontSquirrel @Type-face Generator can be used to generate all the formats
needed by browsers, and it will provide some basic html and css codes as well.
Important: The font used must be licensed for web usage.

The font-face is defined in base.less, and the font files should go into
themere_resources/fonts folder.


Using theme parameters
----------------------
Diazo lets us set variables for a theme within the manifest.cfg that will end
up in @@theming-controlpanel. To use these parameters, we need XSLT.

Display the value of the parameter as a content of an element:

    <xsl:value-of select="$tabletleftcolumndown"/>

Use the parameter for an if statement:

    <rules if="$tabletleftcolumndown">
or:
    <xsl:if test="$tabletleftcolumndown">

Add the value of the parameter to a class attribute:

    <xsl:attribute name="class">$tabletleftcolumndown</xsl:attribute>


Rich drop-down-style menu
-------------------------
(Note: this plugin has been moved to hexagonit.primacontrol!)
For themes that require a drop-down-style menu, we have created a jQuery plugin
(jquery.richmenu.js) that holds all the JavaScript that is needed for the
functionality of the menu. By default this JS file is not enabled in the
JSRegistry, so go to profiles/default/jsregistry.xml and change the
enabled="False" to enabled="True" for the entry that has jquery.richmenu.js in
its ID.
Beside this plugin, we need to have the content for the dropdowns in our Plone
site which will be copied with a diazo rule, or have them in the index.html
(which is not a recommended option).

TODO: how to add this content to plone.

Plone generates a unique id for each menu item, so the dropdown for a specific
menu item needs to have an id in form: '#popup-' + menuItemID. For example menu
item with id="portaltab-news" would be tied to dropdown with
id="popup-portaltab-news".
Html of a menu generated by Plone:

    <ul id="portal-globalnav">
        <li id="portaltab-news" class="plain">
            <a title="Site News" href="http://localhost:8080/Plone/news">News</a>
        </li>
        ...
    </ul>

The dropdown for this menu item would need the following markup:

    <div id="popup-portaltab-news" class="popup-menu">
        <!-- The content of the dropdown -->
    </div>

To have a close button on the dropdown, include this within the content of the
dropdown:

    <div class="popup-close-row">Close</div>

Now that we have all the content on the page, we can set up the richmenu jQuery
plugin. In theme_resources/javascript/script.js add:

    $('#portal-globalnav').richmenu();

The rich menu is turned on by default for mobile version of the site, and if
needed, it can be turned off by setting mobileRichMenu to false. In this case
the script.js would look like this:

    $('#portal-globalnav').richmenu({mobileRichMenu: 0});

The triggering of the rich menu can be set by passing it as a parameter (click,
mouseenter, ...):

    $('#portal-globalnav').richmenu({triger: 'click'});

Also the open and close delay amount can be set:

    $('#portal-globalnav').richmenu({openDelay: 0, closeDelay: 500});

Styling and content of the dropdown is theme specific, so it is not part of the
theme skeleton.


Portlet Overlay
---------------
(Note: this plugin has been moved to hexagonit.primacontrol!)
Adding and editing portlets within an overlay. The JS can be found in the
theme_resources/javascript/libs folder and it is registered in JS registry.
By default it is not enabled, so if needed, go to
profiles/default/jsregistry.xml and change the enabled="False" to enabled="True"
for the entry that has portletoverlay.js in its ID.


Description Tooltip
-------------------
(Note: this plugin has been moved to hexagonit.primacontrol!)
The form help texts can be long ones and they take up too much vertical space,
so this library removes them, adds a help icon and on click, the help text is
displayed in a tooltip.
The JS can be found in the theme_resources/javascript/libs folder and it is
registered in JS registry. By default it is not enabled, so if needed, go to
profiles/default/jsregistry.xml and change the enabled="False" to enabled="True"
for the entry that has descriptiontooltip.js in its ID.


iOS image sizes
---------------
iOS has the possibility of creating an application from a website, so we need
icons and splash screens for it. These images need to be specific sizes in
order to be shown. If the size does not match, it will be ignored.
From iOS 5, media queries can be used for the link tags that set the icons and
splash. We are using these media queries only for the splash, as for the icons
we can use sizes attribute which is backward compatible.

Application icons:
iPhone4: 114 x 114
iPhone3:  57 x  57
iPad:     72 x  72

Splash screen:
iPhone4: 640 x 920
iPhone3: 320 x 460
iPad Landscape: 1024 x  748
iPad Portrait:   768 x 1004


Using CSS3 properties
---------------------
Not all browsers support CSS3 yet, so we need to keep in mind when we are
developing a new theme. Create everything with CSS2 first, and only after
enhance it with CSS3 goodness. This way browsers that do not support CSS3 will
fall back to the CSS2, and still look pretty decent.


New theme roll-out checklist
============================
Follow these steps for each new theme:

  * Create a new theme with zopeskel
  * Create a new git repository for the new theme
  * Update your buildout to include the new theme and run it (development.cfg and local.cfg)
  * Update manifest.cfg with tablet sidebar behavior rule
  * Turn off description tooltip and portlet overlay if they are not needed
  * Update registry.xml with proper portlet style names
  * Update tests with the new portlet style names
  * Start the server and install the new theme
  * Update index.html and rules.xml to suite your layout
  * Change the base.less variable values to match your needs
  * Modify common elements first, and only then move to device specific ones
  * Add needed images and javascripts
  * Create launch icons and splash screens for mobile phones
  * Update print styles
  * Cross browser testing
  * Minify css with Less.app


Useful reads
============

HTML5 Boilerplate
http://html5boilerplate.com/

Mobile HTML5 Boilerplate
http://html5boilerplate.com/mobile

LESS CSS Shapes Library
https://github.com/NathanStrutz/LESS-CSS-Shapes-Library

Lessins - collection of useful mixins
http://code.google.com/p/lessins/

Awesome tutorials to master responsive web design
http://www.catswhocode.com/blog/awesome-tutorials-to-master-responsive-web-design

Grid Calculator - generate a grid for photoshop and illustrator
http://gridcalculator.dk/#/1100/16/24/12

Everything you always wanted to know about touch icons
http://mathiasbynens.be/notes/touch-icons

