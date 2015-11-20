define([
    'backbone',
    'handlebars',
    'underscore',
    'authors/collections/AuthorCollection',
    'text!talks/templates/TalkEditTemplate.html'
], function(Backbone, Handlebars, _,
            AuthorCollection,
            talkEditTemplate) {
    "use strict";

    return Backbone.View.extend({
        className: "media",
        template: Handlebars.compile(talkEditTemplate),
        events: {
            'submit form': 'onSubmitForm',
            'click .delete': 'onDeleteClick'
        },
        initialize: function(options) {
            this.model = options.model;
        },
        render: function() {
            var allAuthors = new AuthorCollection();
            var self = this;

            allAuthors.fetch().done(function() {
                var params = {
                    model: self.model.toJSON(),
                    allAuthors: allAuthors.map(function(author) {
                        return _.extend({
                            'selected': _.contains(self.model.get('authors'),
                                                   author.get('resource_uri'))
                        }, author.toJSON());
                    })
                };

                self.$el.html(self.template(params));
            });
            return this;
        },
        onSubmitForm: function(e) {
            e.preventDefault();
            var target = $(e.target);
            this.model.set('description', target.find('#id_description').val());
            this.model.set('name', target.find('#id_name').val());
            this.model.set('authors', target.find('#id_authors').val());
            this.model.save().done(this.backToList.bind(this));
        },
        onDeleteClick: function(e) {
            e.preventDefault()
            this.model.destroy().done(this.backToList.bind(this));
        },
        backToList: function() {
            this.undelegateEvents();
            Backbone.history.navigate('/talks', true);
        }
    });
});
