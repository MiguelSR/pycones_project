define([
    'backbone',
    'talks/models/TalkModel',
], function(Backbone, AuthorModel) {
    "use strict";

    return Backbone.Collection.extend({
        model: TalkModel,
        urlRoot: '/api/v1/talk/'
    });

});
