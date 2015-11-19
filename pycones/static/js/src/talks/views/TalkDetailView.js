define([
    'backbone',
    'handlebars',
    'text!talks/templates/TalkDetailTemplate.html'
], function(Backbone, Handlebars,
            talkDetailTemplate) {
    "use strict";

    return Backbone.View.extend({
        className: "media",
        template: Handlebars.compile(talkDetailTemplate),
        initialize: function(options) {
            this.model = options.model;
        },
        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });
});
