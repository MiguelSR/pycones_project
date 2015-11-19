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
            var listView = new TalkListView({
                el: this.options.el,
            });
            listView.loadTalks(); 
        },
        editTalk: function(modelId) {
            var talk = new TalkModel({id: modelId});

            talk.fetch().done(function() {
                var editView = new TalkEditView({
                    el: this.options.el,
                    model: talk
                });
                editView.render(); 
            }.bind(this));
        },
        createTalk: function() {
            var editView = new TalkEditView({
                el: this.options.el,
                model: new TalkModel()
            });
            editView.render(); 
        }
    });
    return router;
});
