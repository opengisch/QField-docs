# Web UI

This is only for internal development. Explanations how permissions, data querying and template access are handled using Djangos tools, ie urls, views and django-templates.

(CBV=class based views)

## permissions

### permission control levels
There are 2 levels of permisson control:
#### 1. view-level:
If a user tries to directly access an unpermitted resource (url), then redirect to a 'unpermitted page' with a message.
#### 2. template-level:
Once a user can access a specific url, he will only see the control buttons and information according to his permissions, which is passed to the template with context variables.

### information flow
All permission logic to control Details- and CRUD-templates, is derived from core.permissions_utils.py. The information flow for a http-request via url is as follows:

1. get the url parameters (eg `.../<str:content_owner>/...`)
2. get the objects via `#!python SomeModel.objects.get/filter(field=urlParam)`
3. pass the required objects to the `#!python permissions_utils(...)`
4. add the received permissions to the `#!python View.dispatch(...)` method to redirect if a user wants to access an unpermitted page
5. add the received permissions to the template context to show only the permitted elements (eg. update-button)


???+ info 
    (4. and 5. are implemented via Mixins to stay DRY if used on many Views, else the dispatch method is directly added on a specific View. The Mixins can only be used for Views that are connected to specific urls which contain the necessary url-parameters)

## querysets

Similiar to the template-level permissions, the queryset gets filtered in on views level.

### information flow
Similar to permission flow. The querysets which define the data the user can see get generated using the core.querysets_utils.py. The required SomeMode.objects... are queried using the corresponding url-parameters.
