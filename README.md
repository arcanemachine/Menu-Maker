# Menu Maker

![Coverage Badge](/assets/img/coverage.svg "Coverage Badge")

<strong><h3>Note: This project is currently not feature-complete. Please do not attempt to use it for its stated purpose. This notice will be removed when the project is usable to any reasonable capacity.</h3></strong>

Menu Maker is a project that showcases my understanding of best practices using Python, Django and Git. In short, it is a simple CRUD app that showcases Django's utility as a web-first framework. It is intended to serve as a reference guide for best practices when making a basic CRUD app using Django. Only the code needed to perform the desired task is used. There is no useless boilerplate or filler.

This project allows restaurant owners to register their restaurant and create a customized menu, allowing customers to easily view the restaurant's offerings from a desktop or mobile device.

This app is made using Python 3.8.6 and Django 3.1.2, and takes advantage of modern conveniences offered by the software (e.g. Python's f-strings)

This app makes use of the following Python practices and modules:
- Follows the Python PEP8 style guide (linted using flake8)
- Uses Coverage module to ensure all sections of the code has been tested

Menu Maker makes use of many of Django's primary features:

- Django's built-in ORM:
    - This project uses SQLite for maximum portability and ease of setup
- Whenever possible, Class-Based Views (CBVs) are used, in order to take advantage of the features that are built into Django's CBVs (e.g. easy paging).
- Django's built-in test runner:
    - To the best of my knowledge, all statements in the code have been properly tested (Coverage is currently at 94%).
    - Due to how Python's Coverage module detects code coverage, the number is a bit short of 100%. My goal is not to ensure that the badge says 100%, but to ensure that the codebase is sound.
    - All efforts have been made to ensure that the tests cover all expected circumstances.

This project also represents an effort to implement proper Git best practices, including:

- use of branches for separation of concerns (feature/test/main)
- small, incremental commits
- concise and accurate descriptions of each commit

<br>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="margin-left: auto; margin-right: auto; border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
