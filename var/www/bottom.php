	</div> <!-- #container -->
	
  <!-- JavaScript at the bottom for fast page loading -->

  <!-- Grab Google CDN's jQuery, with a protocol relative URL; fall back to local if offline -->
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  <script>window.jQuery || document.write('<script src="js/libs/jquery-1.7.1.min.js"><\/script>')</script>


  <!-- scripts concatenated and minified via ant build script-->
  <script defer src="js/plugins.js"></script>
  <script defer src="js/script.js"></script>
<?php if (isset($compilation)): ?>
  <script type="text/javascript" src="http://o.aolcdn.com/os_merge/?file=/streampad/sp-player.js&file=/streampad/sp-player-other.js&expsec=86400&ver=11&bgcolor=#000000&trackcolor=#f357a0&clicktext=Cliquez%20ici%20pour%20écouter%20la%20compilation&progressbackcolor=44464e&btncolor=white-gray"></script>
  <script>
$('.play').click(function() {
	SPAPI.start();
	return false;
});
$('.track').click(function() {

});
  </script>
  <?php endif; ?>
  <!-- end scripts-->

	
  <!-- Change UA-XXXXX-X to be your site's ID -->
  <script>
    window._gaq = [['_setAccount','UA-26294503-1'],['_trackPageview'],['_trackPageLoadTime']];
    Modernizr.load({
      load: ('https:' == location.protocol ? '//ssl' : '//www') + '.google-analytics.com/ga.js'
    });
  </script>


  <!-- Prompt IE 6 users to install Chrome Frame. Remove this if you want to support IE 6.
       chromium.org/developers/how-tos/chrome-frame-getting-started -->
  <!--[if lt IE 7 ]>
    <script src="//ajax.googleapis.com/ajax/libs/chrome-frame/1.0.3/CFInstall.min.js"></script>
    <script>window.attachEvent('onload',function(){CFInstall.check({mode:'overlay'})})</script>
  <![endif]-->
  
</body>
</html>
