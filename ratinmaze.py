<!DOCTYPE html>
<!--[if IE 7]>
<html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">
<![endif]-->
<!--[if IE 8]>
<html class="ie ie8" lang="en-US" prefix="og: http://ogp.me/ns#">
<![endif]-->
<!--[if !(IE 7) | !(IE 8)  ]><!-->
<html prefix="og: http://ogp.me/ns#" class=" js" lang="en-US"><!--<![endif]--><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<meta name="description" content="A Computer Science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions.">
<link rel="shortcut icon" href="https://www.geeksforgeeks.org/gfg.png" type="image/x-icon">

<meta name="theme-color" content="#4cb96b">

<meta property="og:image" content="https://www.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="200">
<meta property="og:image:height" content="200">

<title>Backtracking | Set 2 (Rat in a Maze) - GeeksforGeeks</title>
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="">
<!--[if lt IE 9]>
<script src="https://www.geeksforgeeks.org/wp-content/themes/iconic-one/js/html5.js" type="text/javascript"></script>
<![endif]-->

<script async="" src="ratinmaze_files/async-ads.js"></script><script type="text/javascript" async="" src="ratinmaze_files/cse.js"></script><script type="text/javascript" async="" src="ratinmaze_files/ga.js"></script><script type="text/javascript" async="" src="ratinmaze_files/cse.js"></script><script async="" type="text/javascript" src="ratinmaze_files/gpt.js"></script><script type="application/ld+json">
    {
        "@context" : "http://schema.org",
        "@type" : "Organization",
        "name" : "GeeksforGeeks",
        "url" : "https://www.geeksforgeeks.org/",
        "logo" : "https://www.geeksforgeeks.org/gfgLogo.png",
        "description" : "A computer science portal for geeks. It contains well written, well thought and well explained computer science and programming articles, quizzes and practice/competitive programming/company interview Questions.",
        "founder": [
            {
                "@type" : "Person",
                "name" : "Sandeep Jain",
                "url" : "https://in.linkedin.com/in/sandeep-jain-b3940815"
            }
        ],
        "sameAs" : [ "https://www.facebook.com/geeksforgeeks.org/",
            "https://twitter.com/geeksforgeeks",
            "https://www.linkedin.com/company/1299009",
            "https://www.youtube.com/geeksforgeeksvideos/"
        ]
    }
</script>
<script>

    var arrPostCat = new Array();
            arrPostCat.push('1748');
            arrPostCat.push('1760');
        var domain = 1;
    var arrPost = new Array();
    var post_id = "13376";
    var post_type = "post";
    var post_slug = window.location.href;
    var ip = "35.162.63.220";
    var post_title = "Backtracking | Set 2 (Rat in a Maze)";
    var post_status = "publish";
                            var isAdminLoggedIn = 0;
        </script>

<!-- This site is optimized with the Yoast SEO plugin v7.6 - https://yoast.com/wordpress/plugins/seo/ -->
<link rel="canonical" href="https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/">
<meta property="og:locale" content="en_US">
<meta property="og:type" content="article">
<meta property="og:title" content="Backtracking | Set 2 (Rat in a Maze) - GeeksforGeeks">
<meta property="og:description" content="We have discussed Backtracking and Knight’s tour problem in Set 1. Let us discuss Rat in a Maze as another example problem that can be… Read More »">
<meta property="og:url" content="https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/">
<meta property="og:site_name" content="GeeksforGeeks">
<meta property="article:tag" content="Amazon">
<meta property="article:tag" content="Drishti-Soft">
<meta property="article:tag" content="Expedia">
<meta property="article:tag" content="Flipkart">
<meta property="article:tag" content="Grofers">
<meta property="article:tag" content="MakeMyTrip">
<meta property="article:tag" content="Numerify">
<meta property="article:tag" content="Paytm">
<meta property="article:tag" content="Yatra.com">
<meta property="article:tag" content="Zycus">
<meta property="article:section" content="Backtracking">
<meta property="article:published_time" content="2011-07-18T19:52:48+00:00">
<meta property="article:modified_time" content="2018-07-10T13:56:15+00:00">
<meta property="og:updated_time" content="2018-07-10T13:56:15+00:00">
<meta property="og:image" content="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled11.png">
<meta property="og:image:secure_url" content="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled11.png">
<meta property="og:image" content="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled_path1.png">
<meta property="og:image:secure_url" content="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled_path1.png">
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Organization","url":"https:\/\/www.geeksforgeeks.org\/","sameAs":[],"@id":"https:\/\/www.geeksforgeeks.org\/#organization","name":"GeeksforGeeks","logo":"http:\/\/www.cdn.geeksforgeeks.org\/wp-content\/uploads\/gfg_200X200-1.png"}</script>
<!-- / Yoast SEO plugin. -->

