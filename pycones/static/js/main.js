requirejs.config({
    "baseUrl": "/static/js/src/",
    "paths": {
        "app": "./app",
        "backbone": "../bower_components/backbone/backbone-min",
        "backbone-tastypie": "../bower_components/backbone-tastypie/backbone_tastypie/static/js/backbone-tastypie",
        "bootstrap": "../bower_components/bootstrap/dist/js/bootstrap.min",
        "jquery": "../bower_components/jquery/dist/jquery.min",
        "handlebars": "../bower_components/handlebars/handlebars",
        "text": "../bower_components/text/text",
        "underscore": "../bower_components/underscore/underscore-min",
    },
    "shim": {
        "bootstrap":  {"deps": ['jquery']}
    }
});

require([
    "app",
], function(App) {
    "use strict";
    App.initialize();
});
