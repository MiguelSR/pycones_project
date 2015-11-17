define([
    'backbone',
    'authors/models/AuthorModel',
], function(Backbone, AuthorModel) {
    "use strict";

    return Backbone.Collection.extend({
        model: AuthorModel,
        urlRoot: '/api/v1/author/'
    });

});
