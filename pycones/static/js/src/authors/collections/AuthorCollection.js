define([
    'backbone',
    'authors/models/AuthorModel',
], function(Backbone, AuthorModel) {
    "use strict";

    return Backbone.Collection.extend({
        model: AuthorModel,
        url: '/api/v1/author/'
    });

});
