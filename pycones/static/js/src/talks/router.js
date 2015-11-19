define([
    'backbone',
    'talks/models/TalkModel',
    'talks/views/TalkEditView',
    'talks/views/TalkListView',
], function(Backbone,
            TalkModel,
            TalkEditView,
            TalkListView) {
    "use strict";
    var router = Backbone.Router.extend({

        initialize: function(options) {
            this.options = options;
        },
        routes: {
            "(talks)(/)": "loadTalks",
            "talks/add(/)": "createTalk",
            "talks/:id": "editTalk",
        },
        loadTalks: function() {
            this.view = new TalkListView({
                el: this.options.el,
            });
            this.view.loadTalks(); 
        },
        editTalk: function(modelId) {
            var talk = new TalkModel({id: modelId});

            talk.fetch().done(function() {
                this.view = new TalkEditView({
                    el: this.options.el,
                    model: talk
                });
                this.view.render(); 
            }.bind(this));
        },
        createTalk: function() {
            this.view = new TalkEditView({
                el: this.options.el,
                model: new TalkModel()
            });
            this.view.render(); 
        }
    });
    return router;
});
