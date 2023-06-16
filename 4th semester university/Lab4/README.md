# Assignment. 
To implement a site using Django web framework on individual assignment

![hotel](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/f20974f0-5744-4f59-a683-0d3723146e68)

# Problem Statement:
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

# Images
## User
Sign In:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/491eb89e-2a66-462e-8dc4-7cb40e1734d1)

Sign Up:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/5f4bd7f3-e75b-4a0f-8a9f-73b6a29e65b7)

Auto size:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/35ac3b0f-1da8-4e0b-b960-7644863307bc)
![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/7a6a7987-8d7c-4245-be13-8944245ef7ab)

Sort by:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/3faeb51f-72e6-40ea-b500-b7ebc41ddcb7)
![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/31f8e177-db03-4696-88c8-3316f78d0013)

Book a room:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/30602e6f-28fd-4a81-bbac-1ce30eb16c98)

Profile:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/e01f1fbf-e954-4251-a439-25006d30c40d)

## SuperUser:
Analyse:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/8fb99741-4162-4510-a047-f849f6795d70)

Add new Card:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/6a21564c-664c-4463-b8e5-9dd4e41ad681)

Delete Card:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/f5d5c692-152f-4c00-a628-18bd15d12736)

Edit Card:

![image](https://github.com/kolyaklimk/Python-Tasks/assets/93304825/07d976ee-36c3-4314-85bb-efa7fd712486)