<link rel="dns-prefetch" href="https://www.geeksforgeeks.org/">
<link rel="dns-prefetch" href="https://fonts.googleapis.com/">
<link rel="dns-prefetch" href="https://s.w.org/">
<link rel="alternate" type="application/rss+xml" title="GeeksforGeeks » Feed" href="https://www.geeksforgeeks.org/feed/">
<link rel="alternate" type="application/rss+xml" title="GeeksforGeeks » Comments Feed" href="https://www.geeksforgeeks.org/comments/feed/">
<link rel="alternate" type="application/rss+xml" title="GeeksforGeeks » Backtracking | Set 2 (Rat in a Maze) Comments Feed" href="https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/feed/">
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.4\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.4\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/www.geeksforgeeks.org\/wp-includes\/js\/wp-emoji-release.min.js"}};
			!function(a,b,c){function d(a,b){var c=String.fromCharCode;l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,a),0,0);var d=k.toDataURL();l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,b),0,0);var e=k.toDataURL();return d===e}function e(a){var b;if(!l||!l.fillText)return!1;switch(l.textBaseline="top",l.font="600 32px Arial",a){case"flag":return!(b=d([55356,56826,55356,56819],[55356,56826,8203,55356,56819]))&&(b=d([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]),!b);case"emoji":return b=d([55357,56692,8205,9792,65039],[55357,56692,8203,9792,65039]),!b}return!1}function f(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var g,h,i,j,k=b.createElement("canvas"),l=k.getContext&&k.getContext("2d");for(j=Array("flag","emoji"),c.supports={everything:!0,everythingExceptFlag:!0},i=0;i<j.length;i++)c.supports[j[i]]=e(j[i]),c.supports.everything=c.supports.everything&&c.supports[j[i]],"flag"!==j[i]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[j[i]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(h=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",h,!1),a.addEventListener("load",h,!1)):(a.attachEvent("onload",h),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),g=c.source||{},g.concatemoji?f(g.concatemoji):g.wpemoji&&g.twemoji&&(f(g.twemoji),f(g.wpemoji)))}(window,document,window._wpemojiSettings);
		</script><script src="ratinmaze_files/wp-emoji-release.js" type="text/javascript" defer="defer"></script>
		<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel="stylesheet" id="wp-quicklatex-format-css" href="ratinmaze_files/quicklatex-format.css" type="text/css" media="all">
<link rel="stylesheet" id="themonic-fonts-css" href="ratinmaze_files/css.css" type="text/css" media="all">
<link rel="stylesheet" id="custom-style-css" href="ratinmaze_files/gfg-2.css" type="text/css" media="all">
<script type="text/javascript" src="ratinmaze_files/jquery.js"></script>
<script type="text/javascript" src="ratinmaze_files/jquery-migrate.js"></script>
<script type="text/javascript" src="ratinmaze_files/gfg-7.js"></script>
<link rel="https://api.w.org/" href="https://www.geeksforgeeks.org/wp-json/">
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.cdn.geeksforgeeks.org/xmlrpc.php?rsd">
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://www.geeksforgeeks.org/wp-includes/wlwmanifest.xml"> 
<meta name="generator" content="WordPress 4.9.6">
<link rel="shortlink" href="https://www.geeksforgeeks.org/?p=13376">
<link rel="alternate" type="application/json+oembed" href="https://www.geeksforgeeks.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fbackttracking-set-2-rat-in-a-maze%2F">
<link rel="alternate" type="text/xml+oembed" href="https://www.geeksforgeeks.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fbackttracking-set-2-rat-in-a-maze%2F&amp;format=xml">
        <link rel="stylesheet" type="text/css" href="ratinmaze_files/cookieconsent.css">
        <script src="ratinmaze_files/cookieconsent.js"></script>
        <script>
        window.addEventListener("load", function(){
        window.cookieconsent.initialise({
        "palette": {
            "popup": {
              "background": "#3c404d",
              "text": "#d6d6d6"
            },
            "button": {
              "background": "#8bed4f"
            }
          },
          "theme": "classic",
            onStatusChange: function(status) {
            
            },
            law: {
              regionalLaw: false,
            },
            location: true,
            "content": {
            "message": "We use cookies to ensure you have the best browsing experience on our website. By using our site, you acknowledge that you have read and understood our <a href=\"https://www.geeksforgeeks.org/cookie-policy/\" class=\"cc-link\" target=\"_blank\">Cookie Policy</a> & ",
            "link": "Privacy Policy",
            "href": "/privacy-policy/"
            },
        cookie: {
        name : "geeksforgeeks_consent_status",
        }
        })});
    
        </script>
    <style>
#wpadminbar{
background: #ff0000 !important;
}
</style>
<style type="text/css" id="custom-background-css">
body.custom-background { background-color: #ffffff; }
</style>
<link rel="amphtml" href="https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/amp/"><link rel="stylesheet" type="text/css" href="ratinmaze_files/shCore.css"><link rel="stylesheet" type="text/css" href="ratinmaze_files/shThemeDefault.css"><style type="text/css" id="syntaxhighlighteranchor"></style>
<link rel="icon" href="https://www.geeksforgeeks.org/wp-content/uploads/gfg_200X200-100x100.png" sizes="32x32">
<link rel="icon" href="https://www.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png" sizes="192x192">
<link rel="apple-touch-icon-precomposed" href="https://www.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png">
<meta name="msapplication-TileImage" content="https://www.geeksforgeeks.org/wp-content/uploads/gfg_200X200.png">

<script type="text/javascript">
  var googletag = googletag || {};
  googletag.cmd = googletag.cmd || [];
  (function() {
    var gads = document.createElement('script');
    gads.async = true;
    gads.type = 'text/javascript';
    var useSSL = 'https:' == document.location.protocol;
    gads.src = (useSSL ? 'https:' : 'http:') +
      '//www.googletagservices.com/tag/js/gpt.js';
    var node = document.getElementsByTagName('script')[0];
    node.parentNode.insertBefore(gads, node);
  })();
</script>

<script type="text/javascript">
  googletag.cmd.push(function() {
    googletag.defineSlot('/27823234/SP', [300, 250], 'div-gpt-ad-1458112424022-0').addService(googletag.pubads());
    googletag.pubads().enableSingleRequest();
    googletag.enableServices();
  });
</script>
<script type="text/javascript" async="" src="ratinmaze_files/bsa.js"></script><script src="ratinmaze_files/jsapi" type="text/javascript"></script><link type="text/css" href="ratinmaze_files/defaulten.css" rel="stylesheet"><link type="text/css" href="ratinmaze_files/default.css" rel="stylesheet"><script type="text/javascript" src="ratinmaze_files/defaulten.js"></script><script src="ratinmaze_files/jsapi" type="text/javascript"></script><link type="text/css" href="ratinmaze_files/defaulten.css" rel="stylesheet"><link type="text/css" href="ratinmaze_files/default.css" rel="stylesheet"><script type="text/javascript" src="ratinmaze_files/defaulten.js"></script><style type="text/css">.gsc-control-cse{font-family:Arial, sans-serif;border-color:#FFFFFF;background-color:#FFFFFF}.gsc-control-cse .gsc-table-result{font-family:Arial, sans-serif}input.gsc-input,.gsc-input-box,.gsc-input-box-hover,.gsc-input-box-focus{border-color:#6AA84F}.gsc-search-button-v2,.gsc-search-button-v2:hover,.gsc-search-button-v2:focus{border-color:#000000;background-color:#6AA84F;background-image:none;filter:none}.gsc-search-button-v2 svg{fill:#FFFFFF}.gsc-tabHeader.gsc-tabhInactive{border-color:#E9E9E9;background-color:#E9E9E9}.gsc-tabHeader.gsc-tabhActive{border-color:#FF9900;border-bottom-color:#FFFFFF;background-color:#FFFFFF}.gsc-tabsArea{border-color:#FF9900}.gsc-webResult.gsc-result,.gsc-results .gsc-imageResult{border-color:#FFFFFF;background-color:#FFFFFF}.gsc-webResult.gsc-result:hover,.gsc-imageResult:hover{border-color:#FFFFFF;background-color:#FFFFFF}.gs-webResult.gs-result a.gs-title:link,.gs-webResult.gs-result a.gs-title:link b,.gs-imageResult a.gs-title:link,.gs-imageResult a.gs-title:link b{color:#006600}.gs-webResult.gs-result a.gs-title:visited,.gs-webResult.gs-result a.gs-title:visited b,.gs-imageResult a.gs-title:visited,.gs-imageResult a.gs-title:visited b{color:#EC4E20}.gs-webResult.gs-result a.gs-title:hover,.gs-webResult.gs-result a.gs-title:hover b,.gs-imageResult a.gs-title:hover,.gs-imageResult a.gs-title:hover b{color:#CA7700}.gs-webResult.gs-result a.gs-title:active,.gs-webResult.gs-result a.gs-title:active b,.gs-imageResult a.gs-title:active,.gs-imageResult a.gs-title:active b{color:#006600}.gsc-cursor-page{color:#006600}a.gsc-trailing-more-results:link{color:#006600}.gs-webResult .gs-snippet,.gs-imageResult .gs-snippet,.gs-fileFormatType{color:#000000}.gs-webResult div.gs-visibleUrl,.gs-imageResult div.gs-visibleUrl{color:#008000}.gs-webResult div.gs-visibleUrl-short{color:#008000}.gs-webResult div.gs-visibleUrl-short{display:none}.gs-webResult div.gs-visibleUrl-long{display:block}.gs-promotion div.gs-visibleUrl-short{display:none}.gs-promotion div.gs-visibleUrl-long{display:block}.gsc-cursor-box{border-color:#FFFFFF}.gsc-results .gsc-cursor-box .gsc-cursor-page{border-color:#E9E9E9;background-color:#FFFFFF;color:#006600}.gsc-results .gsc-cursor-box .gsc-cursor-current-page{border-color:#FF9900;background-color:#FFFFFF;color:#EC4E20}.gsc-webResult.gsc-result.gsc-promotion{border-color:#336699;background-color:#FFFFFF}.gsc-completion-title{color:#006600}.gsc-completion-snippet{color:#000000}.gs-promotion a.gs-title:link,.gs-promotion a.gs-title:link *,.gs-promotion .gs-snippet a:link{color:#006600}.gs-promotion a.gs-title:visited,.gs-promotion a.gs-title:visited *,.gs-promotion .gs-snippet a:visited{color:#EC4E20}.gs-promotion a.gs-title:hover,.gs-promotion a.gs-title:hover *,.gs-promotion .gs-snippet a:hover{color:#CA7700}.gs-promotion a.gs-title:active,.gs-promotion a.gs-title:active *,.gs-promotion .gs-snippet a:active{color:#006600}.gs-promotion .gs-snippet,.gs-promotion .gs-title .gs-promotion-title-right,.gs-promotion .gs-title .gs-promotion-title-right *{color:#000000}.gs-promotion .gs-visibleUrl,.gs-promotion .gs-visibleUrl-short{color:#008000}</style><style type="text/css">.gscb_a{display:inline-block;font:27px/13px arial,sans-serif}.gsst_a .gscb_a{color:#a1b9ed;cursor:pointer}.gsst_a:hover .gscb_a,.gsst_a:focus .gscb_a{color:#36c}.gsst_a{display:inline-block}.gsst_a{cursor:pointer;padding:0 4px}.gsst_a:hover{text-decoration:none!important}.gsst_b{font-size:16px;padding:0 2px;position:relative;user-select:none;-moz-user-select:none;white-space:nowrap}.gsst_e{opacity:0.55;}.gsst_a:hover .gsst_e,.gsst_a:focus .gsst_e{opacity:0.72;}.gsst_a:active .gsst_e{opacity:1;}.gsst_f{background:white;text-align:left}.gsst_g{background-color:white;border:1px solid #ccc;border-top-color:#d9d9d9;box-shadow:0 2px 4px rgba(0,0,0,0.2);-moz-box-shadow:0 2px 4px rgba(0,0,0,0.2);margin:-1px -3px;padding:0 6px}.gsst_h{background-color:white;height:1px;margin-bottom:-1px;position:relative;top:-1px}.gsib_a{width:100%;padding:4px 6px 0}.gsib_a,.gsib_b{vertical-align:top}.gssb_c{border:0;position:absolute;z-index:989}.gssb_e{border:1px solid #ccc;border-top-color:#d9d9d9;box-shadow:0 2px 4px rgba(0,0,0,0.2);-moz-box-shadow:0 2px 4px rgba(0,0,0,0.2);cursor:default}.gssb_f{visibility:hidden;white-space:nowrap}.gssb_k{border:0;display:block;position:absolute;top:0;z-index:988}.gsdd_a{border:none!important}.gsq_a{padding:0}.gscsep_a{display:none}.gssb_a{padding:0 7px}.gssb_a,.gssb_a td{white-space:nowrap;overflow:hidden;line-height:22px}#gssb_b{font-size:11px;color:#36c;text-decoration:none}#gssb_b:hover{font-size:11px;color:#36c;text-decoration:underline}.gssb_g{text-align:center;padding:8px 0 7px;position:relative}.gssb_h{font-size:15px;height:28px;margin:0.2em}.gssb_i{background:#eee}.gss_ifl{visibility:hidden;padding-left:5px}.gssb_i .gss_ifl{visibility:visible}a.gssb_j{font-size:13px;color:#36c;text-decoration:none;line-height:100%}a.gssb_j:hover{text-decoration:underline}.gssb_l{height:1px;background-color:#e5e5e5}.gssb_m{color:#000;background:#fff}.gsfe_a{border:1px solid #b9b9b9;border-top-color:#a0a0a0;box-shadow:inset 0px 1px 2px rgba(0,0,0,0.1);-moz-box-shadow:inset 0px 1px 2px rgba(0,0,0,0.1);-webkit-box-shadow:inset 0px 1px 2px rgba(0,0,0,0.1);}.gsfe_b{border:1px solid #4d90fe;outline:none;box-shadow:inset 0px 1px 2px rgba(0,0,0,0.3);-moz-box-shadow:inset 0px 1px 2px rgba(0,0,0,0.3);-webkit-box-shadow:inset 0px 1px 2px rgba(0,0,0,0.3);}.gssb_a{padding:0 9px}.gsib_a{padding-right:8px;padding-left:8px}.gsst_a{padding-top:5.5px}.gssb_e{border:0}.gssb_l{margin:5px 0}input.gsc-input::-webkit-input-placeholder{font-size:14px}input.gsc-input:-moz-placeholder{font-size:14px}input.gsc-input::-moz-placeholder{font-size:14px}input.gsc-input:-ms-input-placeholder{font-size:14px}input.gsc-input:focus::-webkit-input-placeholder{color:transparent}input.gsc-input:focus:-moz-placeholder{color:transparent}input.gsc-input:focus::-moz-placeholder{color:transparent}input.gsc-input:focus:-ms-input-placeholder{color:transparent}.gssb_c .gsc-completion-container{position:static}.gssb_c{z-index:5000}.gsc-completion-container table{background:transparent;font-size:inherit;font-family:inherit}.gssb_c > tbody > tr,.gssb_c > tbody > tr > td,.gssb_d,.gssb_d > tbody > tr,.gssb_d > tbody > tr > td,.gssb_e,.gssb_e > tbody > tr,.gssb_e > tbody > tr > td{padding:0;margin:0;border:0}.gssb_a table,.gssb_a table tr,.gssb_a table tr td{padding:0;margin:0;border:0}</style><style type="text/css">.gsc-control-cse{font-family:Arial, sans-serif;border-color:#FFFFFF;background-color:#FFFFFF}.gsc-control-cse .gsc-table-result{font-family:Arial, sans-serif}input.gsc-input,.gsc-input-box,.gsc-input-box-hover,.gsc-input-box-focus{border-color:#6AA84F}.gsc-search-button-v2,.gsc-search-button-v2:hover,.gsc-search-button-v2:focus{border-color:#000000;background-color:#6AA84F;background-image:none;filter:none}.gsc-search-button-v2 svg{fill:#FFFFFF}.gsc-tabHeader.gsc-tabhInactive{border-color:#E9E9E9;background-color:#E9E9E9}.gsc-tabHeader.gsc-tabhActive{border-color:#FF9900;border-bottom-color:#FFFFFF;background-color:#FFFFFF}.gsc-tabsArea{border-color:#FF9900}.gsc-webResult.gsc-result,.gsc-results .gsc-imageResult{border-color:#FFFFFF;background-color:#FFFFFF}.gsc-webResult.gsc-result:hover,.gsc-imageResult:hover{border-color:#FFFFFF;background-color:#FFFFFF}.gs-webResult.gs-result a.gs-title:link,.gs-webResult.gs-result a.gs-title:link b,.gs-imageResult a.gs-title:link,.gs-imageResult a.gs-title:link b{color:#006600}.gs-webResult.gs-result a.gs-title:visited,.gs-webResult.gs-result a.gs-title:visited b,.gs-imageResult a.gs-title:visited,.gs-imageResult a.gs-title:visited b{color:#EC4E20}.gs-webResult.gs-result a.gs-title:hover,.gs-webResult.gs-result a.gs-title:hover b,.gs-imageResult a.gs-title:hover,.gs-imageResult a.gs-title:hover b{color:#CA7700}.gs-webResult.gs-result a.gs-title:active,.gs-webResult.gs-result a.gs-title:active b,.gs-imageResult a.gs-title:active,.gs-imageResult a.gs-title:active b{color:#006600}.gsc-cursor-page{color:#006600}a.gsc-trailing-more-results:link{color:#006600}.gs-webResult .gs-snippet,.gs-imageResult .gs-snippet,.gs-fileFormatType{color:#000000}.gs-webResult div.gs-visibleUrl,.gs-imageResult div.gs-visibleUrl{color:#008000}.gs-webResult div.gs-visibleUrl-short{color:#008000}.gs-webResult div.gs-visibleUrl-short{display:none}.gs-webResult div.gs-visibleUrl-long{display:block}.gs-promotion div.gs-visibleUrl-short{display:none}.gs-promotion div.gs-visibleUrl-long{display:block}.gsc-cursor-box{border-color:#FFFFFF}.gsc-results .gsc-cursor-box .gsc-cursor-page{border-color:#E9E9E9;background-color:#FFFFFF;color:#006600}.gsc-results .gsc-cursor-box .gsc-cursor-current-page{border-color:#FF9900;background-color:#FFFFFF;color:#EC4E20}.gsc-webResult.gsc-result.gsc-promotion{border-color:#336699;background-color:#FFFFFF}.gsc-completion-title{color:#006600}.gsc-completion-snippet{color:#000000}.gs-promotion a.gs-title:link,.gs-promotion a.gs-title:link *,.gs-promotion .gs-snippet a:link{color:#006600}.gs-promotion a.gs-title:visited,.gs-promotion a.gs-title:visited *,.gs-promotion .gs-snippet a:visited{color:#EC4E20}.gs-promotion a.gs-title:hover,.gs-promotion a.gs-title:hover *,.gs-promotion .gs-snippet a:hover{color:#CA7700}.gs-promotion a.gs-title:active,.gs-promotion a.gs-title:active *,.gs-promotion .gs-snippet a:active{color:#006600}.gs-promotion .gs-snippet,.gs-promotion .gs-title .gs-promotion-title-right,.gs-promotion .gs-title .gs-promotion-title-right *{color:#000000}.gs-promotion .gs-visibleUrl,.gs-promotion .gs-visibleUrl-short{color:#008000}</style><style></style><script id="_bsa_srv-CKYDL2JJ_0" type="text/javascript" src="ratinmaze_files/CKYDL2JJ.json"></script><script src="ratinmaze_files/embed.js" data-timestamp="1531849031515"></script><link rel="prefetch" as="style" href="ratinmaze_files/a_data/lounge.css"><link rel="prefetch" as="script" href="ratinmaze_files/a_data/common.js"><link rel="prefetch" as="script" href="ratinmaze_files/a_data/lounge.js"><link rel="prefetch" as="script" href="ratinmaze_files/a_data/config.js"></head>

<body class="post-template-default single single-post postid-13376 single-format-standard custom-background custom-background-white custom-font-enabled"><div role="dialog" aria-live="polite" aria-label="cookieconsent" aria-describedby="cookieconsent:desc" class="cc-window cc-banner cc-type-info cc-theme-classic cc-bottom cc-color-override-382972913  cc-invisible" style="display: none;"><!--googleoff: all--><span id="cookieconsent:desc" class="cc-message">We
 use cookies to ensure you have the best browsing experience on our 
website. By using our site, you acknowledge that you have read and 
understood our <a href="https://www.geeksforgeeks.org/cookie-policy/" class="cc-link" target="_blank">Cookie Policy</a> &amp;  <a aria-label="learn more about cookies" role="button" tabindex="0" class="cc-link" href="https://www.geeksforgeeks.org/privacy-policy/" target="_blank">Privacy Policy</a></span><div class="cc-compliance"><a aria-label="dismiss cookie message" role="button" tabindex="0" class="cc-btn cc-dismiss">Got it!</a></div><!--googleon: all--></div>

<!-- BuySellAds Ad Code -->
<script type="text/javascript">
(function(){
  var bsa = document.createElement('script');
     bsa.type = 'text/javascript';
     bsa.async = true;
     bsa.src = '//s3.buysellads.com/ac/bsa.js';
  (document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);
})();
</script>
<!-- End BuySellAds Ad Code -->

<div id="page" style="position:relative;overflow: unset;z-index:2;" class="hfeed site">
	<header id="masthead" class="site-header" role="banner">
		<div style="margin-bottom: 5px;">	
		<div class="upper-header">
            <div id="container-g4g-header">
                <div id="MasterHead">
                    <div class="header-gfg-logo">
                                    <a href="https://www.geeksforgeeks.org/" title="GeeksforGeeks" rel="home"><img src="ratinmaze_files/GeeksforGeeksLogoHeader.png" alt="GFG-Logo"></a>
                            </div>

     <span class="responsive-custom-search">
    <script>
      (function() {
        var cx = '009682134359037907028:tj6eafkv_be';
        var gcse = document.createElement('script');
        gcse.type = 'text/javascript';
        gcse.async = true;
        gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
            '//cse.google.com/cse.js?cx=' + cx;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(gcse, s);
      })();
    </script>
    <div id="___gcse_0"><div class="gsc-control-cse gsc-control-cse-en"><div class="gsc-control-wrapper-cse" dir="ltr"><form class="gsc-search-box gsc-search-box-tools" accept-charset="utf-8"><table class="gsc-search-box" cellspacing="0" cellpadding="0"><tbody><tr><td class="gsc-input"><div class="gsc-input-box" id="gsc-iw-id1"><table style="width: 100%; padding: 0px;" id="gs_id50" class="gstl_50 " cellspacing="0" cellpadding="0"><tbody><tr><td id="gs_tti50" class="gsib_a"><input autocomplete="off" size="10" class="gsc-input" name="search" title="search" style="width: 100%; padding: 0px; border: medium none; margin: 0px; height: auto; outline: currentcolor none medium; background: rgb(255, 255, 255) url(&quot;https://www.google.com/cse/static/images/1x/googlelogo_lightgrey_46x16dp.png&quot;) no-repeat scroll left center; text-indent: 48px;" id="gsc-i-id1" dir="ltr" spellcheck="false" placeholder="Custom Search" type="text"></td><td class="gsib_b"><div class="gsst_b" id="gs_st50" dir="ltr"><a class="gsst_a" href="javascript:void(0)" style="display: none;"><span class="gscb_a" id="gs_cb50">×</span></a></div></td></tr></tbody></table></div></td><td class="gsc-search-button"><button class="gsc-search-button gsc-search-button-v2"><svg width="13" height="13" viewBox="0 0 13 13"><title>search</title><path d="m4.8495 7.8226c0.82666 0 1.5262-0.29146 2.0985-0.87438 0.57232-0.58292 0.86378-1.2877 0.87438-2.1144 0.010599-0.82666-0.28086-1.5262-0.87438-2.0985-0.59352-0.57232-1.293-0.86378-2.0985-0.87438-0.8055-0.010599-1.5103 0.28086-2.1144 0.87438-0.60414 0.59352-0.8956 1.293-0.87438 2.0985 0.021197 0.8055 0.31266 1.5103 0.87438 2.1144 0.56172 0.60414 1.2665 0.8956 2.1144 0.87438zm4.4695 0.2115 3.681 3.6819-1.259 1.284-3.6817-3.7 0.0019784-0.69479-0.090043-0.098846c-0.87973 0.76087-1.92 1.1413-3.1207 1.1413-1.3553 0-2.5025-0.46363-3.4417-1.3909s-1.4088-2.0686-1.4088-3.4239c0-1.3553 0.4696-2.4966 1.4088-3.4239 0.9392-0.92727 2.0864-1.3969 3.4417-1.4088 1.3553-0.011889 2.4906 0.45771 3.406 1.4088 0.9154 0.95107 1.379 2.0924 1.3909 3.4239 0 1.2126-0.38043 2.2588-1.1413 3.1385l0.098834 0.090049z"></path></svg></button></td><td class="gsc-clear-button"><div class="gsc-clear-button" title="clear results">&nbsp;</div></td></tr></tbody></table></form><div class="gsc-results-wrapper-overlay"><div class="gsc-results-close-btn" tabindex="0"></div><div class="gsc-tabsAreaInvisible"><div class="gsc-tabHeader gsc-inline-block gsc-tabhActive">Custom Search</div><span class="gs-spacer"> </span></div><div class="gsc-tabsAreaInvisible"></div><div class="gsc-above-wrapper-area-invisible"><table class="gsc-above-wrapper-area-container" cellspacing="0" cellpadding="0"><tbody><tr><td class="gsc-result-info-container"><div class="gsc-result-info-invisible"></div></td><td class="gsc-orderby-container"><div class="gsc-orderby-invisible"><div class="gsc-orderby-label gsc-inline-block">Sort by:</div><div class="gsc-option-menu-container gsc-inline-block"><div class="gsc-selected-option-container gsc-inline-block"><div class="gsc-selected-option">Relevance</div><div class="gsc-option-selector"></div></div><div class="gsc-option-menu-invisible"><div class="gsc-option-menu-item gsc-option-menu-item-highlighted"><div class="gsc-option">Relevance</div></div><div class="gsc-option-menu-item"><div class="gsc-option">Date</div></div></div></div></div></td></tr></tbody></table></div><div class="gsc-adBlockInvisible"></div><div class="gsc-wrapper"><div class="gsc-adBlockInvisible"></div><div class="gsc-resultsbox-invisible"><div class="gsc-resultsRoot gsc-tabData gsc-tabdActive"><table class="gsc-resultsHeader" cellspacing="0" cellpadding="0"><tbody><tr><td class="gsc-twiddleRegionCell"><div class="gsc-twiddle"><div class="gsc-title">Web</div></div><div class="gsc-stats"></div><div class="gsc-results-selector gsc-all-results-active"><div class="gsc-result-selector gsc-one-result" title="show one result">&nbsp;</div><div class="gsc-result-selector gsc-more-results" title="show more results">&nbsp;</div><div class="gsc-result-selector gsc-all-results" title="show all results">&nbsp;</div></div></td><td class="gsc-configLabelCell"></td></tr></tbody></table><div><div class="gsc-expansionArea"></div></div></div></div></div></div><div class="gsc-modal-background-image" tabindex="0"></div></div></div></div>
    </span>

                    <div class="buttonsProfileSide">
                        <div class="profile-buttons">
    <a class="ButtonLogin" href="https://auth.geeksforgeeks.org/?to=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/">Login</a>
    </div><div class="masterhead-buttons">
                               
                                <a class="ButtonContribute" href="https://practice.geeksforgeeks.org/courses/SudoPlacement/" style="margin-bottom:5px;">Sudo Placement</a>
                                <a class="ButtonContribute" href="https://contribute.geeksforgeeks.org/wp-admin/post-new.php">Write an Article</a>
                        </div>

                    </div>

                </div>
            </div>
            </div>


<div id="profile" style="float: right; margin-top: -1%;margin-right:1%;"></div>
</div>
</header></div>

		
		
		<nav id="site-navigation" class="themonic-nav" role="navigation" style="width: 100%; position: fixed; top: 0px; z-index: 99998;">
			<a class="assistive-text" href="#content" title="Skip to content">Skip to content</a>
			<div class="menu-iconic-container"><ul id="menu-top" class="nav-menu"><li id="menu-item-147519" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147519"><a href="https://www.geeksforgeeks.org/" class="reduceMenuHeight"><img style="width: 30px;vertical-align: middle;" src="ratinmaze_files/gfg_transparent_white_small.png"></a></li>
<li id="menu-item-141975" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-141975"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">Algo ▼</a>
<ul class="sub-menu">
	<li id="menu-item-135030" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135030"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/#AnalysisofAlgorithms" class="reduceMenuHeight">Analysis of Algorithms</a></li>
	<li id="menu-item-146823" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146823"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">Topicwise ►</a>
	<ul class="sub-menu">
		<li id="menu-item-147774" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147774"><a href="http://www.geeksforgeeks.org/searching-algorithms/" class="reduceMenuHeight">Searching Algorithms</a></li>
		<li id="menu-item-147773" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147773"><a href="http://www.geeksforgeeks.org/sorting-algorithms/" class="reduceMenuHeight">Sorting Algorithms</a></li>
		<li id="menu-item-135041" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135041"><a href="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/" class="reduceMenuHeight">Graph Algorithms</a></li>
		<li id="menu-item-135040" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135040"><a href="http://www.geeksforgeeks.org/bitwise-algorithms/" class="reduceMenuHeight">Bit Algorithms</a></li>
		<li id="menu-item-135034" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135034"><a href="https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/" class="reduceMenuHeight">Pattern Searching</a></li>
		<li id="menu-item-135038" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135038"><a href="http://www.geeksforgeeks.org/geometric-algorithms/" class="reduceMenuHeight">Geometric Algorithms</a></li>
		<li id="menu-item-135039" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135039"><a href="http://www.geeksforgeeks.org/mathematical-algorithms/" class="reduceMenuHeight">Mathematical Algorithms</a></li>
		<li id="menu-item-135042" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135042"><a href="http://www.geeksforgeeks.org/randomized-algorithms/" class="reduceMenuHeight">Randomized Algorithms</a></li>
		<li id="menu-item-156520" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-156520"><a href="https://www.geeksforgeeks.org/game-theory/" class="reduceMenuHeight">Game Theory</a></li>
	</ul>
</li>
	<li id="menu-item-146824" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146824"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">Algorithm Paradigms ►</a>
	<ul class="sub-menu">
		<li id="menu-item-135032" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135032"><a href="http://www.geeksforgeeks.org/greedy-algorithms/" class="reduceMenuHeight">Greedy Algorithms</a></li>
		<li id="menu-item-135033" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135033"><a href="http://www.geeksforgeeks.org/dynamic-programming/" class="reduceMenuHeight">Dynamic Programming</a></li>
		<li id="menu-item-135037" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135037"><a href="http://www.geeksforgeeks.org/divide-and-conquer/" class="reduceMenuHeight">Divide and Conquer</a></li>
		<li id="menu-item-135036" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135036"><a href="http://www.geeksforgeeks.org/backtracking-algorithms/" class="reduceMenuHeight">Backtracking</a></li>
		<li id="menu-item-137933" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137933"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/#BranchandBound" class="reduceMenuHeight">Branch &amp; Bound</a></li>
	</ul>
</li>
	<li id="menu-item-146911" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146911"><a href="http://www.geeksforgeeks.org/fundamentals-of-algorithms/" class="reduceMenuHeight">All Algorithms</a></li>
</ul>
</li>
<li id="menu-item-142016" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-142016"><a href="http://www.geeksforgeeks.org/data-structures/" class="reduceMenuHeight">DS  ▼</a>
<ul class="sub-menu">
	<li id="menu-item-135054" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135054"><a href="http://www.geeksforgeeks.org/array-data-structure/" class="reduceMenuHeight">Array</a></li>
	<li id="menu-item-135045" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135045"><a href="http://www.geeksforgeeks.org/data-structures/linked-list/" class="reduceMenuHeight">LinkedList</a></li>
	<li id="menu-item-135046" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135046"><a href="http://www.geeksforgeeks.org/stack-data-structure/" class="reduceMenuHeight">Stack</a></li>
	<li id="menu-item-135047" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135047"><a href="http://www.geeksforgeeks.org/queue-data-structure/" class="reduceMenuHeight">Queue</a></li>
	<li id="menu-item-146827" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146827"><a href="http://www.geeksforgeeks.org/data-structures/" class="reduceMenuHeight">Tree based DS ►</a>
	<ul class="sub-menu">
		<li id="menu-item-135048" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135048"><a href="http://www.geeksforgeeks.org/binary-tree-data-structure/" class="reduceMenuHeight">Binary Tree</a></li>
		<li id="menu-item-135049" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135049"><a href="http://www.geeksforgeeks.org/binary-search-tree-data-structure/" class="reduceMenuHeight">Binary Search Tree</a></li>
		<li id="menu-item-135050" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135050"><a href="http://www.geeksforgeeks.org/heap-data-structure/" class="reduceMenuHeight">Heap</a></li>
	</ul>
</li>
	<li id="menu-item-135051" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135051"><a href="http://www.geeksforgeeks.org/hashing-data-structure/" class="reduceMenuHeight">Hashing</a></li>
	<li id="menu-item-135052" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135052"><a href="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/" class="reduceMenuHeight">Graph</a></li>
	<li id="menu-item-135053" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135053"><a href="http://www.geeksforgeeks.org/advanced-data-structures/" class="reduceMenuHeight">Advanced Data Structure</a></li>
	<li id="menu-item-135055" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135055"><a href="http://www.geeksforgeeks.org/matrix/" class="reduceMenuHeight">Matrix</a></li>
	<li id="menu-item-147716" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147716"><a href="http://www.geeksforgeeks.org/string-data-structure/" class="reduceMenuHeight">Strings</a></li>
	<li id="menu-item-135056" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135056"><a href="http://www.geeksforgeeks.org/data-structures/" class="reduceMenuHeight">All Data Structures</a></li>
</ul>
</li>
<li id="menu-item-147478" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-147478"><a href="http://www.geeksforgeeks.org/category/program-output/" class="reduceMenuHeight">Languages ▼</a>
<ul class="sub-menu">
	<li id="menu-item-135006" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-135006"><a href="https://www.geeksforgeeks.org/c-programming-language/" class="reduceMenuHeight">C</a></li>
	<li id="menu-item-135007" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-135007"><a href="https://www.geeksforgeeks.org/c-plus-plus/" class="reduceMenuHeight">C++</a></li>
	<li id="menu-item-135012" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-135012"><a href="https://www.geeksforgeeks.org/java/" class="reduceMenuHeight">Java</a></li>
	<li id="menu-item-137004" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-137004"><a href="https://www.geeksforgeeks.org/python-programming-language/" class="reduceMenuHeight">Python</a></li>
	<li id="menu-item-135016" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-135016"><a href="http://www.geeksforgeeks.org/sql-tutorial/" class="reduceMenuHeight">SQL</a></li>
	<li id="menu-item-182096" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-182096"><a href="https://www.geeksforgeeks.org/php/" class="reduceMenuHeight">PHP</a></li>
	<li id="menu-item-188679" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-188679"><a href="https://www.geeksforgeeks.org/javascript-tutorial/" class="reduceMenuHeight">Javascript</a></li>
	<li id="menu-item-140854" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-140854"><a title="http://www.geeksforgeeks.org/category/program-output/" href="https://www.geeksforgeeks.org/category/program-output/" class="reduceMenuHeight">Program Output</a></li>
</ul>
</li>
<li id="menu-item-142017" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-142017"><a href="http://www.geeksforgeeks.org/about/interview-corner/" class="reduceMenuHeight">Interview  ▼</a>
<ul class="sub-menu">
	<li id="menu-item-141326" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-141326"><a href="https://www.geeksforgeeks.org/company-preparation/" class="reduceMenuHeight">Company Prep</a></li>
	<li id="menu-item-137171" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137171"><a href="http://www.geeksforgeeks.org/interview-preparation-for-software-developer/" class="reduceMenuHeight">Top Topics</a></li>
	<li id="menu-item-137172" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137172"><a href="https://practice.geeksforgeeks.org/company-tags" class="reduceMenuHeight">Practice Company Questions</a></li>
	<li id="menu-item-137173" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137173"><a href="http://www.geeksforgeeks.org/about/interview-corner/" class="reduceMenuHeight">Interview Experiences</a></li>
	<li id="menu-item-137174" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137174"><a href="https://www.geeksforgeeks.org/experienced-interview-experiences-company-wise/" class="reduceMenuHeight">Experienced Interviews</a></li>
	<li id="menu-item-137175" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137175"><a href="https://www.geeksforgeeks.org/internship-interview-experiences-company-wise/" class="reduceMenuHeight">Internship Interviews</a></li>
	<li id="menu-item-137176" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137176"><a href="http://www.geeksforgeeks.org/category/competitive-programming/" class="reduceMenuHeight">Competitive Programming</a></li>
	<li id="menu-item-147581" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147581"><a href="http://www.geeksforgeeks.org/software-design-patterns/" class="reduceMenuHeight">Design Patterns</a></li>
	<li id="menu-item-137186" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137186"><a href="http://geeksquiz.com/quiz-corner/" class="reduceMenuHeight">Multiple Choice Quizzes</a></li>
</ul>
</li>
<li id="menu-item-137178" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-137178"><a href="http://www.geeksforgeeks.org/student-corner/" class="reduceMenuHeight">Students  ▼</a>
<ul class="sub-menu">
	<li id="menu-item-137183" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137183"><a href="http://www.geeksforgeeks.org/campus-ambassador-program-by-geeksforgeeks/" class="reduceMenuHeight">Campus Ambassador Program</a></li>
	<li id="menu-item-204869" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-204869"><a href="https://www.geeksforgeeks.org/computer-science-projects/" class="reduceMenuHeight">Project</a></li>
	<li id="menu-item-137179" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137179"><a href="http://www.geeksforgeeks.org/geek-of-the-month/" class="reduceMenuHeight">Geek of the Month</a></li>
	<li id="menu-item-137570" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137570"><a href="http://geeksquiz.com/placements/" class="reduceMenuHeight">Placement Course</a></li>
	<li id="menu-item-137180" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137180"><a href="http://www.geeksforgeeks.org/category/competitive-programming/" class="reduceMenuHeight">Competitive Programming</a></li>
	<li id="menu-item-137181" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137181"><a href="http://www.geeksforgeeks.org/testimonials/" class="reduceMenuHeight">Testimonials</a></li>
	<li id="menu-item-138863" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-138863"><a href="http://www.geeksforgeeks.org/category/geek-on-the-top/" class="reduceMenuHeight">Geek on the Top</a></li>
	<li id="menu-item-141974" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-141974"><a href="http://www.geeksforgeeks.org/careers/" class="reduceMenuHeight">Careers</a></li>
	<li id="menu-item-137378" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137378"><a href="http://www.geeksforgeeks.org/internship/" class="reduceMenuHeight">Internship</a></li>
	<li id="menu-item-147457" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147457"><a href="http://www.geeksforgeeks.org/school-programming/" class="reduceMenuHeight">School Programming</a></li>
</ul>
</li>
<li id="menu-item-146712" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146712"><a href="https://www.geeksforgeeks.org/gate-cs-notes-gq/" class="reduceMenuHeight">GATE ▼</a>
<ul class="sub-menu">
	<li id="menu-item-146714" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146714"><a href="http://www.geeksforgeeks.org/gate-cs-notes-gq/" class="reduceMenuHeight">GATE Notes</a></li>
	<li id="menu-item-146713" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146713"><a href="http://www.geeksforgeeks.org/gate-corner-2-gq/" class="reduceMenuHeight">GATE CS Corner</a></li>
	<li id="menu-item-146715" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146715"><a href="http://www.geeksforgeeks.org/lmns-gq/" class="reduceMenuHeight">Last Minute Notes</a></li>
	<li id="menu-item-146716" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146716"><a href="http://www.geeksforgeeks.org/original-gate-previous-year-question-papers-cse-and-it-gq/" class="reduceMenuHeight">Official Papers</a></li>
	<li id="menu-item-211327" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-211327"><a href="https://www.geeksforgeeks.org/ugc-net-cs-preparation/" class="reduceMenuHeight">UGC NET Papers</a></li>
	<li id="menu-item-211326" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-211326"><a href="https://www.geeksforgeeks.org/isro-cs-preparation/" class="reduceMenuHeight">ISRO CS Exam</a></li>
	<li id="menu-item-211328" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-211328"><a href="https://www.geeksforgeeks.org/ugc-net-cs-notes-according-to-syllabus-of-paper-ii/" class="reduceMenuHeight">UGC NET Notes</a></li>
	<li id="menu-item-146717" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146717"><a href="https://www.geeksforgeeks.org/gate-cs-2019-important-dates-and-links/" class="reduceMenuHeight">GATE 2019</a></li>
</ul>
</li>
<li id="menu-item-146718" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146718"><a href="http://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/" class="reduceMenuHeight">CS Subjects ▼</a>
<ul class="sub-menu">
	<li id="menu-item-203861" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-203861"><a href="https://www.geeksforgeeks.org/gate-cs-notes-gq/" class="reduceMenuHeight">Core Subjects  ►</a>
	<ul class="sub-menu">
		<li id="menu-item-146727" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146727"><a href="http://www.geeksforgeeks.org/engineering-mathematics-tutorials/" class="reduceMenuHeight">Engg. Mathematics</a></li>
		<li id="menu-item-146729" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146729"><a href="http://www.geeksforgeeks.org/operating-systems/" class="reduceMenuHeight">Operating Systems</a></li>
		<li id="menu-item-146721" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146721"><a href="http://www.geeksforgeeks.org/computer-network-tutorials/" class="reduceMenuHeight">Computer Networks</a></li>
		<li id="menu-item-146724" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146724"><a href="http://www.geeksforgeeks.org/dbms/" class="reduceMenuHeight">DBMS</a></li>
		<li id="menu-item-146720" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146720"><a href="http://www.geeksforgeeks.org/compiler-design-tutorials/" class="reduceMenuHeight">Compiler Design</a></li>
		<li id="menu-item-146730" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146730"><a href="http://www.geeksforgeeks.org/theory-of-computation-automata-tutorials/" class="reduceMenuHeight">Theory of Computation</a></li>
		<li id="menu-item-146726" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146726"><a href="http://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/" class="reduceMenuHeight">Digital Electronics</a></li>
		<li id="menu-item-146722" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146722"><a href="http://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/" class="reduceMenuHeight">Computer Organization &amp; Architecture</a></li>
		<li id="menu-item-200760" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-200760"><a href="https://www.geeksforgeeks.org/microprocessor-tutorials/" class="reduceMenuHeight">Microprocessor</a></li>
	</ul>
</li>
	<li id="menu-item-147831" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147831"><a href="http://www.geeksforgeeks.org/web-technology/" class="reduceMenuHeight">Web Technology</a></li>
	<li id="menu-item-147512" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-147512"><a href="http://www.geeksforgeeks.org/advanced-computer-subjects-tutorials/" class="reduceMenuHeight">Advanced Topics</a></li>
	<li id="menu-item-203862" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-203862"><a href="https://www.geeksforgeeks.org/machine-learning/" class="reduceMenuHeight">Machine Learning</a></li>
	<li id="menu-item-204870" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-204870"><a href="https://www.geeksforgeeks.org/computer-graphics-2/" class="reduceMenuHeight">Computer Graphics</a></li>
	<li id="menu-item-146725" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146725"><a href="http://www.geeksforgeeks.org/category/geeksquiz/articles-gq/difference-gq/" class="reduceMenuHeight">What’s Difference?</a></li>
</ul>
</li>
<li id="menu-item-140855" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-140855"><a href="http://quiz.geeksforgeeks.org/quiz-corner/" class="reduceMenuHeight">Quizzes ▼</a>
<ul class="sub-menu">
	<li id="menu-item-146748" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146748"><a href="http://www.geeksforgeeks.org/quizzes-on-programming-languages-gq/" class="reduceMenuHeight">Languages ►</a>
	<ul class="sub-menu">
		<li id="menu-item-146743" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146743"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#C%20Programming%20Mock%20Tests" class="reduceMenuHeight">C</a></li>
		<li id="menu-item-146745" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146745"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#C++%20Programming%20Mock%20Tests" class="reduceMenuHeight">C++</a></li>
		<li id="menu-item-146746" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146746"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Java%20Programming%20Mock%20Tests" class="reduceMenuHeight">Java</a></li>
		<li id="menu-item-146747" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146747"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Python%20Programming%20Mock%20Tests" class="reduceMenuHeight">Python</a></li>
	</ul>
</li>
	<li id="menu-item-146825" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-146825"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests" class="reduceMenuHeight">CS Subjectwise ►</a>
	<ul class="sub-menu">
		<li id="menu-item-146731" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146731"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests" class="reduceMenuHeight">Data Structures</a></li>
		<li id="menu-item-146732" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146732"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Algorithms%20Mock%20Tests" class="reduceMenuHeight">Algorithms</a></li>
		<li id="menu-item-146733" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146733"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Operating%20Systems%20Mock%20Tests" class="reduceMenuHeight">Operating Systems</a></li>
		<li id="menu-item-146734" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146734"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#DBMS%20Mock%20Tests" class="reduceMenuHeight">DBMS</a></li>
		<li id="menu-item-146735" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146735"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Compiler%20Design%20Mock%20Tests" class="reduceMenuHeight">Compiler Design</a></li>
		<li id="menu-item-146736" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146736"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Networks%20Mock%20Tests" class="reduceMenuHeight">Computer Networks</a></li>
		<li id="menu-item-146737" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146737"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Theory%20of%20Computation%20Mock%20Tests" class="reduceMenuHeight">Theory of Computation</a></li>
		<li id="menu-item-146738" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146738"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Organization%20and%20Architecture" class="reduceMenuHeight">Computer Organization</a></li>
		<li id="menu-item-146739" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146739"><a href="http://www.geeksforgeeks.org/software-engineering-gq/" class="reduceMenuHeight">Software Engineering</a></li>
	</ul>
</li>
	<li id="menu-item-146740" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146740"><a href="http://www.geeksforgeeks.org/html-and-xml-gq/" class="reduceMenuHeight">HTML &amp; XML</a></li>
	<li id="menu-item-146741" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146741"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Engineering%20Mathematics" class="reduceMenuHeight">Engg. Mathematics</a></li>
	<li id="menu-item-146742" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-146742"><a href="http://www.geeksforgeeks.org/quiz-corner-gq/#Aptitude%20Mock%20Tests" class="reduceMenuHeight">Aptitude</a></li>
</ul>
</li>
<li id="menu-item-135367" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-135367"><a href="https://www.geeksforgeeks.org/category/guestblogs/" class="reduceMenuHeight">GBlog</a></li>
<li id="menu-item-141885" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-141885"><a href="http://www.geeksforgeeks.org/puzzles/" class="reduceMenuHeight">Puzzles</a></li>
<li id="menu-item-141816" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-141816"><a href="https://www.geeksforgeeks.org/whats-new/" class="reduceMenuHeight">What’s New?</a></li>
</ul><select class="selectnav" id="selectnav1"><option value="" selected="selected">Menu</option><option value="https://www.geeksforgeeks.org/"></option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">Algo ▼</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/#AnalysisofAlgorithms">- Analysis of Algorithms</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">- Topicwise ►</option><option value="http://www.geeksforgeeks.org/searching-algorithms/">-- Searching Algorithms</option><option value="http://www.geeksforgeeks.org/sorting-algorithms/">-- Sorting Algorithms</option><option value="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/">-- Graph Algorithms</option><option value="http://www.geeksforgeeks.org/bitwise-algorithms/">-- Bit Algorithms</option><option value="https://www.geeksforgeeks.org/algorithms-gq/pattern-searching/">-- Pattern Searching</option><option value="http://www.geeksforgeeks.org/geometric-algorithms/">-- Geometric Algorithms</option><option value="http://www.geeksforgeeks.org/mathematical-algorithms/">-- Mathematical Algorithms</option><option value="http://www.geeksforgeeks.org/randomized-algorithms/">-- Randomized Algorithms</option><option value="https://www.geeksforgeeks.org/game-theory/">-- Game Theory</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">- Algorithm Paradigms ►</option><option value="http://www.geeksforgeeks.org/greedy-algorithms/">-- Greedy Algorithms</option><option value="http://www.geeksforgeeks.org/dynamic-programming/">-- Dynamic Programming</option><option value="http://www.geeksforgeeks.org/divide-and-conquer/">-- Divide and Conquer</option><option value="http://www.geeksforgeeks.org/backtracking-algorithms/">-- Backtracking</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/#BranchandBound">-- Branch &amp; Bound</option><option value="http://www.geeksforgeeks.org/fundamentals-of-algorithms/">- All Algorithms</option><option value="http://www.geeksforgeeks.org/data-structures/">DS  ▼</option><option value="http://www.geeksforgeeks.org/array-data-structure/">- Array</option><option value="http://www.geeksforgeeks.org/data-structures/linked-list/">- LinkedList</option><option value="http://www.geeksforgeeks.org/stack-data-structure/">- Stack</option><option value="http://www.geeksforgeeks.org/queue-data-structure/">- Queue</option><option value="http://www.geeksforgeeks.org/data-structures/">- Tree based DS ►</option><option value="http://www.geeksforgeeks.org/binary-tree-data-structure/">-- Binary Tree</option><option value="http://www.geeksforgeeks.org/binary-search-tree-data-structure/">-- Binary Search Tree</option><option value="http://www.geeksforgeeks.org/heap-data-structure/">-- Heap</option><option value="http://www.geeksforgeeks.org/hashing-data-structure/">- Hashing</option><option value="http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/">- Graph</option><option value="http://www.geeksforgeeks.org/advanced-data-structures/">- Advanced Data Structure</option><option value="http://www.geeksforgeeks.org/matrix/">- Matrix</option><option value="http://www.geeksforgeeks.org/string-data-structure/">- Strings</option><option value="http://www.geeksforgeeks.org/data-structures/">- All Data Structures</option><option value="http://www.geeksforgeeks.org/category/program-output/">Languages ▼</option><option value="https://www.geeksforgeeks.org/c-programming-language/">- C</option><option value="https://www.geeksforgeeks.org/c-plus-plus/">- C++</option><option value="https://www.geeksforgeeks.org/java/">- Java</option><option value="https://www.geeksforgeeks.org/python-programming-language/">- Python</option><option value="http://www.geeksforgeeks.org/sql-tutorial/">- SQL</option><option value="https://www.geeksforgeeks.org/php/">- PHP</option><option value="https://www.geeksforgeeks.org/javascript-tutorial/">- Javascript</option><option value="https://www.geeksforgeeks.org/category/program-output/">- Program Output</option><option value="http://www.geeksforgeeks.org/about/interview-corner/">Interview  ▼</option><option value="https://www.geeksforgeeks.org/company-preparation/">- Company Prep</option><option value="http://www.geeksforgeeks.org/interview-preparation-for-software-developer/">- Top Topics</option><option value="https://practice.geeksforgeeks.org/company-tags">- Practice Company Questions</option><option value="http://www.geeksforgeeks.org/about/interview-corner/">- Interview Experiences</option><option value="https://www.geeksforgeeks.org/experienced-interview-experiences-company-wise/">- Experienced Interviews</option><option value="https://www.geeksforgeeks.org/internship-interview-experiences-company-wise/">- Internship Interviews</option><option value="http://www.geeksforgeeks.org/category/competitive-programming/">- Competitive Programming</option><option value="http://www.geeksforgeeks.org/software-design-patterns/">- Design Patterns</option><option value="http://geeksquiz.com/quiz-corner/">- Multiple Choice Quizzes</option><option value="http://www.geeksforgeeks.org/student-corner/">Students  ▼</option><option value="http://www.geeksforgeeks.org/campus-ambassador-program-by-geeksforgeeks/">- Campus Ambassador Program</option><option value="https://www.geeksforgeeks.org/computer-science-projects/">- Project</option><option value="http://www.geeksforgeeks.org/geek-of-the-month/">- Geek of the Month</option><option value="http://geeksquiz.com/placements/">- Placement Course</option><option value="http://www.geeksforgeeks.org/category/competitive-programming/">- Competitive Programming</option><option value="http://www.geeksforgeeks.org/testimonials/">- Testimonials</option><option value="http://www.geeksforgeeks.org/category/geek-on-the-top/">- Geek on the Top</option><option value="http://www.geeksforgeeks.org/careers/">- Careers</option><option value="http://www.geeksforgeeks.org/internship/">- Internship</option><option value="http://www.geeksforgeeks.org/school-programming/">- School Programming</option><option value="https://www.geeksforgeeks.org/gate-cs-notes-gq/">GATE ▼</option><option value="http://www.geeksforgeeks.org/gate-cs-notes-gq/">- GATE Notes</option><option value="http://www.geeksforgeeks.org/gate-corner-2-gq/">- GATE CS Corner</option><option value="http://www.geeksforgeeks.org/lmns-gq/">- Last Minute Notes</option><option value="http://www.geeksforgeeks.org/original-gate-previous-year-question-papers-cse-and-it-gq/">- Official Papers</option><option value="https://www.geeksforgeeks.org/ugc-net-cs-preparation/">- UGC NET Papers</option><option value="https://www.geeksforgeeks.org/isro-cs-preparation/">- ISRO CS Exam</option><option value="https://www.geeksforgeeks.org/ugc-net-cs-notes-according-to-syllabus-of-paper-ii/">- UGC NET Notes</option><option value="https://www.geeksforgeeks.org/gate-cs-2019-important-dates-and-links/">- GATE 2019</option><option value="http://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/">CS Subjects ▼</option><option value="https://www.geeksforgeeks.org/gate-cs-notes-gq/">- Core Subjects  ►</option><option value="http://www.geeksforgeeks.org/engineering-mathematics-tutorials/">-- Engg. Mathematics</option><option value="http://www.geeksforgeeks.org/operating-systems/">-- Operating Systems</option><option value="http://www.geeksforgeeks.org/computer-network-tutorials/">-- Computer Networks</option><option value="http://www.geeksforgeeks.org/dbms/">-- DBMS</option><option value="http://www.geeksforgeeks.org/compiler-design-tutorials/">-- Compiler Design</option><option value="http://www.geeksforgeeks.org/theory-of-computation-automata-tutorials/">-- Theory of Computation</option><option value="http://www.geeksforgeeks.org/digital-electronics-logic-design-tutorials/">-- Digital Electronics</option><option value="http://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/">-- Computer Organization &amp; Architecture</option><option value="https://www.geeksforgeeks.org/microprocessor-tutorials/">-- Microprocessor</option><option value="http://www.geeksforgeeks.org/web-technology/">- Web Technology</option><option value="http://www.geeksforgeeks.org/advanced-computer-subjects-tutorials/">- Advanced Topics</option><option value="https://www.geeksforgeeks.org/machine-learning/">- Machine Learning</option><option value="https://www.geeksforgeeks.org/computer-graphics-2/">- Computer Graphics</option><option value="http://www.geeksforgeeks.org/category/geeksquiz/articles-gq/difference-gq/">- What’s Difference?</option><option value="http://quiz.geeksforgeeks.org/quiz-corner/">Quizzes ▼</option><option value="http://www.geeksforgeeks.org/quizzes-on-programming-languages-gq/">- Languages ►</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#C%20Programming%20Mock%20Tests">-- C</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#C++%20Programming%20Mock%20Tests">-- C++</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Java%20Programming%20Mock%20Tests">-- Java</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Python%20Programming%20Mock%20Tests">-- Python</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests">- CS Subjectwise ►</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Data%20Structures%20Mock%20Tests">-- Data Structures</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Algorithms%20Mock%20Tests">-- Algorithms</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Operating%20Systems%20Mock%20Tests">-- Operating Systems</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#DBMS%20Mock%20Tests">-- DBMS</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Compiler%20Design%20Mock%20Tests">-- Compiler Design</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Networks%20Mock%20Tests">-- Computer Networks</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Theory%20of%20Computation%20Mock%20Tests">-- Theory of Computation</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Computer%20Organization%20and%20Architecture">-- Computer Organization</option><option value="http://www.geeksforgeeks.org/software-engineering-gq/">-- Software Engineering</option><option value="http://www.geeksforgeeks.org/html-and-xml-gq/">- HTML &amp; XML</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Engineering%20Mathematics">- Engg. Mathematics</option><option value="http://www.geeksforgeeks.org/quiz-corner-gq/#Aptitude%20Mock%20Tests">- Aptitude</option><option value="https://www.geeksforgeeks.org/category/guestblogs/">GBlog</option><option value="http://www.geeksforgeeks.org/puzzles/">Puzzles</option><option value="https://www.geeksforgeeks.org/whats-new/">What’s New?</option></select></div>		</nav><!-- #site-navigation -->
		<div class="clear"></div>
	<!-- #masthead -->
<button id="scrollTopBtn" title="Scroll to Top" type="button" class="btn btn-success" style="display: inline-block; opacity: 1;">▲</button>
	<div id="main" class="wrapper">

<!-- Following 2 files are included for Article Feedback Project 'GFGSW-556' -->
<link href="ratinmaze_files/icon.css" rel="stylesheet">
<script src="ratinmaze_files/materialize.js"></script>

<div class="leftSideBarParent">
    <div class="leftSideBar">
        <div class="eventSection"><a class="eventLink" href="https://practice.geeksforgeeks.org/courses/SudoPlacement/">Sudo Placement</a></div><div class="menuDivForLeftbar" style="position: fixed; left: 10px; background-color: rgb(75, 184, 106); padding: 5px; top: 10px; z-index: 1000;"><div class="bar1"></div><div class="bar2"></div><div class="bar3"></div></div><span class="leftbarDataSpan" data-pid="13376" data-lid="40" data-type="post" data-termid="1748"></span><div class="quickLink_S" data-termid="-30">
    <div class="quickLink-header_S">Quick Links for Backtracking</div>
    <table>
        <tbody>
            <tr>
                <td><a href="https://www.geeksforgeeks.org/category/algorithm/backtracking/">Recent Articles</a></td>
            </tr>
            <tr>
                <td><a href="https://www.geeksforgeeks.org/top-20-backtracking-algorithm-interview-questions/">Top 20 Interview Questions</a></td>
            </tr>
            <tr>
                <td><a href="https://practice.geeksforgeeks.org/topics/backtracking/">Practice Problems </a></td>
            </tr>
            <tr>
                <td><a href="https://www.geeksforgeeks.org/algorithms-gq/backtracking-gq/">Quizzes</a></td>
            </tr>
            <tr>
                <td><a href="https://www.youtube.com/playlist?list=PLqM7alHXFySFbuucq7lC8ecRoWZxq1qS5">Videos</a></td>
            </tr>
        </tbody>
    </table>
    <div class="quickLink_S">
        <table>
            <tbody>
                <tr>
                    <td class="quickLink-header_S"><b>Standard Problems :</b></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/">The Knight’s tour problem </a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/">Rat in a Maze | Set 1</a> &amp; <a href="https://www.geeksforgeeks.org/rat-in-a-maze-with-multiple-steps-jump-allowed/">Multiple step | Set 2 </a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/">N Queen Problem | Set 1</a> &amp; <a href="https://www.geeksforgeeks.org/n-queen-in-on-space/">O(n) space | Set 2</a> </td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backttracking-set-4-subset-sum/">Subset Sum</a> &amp; <a href="https://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/">m Coloring Problem</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/">Hamiltonian Cycle</a> &amp; <a href="https://www.geeksforgeeks.org/backtracking-set-7-suduku/">Sudoku</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backtracking-set-8-solving-cryptarithmetic-puzzles/">Solving Cryptarithmetic Puzzles</a> &amp; <a href="https://www.geeksforgeeks.org/backtracking-set-9-magnet-puzzle/">Magnet Puzzle</a></td>
                </tr>

                <tr>
                    <td><a href="https://www.geeksforgeeks.org/boggle-set-2-using-trie/">Boggle</a> &amp; <a href="https://www.geeksforgeeks.org/backtracking-approach-generate-n-bit-gray-codes/">Generate n bit Gray Codes</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/remove-invalid-parentheses/">Remove Invalid Parentheses</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/prime-numbers-after-prime-p-with-sum-s/">Prime numbers after prime P with sum S</a> </td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/c-code-article-backtracking-set-8-solving-cryptarithmetic-puzzles/"> Solving Cryptarithmetic Puzzles</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/">Print all permutations of a given string</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/">Print all possible paths from top left to bottom right of a mXn matrix</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backtracking-algorithms/#standard">Explore more...</a></td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="quickLink_S">
        <table>
            <tbody>
                <tr>
                    <td class="quickLink-header_S"><b>Misc :</b></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/tug-of-war/">Tug of War </a> &amp; <a href="https://www.geeksforgeeks.org/8-queen-problem/">8 queen problem</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/combinational-sum/">Combinational sum</a> &amp; <a href="https://www.geeksforgeeks.org/backtracking-to-find-all-subsets/">Backtracking to find all subsets</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/powet-set-lexicographic-order/">Power Set in Lexicographic order</a> &amp; <a href="https://www.geeksforgeeks.org/check-given-string-sum-string/">Check if a given string is sum-string</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/fill-grid-1-8-numbers/">Fill 8 numbers in grid with given conditions</a> &amp; <a href="https://www.geeksforgeeks.org/word-break-problem-using-backtracking/">Word Break Problem</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/minimize-number-unique-characters-string/">Minimize number of unique characters in string</a> &amp; <a href="https://www.geeksforgeeks.org/count-possible-paths-two-vertices/">Count all possible paths between two vertices</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/">Partition of a set into K subsets with equal sum</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/warnsdorffs-algorithm-knights-tour-problem/">Warnsdorff’s algorithm for Knight’s tour problem</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/">Longest Possible Route in a Matrix with Hurdles</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/">Match a pattern and String without using regular expressions</a> &amp; <a href="https://www.geeksforgeeks.org/fill-two-instances-numbers-1-n-specific-way/">Fill two instances of all numbers from 1 to n in a specific way</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/find-distinct-subsets-given-set/">Find all distinct subsets of a given set</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/">Shortest safe route in a path with landmines</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/find-paths-from-corner-cell-to-middle-cell-in-maze/">Paths from corner cell to middle cell in maze</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/">Find if there is a path of more than k length from a source</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/">Find Maximum number possible by doing at-most K swaps</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/print-palindromic-partitions-string/">Print all palindromic partitions of a string</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/">Printing all solutions in N-Queen Problem</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/find-paths-given-source-destination/">Print all paths from a given source to a destination</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/print-possible-strings-can-made-placing-spaces/">Print all possible strings that can be made by placing spaces | Set 1</a> &amp; <a href="https://www.geeksforgeeks.org/print-possible-strings-can-made-placing-spaces-2/">Set 2</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/print-longest-common-sub-sequences-lexicographical-order/">Print all longest common sub-sequences in lexicographical order
</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/smallest-expression-represent-number-using-single-digit/">Smallest expression to represent a number using single digit</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/">Given an array A[] and a number x, check for pair in A[] with sum as x</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/combinations-every-element-appears-twice-distance-appearances-equal-value/">Combinations where every element appears twice and distance between appearances is equal to the value</a></td>
                </tr>
                <tr>
                    <td><a href="https://www.geeksforgeeks.org/backtracking-algorithms/#misc">Explore more...</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>    </div>
</div>
	<div id="primary" class="site-content">
		<div id="content" role="main">
                        							 	<article id="post-13376" class="post-13376 post type-post status-publish format-standard hentry category-backtracking category-matrix tag-amazon tag-drishti-soft tag-expedia tag-flipkart tag-grofers tag-makemytrip tag-numerify tag-paytm tag-yatra-com tag-zycus">
				<header class="entry-header">
						<h1 class="entry-title">Backtracking | Set 2 (Rat in a Maze)</h1>
				
						</header><!-- .entry-header -->

				<div class="entry-content">
			<p>We have discussed Backtracking and Knight’s tour problem in <a href="https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/" rel="noopener" target="_blank">Set 1</a>.  Let us discuss Rat in a <a href="http://en.wikipedia.org/wiki/Maze" rel="noopener" target="_blank">Maze </a>as another example problem that can be solved using Backtracking.<span id="more-13376"></span></p>
<p>A Maze is given as N*N binary matrix of blocks where source block is 
the upper left most block i.e., maze[0][0] and destination block is 
lower rightmost block i.e., maze[N-1][N-1].  A rat starts from source 
and has to reach the destination. The rat can move only in two 
directions: forward and down.<br>
In the maze matrix, 0 means the block is a dead end and 1 means the 
block can be used in the path from source to destination. Note that this
 is a simple version of the typical Maze problem. For example, a more 
complex version can be that the rat can move in 4 directions and a more 
complex version can be with a limited number of moves.</p>
<p>Following is an example maze.</p><br>
        <script async="" src="ratinmaze_files/adsbygoogle.js"></script>
          <!-- post_top_responsive -->
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9465609616171866" data-ad-slot="4501693235" data-ad-format="auto"></ins>
          <script>
          (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
        <br>
            
<pre> Gray blocks are dead ends (value = 0). </pre>
<p><a href="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled11.png"><img src="ratinmaze_files/ratinmaze_filled11.png" alt="" title="ratinmaze_filled1" class="aligncenter size-full wp-image-13423" srcset="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled11.png 363w, https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled11-300x260.png 300w" sizes="(max-width: 181px) 100vw, 181px" width="181" height="157"></a></p>
<p>Following is binary matrix representation of the above maze.</p>
<pre>                {1, 0, 0, 0}
                {1, 1, 0, 1}
                {0, 1, 0, 0}
                {1, 1, 1, 1}
</pre>
<p>Following is a maze with highlighted solution path.</p>
<p><a href="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled_path1.png"><img src="ratinmaze_files/ratinmaze_filled_path1.png" alt="" title="ratinmaze_filled_path" class="aligncenter size-full wp-image-13424" srcset="https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled_path1.png 353w, https://www.geeksforgeeks.org/wp-content/uploads/ratinmaze_filled_path1-300x267.png 300w" sizes="(max-width: 176px) 100vw, 176px" width="176" height="157"></a></p><br>
        <script async="" src="ratinmaze_files/adsbygoogle.js"></script>
          <!-- post_top_responsive -->
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9465609616171866" data-ad-slot="4501693235" data-ad-format="auto"></ins>
          <script>
          (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
        <br>
            
<p>Following is the solution matrix (output of program) for the above input matrx.</p>
<pre>                {1, 0, 0, 0}
                {1, 1, 0, 0}
                {0, 1, 0, 0}
                {0, 1, 1, 1}
 All enteries in solution path are marked as 1.
</pre>
<div id="practiceLinkDiv">
<h2><a href="https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1">Recommended: Please solve it on “<b><i><u>PRACTICE</u></i></b>” first, before moving on to the solution.</a></h2>
</div>
<p><strong>Naive Algorithm</strong><br>
The Naive Algorithm is to generate all paths from source to destination 
and one by one check if the generated path satisfies the constraints.</p>
<pre>while there are untried paths
{
   generate the next path
   if this path has all blocks as 1
   {
      print this path;
   }
}</pre>
<p><strong>Backtracking Algorithm</strong></p>
<pre>If destination is reached
    print the solution matrix
Else
   a) Mark current cell in solution matrix as 1. 
   b) Move forward in the horizontal direction and recursively check if this 
       move leads to a solution. 
   c) If the move chosen in the above step doesn't lead to a solution
       then move down and check if this move leads to a solution. 
   d) If none of the above solutions works then unmark this cell as 0 
       (BACKTRACK) and return false.
</pre>
<p><strong>Implementation of Backtracking solution</strong><br>
</p><div class="responsive-tabs-wrapper"><div class="responsive-tabs responsive-tabs--enabled"><ul class="responsive-tabs__list" role="tablist"><li class="responsive-tabs__list__item" id="tablist1-tab1" aria-controls="tablist1-panel1" role="tab" tabindex="0">C/C++</li><li class="responsive-tabs__list__item" id="tablist1-tab2" aria-controls="tablist1-panel2" role="tab" tabindex="0">Java</li><li class="responsive-tabs__list__item responsive-tabs__list__item--active" id="tablist1-tab3" aria-controls="tablist1-panel3" role="tab" tabindex="0">Python3</li></ul>
<h2 class="tabtitle responsive-tabs__heading" tabindex="0">C/C++</h2>
<div class="tabcontent responsive-tabs__panel" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab1" id="tablist1-panel1" style="display: none;">
<p></p>
<div><div id="highlighter_421367" class="syntaxhighlighter nogutter  c"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="c comments">/* C/C++ program to solve Rat in a Maze problem using</code></div><div class="line number2 index1 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;</code><code class="c comments">backtracking */</code></div><div class="line number3 index2 alt2"><code class="c preprocessor">#include&lt;stdio.h&gt;</code></div><div class="line number4 index3 alt1">&nbsp;</div><div class="line number5 index4 alt2"><code class="c comments">// Maze size</code></div><div class="line number6 index5 alt1"><code class="c preprocessor">#define N 4 </code></div><div class="line number7 index6 alt2">&nbsp;</div><div class="line number8 index7 alt1"><code class="c color1 bold">bool</code> <code class="c plain">solveMazeUtil(</code><code class="c color1 bold">int</code> <code class="c plain">maze[N][N], </code><code class="c color1 bold">int</code> <code class="c plain">x, </code><code class="c color1 bold">int</code> <code class="c plain">y, </code><code class="c color1 bold">int</code> <code class="c plain">sol[N][N]);</code></div><div class="line number9 index8 alt2">&nbsp;</div><div class="line number10 index9 alt1"><code class="c comments">/* A utility function to print solution matrix sol[N][N] */</code></div><div class="line number11 index10 alt2"><code class="c keyword bold">void</code> <code class="c plain">printSolution(</code><code class="c color1 bold">int</code> <code class="c plain">sol[N][N])</code></div><div class="line number12 index11 alt1"><code class="c plain">{</code></div><div class="line number13 index12 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">for</code> <code class="c plain">(</code><code class="c color1 bold">int</code> <code class="c plain">i = 0; i &lt; N; i++)</code></div><div class="line number14 index13 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{</code></div><div class="line number15 index14 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">for</code> <code class="c plain">(</code><code class="c color1 bold">int</code> <code class="c plain">j = 0; j &lt; N; j++)</code></div><div class="line number16 index15 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c functions bold">printf</code><code class="c plain">(</code><code class="c string">" %d "</code><code class="c plain">, sol[i][j]);</code></div><div class="line number17 index16 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c functions bold">printf</code><code class="c plain">(</code><code class="c string">"\n"</code><code class="c plain">);</code></div><div class="line number18 index17 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">}</code></div><div class="line number19 index18 alt2"><code class="c plain">}</code></div><div class="line number20 index19 alt1">&nbsp;</div><div class="line number21 index20 alt2"><code class="c comments">/* A utility function to check if x,y is valid index for N*N maze */</code></div><div class="line number22 index21 alt1"><code class="c color1 bold">bool</code> <code class="c plain">isSafe(</code><code class="c color1 bold">int</code> <code class="c plain">maze[N][N], </code><code class="c color1 bold">int</code> <code class="c plain">x, </code><code class="c color1 bold">int</code> <code class="c plain">y)</code></div><div class="line number23 index22 alt2"><code class="c plain">{</code></div><div class="line number24 index23 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">// if (x,y outside maze) return false</code></div><div class="line number25 index24 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">if</code><code class="c plain">(x &gt;= 0 &amp;&amp; x &lt; N &amp;&amp; y &gt;= 0 &amp;&amp; y &lt; N &amp;&amp; maze[x][y] == 1)</code></div><div class="line number26 index25 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">true</code><code class="c plain">;</code></div><div class="line number27 index26 alt2">&nbsp;</div><div class="line number28 index27 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">false</code><code class="c plain">;</code></div><div class="line number29 index28 alt2"><code class="c plain">}</code></div><div class="line number30 index29 alt1">&nbsp;</div><div class="line number31 index30 alt2 highlighted"><code class="c comments">/* This function solves the Maze problem using Backtracking.&nbsp; It mainly</code></div><div class="line number32 index31 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;</code><code class="c comments">uses solveMazeUtil() to solve the problem. It returns false if no </code></div><div class="line number33 index32 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;</code><code class="c comments">path is possible, otherwise return true and prints the path in the</code></div><div class="line number34 index33 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;</code><code class="c comments">form of 1s. Please note that there may be more than one solutions, </code></div><div class="line number35 index34 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;</code><code class="c comments">this function prints one of the feasible solutions.*/</code></div><div class="line number36 index35 alt1 highlighted"><code class="c color1 bold">bool</code> <code class="c plain">solveMaze(</code><code class="c color1 bold">int</code> <code class="c plain">maze[N][N])</code></div><div class="line number37 index36 alt2 highlighted"><code class="c plain">{</code></div><div class="line number38 index37 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c color1 bold">int</code> <code class="c plain">sol[N][N] = { {0, 0, 0, 0},</code></div><div class="line number39 index38 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{0, 0, 0, 0},</code></div><div class="line number40 index39 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{0, 0, 0, 0},</code></div><div class="line number41 index40 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{0, 0, 0, 0}</code></div><div class="line number42 index41 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">};</code></div><div class="line number43 index42 alt2 highlighted">&nbsp;</div><div class="line number44 index43 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">if</code><code class="c plain">(solveMazeUtil(maze, 0, 0, sol) == </code><code class="c keyword bold">false</code><code class="c plain">)</code></div><div class="line number45 index44 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{</code></div><div class="line number46 index45 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c functions bold">printf</code><code class="c plain">(</code><code class="c string">"Solution doesn't exist"</code><code class="c plain">);</code></div><div class="line number47 index46 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">false</code><code class="c plain">;</code></div><div class="line number48 index47 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">}</code></div><div class="line number49 index48 alt2 highlighted">&nbsp;</div><div class="line number50 index49 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">printSolution(sol);</code></div><div class="line number51 index50 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">true</code><code class="c plain">;</code></div><div class="line number52 index51 alt1 highlighted"><code class="c plain">}</code></div><div class="line number53 index52 alt2 highlighted">&nbsp;</div><div class="line number54 index53 alt1 highlighted"><code class="c comments">/* A recursive utility function to solve Maze problem */</code></div><div class="line number55 index54 alt2 highlighted"><code class="c color1 bold">bool</code> <code class="c plain">solveMazeUtil(</code><code class="c color1 bold">int</code> <code class="c plain">maze[N][N], </code><code class="c color1 bold">int</code> <code class="c plain">x, </code><code class="c color1 bold">int</code> <code class="c plain">y, </code><code class="c color1 bold">int</code> <code class="c plain">sol[N][N])</code></div><div class="line number56 index55 alt1 highlighted"><code class="c plain">{</code></div><div class="line number57 index56 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">// if (x,y is goal) return true</code></div><div class="line number58 index57 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">if</code><code class="c plain">(x == N-1 &amp;&amp; y == N-1)</code></div><div class="line number59 index58 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{</code></div><div class="line number60 index59 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">sol[x][y] = 1;</code></div><div class="line number61 index60 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">true</code><code class="c plain">;</code></div><div class="line number62 index61 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">}</code></div><div class="line number63 index62 alt2 highlighted">&nbsp;</div><div class="line number64 index63 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">// Check if maze[x][y] is valid</code></div><div class="line number65 index64 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">if</code><code class="c plain">(isSafe(maze, x, y) == </code><code class="c keyword bold">true</code><code class="c plain">)</code></div><div class="line number66 index65 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{</code></div><div class="line number67 index66 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">// mark x,y as part of solution path</code></div><div class="line number68 index67 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">sol[x][y] = 1;</code></div><div class="line number69 index68 alt2 highlighted">&nbsp;</div><div class="line number70 index69 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">/* Move forward in x direction */</code></div><div class="line number71 index70 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">if</code> <code class="c plain">(solveMazeUtil(maze, x+1, y, sol) == </code><code class="c keyword bold">true</code><code class="c plain">)</code></div><div class="line number72 index71 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">true</code><code class="c plain">;</code></div><div class="line number73 index72 alt2 highlighted">&nbsp;</div><div class="line number74 index73 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">/* If moving in x direction doesn't give solution then</code></div><div class="line number75 index74 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">Move down in y direction&nbsp; */</code></div><div class="line number76 index75 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">if</code> <code class="c plain">(solveMazeUtil(maze, x, y+1, sol) == </code><code class="c keyword bold">true</code><code class="c plain">)</code></div><div class="line number77 index76 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">true</code><code class="c plain">;</code></div><div class="line number78 index77 alt1 highlighted">&nbsp;</div><div class="line number79 index78 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">/* If none of the above movements work then BACKTRACK: </code></div><div class="line number80 index79 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c comments">unmark x,y as part of solution path */</code></div><div class="line number81 index80 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">sol[x][y] = 0;</code></div><div class="line number82 index81 alt1 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">false</code><code class="c plain">;</code></div><div class="line number83 index82 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">}&nbsp;&nbsp; </code></div><div class="line number84 index83 alt1 highlighted">&nbsp;</div><div class="line number85 index84 alt2 highlighted"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c keyword bold">false</code><code class="c plain">;</code></div><div class="line number86 index85 alt1 highlighted"><code class="c plain">}</code></div><div class="line number87 index86 alt2">&nbsp;</div><div class="line number88 index87 alt1"><code class="c comments">// driver program to test above function</code></div><div class="line number89 index88 alt2"><code class="c color1 bold">int</code> <code class="c plain">main()</code></div><div class="line number90 index89 alt1"><code class="c plain">{</code></div><div class="line number91 index90 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c color1 bold">int</code> <code class="c plain">maze[N][N]&nbsp; =&nbsp; { {1, 0, 0, 0},</code></div><div class="line number92 index91 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{1, 1, 0, 1},</code></div><div class="line number93 index92 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{0, 1, 0, 0},</code></div><div class="line number94 index93 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">{1, 1, 1, 1}</code></div><div class="line number95 index94 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">};</code></div><div class="line number96 index95 alt1">&nbsp;</div><div class="line number97 index96 alt2"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c plain">solveMaze(maze);</code></div><div class="line number98 index97 alt1"><code class="c spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="c keyword bold">return</code> <code class="c plain">0;</code></div><div class="line number99 index98 alt2"><code class="c plain">}</code></div></div></td></tr></tbody></table><button class="runIdeBtn" onclick="redirect( 'highlighter_421367', 'c' )">Run on IDE</button></div></div>

</div><h2 class="tabtitle responsive-tabs__heading" tabindex="0">Java</h2>
<div class="tabcontent responsive-tabs__panel" style="display: none;" aria-hidden="true" role="tabpanel" aria-labelledby="tablist1-tab2" id="tablist1-panel2">

<div><div id="highlighter_68316" class="syntaxhighlighter nogutter  java"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="java comments">/* Java program to solve Rat in a Maze problem using</code></div><div class="line number2 index1 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;</code><code class="java comments">backtracking */</code></div><div class="line number3 index2 alt2">&nbsp;</div><div class="line number4 index3 alt1"><code class="java keyword">public</code> <code class="java keyword">class</code> <code class="java plain">RatMaze</code></div><div class="line number5 index4 alt2"><code class="java plain">{</code></div><div class="line number6 index5 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">final</code> <code class="java keyword">int</code> <code class="java plain">N = </code><code class="java value">4</code><code class="java plain">;</code></div><div class="line number7 index6 alt2">&nbsp;</div><div class="line number8 index7 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* A utility function to print solution matrix</code></div><div class="line number9 index8 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">sol[N][N] */</code></div><div class="line number10 index9 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">void</code> <code class="java plain">printSolution(</code><code class="java keyword">int</code> <code class="java plain">sol[][])</code></div><div class="line number11 index10 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number12 index11 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">for</code> <code class="java plain">(</code><code class="java keyword">int</code> <code class="java plain">i = </code><code class="java value">0</code><code class="java plain">; i &lt; N; i++)</code></div><div class="line number13 index12 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number14 index13 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">for</code> <code class="java plain">(</code><code class="java keyword">int</code> <code class="java plain">j = </code><code class="java value">0</code><code class="java plain">; j &lt; N; j++)</code></div><div class="line number15 index14 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">System.out.print(</code><code class="java string">" "</code> <code class="java plain">+ sol[i][j] +</code></div><div class="line number16 index15 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java string">" "</code><code class="java plain">);</code></div><div class="line number17 index16 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">System.out.println();</code></div><div class="line number18 index17 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number19 index18 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number20 index19 alt1">&nbsp;</div><div class="line number21 index20 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* A utility function to check if x,y is valid</code></div><div class="line number22 index21 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">index for N*N maze */</code></div><div class="line number23 index22 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">boolean</code> <code class="java plain">isSafe(</code><code class="java keyword">int</code> <code class="java plain">maze[][], </code><code class="java keyword">int</code> <code class="java plain">x, </code><code class="java keyword">int</code> <code class="java plain">y)</code></div><div class="line number24 index23 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number25 index24 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">// if (x,y outside maze) return false</code></div><div class="line number26 index25 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java plain">(x &gt;= </code><code class="java value">0</code> <code class="java plain">&amp;&amp; x &lt; N &amp;&amp; y &gt;= </code><code class="java value">0</code> <code class="java plain">&amp;&amp;</code></div><div class="line number27 index26 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">y &lt; N &amp;&amp; maze[x][y] == </code><code class="java value">1</code><code class="java plain">);</code></div><div class="line number28 index27 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number29 index28 alt2">&nbsp;</div><div class="line number30 index29 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* This function solves the Maze problem using</code></div><div class="line number31 index30 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">Backtracking. It mainly uses solveMazeUtil()</code></div><div class="line number32 index31 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">to solve the problem. It returns false if no</code></div><div class="line number33 index32 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">path is possible, otherwise return true and</code></div><div class="line number34 index33 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">prints the path in the form of 1s. Please note</code></div><div class="line number35 index34 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">that there may be more than one solutions, this</code></div><div class="line number36 index35 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">function prints one of the feasible solutions.*/</code></div><div class="line number37 index36 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">boolean</code> <code class="java plain">solveMaze(</code><code class="java keyword">int</code> <code class="java plain">maze[][])</code></div><div class="line number38 index37 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number39 index38 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">int</code> <code class="java plain">sol[][] = {{</code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">},</code></div><div class="line number40 index39 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">},</code></div><div class="line number41 index40 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">},</code></div><div class="line number42 index41 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">}</code></div><div class="line number43 index42 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">};</code></div><div class="line number44 index43 alt1 highlighted">&nbsp;</div><div class="line number45 index44 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">if</code> <code class="java plain">(solveMazeUtil(maze, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, sol) == </code><code class="java keyword">false</code><code class="java plain">)</code></div><div class="line number46 index45 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number47 index46 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">System.out.print(</code><code class="java string">"Solution doesn't exist"</code><code class="java plain">);</code></div><div class="line number48 index47 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">false</code><code class="java plain">;</code></div><div class="line number49 index48 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number50 index49 alt1 highlighted">&nbsp;</div><div class="line number51 index50 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">printSolution(sol);</code></div><div class="line number52 index51 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">true</code><code class="java plain">;</code></div><div class="line number53 index52 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number54 index53 alt1 highlighted">&nbsp;</div><div class="line number55 index54 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* A recursive utility function to solve Maze</code></div><div class="line number56 index55 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">problem */</code></div><div class="line number57 index56 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">boolean</code> <code class="java plain">solveMazeUtil(</code><code class="java keyword">int</code> <code class="java plain">maze[][], </code><code class="java keyword">int</code> <code class="java plain">x, </code><code class="java keyword">int</code> <code class="java plain">y,</code></div><div class="line number58 index57 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">int</code> <code class="java plain">sol[][])</code></div><div class="line number59 index58 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number60 index59 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">// if (x,y is goal) return true</code></div><div class="line number61 index60 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">if</code> <code class="java plain">(x == N - </code><code class="java value">1</code> <code class="java plain">&amp;&amp; y == N - </code><code class="java value">1</code><code class="java plain">)</code></div><div class="line number62 index61 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number63 index62 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">sol[x][y] = </code><code class="java value">1</code><code class="java plain">;</code></div><div class="line number64 index63 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">true</code><code class="java plain">;</code></div><div class="line number65 index64 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number66 index65 alt1 highlighted">&nbsp;</div><div class="line number67 index66 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">// Check if maze[x][y] is valid</code></div><div class="line number68 index67 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">if</code> <code class="java plain">(isSafe(maze, x, y) == </code><code class="java keyword">true</code><code class="java plain">)</code></div><div class="line number69 index68 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number70 index69 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">// mark x,y as part of solution path</code></div><div class="line number71 index70 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">sol[x][y] = </code><code class="java value">1</code><code class="java plain">;</code></div><div class="line number72 index71 alt1 highlighted">&nbsp;</div><div class="line number73 index72 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* Move forward in x direction */</code></div><div class="line number74 index73 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">if</code> <code class="java plain">(solveMazeUtil(maze, x + </code><code class="java value">1</code><code class="java plain">, y, sol))</code></div><div class="line number75 index74 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">true</code><code class="java plain">;</code></div><div class="line number76 index75 alt1 highlighted">&nbsp;</div><div class="line number77 index76 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* If moving in x direction doesn't give</code></div><div class="line number78 index77 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">solution then&nbsp; Move down in y direction */</code></div><div class="line number79 index78 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">if</code> <code class="java plain">(solveMazeUtil(maze, x, y + </code><code class="java value">1</code><code class="java plain">, sol))</code></div><div class="line number80 index79 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">true</code><code class="java plain">;</code></div><div class="line number81 index80 alt2 highlighted">&nbsp;</div><div class="line number82 index81 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">/* If none of the above movements works then</code></div><div class="line number83 index82 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">BACKTRACK: unmark x,y as part of solution</code></div><div class="line number84 index83 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java comments">path */</code></div><div class="line number85 index84 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">sol[x][y] = </code><code class="java value">0</code><code class="java plain">;</code></div><div class="line number86 index85 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">false</code><code class="java plain">;</code></div><div class="line number87 index86 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number88 index87 alt1 highlighted">&nbsp;</div><div class="line number89 index88 alt2 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">return</code> <code class="java keyword">false</code><code class="java plain">;</code></div><div class="line number90 index89 alt1 highlighted"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number91 index90 alt2">&nbsp;</div><div class="line number92 index91 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">public</code> <code class="java keyword">static</code> <code class="java keyword">void</code> <code class="java plain">main(String args[])</code></div><div class="line number93 index92 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code></div><div class="line number94 index93 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">RatMaze rat = </code><code class="java keyword">new</code> <code class="java plain">RatMaze();</code></div><div class="line number95 index94 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java keyword">int</code> <code class="java plain">maze[][] = {{</code><code class="java value">1</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">},</code></div><div class="line number96 index95 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code><code class="java value">1</code><code class="java plain">, </code><code class="java value">1</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">1</code><code class="java plain">},</code></div><div class="line number97 index96 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code><code class="java value">0</code><code class="java plain">, </code><code class="java value">1</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">, </code><code class="java value">0</code><code class="java plain">},</code></div><div class="line number98 index97 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">{</code><code class="java value">1</code><code class="java plain">, </code><code class="java value">1</code><code class="java plain">, </code><code class="java value">1</code><code class="java plain">, </code><code class="java value">1</code><code class="java plain">}</code></div><div class="line number99 index98 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">};</code></div><div class="line number100 index99 alt1"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">rat.solveMaze(maze);</code></div><div class="line number101 index100 alt2"><code class="java spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="java plain">}</code></div><div class="line number102 index101 alt1"><code class="java plain">}</code></div><div class="line number103 index102 alt2"><code class="java comments">// This code is contributed by Abhishek Shankhadhar</code></div></div></td></tr></tbody></table><button class="runIdeBtn" onclick="redirect( 'highlighter_68316', 'java' )">Run on IDE</button></div></div>

</div><h2 class="tabtitle responsive-tabs__heading responsive-tabs__heading--active" tabindex="0">Python3</h2>
<div class="tabcontent responsive-tabs__panel responsive-tabs__panel--active" style="display: block;" aria-hidden="false" role="tabpanel" aria-labelledby="tablist1-tab3" id="tablist1-panel3">

<div><div id="highlighter_816435" class="syntaxhighlighter nogutter  python3"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="python3 comments"># Python3 program to solve Rat in a Maze </code></div><div class="line number2 index1 alt1"><code class="python3 comments"># problem using backracking </code></div><div class="line number3 index2 alt2">&nbsp;</div><div class="line number4 index3 alt1"><code class="python3 comments"># Maze size</code></div><div class="line number5 index4 alt2"><code class="python3 plain">N </code><code class="python3 keyword">=</code> <code class="python3 value">4</code></div><div class="line number6 index5 alt1">&nbsp;</div><div class="line number7 index6 alt2"><code class="python3 comments"># A utility function to print solution matrix sol</code></div><div class="line number8 index7 alt1"><code class="python3 keyword">def</code> <code class="python3 plain">printSolution( sol ):</code></div><div class="line number9 index8 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number10 index9 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">for</code> <code class="python3 plain">i </code><code class="python3 keyword">in</code> <code class="python3 plain">sol:</code></div><div class="line number11 index10 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">for</code> <code class="python3 plain">j </code><code class="python3 keyword">in</code> <code class="python3 plain">i:</code></div><div class="line number12 index11 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 functions">print</code><code class="python3 plain">(</code><code class="python3 functions">str</code><code class="python3 plain">(j) </code><code class="python3 keyword">+</code> <code class="python3 string">" "</code><code class="python3 plain">, end</code><code class="python3 keyword">=</code><code class="python3 plain">"")</code></div><div class="line number13 index12 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 functions">print</code><code class="python3 plain">("")</code></div><div class="line number14 index13 alt1">&nbsp;</div><div class="line number15 index14 alt2"><code class="python3 comments"># A utility function to check if x,y is valid</code></div><div class="line number16 index15 alt1"><code class="python3 comments"># index for N*N Maze</code></div><div class="line number17 index16 alt2"><code class="python3 keyword">def</code> <code class="python3 plain">isSafe( maze, x, y ):</code></div><div class="line number18 index17 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number19 index18 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">if</code> <code class="python3 plain">x &gt;</code><code class="python3 keyword">=</code> <code class="python3 value">0</code> <code class="python3 keyword">and</code> <code class="python3 plain">x &lt; N </code><code class="python3 keyword">and</code> <code class="python3 plain">y &gt;</code><code class="python3 keyword">=</code> <code class="python3 value">0</code> <code class="python3 keyword">and</code> <code class="python3 plain">y &lt; N </code><code class="python3 keyword">and</code> <code class="python3 plain">maze[x][y] </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 value">1</code><code class="python3 plain">:</code></div><div class="line number20 index19 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">True</code></div><div class="line number21 index20 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number22 index21 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">False</code></div><div class="line number23 index22 alt2">&nbsp;</div><div class="line number24 index23 alt1 highlighted"><code class="python3 comments">""" This function solves the Maze problem using Backtracking. </code></div><div class="line number25 index24 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments">It mainly uses solveMazeUtil() to solve the problem. It </code></div><div class="line number26 index25 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments">returns false if no path is possible, otherwise return </code></div><div class="line number27 index26 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments">true and prints the path in the form of 1s. Please note</code></div><div class="line number28 index27 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments">that there may be more than one solutions, this function</code></div><div class="line number29 index28 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments">prints one of the feasable solutions. """</code></div><div class="line number30 index29 alt1 highlighted"><code class="python3 keyword">def</code> <code class="python3 plain">solveMaze( maze ):</code></div><div class="line number31 index30 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number32 index31 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># Creating a 4 * 4 2-D list</code></div><div class="line number33 index32 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">sol </code><code class="python3 keyword">=</code> <code class="python3 plain">[ [ </code><code class="python3 value">0</code> <code class="python3 keyword">for</code> <code class="python3 plain">j </code><code class="python3 keyword">in</code> <code class="python3 functions">range</code><code class="python3 plain">(</code><code class="python3 value">4</code><code class="python3 plain">) ] </code><code class="python3 keyword">for</code> <code class="python3 plain">i </code><code class="python3 keyword">in</code> <code class="python3 functions">range</code><code class="python3 plain">(</code><code class="python3 value">4</code><code class="python3 plain">) ]</code></div><div class="line number34 index33 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number35 index34 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">if</code> <code class="python3 plain">solveMazeUtil(maze, </code><code class="python3 value">0</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">, sol) </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 color1">False</code><code class="python3 plain">:</code></div><div class="line number36 index35 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 functions">print</code><code class="python3 plain">(</code><code class="python3 string">"Solution doesn't exist"</code><code class="python3 plain">);</code></div><div class="line number37 index36 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">False</code></div><div class="line number38 index37 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number39 index38 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">printSolution(sol)</code></div><div class="line number40 index39 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">True</code></div><div class="line number41 index40 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number42 index41 alt1 highlighted"><code class="python3 comments"># A recursive utility function to solve Maze problem</code></div><div class="line number43 index42 alt2 highlighted"><code class="python3 keyword">def</code> <code class="python3 plain">solveMazeUtil(maze, x, y, sol):</code></div><div class="line number44 index43 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number45 index44 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments">#if (x,y is goal) return True</code></div><div class="line number46 index45 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">if</code> <code class="python3 plain">x </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 plain">N </code><code class="python3 keyword">-</code> <code class="python3 value">1</code> <code class="python3 keyword">and</code> <code class="python3 plain">y </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 plain">N </code><code class="python3 keyword">-</code> <code class="python3 value">1</code><code class="python3 plain">:</code></div><div class="line number47 index46 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">sol[x][y] </code><code class="python3 keyword">=</code> <code class="python3 value">1</code></div><div class="line number48 index47 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">True</code></div><div class="line number49 index48 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number50 index49 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># Check if maze[x][y] is valid</code></div><div class="line number51 index50 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">if</code> <code class="python3 plain">isSafe(maze, x, y) </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 color1">True</code><code class="python3 plain">:</code></div><div class="line number52 index51 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># mark x, y as part of solution path</code></div><div class="line number53 index52 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">sol[x][y] </code><code class="python3 keyword">=</code> <code class="python3 value">1</code></div><div class="line number54 index53 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number55 index54 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># Move forward in x direction</code></div><div class="line number56 index55 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">if</code> <code class="python3 plain">solveMazeUtil(maze, x </code><code class="python3 keyword">+</code> <code class="python3 value">1</code><code class="python3 plain">, y, sol) </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 color1">True</code><code class="python3 plain">:</code></div><div class="line number57 index56 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">True</code></div><div class="line number58 index57 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number59 index58 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># If moving in x direction doesn't give solution </code></div><div class="line number60 index59 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># then Move down in y direction</code></div><div class="line number61 index60 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">if</code> <code class="python3 plain">solveMazeUtil(maze, x, y </code><code class="python3 keyword">+</code> <code class="python3 value">1</code><code class="python3 plain">, sol) </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 color1">True</code><code class="python3 plain">:</code></div><div class="line number62 index61 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">True</code></div><div class="line number63 index62 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number64 index63 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># If none of the above movements work then </code></div><div class="line number65 index64 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># BACKTRACK: unmark x,y as part of solution path</code></div><div class="line number66 index65 alt1 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">sol[x][y] </code><code class="python3 keyword">=</code> <code class="python3 value">0</code></div><div class="line number67 index66 alt2 highlighted"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 keyword">return</code> <code class="python3 color1">False</code></div><div class="line number68 index67 alt1">&nbsp;</div><div class="line number69 index68 alt2"><code class="python3 comments"># Driver program to test above function</code></div><div class="line number70 index69 alt1"><code class="python3 keyword">if</code> <code class="python3 plain">__name__ </code><code class="python3 keyword">=</code><code class="python3 keyword">=</code> <code class="python3 string">"__main__"</code><code class="python3 plain">:</code></div><div class="line number71 index70 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 comments"># Initialising the maze</code></div><div class="line number72 index71 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">maze </code><code class="python3 keyword">=</code> <code class="python3 plain">[ [</code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">],</code></div><div class="line number73 index72 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">[</code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">, </code><code class="python3 value">1</code><code class="python3 plain">],</code></div><div class="line number74 index73 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">[</code><code class="python3 value">0</code><code class="python3 plain">, </code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">, </code><code class="python3 value">0</code><code class="python3 plain">],</code></div><div class="line number75 index74 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">[</code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">1</code><code class="python3 plain">, </code><code class="python3 value">1</code><code class="python3 plain">] ]</code></div><div class="line number76 index75 alt1"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</code>&nbsp;</div><div class="line number77 index76 alt2"><code class="python3 spaces">&nbsp;&nbsp;&nbsp;&nbsp;</code><code class="python3 plain">solveMaze(maze)</code></div><div class="line number78 index77 alt1">&nbsp;</div><div class="line number79 index78 alt2"><code class="python3 comments"># This code is contributed by Shiv Shankar</code></div></div></td></tr></tbody></table><button class="runIdeBtn" onclick="redirect( 'highlighter_816435', 'python3' )">Run on IDE</button></div></div>
<p></p></div></div></div><br>
Output: The 1 values show the path for rat <p></p>
<pre> 1  0  0  0 
 1  1  0  0 
 0  1  0  0 
 0  1  1  1 </pre>
<div id="video">
<iframe src="ratinmaze_files/PwxGTHraMNg.html" allow="autoplay; encrypted-media" allowfullscreen="" width="665" height="374" frameborder="0"></iframe>
</div>
<p>Below is an extended version of this problem.<a href="https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/">Count number of ways to reach destination in a Maze</a></p>
<p>Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.</p>
<br><script async="" src="ratinmaze_files/adsbygoogle.js"></script>
          <!-- post_bottom_responsive -->
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9465609616171866" data-ad-slot="8385097921" data-ad-format="auto"></ins>
          <script>
          (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
          <br>
            <br><style>.no-p-tag p{display: none;}</style>&nbsp;<div class="no-p-tag" style="text-align:left;"><b style="color: #757575;">Practice Tags : </b> <div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Paytm">Paytm</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Amazon">Amazon</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Flipkart">Flipkart</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/MakeMyTrip">MakeMyTrip</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Yatra.com">Yatra.com</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Drishti-Soft">Drishti-Soft</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Zycus">Zycus</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Expedia">Expedia</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Grofers">Grofers</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/company/Numerify">Numerify</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/topics/Matrix">Matrix</a></div><div class="practiceButton"><a href="https://practice.geeksforgeeks.org/topics/Backtracking">Backtracking</a></div></div>
					
		<footer class="entry-meta">
    <span><b>Article Tags : </b><div class="practiceButton"><a href="https://www.geeksforgeeks.org/category/algorithm/backtracking/" rel="category tag">Backtracking</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/category/data-structures/matrix/" rel="category tag">Matrix</a></div></span><span><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/amazon/" rel="tag">Amazon</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/drishti-soft/" rel="tag">Drishti-Soft</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/expedia/" rel="tag">Expedia</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/flipkart/" rel="tag">Flipkart</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/grofers/" rel="tag">Grofers</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/makemytrip/" rel="tag">MakeMyTrip</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/numerify/" rel="tag">Numerify</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/paytm/" rel="tag">Paytm</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/yatra-com/" rel="tag">Yatra.com</a></div><div class="practiceButton"><a href="https://www.geeksforgeeks.org/tag/zycus/" rel="tag">Zycus</a></div></span>
           	<div id="improveArticle" style="float: right;cursor: pointer;"><a style="color:#060" href="https://auth.geeksforgeeks.org/?to=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/">Login to Improve this Article</a></div><div class="common-bottom">Please write to us at contribute@geeksforgeeks.org to report any issue with the above content.</div>          	
					</footer><!-- .entry-meta -->
	</div></article><!-- #post -->


<div style="font-size:15px; line-height:22px; margin-left:20px; color:green">

<h2 style="font-size:20px; color: #838383">Recommended Posts:</h2><br><ul><li><a href="https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/">Backtracking | Set 3 (N Queen Problem)</a></li><li><a href="https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/">Backtracking | Set 1 (The Knight’s tour problem)</a></li><li><a href="https://www.geeksforgeeks.org/backttracking-set-4-subset-sum/">Backtracking | Set 4 (Subset Sum)</a></li><li><a href="https://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/">Backtracking | Set 5 (m Coloring Problem)</a></li><li><a href="https://www.geeksforgeeks.org/backtracking-set-7-suduku/">Backtracking | Set 7 (Sudoku)</a></li><li><a href="https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/">Recursive program to generate power set</a></li><li><a href="https://www.geeksforgeeks.org/smallest-number-with-given-sum-of-digits-and-sum-of-square-of-digits/">Smallest number with given sum of digits and sum of square of digits</a></li><li><a href="https://www.geeksforgeeks.org/minimize-number-unique-characters-string/">Minimize number of unique characters in string</a></li><li><a href="https://www.geeksforgeeks.org/rat-in-a-maze-with-multiple-steps-jump-allowed/">Rat in a Maze with multiple steps or  jump allowed</a></li><li><a href="https://www.geeksforgeeks.org/fill-grid-1-8-numbers/">Fill 8 numbers in grid with given conditions</a></li></ul><br></div>


<!-- Added on 29 Oct 2015 for next and previous from same category -->
<nav class="nav-single">
					<div class="assistive-text">Post navigation</div>
					<span class="nav-previous"><a href="https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/" rel="prev">&lt;&lt; Previous Post</a></span>
					<span class="nav-next"><a href="https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/" rel="next">Next Post &gt;&gt;</a></span>
				</nav><!-- .nav-single -->
<!--
<script type="text/javascript">
	
				arrPost.push('');
	
		   <?php// } ?>

</script>
-->



<div class="plugins">
<div pid="13376" ptitle="Backtracking | Set 2 (Rat in a Maze)" id="ratePlugin"><div class="login">
            (<a href="https://auth.geeksforgeeks.org/?to=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/">Login</a> to Rate)
            <br><br>
            </div>
            <div class="techno">
            <span id="rating_box" class="avg-rating level-3">3.2</span>
            <span class="rating-desc"> Average Difficulty : <b id="diff-rating">3.2/5.0</b><br><span id="vote_count">Based on <b>142</b> vote(s)</span></span><br><br>
        <input rating="1" class="box basic" value="Basic" type="button">
        <input rating="2" class="box easy" value="Easy" type="button">
        <input rating="3" class="box medium" value="Medium" type="button">
        <input rating="4" class="box hard" value="Hard" type="button">
        <input rating="5" class="box expert" value="Expert" type="button">
        <br><span class="process"></span></div></div><div pid="13376" ptitle="Backtracking | Set 2 (Rat in a Maze)" id="markPlugin"><br>
      <br>
      <div class="lists">
      <input id="todo" class="mark" type="checkbox">
      <label class="checkbox" for="todo"> Add to TODO List </label>
      <br>
      <input id="done" class="mark" type="checkbox">
      <label class="checkbox" for="done"> Mark as DONE </label>
      </div></div><div pid="13376" ptitle="Backtracking | Set 2 (Rat in a Maze)" id="feedbackButtonDiv"><a href="https://auth.geeksforgeeks.org/?to=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/"><button class="feedbackButton">Login to Give Feedback</button></a></div></div>
<div id="author" name="GeeksforGeeks"></div>
<br><br>

<style type="text/css">
 
#share-buttons img {
width: 35px;
padding: 5px;
border: 0;
box-shadow: 0;
display: inline;
}
#share-buttons a:hover {
	text-decoration: none;
}
</style>


<div id="share-buttons" style="display:none">
   
    <!-- Facebook -->
    <a href="http://www.facebook.com/sharer.php?u=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/" target="_blank" title="Share on Facebook">
        <img src="ratinmaze_files/facebook.png" alt="Facebook">
    </a>
    
    <!-- Google+ -->
    <a href="https://plus.google.com/share?url=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/" target="_blank" title="Share on Google">
        <img src="ratinmaze_files/google.png" alt="Google">
    </a>
    
    <!-- LinkedIn -->
    <a href="http://www.linkedin.com/shareArticle?mini=true&amp;url=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/" target="_blank" title="Share on LinkedIn">
        <img src="ratinmaze_files/linkedin.png" alt="LinkedIn">
    </a>
    
    <!-- Twitter -->
    <a href="https://twitter.com/share?url=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/&amp;text=Backtracking%20|%20Set%202%20(Rat%20in%20a%20Maze)&amp;hashtags=GeeksforGeeks" target="_blank" title="Share on Twitter">
        <img src="ratinmaze_files/twitter.png" alt="Twitter">
    </a>

    <!-- Pinterest -->
    <a href="javascript:void((function()%7Bvar%20e=document.createElement('script');e.setAttribute('type','text/javascript');e.setAttribute('charset','UTF-8');e.setAttribute('src','http://assets.pinterest.com/js/pinmarklet.js?r='+Math.random()*99999999);document.body.appendChild(e)%7D)());" title="Share on Pinterest">
        <img src="ratinmaze_files/pinterest.png" alt="Pinterest">
    </a>
    
    <!-- Reddit -->
    <a href="http://reddit.com/submit?url=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/&amp;title=Backtracking%20|%20Set%202%20(Rat%20in%20a%20Maze)" target="_blank" title="Share on Reddit">
        <img src="ratinmaze_files/reddit.png" alt="Reddit">
    </a>
    
    <!-- StumbleUpon-->
    <a href="http://www.stumbleupon.com/submit?url=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/&amp;title=Backtracking%20|%20Set%202%20(Rat%20in%20a%20Maze)" target="_blank" title="Share on StumbleUpon">
        <img src="ratinmaze_files/stumbleupon.png" alt="StumbleUpon">
    </a>
    
    <!-- Tumblr-->
    <a href="http://www.tumblr.com/share/link?url=https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/&amp;title=Backtracking%20|%20Set%202%20(Rat%20in%20a%20Maze)" target="_blank" title="Share on Tumblr">
        <img src="ratinmaze_files/tumblr.png" alt="Tumblr">
    </a>
   
</div>

<br><br>
<div id="ide_link">
<p>Writing code in comment? Please use <a href="https://ide.geeksforgeeks.org/">ide.geeksforgeeks.org</a>, generate link and share the link here.</p>
</div>
<br>
<div style="display:flex">
<button id="comment" class="action-button" style="width: 45%; cursor: pointer; margin-right: 10%; box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 5px 0px, rgba(0, 0, 0, 0) 0px 6px 20px 0px; border-color: rgb(76, 185, 107); border-radius: 4px; display: none;">Load Comments</button>
<button id="share" class="action-button" onclick="document.getElementById('share-buttons').style.display='block';this.style.display='none';" style="width:45%;cursor: pointer;margin-right:10%;box-shadow: 0 2px 5px 0 rgba(0,0,0,0.4), 0 6px 20px 0 rgba(0,0,0,0);border-color: #4cb96b;border-radius: 4px;">Share this post!</button>

</div>

<div id="disqus_thread"><iframe id="dsq-app5814" name="dsq-app5814" allowtransparency="true" scrolling="no" tabindex="0" title="Disqus" style="width: 1px !important; min-width: 100% !important; border: medium none !important; overflow: hidden !important; height: 8899px !important;" src="ratinmaze_files/a.html" horizontalscrolling="no" verticalscrolling="no" width="100%" frameborder="0"></iframe></div>

					</div><!-- #content -->
	</div><!-- #primary -->


			<div id="secondary" class="widget-area" role="complementary">
			<aside id="text-2" class="widget widget_text">			<div class="textwidget"><script async="" src="ratinmaze_files/adsbygoogle.js"></script>
<!-- Big 300x600 Sidebar -->
<ins class="adsbygoogle" style="display:inline-block;width:300px;height:600px" data-ad-client="ca-pub-9465609616171866" data-ad-slot="4402736037"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</aside><aside id="text-3" class="widget widget_text">			<div class="textwidget"><div class="trendings_gfg">
					<table width="100%" align="center">
						<thead>
							<tr>
								<th style="border:1px solid #6AA84F;background-color:#4CB96B;color:#fff;text-align: center;font-size: 16px;">Trending Content</th>
							</tr>
						</thead>
						<tbody>

<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">


							<a href="https://www.geeksforgeeks.org/python-list/">Python List</a>,  <a href="https://www.geeksforgeeks.org/sets-in-python/">Set</a>, <a href="https://www.geeksforgeeks.org/tuples-in-python/">Tuple</a> &amp; <a href="https://www.geeksforgeeks.org/python-dictionary/">Dictionary</a>
				</td>
					</tr>		

<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">


							<a href="https://www.geeksforgeeks.org/number-theory-interesting-facts-and-algorithms/">Number Theory</a>
				</td>
					</tr>			
	
<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">
							<a href="https://www.geeksforgeeks.org/set-to-array-in-java/">Set to Array in Java</a>

						</td>
					</tr>			
												<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">


							<a href="http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/">BFS</a>, 	<a href="http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/">DFS </a>

						</td>
					</tr>					<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">

							<a href="http://www.geeksforgeeks.org/school-programming/">School Programming</a>

						</td>
					</tr>					<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">
							<a href="http://www.geeksforgeeks.org/longest-repeated-subsequence/">Longest Repeated Subsequence</a>
						</td>
					</tr>					<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">
							<a href="http://www.geeksforgeeks.org/dynamic-programming-set-12-longest-palindromic-subsequence/">Longest Palindromic Subsequence</a>
						</td>
					</tr>					<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">
							<a href="http://www.geeksforgeeks.org/detect-negative-cycle-graph-bellman-ford/">Detect a negative cycle.</a>
						</td>
					</tr>							<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">
							<a href="http://www.geeksforgeeks.org/gate-cs-notes-gq/">GATE CS Notes</a>
						</td>
					</tr>								<tr>
						<td style="border:1px solid #6AA84F;padding:2px;">
							<a href="http://www.geeksforgeeks.org/reverse-a-linked-list/">Reverse a linked list</a>

						</td>
					</tr>
						</tbody>
					</table>
				</div></div>
		</aside><aside id="text-4" class="widget widget_text">			<div class="textwidget"><script async="" src="ratinmaze_files/adsbygoogle.js"></script>
<!-- ResponsiveRightBarMay16 -->
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9465609616171866" data-ad-slot="7089558833" data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</aside><aside id="text-5" class="widget widget_text">			<div class="textwidget"><table width="100%" align="center">
    <thead>
        <tr>
            <th style="border:1px solid #6AA84F;background-color:#4CB96B;color:#fff;text-align: center;font-size: 16px;line-height:1.7;">
                Most Visited Posts
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/">Top 10 Algorithms and Data Structures for Competitive Programming</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/">Top 10 algorithms in Interview Questions</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/how-to-begin-with-competitive-programming/">How to begin with Competitive Programming?</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/a-complete-step-by-step-guide-for-placement-preparation-by-geeksforgeeks/">Step by Step Guide for Placement Preparation</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/how-to-prepare-for-acm-icpc/">How to prepare for ACM-ICPC?</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://quiz.geeksforgeeks.org/insertion-sort/">Insertion Sort</a>,
                <a href="http://geeksquiz.com/binary-search/">Binary Search</a>,
                <a href="http://geeksquiz.com/quick-sort/">QuickSort</a>,
                <a href="http://geeksquiz.com/merge-sort/">MergeSort</a>,
                <a href="http://geeksquiz.com/heap-sort/">HeapSort</a>
            </td>
        </tr>
    </tbody>
</table></div>
		</aside><aside id="text-7" class="widget widget_text">			<div class="textwidget"><script async="" src="ratinmaze_files/adsbygoogle.js"></script>
<!-- GfGSideBottomResponsive -->
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9465609616171866" data-ad-slot="5749413230" data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>
		</aside><aside id="text-6" class="widget widget_text">			<div class="textwidget"><table width="100%" align="center">
    <thead>
        <tr>
            <th style="border:1px solid #6AA84F;background-color:#4CB96B;color:#fff;text-align: center;font-size: 16px;line-height:1.7;">
                Popular Categories
            </th>
        </tr>
    </thead>
    <tbody>

        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/interview-experiences/">Interview Experiences</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/advanced-data-structures/">Advanced Data Structures</a>
            </td>
        </tr>

        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/dynamic-programming/">Dynamic Programming</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/greedy/">Greedy Algorithms</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/backtracking/">Backtracking</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/pattern-searching/">Pattern Searching</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/divide-and-conquer/">Divide &amp; Conquer</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/algorithm/geometric/">Geometric Algorithms</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/searching/">Searching</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/sorting/">Sorting</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/algorithm/analysis/">Analysis of Algorithms</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/algorithm/mathematical/">Mathematical Algorithms</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/algorithm/randomized/">Randomized Algorithms</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/tag/recursion">Recursion</a>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">
                <a href="http://www.geeksforgeeks.org/category/algorithm/game-theory/">Game Theory</a>
            </td>
</tr><tr>
            <td style="border:1px solid #6AA84F;padding:2px;line-height:1.7;font-size:13px;">							<a href="http://www.geeksforgeeks.org/tag/statistical-algorithms/">Statistical Algorithms</a>            </td>

        </tr>

    </tbody>
</table></div>
		</aside><aside id="text-8" class="widget widget_text">			<div class="textwidget"><!-- BuySellAds Zone Code -->
<div id="bsap_1306934" class="bsarocks bsap_785bf45b162de1c5511e8baa02854e5c"></div>
<!-- End BuySellAds Zone Code --></div>
		</aside><aside id="tag_cloud-3" class="widget widget_tag_cloud"><p class="widget-title">Tags</p><div class="tagcloud"><a href="https://www.geeksforgeeks.org/category/advanced-data-structure/" class="tag-cloud-link tag-link-1762 tag-link-position-1" style="font-size: 8.6422018348624pt;" aria-label="Advanced Data Structure (209 items)">Advanced Data Structure</a>
<a href="https://www.geeksforgeeks.org/tag/amazon/" class="tag-cloud-link tag-link-1942 tag-link-position-2" style="font-size: 16.348623853211pt;" aria-label="Amazon (838 items)">Amazon</a>
<a href="https://www.geeksforgeeks.org/category/quizzes-gq/aptitude-gq/" class="tag-cloud-link tag-link-2200 tag-link-position-3" style="font-size: 10.05504587156pt;" aria-label="Aptitude (270 items)">Aptitude</a>
<a href="https://www.geeksforgeeks.org/tag/aptitude/" class="tag-cloud-link tag-link-2159 tag-link-position-4" style="font-size: 10.311926605505pt;" aria-label="Aptitude (279 items)">Aptitude</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/c-arrays/" class="tag-cloud-link tag-link-3 tag-link-position-5" style="font-size: 18.275229357798pt;" aria-label="Arrays (1,167 items)">Arrays</a>
<a href="https://www.geeksforgeeks.org/category/algorithm/bit-magic/" class="tag-cloud-link tag-link-17 tag-link-position-6" style="font-size: 11.211009174312pt;" aria-label="Bit Magic (330 items)">Bit Magic</a>
<a href="https://www.geeksforgeeks.org/tag/c/" class="tag-cloud-link tag-link-2138 tag-link-position-7" style="font-size: 12.238532110092pt;" aria-label="C (401 items)">C</a>
<a href="https://www.geeksforgeeks.org/category/programming-language/c/" class="tag-cloud-link tag-link-2064 tag-link-position-8" style="font-size: 14.935779816514pt;" aria-label="C (650 items)">C</a>
<a href="https://www.geeksforgeeks.org/category/programming-language/cpp/" class="tag-cloud-link tag-link-2065 tag-link-position-9" style="font-size: 17.247706422018pt;" aria-label="C++ (972 items)">C++</a>
<a href="https://www.geeksforgeeks.org/category/computer-subject/computer-networks/" class="tag-cloud-link tag-link-2051 tag-link-position-10" style="font-size: 9.1559633027523pt;" aria-label="Computer Networks (228 items)">Computer Networks</a>
<a href="https://www.geeksforgeeks.org/category/quizzes-gq/computer-science-quizzes-gq/c-gq/" class="tag-cloud-link tag-link-2206 tag-link-position-11" style="font-size: 10.183486238532pt;" aria-label="C Quiz (275 items)">C Quiz</a>
<a href="https://www.geeksforgeeks.org/category/algorithm/dynamic-programming/" class="tag-cloud-link tag-link-1746 tag-link-position-12" style="font-size: 12.752293577982pt;" aria-label="Dynamic Programming (435 items)">Dynamic Programming</a>
<a href="https://www.geeksforgeeks.org/category/guestblogs/" class="tag-cloud-link tag-link-1710 tag-link-position-13" style="font-size: 11.853211009174pt;" aria-label="GBlog (371 items)">GBlog</a>
<a href="https://www.geeksforgeeks.org/category/algorithm/geometric/" class="tag-cloud-link tag-link-1754 tag-link-position-14" style="font-size: 8.256880733945pt;" aria-label="Geometric (192 items)">Geometric</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/graph/" class="tag-cloud-link tag-link-2068 tag-link-position-15" style="font-size: 9.5412844036697pt;" aria-label="Graph (243 items)">Graph</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/hash/" class="tag-cloud-link tag-link-1756 tag-link-position-16" style="font-size: 10.56880733945pt;" aria-label="Hash (292 items)">Hash</a>
<a href="https://www.geeksforgeeks.org/category/interview-experiences/internship-interview-experiences/" class="tag-cloud-link tag-link-1794 tag-link-position-17" style="font-size: 8.3853211009174pt;" aria-label="Internship (197 items)">Internship</a>
<a href="https://www.geeksforgeeks.org/category/interview-experiences/" class="tag-cloud-link tag-link-1140 tag-link-position-18" style="font-size: 22pt;" aria-label="Interview Experiences (2,315 items)">Interview Experiences</a>
<a href="https://www.geeksforgeeks.org/category/quizzes-gq/isro/" class="tag-cloud-link tag-link-2805 tag-link-position-19" style="font-size: 16.605504587156pt;" aria-label="ISRO (876 items)">ISRO</a>
<a href="https://www.geeksforgeeks.org/category/programming-language/java/" class="tag-cloud-link tag-link-2058 tag-link-position-20" style="font-size: 19.302752293578pt;" aria-label="Java (1,405 items)">Java</a>
<a href="https://www.geeksforgeeks.org/tag/java-collections/" class="tag-cloud-link tag-link-1896 tag-link-position-21" style="font-size: 8.3853211009174pt;" aria-label="Java-Collections (198 items)">Java-Collections</a>
<a href="https://www.geeksforgeeks.org/tag/java-util-package/" class="tag-cloud-link tag-link-2074 tag-link-position-22" style="font-size: 8.8990825688073pt;" aria-label="Java - util package (218 items)">Java - util package</a>
<a href="https://www.geeksforgeeks.org/category/javascript/" class="tag-cloud-link tag-link-2629 tag-link-position-23" style="font-size: 11.339449541284pt;" aria-label="JavaScript (336 items)">JavaScript</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/linked-list/" class="tag-cloud-link tag-link-8 tag-link-position-24" style="font-size: 10.825688073394pt;" aria-label="Linked List (306 items)">Linked List</a>
<a href="https://www.geeksforgeeks.org/category/algorithm/mathematical/" class="tag-cloud-link tag-link-1753 tag-link-position-25" style="font-size: 19.174311926606pt;" aria-label="Mathematical (1,389 items)">Mathematical</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/matrix/" class="tag-cloud-link tag-link-1760 tag-link-position-26" style="font-size: 11.082568807339pt;" aria-label="Matrix (326 items)">Matrix</a>
<a href="https://www.geeksforgeeks.org/tag/microsoft/" class="tag-cloud-link tag-link-104 tag-link-position-27" style="font-size: 12.110091743119pt;" aria-label="Microsoft (386 items)">Microsoft</a>
<a href="https://www.geeksforgeeks.org/tag/php/" class="tag-cloud-link tag-link-2654 tag-link-position-28" style="font-size: 13.266055045872pt;" aria-label="PHP (478 items)">PHP</a>
<a href="https://www.geeksforgeeks.org/tag/php-function/" class="tag-cloud-link tag-link-2803 tag-link-position-29" style="font-size: 9.0275229357798pt;" aria-label="PHP-function (224 items)">PHP-function</a>
<a href="https://www.geeksforgeeks.org/category/program-output/" class="tag-cloud-link tag-link-5 tag-link-position-30" style="font-size: 8.3853211009174pt;" aria-label="Program Output (198 items)">Program Output</a>
<a href="https://www.geeksforgeeks.org/category/puzzles/" class="tag-cloud-link tag-link-2063 tag-link-position-31" style="font-size: 8pt;" aria-label="Puzzles (185 items)">Puzzles</a>
<a href="https://www.geeksforgeeks.org/category/programming-language/python/" class="tag-cloud-link tag-link-1789 tag-link-position-32" style="font-size: 16.990825688073pt;" aria-label="Python (930 items)">Python</a>
<a href="https://www.geeksforgeeks.org/category/quizzes-gq/qa-placement-quizzes-gq/" class="tag-cloud-link tag-link-2204 tag-link-position-33" style="font-size: 10.311926605505pt;" aria-label="QA - Placement Quizzes (284 items)">QA - Placement Quizzes</a>
<a href="https://www.geeksforgeeks.org/tag/qa-placement-quizzes/" class="tag-cloud-link tag-link-2187 tag-link-position-34" style="font-size: 10.311926605505pt;" aria-label="QA - Placement Quizzes (284 items)">QA - Placement Quizzes</a>
<a href="https://www.geeksforgeeks.org/category/school-programming/" class="tag-cloud-link tag-link-2078 tag-link-position-35" style="font-size: 14.036697247706pt;" aria-label="School Programming (549 items)">School Programming</a>
<a href="https://www.geeksforgeeks.org/category/algorithm/searching/" class="tag-cloud-link tag-link-1751 tag-link-position-36" style="font-size: 9.6697247706422pt;" aria-label="Searching (248 items)">Searching</a>
<a href="https://www.geeksforgeeks.org/tag/series/" class="tag-cloud-link tag-link-1919 tag-link-position-37" style="font-size: 9.6697247706422pt;" aria-label="series (252 items)">series</a>
<a href="https://www.geeksforgeeks.org/category/algorithm/sorting/" class="tag-cloud-link tag-link-1752 tag-link-position-38" style="font-size: 12.366972477064pt;" aria-label="Sorting (410 items)">Sorting</a>
<a href="https://www.geeksforgeeks.org/tag/stl/" class="tag-cloud-link tag-link-1797 tag-link-position-39" style="font-size: 13.651376146789pt;" aria-label="STL (509 items)">STL</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/c-strings/" class="tag-cloud-link tag-link-7 tag-link-position-40" style="font-size: 16.348623853211pt;" aria-label="Strings (830 items)">Strings</a>
<a href="https://www.geeksforgeeks.org/tag/system-programming/" class="tag-cloud-link tag-link-2533 tag-link-position-41" style="font-size: 8pt;" aria-label="system-programming (185 items)">system-programming</a>
<a href="https://www.geeksforgeeks.org/category/technical-scripter/" class="tag-cloud-link tag-link-1788 tag-link-position-42" style="font-size: 11.981651376147pt;" aria-label="Technical Scripter (376 items)">Technical Scripter</a>
<a href="https://www.geeksforgeeks.org/category/data-structures/tree/" class="tag-cloud-link tag-link-19 tag-link-position-43" style="font-size: 13.266055045872pt;" aria-label="Tree (475 items)">Tree</a>
<a href="https://www.geeksforgeeks.org/category/quizzes-gq/ugc-net/" class="tag-cloud-link tag-link-2806 tag-link-position-44" style="font-size: 16.733944954128pt;" aria-label="UGC-NET (887 items)">UGC-NET</a>
<a href="https://www.geeksforgeeks.org/category/web-technologies/" class="tag-cloud-link tag-link-2628 tag-link-position-45" style="font-size: 14.935779816514pt;" aria-label="Web Technologies (640 items)">Web Technologies</a></div>
</aside><aside id="text-9" class="widget widget_text">			<div class="textwidget"><!-- BuySellAds Zone Code -->
<div id="bsap_1304848" class="bsarocks bsap_785bf45b162de1c5511e8baa02854e5c"></div>
<!-- End BuySellAds Zone Code --></div>
		</aside><aside id="text-10" class="widget widget_text">			<div class="textwidget"><a href="http://www.geeksforgeeks.org/recent-comments/" style="margin-right: 0px !important;">
  <center>
    <input value="Recent Comments" style="background-color: #4cb96b; color:white; width:100%; font-size:large; cursor:pointer;font-weight:bold;" type="button">
  </center>
</a></div>
		</aside>		</div><!-- #secondary -->
		</div><!-- #main .wrapper -->
  <footer>
    <div id="container-g4g-footer">

        <div id="footer">
            <div class="logo">
                <ul class="gfg-logo-ul">
                    <li>
                      <a href="https://www.geeksforgeeks.org/">
                        <img src="ratinmaze_files/GeeksforGeeksLogoFooterSmall.png" alt="GeeksforGeeks">
                      </a>
                    </li>
                </ul>
                <ul class="social-ul">
                    <li>710-B, Advant Navis Business Park,</li>
                    <li>Sector-142, Noida, Uttar Pradesh - 201305</li>
        <li>feedback@geeksforgeeks.org</li>
                </ul>
                
            </div>
            <div class="footer-column">
                <ul>
                    <li><b>COMPANY</b></li>
                    <li><a href="https://www.geeksforgeeks.org/about/">About Us</a></li>
                    <li><a href="https://www.geeksforgeeks.org/careers/">Careers</a></li>
                    <li><a href="https://www.geeksforgeeks.org/privacy-policy/">Privacy Policy</a></li>
                    <li><a href="https://www.geeksforgeeks.org/about/contact-us/">Contact Us</a></li>
                </ul>
            </div>


            <div class="footer-column">
                <ul>
                    <li><b>LEARN</b></li>
                    <li><a href="https://www.geeksforgeeks.org/fundamentals-of-algorithms/">Algorithms</a></li>
                    <li><a href="https://www.geeksforgeeks.org/data-structures/">Data Structures</a></li>
                    <li><a href="https://www.geeksforgeeks.org/category/program-output/">Languages</a></li>
                    <li><a href="https://www.geeksforgeeks.org/articles-on-computer-science-subjects-gq/">CS Subjects</a></li>
                    <li><a href="https://www.youtube.com/geeksforgeeksvideos/">Video Tutorials</a></li>
                </ul>
            </div>

            <div class="footer-column">
                <ul>
                    <li><b>PRACTICE</b></li>
                    <li><a href="https://practice.geeksforgeeks.org/company-tags/">Company-wise</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/topic-tags/">Topic-wise</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/contests/">Contests</a></li>
                    <li><a href="https://practice.geeksforgeeks.org/subjective-page.php">Subjective Questions</a></li>
                </ul>
            </div>

            <div class="footer-column">
                <ul>
                    <li><b>CONTRIBUTE</b>
                    </li><li><a href="https://www.geeksforgeeks.org/contribute/">Write an Article</a></li>
                    <li><a href="https://www.geeksforgeeks.org/write-interview-experience/">Write Interview Experience</a></li>
                    <li><a href="https://www.geeksforgeeks.org/internship/">Internships</a></li>
                    <li><a href="https://www.geeksforgeeks.org/how-to-contribute-videos-to-geeksforgeeks/">Videos</a></li>
                </ul>
            </div>

        </div>

        <div class="footer-bottom-div footer-bottom-social">
    <ul class="social-ul" style="padding-left: 0px;">
                    <li>
                        <a class="social-link" href="https://www.facebook.com/GeeksforGeeks-316764689022/timeline/"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://in.linkedin.com/company/geeksforgeeks"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://play.google.com/store/apps/details?id=free.programming.programming&amp;hl=en"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://twitter.com/geeksforgeeks"><div class="social-img-div"></div></a>
                        <a class="social-link" href="https://www.youtube.com/geeksforgeeksvideos"><div class="social-img-div"></div></a>
                    </li>
                </ul>
  </div>
  <div class="footer-bottom-div">
            @geeksforgeeks, <a style="color:#fff !important" href="https://creativecommons.org/licenses/by-sa/4.0/">Some rights reserved</a>
        </div>

    </div>
</footer>
<!-- #page -->

<script type="text/javascript" src="ratinmaze_files/shCore-1.js"></script>
<script type="text/javascript" src="ratinmaze_files/shBrushC.js"></script>
<script type="text/javascript" src="ratinmaze_files/shBrushJava.js"></script>
<script type="text/javascript" src="ratinmaze_files/shBrushPython3.js"></script>
<script type="text/javascript">
	(function(){
		var corecss = document.createElement('link');
		var themecss = document.createElement('link');
		var corecssurl = "https://www.geeksforgeeks.org/wp-content/plugins/syntaxhighlighter/syntaxhighlighter3/styles/shCore.css?ver=3.0.9b";
		if ( corecss.setAttribute ) {
				corecss.setAttribute( "rel", "stylesheet" );
				corecss.setAttribute( "type", "text/css" );
				corecss.setAttribute( "href", corecssurl );
		} else {
				corecss.rel = "stylesheet";
				corecss.href = corecssurl;
		}
		document.getElementsByTagName("head")[0].insertBefore( corecss, document.getElementById("syntaxhighlighteranchor") );
		var themecssurl = "https://www.geeksforgeeks.org/wp-content/plugins/syntaxhighlighter/syntaxhighlighter3/styles/shThemeDefault.css?ver=3.0.9b";
		if ( themecss.setAttribute ) {
				themecss.setAttribute( "rel", "stylesheet" );
				themecss.setAttribute( "type", "text/css" );
				themecss.setAttribute( "href", themecssurl );
		} else {
				themecss.rel = "stylesheet";
				themecss.href = themecssurl;
		}
		//document.getElementById("syntaxhighlighteranchor").appendChild(themecss);
		document.getElementsByTagName("head")[0].insertBefore( themecss, document.getElementById("syntaxhighlighteranchor") );
	})();
	SyntaxHighlighter.config.strings.expandSource = '+ expand source';
	SyntaxHighlighter.config.strings.help = '?';
	SyntaxHighlighter.config.strings.alert = 'SyntaxHighlighter\n\n';
	SyntaxHighlighter.config.strings.noBrush = 'Can\'t find brush for: ';
	SyntaxHighlighter.config.strings.brushNotHtmlScript = 'Brush wasn\'t configured for html-script option: ';
	SyntaxHighlighter.defaults['gutter'] = false;
	SyntaxHighlighter.defaults['pad-line-numbers'] = true;
	SyntaxHighlighter.defaults['toolbar'] = false;
	SyntaxHighlighter.all();
</script>
<link rel="stylesheet" id="tabby-print-css" href="ratinmaze_files/tabby-print.css" type="text/css" media="all">
<script type="text/javascript" src="ratinmaze_files/wp-embed.js"></script>
<script type="text/javascript" src="ratinmaze_files/tabby.js"></script>

<script>jQuery(document).ready(function($) { RESPONSIVEUI.responsiveTabs(); })</script>

<style>
.eventLink{
border: 1px solid #868686;
background-color: #e0e0e0;
padding: 10px;
box-shadow: none;
display: block;
text-align: center;
color: #555 !important;
font-size: 14px;
font-weight: bold;
}
</style>

<script type="text/javascript">
// below changes to be added in gfg.js in future.
// load comment button click when page scroll to it and positioned ad in mobile view.
flag=0;jQuery(window).scroll(function(){if(jQuery('#comment').length !=0 ){var hT=jQuery('#comment').offset().top,hH=jQuery('#comment').outerHeight(),wH=jQuery(window).height(),wS=jQuery(this).scrollTop();if(wS>(hT+hH-wH-70)&&!flag){jQuery('#comment').click();flag=1}}});
/*var temp_width=jQuery(window).width();if(temp_width<468){if(jQuery('article').length>1){jQuery(jQuery('.responsiveAd')).insertAfter('article:eq(2)');jQuery('.rectangleAd').hide()}
else if(jQuery('#practiceLinkDiv').length>0){jQuery(jQuery('.responsiveAd')).insertAfter('#practiceLinkDiv');jQuery('.rectangleAd').css('width','')}else{jQuery('.responsiveAd').hide();jQuery('.rectangleAd').css('width','')}}
*/

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-12148232-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
<script type="text/javascript" src="ratinmaze_files/monetization.js"></script>
<script>
(function(){
    if(typeof _bsa !== 'undefined' && _bsa) {
        _bsa.init('fancybar', 'C6ADVKE', 'placement:geeksforgeeks');
    }
})();
</script>






<table style="width: 540px; display: none; top: 106px; position: absolute; left: 30px;" class="gstl_50 gssb_c" cellspacing="0" cellpadding="0"><tbody><tr><td class="gssb_f"></td><td class="gssb_e" style="width: 100%;"></td></tr></tbody></table><script type="text/javascript" src="ratinmaze_files/a.json"></script><script type="text/javascript" src="ratinmaze_files/geoip2.js"></script><iframe style="display: none;"></iframe></body></html>
<!-- Dynamic page generated in 2.068 seconds. -->
<!-- Cached page generated by WP-Super-Cache on 2018-07-13 13:12:05 -->
<!-- Compression = gzip -->