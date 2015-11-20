define([
    'backbone',
    'authors/views/AuthorListView',
], function(Backbone,
            AuthorListView) {
    "use strict";
    return Backbone.Router.extend({

        initialize: function(options) {
            this.options = options;
        },

        routes: {
            "authors(/)": "loadAuthors",
        },

        loadAuthors: function() {
            this.view = new AuthorListView({
                el: this.options.el,
            });
            this.view.loadAuthors();
        }
    });
});
