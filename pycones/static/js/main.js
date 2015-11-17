requirejs.config({
    "baseUrl": "/static/js/src/",
    "paths": {
        "app": "./app",
        "backbone": "../bower_components/backbone/backbone-min",
        "bootstrap": "../bower_components/bootstrap/dist/js/bootstrap.min",
        "jquery": "../bower_components/jquery/dist/jquery.min",
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
