define([
    'backbone',
    'talks/models/TalkModel',
], function(Backbone, TalkModel) {
    "use strict";

    return Backbone.Collection.extend({
        model: TalkModel,
        url: '/api/v1/talk/'
    });

});
