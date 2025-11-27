# Easier Task - movie database

This flask site currently has a csv of movies, and we want to create a site similar to the example.

We want to be able to:
- See all the movies
- See an individual movie's details
- Add a movie to our own collection
- View our collection

## Step 1 - See All

The file-reading function and the template have been made for you, but you need to fill in the route so that it sends the movie information to the page.

The route is `see_all()` in the `views.py` file.

You can look at how this was done in the example_site, but adapt the code and then run and test the website.

## Step 2 - View One

Now that you have adapted the code to create a working all_movies page, you might notice that each row has a button which currently does nothing.

This should link to a page which gives all the details of the movie - but at the moment, the template and view for this page, and the links need to be implemented.

Adapt the code so that this link works, and take users to a page showing all the data which is in the row for the movie.

## Step 3 - Collections

Next is to implement a 'collection' feature so that users can make a personal list of movies.

To help you with this, a global variable called `collection` is included in `views.py`.

To implement this feature, you can:
- Create a route which adds the ID of this movie (the [0] element of the row) into `collection` and redirect to the same page.
- Add a button which links to this route on the movie page
- Create a route which shows all movies in the collection:
    - make a list of all the movies whose ids are in `collection`
    - add to the template `collection.html` to print out all of the movies in the collection

## General

Change the layout and style of the website to suit you - you can edit the .css file in static, and it contains some hints to help you to change the formatting.

