# Project Summary: Knowledge Quiz Web Application using Django and Twitter Bootstrap

The Knowledge Quiz Web Application is a feature-rich educational platform designed to test users' knowledge on various topics. Developed using the Django framework and Python, the application offers engaging quizzes, result tracking, and a user-friendly interface. The project aims to enhance learning and challenge users' understanding through interactive quizzes and insightful performance analysis.

## Key Features:

### User Authentication:
- Users can register new accounts or log in using existing credentials.
- Django's built-in User model handles account creation and management.

### Question Management:
- Questions are stored in a database, each with multiple choices and a correct answer.
- A Question model ensures consistency and coherence in quizzes.

### Quiz Functionality:
- Users initiate quizzes, selecting a set of questions at random from the database.
- After quiz completion, scores are calculated and personalized feedback is provided.
- Scores are presented as a percentage along with performance-based messages.
go
### Result Tracking:
- Quiz results are stored in the database for each user.
- Users can review their past performances and access their average, highest, and lowest scores.

### Retake Option:
- Users who score below a threshold can retake quizzes to improve their performance.

### Admin Panel Integration:
- The admin panel allows administrators to manage questions and view quiz results.
- QuizResult objects are stored with user scores and timestamps.

### Design and Presentation:
- The application boasts a user-friendly interface with appealing and consistent design elements.
- CSS styling and optional JavaScript elements enhance the overall user experience.

## Evaluation Criteria:
- **Presentation:** Clear and effective communication of project objectives and features.
- **Specification:** Successful implementation of the specified functionalities.
- **Navigation:** Intuitive navigation between sections and functionalities for a seamless user experience.
- **Design:** Consistent and visually appealing design elements throughout the application.
- **Individual Involvement:** Demonstrated understanding and contribution of each team member.

## Conclusion:
The Knowledge Quiz Web Application, developed using Django, offers a dynamic platform for users to test their knowledge and improve their understanding on a chosen topic. With user accounts, interactive quizzes, performance analysis, and result tracking, the application provides an engaging and educational experience. The combination of Django's powerful features, well-designed templates, and user-friendly interface makes it a compelling tool for both learning and assessment.

# Getting Started

Follow these steps to set up and run the Knowledge Quiz Web Application on your local machine:

## Prerequisites

- Python (3.6 or higher)
- Django (3.1 or higher)

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/mr-saxena-aditya/Django_QuizApp.git

2. Navigate to the project directory:

3. Install the project dependencies using pip:

2. Create a superuser account to access the admin panel or use the following username and password: 
- Username : superuser
- Password : superpassword

3. Start the development server:

4. Open your web browser and navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the admin panel and manage questions and quiz results.

5. To access the user interface, navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

6. Register or log in to start taking quizzes and exploring the application.

## Credits

This project is developed by Aditya Saxena (https://github.com/mr-saxena-aditya).

## License

This project is licensed under the MIT License

