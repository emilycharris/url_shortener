# url_shortener
URL Shortener homework

The objective for this assignment was to create a URL shortener/bookmarking site with Django.  The assignment was intended to teach familiarity with Django's class-based views and Django's default authentication views and forms.

The requirements for the assignment were as follows: 

User can save a URL as a bookmark with a title and an optional description.

User can see all of the bookmarks in reverse chronological order.

User can access a bookmark through a URL with a short code, allowing them to share bookmarks.

When a user accesses a bookmark, the access is recorded with the bookmark and the timestamp.

Users can create an account, log in, and log out.

A logged in user can create, edit, and create bookmarks that are tied to themselves.

A logged in user can not edit or delete a bookmark created by another user.

Be able to update and delete existing bookmarks

In addition to the requirements above, the following requirements were part of the "hard mode" assignment:

Allow a user to create a bookmark as public or private.

Only show bookmarks that are flagged as public in the list view.

The application was created using the Python programming language, as well as the Django web framework. The shortened version of the URL was accomplished using hashids. Front-end development includes HTML, CSS, and Bootstrap. The application was successfully deployed to the web using Heroku.

The live site can be viewed at the following address:
https://emily-url-shortener.herokuapp.com/
