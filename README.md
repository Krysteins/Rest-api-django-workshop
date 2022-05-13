# Rest api django workshop

# Workshop &ndash; Models

Create the `Cinema` and` Screening` models.

The `Cinema` model includes:
* `name` &ndash; cinema name (`string` max 255 characters),
* `city` &ndash; city (`string` max 255 characters),
* `movies` &ndash; a many-to-many relationship with the `Movie` model (via the` Screening` model).

The 'Screening' model includes:
* `movie` &ndash; relation to the `Movie` model,
* `cinema` &ndash; relation to the `Cinema` model,
* `date` &ndash; date of the screening (field type `datetime`).


# Workshop &ndash; Cinema serializer

Serializer for the `Cinema` class:
* Movies in the `movies` field are to be represented as links to their corresponding API resources.

# Workshop &ndash; Cinema views

Create views for the cinema:
* There are views in the views.py file that support the `cinemas` resource:
    * `CinemaListView`,
    * `CinemaView`.
* There are tests to check the operation of all shared `url` addresses and` HTTP` methods.


#### Tests:

* `test_add_cinema` &ndash; checking if adding a new cinema works.
* `test_get_cinema_list` &ndash; checking that the list of all cinemas works.
* `test_get_cinema_detail`& ndash; checking if the cinema detail view is working.
* `test_delete_cinema` &ndash; checking cinema removal.
* `test_update_cinema` &ndash; checking if the movie update is working.


# Workshop &ndash; Seance serializer

* Serializer for the `Screening` class.
* Theaters are to be represented as their names.
* Videos are to be represented as their titles.

# Workshop &ndash; Session views

Create views for the show:
* In the views.py file, write the views that handle the `screening` resource:
    * `ScreeningListView`,
    * `ScreeningView`.
* There are tests to check the operation of all shared `url` addresses and` HTTP` methods.


#### Tests:

Create tests:
* `test_add_screening` &ndash; checking if adding a new session works.
* `test_get_screening_list` &ndash; checking if the list of all screenings works.
* `test_get_screening_detail` &ndash; checking if the detailed view of the session is working.
* `test_delete_screening` &ndash; checking the removal of the session.
* `test_update_screening` &ndash; checking if the update of the session works.