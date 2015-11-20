define([
    'backbone',
    'handlebars',
    'talks/collections/TalkCollection',
    'talks/views/TalkDetailView',
    'text!talks/templates/TalkListTemplate.html'
], function(Backbone,
            Handlebars,
            TalkCollection,
            TalkDetailView,
            talkListTemplate) {
    "use strict";
    return Backbone.View.extend({
        template: Handlebars.compile(talkListTemplate),

        initialize: function(options) {
            this.collection = new TalkCollection();
            this.render();
        },

        loadTalks: function(foo) {
            this.collection.fetch();
        },

        render: function() {
            this.$el.html(this.template());
            this.listenTo(this.collection, 'add', this.renderChild);
        },

        renderChild: function(child) {
            var childView = new TalkDetailView({model: child});
            this.$el.append(childView.render().el);
        }
    });
});
