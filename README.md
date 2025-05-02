## Recipe API + Frontend Browser UI

This project is a Django REST Framework API + Simple Frontend UI application for browsing and searching recipes.
Users can filter recipes, search by title or cuisine, sort by rating, and view detailed recipe info via a dynamic drawer interface.

* REST API with Django REST Framework
* API endpoints for listing and searching recipes
* Pagination support
* Frontend UI built with Django templates + Bootstrap
* Filtering options → Title, Cuisine, Min Rating
* Pagination limit → 15/25/50 per page
* Drawer/Modal popup for recipe details (Description + Nutrition)
* Fallback "No results found" message when no recipes match search
* Responsive and clean UI

## Technologies Used
* Python 3.x
* Django
* Django REST Framework
* Bootstrap 5 (for responsive frontend)
* JavaScript (vanilla for frontend interactions)

## Folder Structure
![image](https://github.com/user-attachments/assets/0849fe5e-c927-418c-ad99-fcc503f84497)

## Installation and Setup
1️⃣ Clone the repository
```
https://github.com/eliashossain001/-Recipe-API-Frontend-Browser-UI.git
```
Once the project is cloned, then type the following command to navigate the directory:
```
cd recipe-api-ui
```
2️⃣ Install dependencies
```
pip install django djangorestframework django-filter
```
3️⃣ Run migrations and load data

```
python manage.py migrate
python manage.py runserver
```
4️⃣ Access API and UI

* API: ```http://127.0.0.1:8000/api/recipes/```
* Frontend UI: ```http://127.0.0.1:8000/api/ui/```

## Usage
Look at the following to understand the Searching and Filtering:
* Search Title: Type a keyword (e.g. "potato", "sweet") → shows matching recipes.
* Filter Cuisine: Type cuisine name (e.g. "Southern Recipes") → filters by cuisine.
* Min Rating: Enter exact rating (e.g. 4.8) → filters by rating.
* Pagination: Change number of results per page → use Next/Previous buttons.

🧾 Viewing Recipe Details
Click on a recipe row → opens a drawer/modal.

* Shows:
* Recipe Title + Cuisine
* Description
* Total Time (Prep + Cook Time)
* Nutrition (in table format)
🚫 No Results Found
If no recipes match → "No recipes found." message appears.

## Sample Output 
Hit the following query in the browser end point:

```
http://127.0.0.1:8000/api/recipes/?page=1&limit=10
```
This will retrieve the following output:

![image](https://github.com/user-attachments/assets/5abd580a-cf9e-40d8-adad-a2708309b700)

Now, again Hit the following query in the browser end point:
```
http://127.0.0.1:8000/api/recipes/search/?calories=%3C=400&title=pie&rating=%3E=4.5
```
This will retrieve the following output:
![image](https://github.com/user-attachments/assets/78b5ce0d-2bf5-4dd2-a4bd-73073a13901d)

Lastly, to access the UI, hit the following command:
```
http://127.0.0.1:8000/api/ui/
```
This will get you the following output:
![image](https://github.com/user-attachments/assets/59b96e41-bc7f-4456-a02a-3387a720f184)



