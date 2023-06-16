## Assignment. 
To implement a site using Django web framework on individual assignment

![hotel](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/f20974f0-5744-4f59-a683-0d3723146e68)

## Problem Statement:
- Define the necessary entities to describe the domain. Implement them as models, using appropriate data types and object relations https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Models. Present them as a diagram, as in the example below. The recommended database is sqlite, but you can use any other database in consultation with the instructor.
- Implement one-to-one (OneToOneField), one-to-many (ForeignKey), and many-to-many (ManyToManyField) relationships.
- Implement CRUD operations (create, read, update, delete) (https://metanit.com/python/django/5.4.php );
- Add all models to the admin panel, create a superuser, provide data processing, filtering, inline editing of related records (https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Admin_site ). 
- Implement authorization/authentication mechanisms;
- Differentiate access depending on rights: e.g. store owner (superuser), User with registration, User without registration (see individual task).
- Ensure that at least 10 items in the list of products/services/objects/customers are populated with data.
- Connect and use at least 2 third-party APIs (a basic list is attached), choose the ones you like.
- Use regular expressions to associate a URL with a display function (https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Generic_views ).
- Display statistical metrics for your site (use data relevant to the topic area). 
- Display user's time zone, current date, date of adding/changing data in tables for user's time zone and for UTC, calendar in text form. Specify the date in the format (DD/MM/YYYYY).
- The client's phone number should be in the format +375 (29) XXX-XX-XX;
- Customers and employees must have an age limit of 18+;
- To implement visualization in the form of a diagram or chart to display the distribution of indicators by groups and/or changes in indicators by dates/groups.
- Implement a search by any of the parameters and sort the displayed data
- Add tests to pytest. Use fixtures to create users and connect to the database. Use parametrize(https://pytest-docs-ru.readthedocs.io/ru/latest/parametrize.html );
- Add logging(https://habr.com/ru/companies/wunderfund/articles/683880/ );
- Add tests; Code coverage of tests is 80% or higher;
- Acceptable appearance. Use css (e.g. https://www.bootstrapcdn.com/), implement your own styles if you wish (find and download templates online);
- Validation of forms both on the server side and on the client side;
- Support of different logging levels (take the logging level from the application configuration);
- Restriction of using the project's API for unauthorized requests.

