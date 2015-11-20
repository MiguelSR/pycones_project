define([
    'backbone',
    'backbone-tastypie',
    'bootstrap',
    'jquery',
    'talks/router',
    'authors/router',
], function(Backbone, __backbone_tastypie, __boostrap, $,
            TalkRouter, AuthorRouter) {
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
            new TalkRouter({
                el: '#main_container',
            });
            new AuthorRouter({
                el: '#main_container',
            });
            Backbone.history.start({pushState:true});
            
            $('body').on('click', 'a', function(e) {
                if ($(this).attr('href').split('/')[1] === 'authors') return;
                e.preventDefault();
                var href = $(this).attr('href');
                Backbone.history.navigate(href, true);
            });
        }
    };
});
