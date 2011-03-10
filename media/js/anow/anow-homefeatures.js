$(document).ready(function() {
  
  var $ht = $('.home-features:first-child').height();
  $('.home-features').css({height: $ht});
  
  
  function onBefore(currSlideElement, nextSlideElement, options, forwardFlag) {
    
    cfn = parseInt(currSlideElement.attributes['feature_number'].value);
    $btns = $('.home-feature-button');
    console.log("moving from image: " + cfn);
    
    $btns.removeClass('active');
    console.log("removing classes active from $btns");
    
    cfn = parseInt(nextSlideElement.attributes['feature_number'].value );
    $btn = $('.home-feature-button[feature_number="' + cfn + '"]');
    $btn.addClass('active');
    
  };
  
  function onAfter(currSlideElement, nextSlideElement, options, forwardFlag) {
    
    cfn = parseInt(nextSlideElement.attributes['feature_number'].value);
    console.log("now at image: " + cfn);
	
	 var $ht = $(this).height();
	 $(this).parent().css({height: $ht});
	
  };
  
  toggleCycle = function() {
    
      if (isPlaying) {
        $('.home-features').cycle('pause');
        $('#home-feature-cycle-toggle').removeClass('home-feature-button-pause');
        $('#home-feature-cycle-toggle').addClass('home-feature-button-play');
        isPlaying = false;
      } else {
        $('.home-features').cycle('resume');
        $('#home-feature-cycle-toggle').removeClass('home-feature-button-play');
        $('#home-feature-cycle-toggle').addClass('home-feature-button-pause');
        isPlaying = true;
      }
      console.log("cycle: " + isPlaying);
  };
  
  $('#home-feature-cycle-toggle').click(function(e) {
    e.preventDefault();
    console.log('clicked play/pause');
    toggleCycle();
  });
  
  $('.home-features').cycle({ 
    fx: 'fade', 
    fastOnEvent: 0,
    delay: 0,
    before: onBefore,
    after: onAfter,
	slideResize : 0
  });
  


  $('.home-feature-button').click(function(e) {
    e.preventDefault();
    
    $('.home-features').cycle(
      parseInt($(this).attr('feature_number'))
    );
    
    $(this).addClass('active');

    if (isPlaying) {
      toggleCycle();
    } else {
      // ignore
    }
    
    // $('.home-features').cycle('pause');
    
    console.log(e + "going to image: " + $(this).attr('feature_number'));
    
  });
  
  $('.home-features').cycle('resume');
  var isPlaying = true;
  
});