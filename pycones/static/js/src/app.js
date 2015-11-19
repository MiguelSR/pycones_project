define([
    'backbone',
    'backbone-tastypie',
    'bootstrap',
    'jquery',
    'talks/router',
], function(Backbone, __backbone_tastypie, __boostrap, $,
            Router) {
    "use strict";

    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = $.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
      crossDomain: false, // obviates need for sameOrigin test
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
    });

    return {
        initialize: function() {
            new Router({
                el: '#main_container'
            });
            Backbone.history.start({pushState:true});
            
            $('body').on('click', 'a', function(e) {
                e.preventDefault();
                var href = $(this).attr('href');
                Backbone.history.navigate(href, true);
            });
        }
    };
});
