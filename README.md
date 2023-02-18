# Whales Blog with Django
This is a blog about whales developed with Django framework, where users can read articles and news related to the topic of whales, leave comments, and register/login to the website to leave feedback.

### Table of Contents
* Installation
* Usage
* Features
* Contributing
* License

### Installation
1. Clone the repository:

```
git clone https://github.com/sorryduck/WhaleOfATale-site.git
```

2. Install the requirements:

```
pip install -r requirements.txt
```

3. Apply migrations:

```
python manage.py migrate
```

4. Create a superuser:

```
python manage.py createsuperuser
```

5. Run the development server:

```
python manage.py runserver
```

6. Access the site at http://localhost:8000/.

### URLs
* Home: /
* Show articles by category: /categories/slug:cat_slug/
* Feedback form: /feedback/
* About page: /about/
* Ocean news: /ocean_news/
* Search: /search/
* User registration: /register/
* User login: /login/
* User logout: /logout/

### Views
* MainView: displays the home page and a list of articles
* CategoryView: displays articles for a particular category
* FeedbackFormView: displays a feedback form
* about: displays the about page
* SearchView: displays search results
* UserRegister: handles user registration
* UserLogin: handles user login

### Admin
* ArticleAdmin: admin for Article model
* NewsAdmin: admin for News model
* CategoryAdmin: admin for Category model
* FeedbackAdmin: admin for Feedback model
* CommentaryAdmin: admin for ArticleCommentaries model

### Forms
* UserLoginForm: form for user login
* UserRegisterForm: form for user registration
* FeedbackForm: form for feedback
* CommentForm: form for adding comments to articles

### Models
* ArticleCommentaries: model for article comments
* Article: model for articles
* Category: model for article categories

### Usage
Once the site is running, users can access the different pages using the navbar or the links on the home page.

The home page displays a list of articles sorted by most recent. The articles can be filtered by category using the links in the sidebar.

The user can view the article details, including the comments left by other users. They can also leave their own comments.

Users can leave feedback for the website owners using the "Feedback" page.

### Features

* Display articles on the home page
* Filter articles by category
* View article details and comments
* Leave comments on articles
* Leave feedback for the website owners
* User registration and login

### Contributing
Contributions are welcome. Please create a pull request with your changes.
