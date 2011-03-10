django.jQuery.fn.counter = function() {
  // setup initial counter display
  django.jQuery(this).each(function() {

    var max = django.jQuery(this).attr('idealmaxlength');
    if(django.jQuery(this).attr('maxlength') && django.jQuery(this).attr('maxlength') != -1)
        max = django.jQuery(this).attr('maxlength');

    var val = django.jQuery(this).attr('value');
    var cur = 0;
    if(val) // value="", or no value at all will cause an error
      cur = val.length;
    var left = max-cur;
    django.jQuery(this).after("<p><span class='counter'>"
      + left.toString()+"</span> characters remaining</p>");
    // Style as desired
    var c = django.jQuery(this).next("p").find(".counter");
    c.css("margin-left","10px");
    c.css("padding", "0 3px 0 3px")
    c.css("border", "1px solid #ccc")
    if(left <= 10)
        c.css("background","#FF9900");
    else
        c.css("background","none");
 
    // setup counter to change with keystrokes 
    django.jQuery(this).keyup(function(i) {

    var max = django.jQuery(this).attr('idealmaxlength');
    if(django.jQuery(this).attr('maxlength') && django.jQuery(this).attr('maxlength') != -1)
        max = django.jQuery(this).attr('maxlength');

      var val = django.jQuery(this).attr('value');
      var cur = 0;
      if(val)
        cur = val.length;
      var left = max-cur;
      var c = django.jQuery(this).next("p").find(".counter");
      c.text(left.toString());
      if(left <= 10)
          c.css("background","#FF9900");
      else
          c.css("background","none");
      return this;
    });
  });
  return this;
}

django.jQuery(document).ready(function() {
  django.jQuery(".text-counter").counter();
});
